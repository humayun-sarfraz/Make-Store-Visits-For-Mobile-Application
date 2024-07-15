
Store Visit API

Overview

This project is a simple API for a mobile application that allows a customer’s field employee to record store visits. The API is built using Django and Django REST Framework.

Requirements

- Python 3.8+
- Django 4.2
- Django REST Framework
- MySQL or PostgreSQL

Setup Instructions

Step 1: Clone the Repository

Clone the repository from GitHub:

```sh
git clone https://github.com/yourusername/store-visit-api.git
cd store-visit-api
```

Step 2: Create and Activate Virtual Environment

Create a virtual environment and activate it:

On Windows

```sh
python -m venv env
env\Scripts ctivate
```

On macOS and Linux

```sh
python3 -m venv env
source env/bin/activate
```

Step 3: Install Dependencies

Install the required packages:

```sh
pip install -r requirements.txt
```

Step 4: Configure Database

Update the database configuration in `store_visit/settings.py` to use your MySQL or PostgreSQL database. For example:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # or 'django.db.backends.postgresql'
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'your_database_host',
        'PORT': 'your_database_port',
    }
}
```

Step 5: Apply Migrations

Apply the database migrations:

```sh
python manage.py makemigrations
python manage.py migrate
```

Step 6: Create a Superuser

Create a superuser to access the Django admin interface:

```sh
python manage.py createsuperuser
```

Follow the prompts to set the username, email, and password.

Step 7: Load Test Data

Load the test data into the database:

```sh
python manage.py loaddata test_data.json
```

Step 8: Run the Server

Start the development server:

```sh
python manage.py runserver
```

Step 9: Access the Admin Interface

Open your web browser and navigate to `http://127.0.0.1:8000/admin/`. Log in with the superuser credentials you created earlier.

API Endpoints

Authentication

All requests must include an authorization header with the format:

```plaintext
Authorization: Phone {employee phone number}
```

Endpoints

Get a List of Stores

URL: GET /api/stores/

Description: Retrieve a list of stores linked to the authenticated employee.

Response:

```json
[
    {
        "id": 1,
        "name": "Store 1",
        "employee": 1
    },
    {
        "id": 2,
        "name": "Store 2",
        "employee": 1
    }
]
```

Create a Visit

URL: POST /api/visits/

Description: Record a visit to a store.

Request Body:

```json
{
    "store_pk": 1,
    "latitude": 12.345678,
    "longitude": 98.765432
}
```

Response:

```json
{
    "id": 1,
    "date_time": "2023-07-15T12:34:56Z",
    "store": 1,
    "employee": 1,
    "latitude": 12.345678,
    "longitude": 98.765432
}
```

Admin Interface

The admin interface allows for creation, editing, and deletion of Employee, Store, and Visit records. It also includes search functionality for these models.

Project Structure

store-visit-api/
├── api/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── store_visit/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md

Testing

To run the tests, use the following command:

```sh
python manage.py test
```

Deployment

For deployment, make sure to set the appropriate environment variables and configure the database settings in settings.py. Additionally, collect static files using:

```sh
python manage.py collectstatic
```

Deploy the application using a WSGI server such as Gunicorn, and configure your web server (e.g., Nginx or Apache) to forward requests to the WSGI server.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Contact

