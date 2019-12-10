# stuffToDo

As busy college students, one of the biggest challenges we face is keeping track of all the things to do. Students have many classes throughout the day, multiple assignments to do, study for other classes, and may have their own errands to run. With this issue in mind, our group felt this to be an interesting challenge to take on and decided to create **stuffToDo**. 

## Getting Started

The computer should have Python version 3.6 as well as pip installed to setup a localhost web server to serve for the development of the project.

### Prerequisites:

Python 3.6 with pip required extensions:

1. Flask
2. Flask-SQLAlchemy
3. Flask-WTF
4. Flask-Login
5. Flask-Mail
6. Flask-bcrypt
7. WTForms
8. SQLAlchemy
9. Flask-Bootstrap
10. Werkzeug
11. Jinja2
12. datetime

### Installing

Clone this git repo then install the required extensions. 
Use Terminal to install each extension:

Install Flask:
```
pip install Flask
```
Install flask-wtf, flask-sqlalchemy, flask-login:
```
pip install flask-wtf flask-sqlalchemy flask-login
```
Apply the above command until every extension is installed.

## Running Flask Project

Export the main file of the project by one of two following commands:

For Windows:
```
set FLASK_APP=<filename.py>
```
For Mac:
```
export FLASK_APP=<filename.py>
```

Then, type:
```
flask run
```

## Features

### Register ####
To access the web app, a user must have an account. New users can create their own personal accounts by entering their name, a valid email address, and a password. Once registered, the user's credentials are saved via MySQL Database and will allow the user to login at any time. 

### Login
Existing users who have made accounts can log into the web app to access its features. Once a user is logged in, they are redirected to the homepage where they will be able to create a task and logout.

### Logout 
Users who are logged into the web app are given the option to log out. Logging out will save the user's tasks/lists until the next login via database. 

### Create Task
Creating a task is the main feature of this web app. Here, users enter a task name, task description, and a date they would like to complete the task by. Once hitting the submit button, task will be stored to the database.

### View Tasks
Tasks after being created will be display in the homepage. After the users hit submit to create the new tasks, they will be immediately carried to he homepage to see what they've just created as well as the list of old tasks. Tasks displayed in the homepage will include the information the users input such as title, date, time, description.

### Edit Task
Users have the ability to fix any information of the task. By hitting the edit button below the task in the homepage, the edit form will be displayed to let the users decide what they want to keep and change. After hitting the submit button, it will go back to the homepage and display task after editting.  

### Delete Task
Users have the ability to delete task they no long want to keep track. By hitting the delete button below the task in the homepage, the task will be removed.

### Check Complete
In this feature, users have the ability to classify which tasks are finishes and which tasks are unfinished. The finished tasked will be displayed in a column beside the column storing unfinished tasks. It could help users know which tasks need to be completed.

### Send Message
Users have the ability to send a message to someone by entering email address.

## Built With

* [Python](https://www.python.org/) - An interpreted, high-level, general-purpose programming language.
* [JQuery](https://www.jquery.com) - A fast, small, and feature-rich JavaScript library.
* [MaterializeCSS](https://materializecss.com/) - A modern responsive front-end framework based on Material Design
* [Bootstrap](https://getbootstrap.com) - Responsive, mobile-first projects on the web with the world's most popular front-end component library

## Authors 

* **Emanual Donie Ypon** - *Initial work* - [Team8 - stuffToDo](https://github.com/donieypon/Team8)
* **Huan Tran** - *Initial work* - [Team8 - stuffToDo](https://github.com/donieypon/Team8)
* **Yenni Lam** - *Initial work* - [Team8 - stuffToDo](https://github.com/donieypon/Team8)
* **Tatsuya Hayashi** - *Initial work* - [Team8 - stuffToDo](https://github.com/donieypon/Team8)

## Lincense

This project is licensed under the MIT License.

# Travis CI

[![Build Status](https://travis-ci.com/donieypon/Team8.svg?branch=master)](https://travis-ci.com/donieypon/Team8)
