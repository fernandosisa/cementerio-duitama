
# django-crud-auth

## Contents of this file

 - Introduction
 - Requirements
 - Installation
 - Configuration
 - Troubleshooting
 - Maintainers
## Introduction

this system allows users to create, update, and delete tasks, and the login feature enables users to access their tasks securely and ensures that only authorized personnel can view or modify them.

## Requirements

- browser 
- django and python installed

## Installation

- First, make sure you have Python installed on your computer. You can download the latest version of Python from the official website: https://www.python.org/downloads/

- Next, open a command prompt or terminal window on your computer and install Django using pip (Python's package installer). Type the following command:

pip install Django

This will download and install the latest version of Django on your computer.

- Once Django is installed, you can create a new Django project by running the following command:

django-admin startproject projectname

Replace projectname with the name of your project. This will create a new directory with the same name as your project and a basic file structure.

- Navigate to the project directory using the command prompt or terminal window:

cd projectname

- Now you can create a new Django app within your project by running the following command:

python manage.py startapp appname

Replace appname with the name of your app. This will create a new directory with the same name as your app and a basic file structure.

- Once you have created your app, you can start the Django development server by running the following command:

python manage.py runserver

This will start the development server on your local machine, and you can access your Django project by going to http://localhost:8000/ in your web browser.



## Troubleshooting

- to run the server in the console (vnv)write
`python manage.py runserver`

## Maintainers

Current maintainers:
- Fernando Sisa