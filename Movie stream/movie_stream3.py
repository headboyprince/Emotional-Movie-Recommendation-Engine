import pandas as pd
import sqlite3
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

st.set_page_config(page_title="My App", page_icon=":guardsman:", layout="wide")


# Connect to the database
conn = sqlite3.connect('model_movies_data.db')
conn1 = sqlite3.connect('emotion_movies_data.db')

# Define the SQL query
query = 'SELECT * FROM movies'
query1 = 'SELECT * FROM movies'

# Read the query results into a DataFrame
df = pd.read_sql_query(query, conn)
df2 = pd.read_sql_query(query1, conn1)


# Define the features to use in the vectorizer
features = ['genre1', 'genre2', 'genre3', 'duration', 'year']

# Fill any NaN values in the feature columns
for feature in features:
    df[feature] = df[feature].fillna('')

# Create a new column to store the combined feature text
df['combined_features'] = df.apply(lambda row: row['genre1'] + " " + row['genre2'] + " " + row['genre3'] + " " + row['duration'] + " " + row['year'], axis=1)

# Create a vectorizer and count matrix
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])

# Create a cosine similarity matrix
cosine_sim = cosine_similarity(count_matrix)

def filter_movie(df2):

    select_emotion = st.sidebar.selectbox("Select the type of emotion?", df2.columns[8:])
    select_year = st.sidebar.selectbox("Classic or modern movies?", ['Classic', 'Modern'])
    select_duration = st.sidebar.selectbox("Short or long movies?", ['Short', 'Long'])
    if st.sidebar.button('Generate random movie'):

        filtered_movies = df2.loc[df2[select_emotion] == 1]

        if select_year.lower() == 'classic':
            filtered_movies = filtered_movies[filtered_movies['year'] < 2000]
        elif select_year.lower() == 'modern':
            filtered_movies = filtered_movies[filtered_movies['year'] >= 2000]
        else:
            st.warning('Invalid input')

        if select_duration.lower() == 'long':
            filtered_movies = filtered_movies[filtered_movies['duration'] > 120]
        elif select_duration.lower() == 'short':
            filtered_movies = filtered_movies[filtered_movies['duration'] <= 120]
        else:
            st.warning('Invalid input')

        if filtered_movies.empty:
            st.warning("No movie matches your input, please make another input!")
        else:
            watch_movie = filtered_movies.sample()
            st.markdown(
                f'<h3 style="color:#1aa3ff;font-size:18px;">{"Your randomly selected movie is:"}</h3>',
                unsafe_allow_html=True)
            #st.write(watch_movie.title.values[0])
            title = watch_movie.title.values[0]
            st.markdown(
                f'<p style="text-align:left;background-image: linear-gradient(to right,#1aa3ff, #00ff00);'
                f'color:#ffffff;font-size:18px;border-radius:1%;border: 1px solid #1aa3ff">{title}</p>',
                unsafe_allow_html=True)
            return title

def get_recommendation(title, cosine_sim, df, num_of_rec=10):
    # Get the index of the input title in the dataframe
    idx = df[df['title'] == title].index[0]

    # Get the cosine similarity scores for the input title
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the scores in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Get the indexes of the 10 most similar movies
    sim_scores = sim_scores[1:num_of_rec + 1]
    movie_indices = [i[0] for i in sim_scores]
    final_recommended_movies = df.iloc[movie_indices]['title']
    return final_recommended_movies

#Main function
def main():
    color1 = ('#1aa3ff')
    color2 = ('#00ff00')
    color3 = ('#ffffff')
    content = "Welcome to the Emotions Movie Recommender Engine!"
    st.markdown(f'<p style="text-align:center;background-image: linear-gradient(to right,{color1}, '
        f'{color2});color:{color3};font-size:28px;border-radius:2%;">{content}</p>',
        unsafe_allow_html=True)
    title = filter_movie(df2)
    if title:
        recommended_movies = get_recommendation(title, cosine_sim, df)
        st.markdown(f'<h2 style="color:#ff1af3;font-size:20px;">{"Based on your selected movie, we recommend you the following movies:"}</h2>',
                    unsafe_allow_html=True)

        st.dataframe(recommended_movies)



if __name__ == '__main__':
    main()
