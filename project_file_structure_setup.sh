#!/bin/sh

# Create root files/folders
mkdir flask_app
mv SETUP_ITEMS/server.py .

# set up flask app files and folders
mv SETUP_ITEMS/__init__.py flask_app
cd flask_app
mkdir config
mkdir controllers
mkdir templates
mkdir static
mkdir models

# move temp index.html file into templates
mv ../SETUP_ITEMS/index.html templates

# move temp controller file into controllers
mv ../SETUP_ITEMS/temp_controller.py controllers

# move temp model file into models
mv ../SETUP_ITEMS/temp_model.py models

# move mysql config file into config
mv ../SETUP_ITEMS/mysqlconnection.py config

# set up static folders and files
cd  static

mkdir css
touch css/style.css
mkdir js
touch js/script.js
mkdir images

cd ..
cd ..

# removes the SETUP folder
rm -R SETUP_ITEMS

# install the packages for MVC
pipenv install PyMySQL flask flask-bcrypt

# set up git and with intial commit
git init
git add .
git commit -m "intial commit"

# Open folder into vscode
code .

# # open browser 
# open -a safari

# enter pipenv shell
pipenv shell

# start server
Python3 server.py









