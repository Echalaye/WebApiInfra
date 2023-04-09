dnf install mysql -y

dnf install pip -y

useradd -m -s /bin/bash apiuser

su - apiuser << EOF

pip install virtualenv

virtualenv ./env

source ./env/bin/activate

pip install flask

flask --app app.py run --debug