## Description ##

This is a shopping website I created on python using Django inspired by the recent Sephora sale. 

## Getting Started ##
1. Clone repository 

2. Set up a virtual environment to keep packages isolated: 
`python -m venv .venv`
3. Activate your environment.

* For Mac: `source .venv/bin/activate`

* For Windows: `.venv/scripts/activate.ps1`

4. Install dependencies listed in requirements.txt. `pip install requirements.txt`

5. Once you have the dependencies installed, you should be able to run the server locally. Navigate into catalogue_project and run server:
```
cd catalogue_project
python manage.py runserver
```

## Usage ##
This is a beauty store page where you can scroll through various products found in a makeup store. In the navigation bar, the "home" page shows the list of all products. A user can also click on a product to view a detailed page of that product's name, price, description, category, and tags.

A user can filter by the category or tags in the navigation bar, and also search for words found in the name or description of a product. Filter and search features can be used together. 

## AI Usage ##
AI was used as a search engine for some features of Django which were new to me, and with some HTML conventions (this was my first time using HTML). All code was written by me.
