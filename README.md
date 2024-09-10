# Django REST API

## Overview

This project is a Django REST API designed for [brief description of your project]. It includes functionalities for user login/signup, search, friend requests, and listing friends.

## Features

- User authentication and authorization
- Search functionality
- Friend requests
- List friends

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Django
- Django REST Framework
- Docker (for containerization)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ajith-te/accuknox_task.git
   cd accuknox_task


2. **Create a virtual environment and activate it**
   ```bash
    python -m venv venv
   ```bash
    source venv/bin/activate  # On Windows `venv\Scripts\activate`


4. **Install the required packages**
   ```bash
    pip install -r requirements.txt


6. **Run migrations**
   ```bash
    python manage.py migrate

   
8. **Create a superuser**
   ```bash
    python manage.py createsuperuser


10. **Start the development server:**
    ```bash
    python manage.py runserver


### Docker Setup

1. **Build the Docker image**
   ```bash
    docker build -t your-image-name .


3. **Run the Docker container**
   ```bash
    docker run -p 8000:8000 your-image-name


### API Endpoints

 - User Signup: POST /api/signup/
 - User Login: POST /api/login/
 - Search Users: GET /api/search/
 - Send Friend Request: POST /api/friend-request/
 - List Friends: GET /api/friends/
