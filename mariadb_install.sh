dnf update -y
firewall-cmd --add-port=3306/tcp --permanent
firewall-cmd --reload
dnf install mariadb-server -y
systemctl enable mariadb
systemctl start mariadb