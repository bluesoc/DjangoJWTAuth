# Django JWT Authentication API

## Overview

This repository contains a comprehensive authentication system built with Django that utilizes JSON Web Tokens (JWT) for token-based authentication.This implementation allows for secure token authentication and session management, making it suitable for modern web applications.

You can find the full, step-by-step building guide [here](https://renandev.hashnode.dev/django-and-jwt-how-to-set-up-a-secure-authentication-system).

## Features

- User registration and login
- Token-based authentication using JWT
- Secure access to private endpoints
- Easy integration with frontend applications

## Table of Endpoints

| Method | Endpoint       | Description                        |
|--------|----------------|------------------------------------|
| POST   | `/register`| Register a new user               |
| POST   | `/login`   | Authenticate user and receive a JWT |
| GET    | `/private` | Access a protected resource (requires authentication) |

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/bluesoc/DjangoJWTAuth.git

    cd DjangoJWTAuth/
    ```

2. **Create a virtual environment (optional but highly recommended):**

    ```bash
    python -m venv venv

    source venv/bin/activate
    ```

2. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run database migrations:**

    ```bash
    python manage.py makemigrations

    python manage.py migrate
    ```

4. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage:

To register a new user, you can send a POST request to `/register` with the following JSON payload:

```json
{
  "username": "user_username",
  "password": "user_password",
  "email": "your_email@example.com"
}
```

## Login

To log in, send a POST request to `/login` with the following JSON payload:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

But please ensure that you have registered in advance.

Upon successful login, you will receive a JWT token that you can use for authentication in subsequent requests.

### Accessing the `private` Endpoint

To access the protected view, send a GET request to `/private` with the JWT token included in the authorization header, this can be done with curl:

```bash
curl -H "Authorization: Bearer <YOUR-TOKEN>" http://localhost:8000/private/
```

You should see the following greeting message:

```JSON
{"message":"Access Granted!"}
```

## Documentation

You can find the full, step-by-step building guide [here](https://renandev.hashnode.dev/django-and-jwt-how-to-set-up-a-secure-authentication-system).