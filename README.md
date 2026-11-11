## Description ##

Django shopping catalogue for beauty products, inspired by the recent Sephora sale. 

## Getting Started ##
1. Clone repository 

2. Set up a virtual environment to keep packages isolated: 
`python -m venv .venv`
3. Activate your environment.

* For Mac: `source .venv/bin/activate`

* For Windows: `.venv\scripts\activate.ps1`

4. Install dependencies listed in requirements.txt. `pip install -r requirements.txt`

5. Once you have the dependencies installed, you should be able to run the server locally. Navigate into catalogue_project, and run server:
```
cd catalogue_project
python manage.py migrate
python manage.py runserver
```

## Usage ##
- ** Home** lists all products. Click a product for its name, price, description, and category
- **Filter** by category and tags using the filter bar
- **Search** products by name and description using search bar on the right.

Example searches: "foundation", "stick", "spray". 

## Assumptions and Notes ##
- search is case-insensitive
- selecting multiple tags return products matching any tag
- search and filter are separate forms

## AI Usage ##
AI was used as a search engine for some features of Django which were new to me, and with some HTML conventions (this was my first time using HTML). All code was written by me.
