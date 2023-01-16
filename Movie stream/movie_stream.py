import pandas as pd
import sqlite3
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

@st.cache
def load_data():
    # Connect to the database
    conn = sqlite3.connect('model_movies_data.db')

    # Define the SQL query
    query = 'SELECT * FROM movies'

    # Read the query results into a DataFrame
    df4 = pd.read_sql_query(query, conn)


    features = ['genre1', 'genre2', 'genre3', 'duration', 'year']

    for feature in features:
        df4[feature] = df4[feature].fillna('')
    df4["combined_features"] = df4.apply(lambda row: f"{row['genre1']} {row['genre2']} {row['genre3']} {row['duration']} {row['year']}", axis=1)
    df4 = df4.reset_index()

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df4["combined_features"])
    cosine_sim = cosine_similarity(count_matrix)
    return df4, cosine_sim

df4, cosine_sim = load_data()

def get_recommendation(title, cosine_sim, df, num_of_rec=10):
    # indices of the course
    movie_indices = pd.Series(df.index,index=df['title']).drop_duplicates()
    # Index of course
    idx = movie_indices[title]

    # Look into the cosine matr for that index
    sim_scores =list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores,key=lambda x: x[1],reverse=True)
    selected_movie_indices = [i[0] for i in sim_scores[1:]]
    selected_movie_scores = [i[1] for i in sim_scores[1:]]

    # Get the dataframe & title
    result_df = df.iloc[selected_movie_indices]
    result_df['similarity_score'] = selected_movie_scores
    final_recommended_movies = result_df[['title','similarity_score']]
    return final_recommended_movies.head(num_of_rec)

def main():
    st.title("Movie Recommendation App")

    df4, cosine_sim = load_data()
    choice = st.sidebar.selectbox("Menu", ["Home","Recommend"])

    if choice == "Home":
        st.subheader("Home")
        st.dataframe(df4.head(10))

    elif choice == "Recommend":
        st.subheader("Recommend Movies")
        title = st.text_input("Enter movie title")
        if title:
            final_recommended_movies = get_recommendation(title, cosine_sim, df4)
            st.dataframe(final_recommended_movies)
    elif choice == "Random Movie":
        st.subheader("Random Movie")
        select_emotion = st.selectbox("Which emotion type movie do you want to watch?", df4.emotion.unique())
        select_year = st.selectbox("Classic or modern movies?", ["classic", "modern"])
        select_duration = st.selectbox("short or long movies?", ["short", "long"])

        filterm3 = df4.loc[df4['emotion'] == select_emotion]

        if select_year == 'classic':
            filterm3 = filterm3[df4['year'] < 2000]
        elif select_year == 'modern':
            filterm3 = filterm3[df4['year'] >= 2000]

        if select_duration == 'long':
            filterm3 = filterm3[df4['duration'] > 120]
        elif select_duration == 'short':
            filterm3 = filterm3[df4['duration'] <= 120]
    if filterm3.empty:
        st.warning("No movie matches your input, please make another input!")
    else:
        watch_movie2=filterm3.sample()
        st.write("Your randomly selected movie is:")
        st.write(watch_movie2.title.values[0])
        title = watch_movie2.title.values[0]
        final_recommended_movies = get_recommendation(title, cosine_sim, df4)



    else:
        st.subheader("About")
        st.text("Built with Streamlit & Pandas")

if __name__ == '__main__':
	main()

