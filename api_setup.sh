pip install virtualenv

virtualenv ./env

source ./env/bin/activate

pip install flask

pip install mysql-connector

flask --app app.py run --host=10.110.1.11