# Movie Trailer Website

This repository builds a movie trailer website.

Displayed on the static web page are a list of my favourite movies.
You can click on the poster of a movie to watch its trailer.

Modules in this project:
* **fresh_tomatoes** deals with the front-end of the website,
credit to adarsh0806.
* **media** defines class Movie at the back-end.
* **entertainment_centre** creates a list of Movie
objects, stores them in a list, and calls the open_movies_page
 function of fresh_tomatoes to generate an HTML web page at the back-end.

 To run the code, download the master branch of the repository,
 unzip it, and then run entertainment_centre.py at command line
 to generate a new web page:
```
$ python <path-to-repository>/entertainment_centre.py
```
