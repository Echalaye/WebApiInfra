dnf update -y  
dnf install mysql -y  
dnf install pip -y  
dnf install git -y  
git clone https://github.com/Echalaye/WebApiInfra.git  
firewall-cmd --add-port=5000/tcp --permanent
firewall-cmd --reload
