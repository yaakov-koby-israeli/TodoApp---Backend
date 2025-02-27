# TodoApp - Backend

## Overview

To-Do App is a task management application built with **FastAPI** and **SQLAlchemy**, featuring secure user authentication, role-based access control, and task management functionalities. Admins can manage all tasks, while users can create, update, and delete their own tasks.

## Features

- **User Authentication**: Secure login with JWT-based authentication and hashed passwords.
- **Role-Based Access Control**: Admins can manage all tasks, users can manage their own.
- **Task Management**: Create, update, delete, and retrieve to-dos.
- **FastAPI-Based Backend**: High-performance API using FastAPI and SQLAlchemy.
- **Secure Password Handling**: Uses hashed passwords with bcrypt.

## Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: SQLAlchemy + SQLite/PostgreSQL
- **Security**: JWT authentication, password hashing, role-based access control

## Project Structure

```
/todo-app
│── main.py           # FastAPI application setup
│── models.py         # Database models (Users, ToDos)
│── database.py       # SQLAlchemy setup and session management
│── routers/
│   ├── auth.py       # User authentication (JWT, login, registration)
│   ├── admin.py      # Admin functionalities (manage all tasks)
│   ├── users.py      # User functionalities (manage own tasks, change password)
│   ├── todos.py      # CRUD operations for to-dos
```

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yaakov-koby-israeli/todo-app.git
   cd todo-app
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
4. Start the backend server:
   ```sh
   uvicorn main:app --reload
   ```

## API Endpoints

### Authentication

- **POST `/auth/`** - Register a new user
- **POST `/auth/token`** - Authenticate user and generate JWT token

### Admin Functions

- **GET `/admin/todos`** - View all to-dos
- **DELETE `/admin/todo/{todo_id}`** - Delete any to-do

### User Functions

- **GET `/user/`** - View user profile
- **POST `/user/password`** - Change password
- **PUT `/todo/{todo_id}`** - Update a to-do
- **DELETE `/todo/{todo_id}`** - Delete a to-do

### To-Do Management

- **GET `/todo/{todo_id}`** - Retrieve a specific to-do
- **POST `/todo/`** - Create a new to-do
- **GET `/todos/`** - Retrieve all to-dos for the logged-in user

## Security Measures

- **JWT Authentication**: Secure token-based user authentication.
- **Role-Based Access Control**: Restricts admin and user functionalities.
- **Password Hashing**: User passwords are securely hashed using `passlib`.


## :hammer_and_wrench: Languages and Tools :
<div>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"  title="Python"  alt="python" width="50" height="50"/> 
  <img src="https://icon.icepanel.io/Technology/svg/FastAPI.svg" title="FastAPI" alt="FastAPI" width="50" height="50"/> 
  <img src="https://pbs.twimg.com/profile_images/1786389425678663680/zlm8fLps_400x400.png" title="PyCharm" alt="PyCharm" width="50" height="50"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/9/97/Sqlite-square-icon.svg" title="Sqlite" alt="Sqlite" width="50" height="50"/>   
<div/>







