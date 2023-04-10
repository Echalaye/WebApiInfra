dnf update -y
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="10.110.1.1" service name=ssh accept'
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="10.110.1.11" port port=3306 protocol=tcp accept'     
firewall-cmd --permanent --add-rich-rule='rule protocol value=icmp reject'
firewall-cmd --reload
dnf install mariadb-server -y
systemctl enable mariadb
systemctl start mariadb