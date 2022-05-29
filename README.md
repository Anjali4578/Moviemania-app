# MOVIEMANIA - A MOVIE RECOMMENDATION ENGINE

## MICROSOFT ENGAGE 2022 CHALLENGE 3 - ALGORITHMS

### Brief Introduction

Moviemania is a movie recommenation engine (web application) which uses the content based data filtering method for recommending movies to the user. Now, let's understand what the term recommendation engine actually means.

#### Recommendation Engine

A **recommendation engine** is a type of data filtering tool using machine learning algorithms to recommend the most relevant items to a particular user or customer. It operates on the principle of finding patterns in consumer behavior data, which can be collected implicitly or explicitly.

There are three different types of recommendation engines:

1. Collaborative filtering
2. Content-based filtering
3. Hybrid model

### Project Description

In this project, content-based filtering method has been used and implemented. This web aplication has been made using frameworks like React Redux for the frontend and the Streamlit python framework for the backend.

- The movie details like title, genre, rating, poster, description have been fetched through TMDB API,see "https://www.themoviedb.org/", "https://www.themoviedb.org/documentation/api"

- The dataset used in the model building has been taken from Kaggle - **TMDB 5000 Movie Dataset**
  Link to the dataset: "https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv"

#### Deployed app link

The link to the deployed app on firebase is: "https://moviemania-web.web.app"

### How To Run This App

- Install/import all the required libraries to run the app: python, pickle, ast, nltk, numpy, pandas, streamlit, react-redux, react-router-dom (also see requirements.txt)
- Download the dataset from the above link and upload it to your file location or jupyter notebook(if using)
- Run and execute the content-based-filtering.ipynb jupyter notebook file or run the following command on command prompt: python get_recommendation.ipynb After completing the execution of this file, there will be two files downloaded to the main folder : movies_list.pkl, similarity.pkl These files will be used during the execution of app.py file.

1. Clone or download this repository to your local machine.
2. For the movie-recommender page:

   - Install all the libraries mentioned in the requirements.txt file with the command pip install -r requirements.txt
   - Open your terminal/command prompt from your project directory and run the file main.py by executing the command streamlit run main.py or streamlit run 'path of the file' .
   - It will automatically open the website or go to your browser and type http://192.168.0.106:8501 in the address bar.

   ##### Note: For running the python recommendation file please follow these steps carefully.

   1. Either download both the pkl files from the give links: similarity.pkl file: "https://drive.google.com/file/d/1PBP1cC74psLxtYqvAd7PEFjwmdyM6L2Z/view?usp=sharing", movies.pkl file: "https://drive.google.com/file/d/19odpVt8WXeU25alXPwdAemXJ_lTPSkwX/view?usp=sharing" **Important**
   2. Or download the csv files from the dataset folder of the repo and run it with the jupyter file (content-based-filtering) which generates the pkl files as above which can be used to run the app.py file.
   3. The separate deployed link of the recommendation page is : "https://moviemania-app-engage.herokuapp.com/"

3. Open your terminal and then type. $ git clone {the url to the GitHub repo} This clones the repo.
   cd into the new folder and type. $ npm install. This installs the required dependencies.
   To run the React project. $ npm start.
   4.It will automatically open the website or go to your browser and type "http://http://localhost:3000" in the address bar.

### References

- "https://towardsdatascience.com/introduction-to-recommender-systems-1-971bd274f421"
- "https://www.geeksforgeeks.org/ml-content-based-recommender-system/"
- "https://www.kaggle.com/code/mobasshir/recommendation-engine-exploration/notebook"
- "https://www.snet.tu-berlin.de/fileadmin/fg220/courses/SS11/snet-project/recommender-systems_asanov.pdf"
- "https://colab.research.google.com/github/google/eng-edu/blob/main/ml/recommendation-systems/recommendation-systems.ipynb?utm_source=ss-recommendation-systems&utm_campaign=colab-external&utm_medium=referral&utm_content=recommendation-systems#scrollTo=Le0Z54X68_iq"
