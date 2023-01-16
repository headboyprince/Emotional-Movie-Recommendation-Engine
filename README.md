<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Emotional-Movie-Recommendation-Engine
The code uses the Streamlit library to create a simple movie recommendation system. The system allows a user to filter movies based on their preferred emotion type, and whether they prefer classic or modern movies, and whether they prefer short or long movies. It then returns a randomly selected movie from the filtered list and generates a list of movie recommendations based on the selected movie using cosine similarity.

The code is also using pandas library to load data from SQLite databases and sklearn library for feature extraction and similarity calculation. It starts by connecting to two SQLite databases, one containing movie data and the other containing emotion-labeled movie data. Then it loads the data into dataframes, preprocesses the data, and creates a vectorizer and cosine similarity matrix.

Next, it defines two functions:

The filter_movie function allows a user to filter movies based on their preferred emotion type, year, and duration, and returns a randomly selected movie from the filtered list.
The get_recommendation function takes the title of a selected movie as an input and generates a list of movie recommendations based on the selected movie using cosine similarity.
Finally, it defines a main function which calls the filter_movie and get_recommendation functions and displays the selected movie and recommended movies in the Streamlit app.</title>
</head>
<body>

</body>
</html>
