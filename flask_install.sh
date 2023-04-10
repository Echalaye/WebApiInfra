dnf update -y  
dnf install mysql -y  
dnf install pip -y   
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="10.110.1.1" service name=ssh accept'
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="10.110.1.13" port port=5000 protocol=tcp accept'     
firewall-cmd --permanent --add-rich-rule='rule protocol value=icmp reject'
firewall-cmd --reload
