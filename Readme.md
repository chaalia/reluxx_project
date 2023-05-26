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


### Run the tests:
    - python3 manage.py test   