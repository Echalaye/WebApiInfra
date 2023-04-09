dnf update -y
dnf install nginx -y
firewall-cmd --add-port=80/tcp --permanent
firewall-cmd --reload
touch /etc/nginx/conf.d/nginx.conf
echo "server {
    server_name flaskweb;

    listen 80;

    location / {

        proxy_set_header  Host $host;
        proxy_set_header  X-Real-IP $remote_addr;
        proxy_set_header  X-Forwarded-Proto https;
        proxy_set_header  X-Forwarded-Host $remote_addr;
        proxy_set_header  X-Forwarded-For $proxy_add_x_forwarded_for;

        proxy_pass http://10.110.1.11:5000;
    }
}" | tee /etc/nginx/conf.d/nginx.conf > /dev/null
systemctl start nginx
systemctl enable nginx