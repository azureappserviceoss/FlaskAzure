"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, g, Flask, request
from FlaskWebProject1 import app
import json

###############################################################################
#                                 Database Functions                          #
###############################################################################
database = [{},{},{}] #Convention: teach := 0 | practice := 1 | conversation := 2

# Intakes a post request with a name, a skill, and a list of categories.
@app.route('/db_add', methods = ['GET', 'POST'])
def db_add():
  if request.method == 'POST':
    name = request.form.get('andrewID')
    skill = request.form.get('skill')
    teach = request.form.get('teach')
    prac = request.form.get('help_others')
    con = request.form.get('have_conversation')
    categories = []
    if (teach != None):
      categories.append(0);
    if (prac != None):
      categories.append(1);
    if (con != None):
      categories.append(2);

    for cat in categories:
      if(database[cat].get(skill) != None):
        database[cat].get(skill).add(name)
      else:
        database[cat][skill] = set()
        database[cat][skill].add(name)
    print(database)
    return redirect()
  else:
    return render_template(
      'redirect.html',
  )

# Intake a post request with a skill and a category, and return a list of
# andrewids that are offering that
@app.route('/db_lookup', methods =  ['GET', 'POST'])
def db_lookup():
  if request.method == 'POST':
    skill = request.form.get('skill')
    t_cat = request.form.get('category')
    cat = -1
    if (t_cat == "teach"):
      cat = 0
    elif (t_cat == "prac"):
      cat = 1
    elif (t_cat == "talk"):
      cat = 2

    if (database[cat].get(skill) == None):
      return render_template(
        'return_results.html'
        )

    jsoned  = json.dumps (list(database[cat].get(skill)))
    print(jsoned)
    return render_template(
      'return_results.html',
      results = jsoned    )
  else:
    return render_template(
      'return_results.html',
      results=None,
    )

##############################################################################
#                             Flask Page Runners                             #
##############################################################################
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
def redirect():
  return render_template(
      "redirect.html",
      year = datetime.now().year,
      message = 'Thank you for your submission!'
      )
