"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, g, Flask, jsonify, request
from FlaskWebProject1 import app

###############################################################################
#                                 Database Functions                          #
###############################################################################
database = [{},{},{}] #Convention: teach := 0 | practice := 1 | conversation := 2

# Intakes a post request with a name, a skill, and a list of categories.
@app.route('/db_add', methods = ['POST'])
def db_add():
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

# Intake a post request with a skill and a category, and return a list of
# andrewids that are offering that
@app.route('/db_lookup', methods =  ['POST'])
def db_lookup():
  skill = request.form.get('skill')
  cat = request.form.get('category')
  return jsonify (list(database[cat].get(skill)))

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
