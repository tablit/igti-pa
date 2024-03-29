# igti-pa
Repositório para projeto aplicado da pós de engenharia de dados do igti

# Criação de virtualenv

python -m venv /path/to/new/virtual/environment

source env/bin/activate

pip install poetry

poetry build

poetry completions bash >> ~/.bash_completion

poetry run python your_script.py

# Export poetry setting to requirements.txt
poetry export -f requirements.txt --output requirements.txt

# Para interagir com o Elastic Beanstalk
pip install awsebcli


# Criação de aplicação no Elastic Beanstalke
eb init -p python-3.11 gandarela

# Criação de ambiente para a aplicação
eb create my-dash-env

# Deploy do elastic beanstalk
eb deploy

# About the app

Basic Structure blebous

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