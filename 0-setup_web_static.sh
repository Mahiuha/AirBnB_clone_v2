#!/usr/bin/env bash
# Install nginx
sudo apt-get -y update
sudo apt-get -y install nginx

# Create the next folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#Create a fake HTML file
echo "Hi guys!!" >> /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content
sudo sed -i "/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/; }" /etc/nginx/sites-available/default

# Restart nginx
sudo service nginx restart

# Exit successfully
exit 0
