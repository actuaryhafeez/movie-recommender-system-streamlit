# movie-recommender-system-streamlit
This is a web application built using Streamlit and Python that recommends similar movies based on the user's selected movie. 
The dataset used in this project is the TMDb 5000 Movie Dataset. It contains data on approximately 5,000 movies, including budget, revenue, cast, crew, genres, and ratings. The data was scraped from the TMDb website and made available for research purposes. It can be found on Kaggle: https://www.kaggle.com/tmdb/tmdb-movie-metadata

The application uses a content-based recommendation system, where the similarities between movies are calculated based on their genres, cast, directors, and keywords. The similarity scores are precomputed and stored in a pickle file for fast access during runtime.

The front-end of the application is built using Streamlit, a Python library for building web applications. The user can select a movie from a dropdown list or type in the name of a movie. Once the user selects a movie and clicks on the "Recommend" button, the application displays five similar movies along with their posters.

The posters are fetched using The Movie Database (TMDb) API, which provides a rich set of metadata for movies, TV shows, and other media.

### How to Use
#### To run the app, first clone the repository:
    git clone https://github.com/actuaryhafeez/movie-recommender-system-streamlit.git
### Create a new virtual environment in the project directory.
    python3 -m venv venv
### Activate the virtual environment. 
    source venv/bin/activate
#### Next, install the required packages using pip:
    pip install -r requirements.txt
### Run Jupyter Notebook using the following command to open notebook.ipynb
    jupyter notebook
#### Then, run the app:
    streamlit run app.py

This will open the app in your default web browser. From here, you can select a movie from the dropdown menu and click the "Recommend" button to see a list of similar movies.

![movie_recomm1](https://user-images.githubusercontent.com/55107467/233811599-62236aaa-3e74-4bb3-bf2d-b54e03bccb8f.png)
![movie_recomm2](https://user-images.githubusercontent.com/55107467/233811603-0d69662b-897e-466f-b30a-c086e155b0a0.png)


### Dataset
The dataset used for this project is the TMDb 5000 Movie Dataset. It contains metadata for ~5,000 movies, including information on user ratings, cast, crew, budget, revenue, and more. The dataset can be found in the data directory.

## Project Structure 

    movie-recommender-system-streamlit/
        ├── data/
        |   └── tmdb_5000_credits.csv
        |   └── tmdb_5000_movies.csv
        │   
        ├── model/
        │   └── movie_list.pkl
        │   └── similarity.pkl
        ├── app.py/
        │  
        ├── notebook.ipynb/
        ├── requirements.txt/
        ├── README.md/

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

This project adheres to the [Open Source Initiative's](https://opensource.org) definition of open source software and the [Open Source Initiative's Approved License List](https://opensource.org/licenses/alphabetical).


# References

### Acknowledgements
This project was built using the following tools and resources:

* Python
* Streamlit
* TMDb API
* TMDb 5000 Movie Datase
