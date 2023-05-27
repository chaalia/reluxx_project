# Reluxx community project

Run the project using Docker:
 * docker-compose  up -d

## Run the project without Docker:
  - Create a virtual environment
    - python3 -m venv env_name
    - source env_name/bin/activate
    - pip3 install -r requirements.txt
    - In reluxx_project directory, make a copy for the file env.tpl file and add it to the same directory as .env
    - python3 manage.py migrate
    - python3 manage.py runserver
  - Or run the project using the script build.sh:
    - bash build.sh


### Run the tests:
    - python3 manage.py test


### Test the appliction using these credentials:
 user: admin
 password: complexpassword123


Production informations:
the django app is deployed on the server: render.com
The database is deployed on the server: elephantsql.com
