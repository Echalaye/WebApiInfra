dnf update -y  
dnf install mysql -y  
dnf install pip -y   
firewall-cmd --add-port=5000/tcp --permanent
firewall-cmd --reload
