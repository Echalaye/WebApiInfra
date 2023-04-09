pip install virtualenv

virtualenv ./env

source ./env/bin/activate

pip install flask

flask --app app.py run --debug