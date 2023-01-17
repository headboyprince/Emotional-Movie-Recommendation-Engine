# Emotional-Movie-Recommendation-Engine
A simple movie recommendation system that allows users to filter movies based on their preferred emotion type, and whether they prefer *classic or modern movies*, and whether they prefer *short or long movies*. It then returns a randomly selected movie from the filtered list and generates a list of movie recommendations based on the selected movie using **cosine similarity**.

The **"Emotional-Movie-Recommendation-Engine"** Github repository contains several files that work together to create a movie recommendation system. The **main script, "movie_stream.py,"** uses the Streamlit library to create a simple web app that allows a user to filter movies based on their preferred emotion type, and whether they prefer *classic or modern movies*, and whether they prefer *short or long movies*. 

It then returns a randomly selected movie from the filtered list and generates a list of movie recommendations based on the selected movie using cosine similarity. The script also uses pandas library to load data from SQLite databases and sklearn library for feature extraction and similarity calculation.

## Setting up the Database

The **"scraped_movies_data.db", "cleaned_movies_data (1).db", "emotion_movies_data.db", "prepare_movies_data (1).db" and "model_movies_data.db"** are SQLite databases that contain the same movie dataset but with some slight modifications. 

The **scraped_movies_data.db** is the raw data gotten from the web scraping of movies and their details, then **cleaned_movies_data (1).db** was cleaned and some modifications were made to the data, then emotion_movies_data.db was created to label the movies with their corresponding emotions, then **prepare_movies_data (1).db** was prepared for the final dataset which is the model_movies_data.db which was used to train the model that the app uses to make the recommendations.

## Running the App

To use the app, first, make sure you have all the necessary dependencies installed, then run the "movie_stream.py" script. The app will start a local server, and you can access it in your web browser by navigating to "http://localhost:8501/". Use the app to filter movies based on your preferences and get recommendations.

The other versions of the app are **movie_stream1.py, movie_stream2.py and movie_stream3.py,** they all do the same thing but with different features and functionalities.
You can also check out the other files in the repository, including the "database.py" script, which was used to create and populate the SQLite databases.

## Getting Started
### Dependencies
Python 3.x

*   Pandas
*   Sklearn
*   SQLite3
*   Streamlit



## Installing...
👉 Clone the repository to your local machine

👉 Install the required dependencies using pip

`pip install pandas sklearn sqlite3 streamlit`

## Executing program

*   Navigate to the project directory and run the following command

`streamlit run app.py`


*   This will launch the Streamlit app in your browser.

## Help
If you encounter any problems or issues, please contact me at https://github.com/headboyprince or email me at princeben4real@gmail.com

## Authors
Prince Ben

## Acknowledgments
Geeksforgeeks
TowardsDataScience
Sk70249
SheCodes-IEEE-CIS-GHRCE

## Future Research
Adding a face detector that can automatically detect the users emotion instead of asking the user to enter his emotions manually.

## Contact
Github
Linkedin
Rulehour
Email: princeben4real@gmail.com
