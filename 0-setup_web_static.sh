#!/usr/bin/env bash
# Bash script that sets up your web servers for deploymentof web_static
apt-get update
apt-get install -y nginx
mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
echo "<html>
    <head>
    </head>
    <body>
	Holberton School
    </body>
  </html>" | tee /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '53i \\tlocation \/hbnb_static {\n\t\t alias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
/etc/init.d/nginx restart
