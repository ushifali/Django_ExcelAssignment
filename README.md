# Django_Excel_Assignment
## Django_Assignment

Problem Statement:

Implement an API which reads an excel file to populate the records for the table\
And also serialise the data to manipulate the following:\
Serial number - upper to lower case\
mac_address - add colons (1A1B1C1D1E1F => 1A:1B:1C:1D:1E:1F)

CREATE A FOLDER >> INSIDE IT 

## STEP 1:

CREATE A VIRTUAL ENVIRONMENT

commands:
python3 -m venv env
source env/bin/activate
pip install Django

## STEP 2:

django-admin startproject Excel_Project\
this will create the project file along with manage.py

python manage.py startapp Excel_Application

//creates the application


## STEP 3:

MODELS > model.py

Write your models

## Step 4:

import models in admin.py
Register the models in admin.py\
admin.site.register(<model name>)

## Step 5:

Application definition in installed apps\
Add the application created

## Step 6:

python3 manage.py makemigrations \
//create the folder\
python3 manage.py migrate\
#migrates all dataqueries and creates tables in 0001.py

## Step 7:

python3 manage.py runserver\
http://127.0.0.1:8000/admin/

#to add superuser
python3 manage.py createsuperuser\
// you can ignore the email that comes up
