## Flask Registration with Blog

Author: Nino Ross

## Description

This Flask application serves as a registration system with an integrated blog feature. The application uses Flask as the web framework, Flask-Login for user authentication, and Flask-SQLAlchemy for database management.

## Features

User Registration and Login: Users can register for an account and log in securely.

Integrated Blog: The application includes a blog feature where registered users can create, edit, and delete blog posts.

## Setup

**1.Environment Setup:**

Create a virtual environment and activate it.

Install dependencies using pip install -r requirements.txt.

**2.Database Initialization:**

The application uses an SQLite database. Run the following commands to initialize the database:

bash

Copy code

flask db init

flask db migrate

flask db upgrade

**3.Run the Application:**

Execute the Flask application with python app.py.

**4.Access the Application:**

Open a web browser and go to http://localhost:5000/ to access the application.

## Configuration

The application uses a SQLite database named users.db.

The SECRET_KEY is set to "helloworld" for securing session cookies.

## Dependencies

SQLAlchemy==2.0.5.post1

flask_sqlalchemy==3.0.3

greenlet==2.0.2

flask_login==0.6.2

bcrypt==4.0.1

flask_bcrypt==1.0.1


![editted](https://github.com/Chibdibs/flask_registration_with_blog/assets/9670771/e11d9e6d-9468-4cc5-95b7-7afd2c50fa51)
![Screenshot 2024-02-05 043747](https://github.com/Chibdibs/flask_registration_with_blog/assets/9670771/7e74af8b-4236-4a59-9906-f0aa80d11186)
![Screenshot 2024-02-05 043734](https://github.com/Chibdibs/flask_registration_with_blog/assets/9670771/a402c4db-49a8-4676-a63f-38ac397aecfe)
![Screenshot 2024-02-05 043014](https://github.com/Chibdibs/flask_registration_with_blog/assets/9670771/bede2a98-9d73-42d5-80f8-0b6c3efdc17a)
![Screenshot 2024-02-05 043003](https://github.com/Chibdibs/flask_registration_with_blog/assets/9670771/e24c5bb8-db01-4693-8770-8b77b47883ed)
![Screenshot 2024-02-05 042950](https://github.com/Chibdibs/flask_registration_with_blog/assets/9670771/a3b6e8d0-e46d-43f0-affb-21c42196c80f)
![Screenshot 2024-02-05 042910](https://github.com/Chibdibs/flask_registration_with_blog/assets/9670771/55e07cae-d833-4144-ae80-cbaff681c40e)
![Screenshot 2024-02-05 043028](https://github.com/Chibdibs/flask_registration_with_blog/assets/9670771/7e4e7f1c-9bcf-4830-90aa-6661300e2ac1)
