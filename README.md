## Project and Task

This is a project to create a simple web application that allows users to create, read, update, and delete (CRUD) tasks. The application will be built using the Flask web framework and will use a SQLite database to store the tasks.

## Prerequisites

- Python 3.6 or later
- Django 3.0 or later

## Installation

1. Clone the repository
   ```bash
    git clone https://github.com/<Your_username>/Benmore.git
    ```
2. Create a virtual environment and activate it: 
- Linux and macOS
```bash
python -m venv venv 
source venv/bin/activate 
```
- Windows
Create a virtual environment

```bash
python -m venv venv 
```
Activate the virtual environment
```bash
venv\Scripts\activate 
```
3. Navigate to the project directory and create a .env file with the following content:
```bash
SECRET_KEY=your_secret_key
DEBUG=True
```
1. Install the required packages using pip:
```bash
pip install -r requirements.txt
```
## Usage

To run the application, use the following command:
```bash
python manage.py runserver
```
## Running the tests

To run the tests, use the following command:
```bash
python manage.py test
```

## NOTE: 
API.md file contains the API documentation for the application.