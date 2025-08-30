Tweets

A simple web application to create, view, and manage tweets, built with Django. This project demonstrates basic CRUD operations and Django templates for a micro-blogging experience.

Features

Create new tweets

View all tweets in a card-style layout

Easy navigation and responsive design

Built using Django and Bootstrap

Tech Stack

Backend: Django

Frontend: HTML, CSS, Bootstrap

Database: SQLite (default Django DB)

Installation

Clone the repository:

git clone https://github.com/vikassharma878/tweets.git
cd tweets


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Run migrations:

python manage.py migrate


Start the development server:

python manage.py runserver


Open your browser and go to http://127.0.0.1:8000/

Usage

Click Create a tweet to add a new tweet

View all tweets on the homepage

Contributing

Fork the repository

Create a new branch (git checkout -b feature-name)

Commit your changes (git commit -m "Add feature")

Push to your branch (git push origin feature-name)

Open a Pull Request
