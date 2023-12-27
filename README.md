# igti-pa
Repositório para projeto aplicado da pós de engenharia de dados do igti

# Criação de virtualenv

python -m venv /path/to/new/virtual/environment

source env/bin/activate

pip install poetry

poetry completions bash >> ~/.bash_completion

poetry run python your_script.py



# About the app

Basic Structure

    app.py: This file initializes the Dash app and contains global settings.

    layout.py: Contains the layout of the app (UI components).

    callbacks.py: Contains the callbacks for interactivity.

    data.py (or similar): Contains data processing, loading, and graph creation logic.

    assets/ folder: Contains CSS, JavaScript, and other static files.

    application.py: Main entry point for deployment (particularly for platforms like AWS Elastic Beanstalk).

Advantages of This Structure

    Modularity: Separating concerns into different files makes the code more manageable and scalable.
    Readability: Each file has a clear purpose, making it easier to understand and modify.
    Reusability: Components like data processing and graph creation can be reused in different parts of the application.

# Running locally
An .env file must be created at the root directory containing the following env vars:
AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''