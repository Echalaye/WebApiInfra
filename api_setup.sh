pip install virtualenv
virtualenv ./env
source ./env/bin/activate
pip install flask
pip install mysql-connector
flask --app WebApiInfra/app.py run --host=10.110.1.13
