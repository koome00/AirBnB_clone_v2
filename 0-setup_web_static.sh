#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static


source_folder="/data/web_static/releases/test"
link_path="/data/web_static/current"
ADD_WEBSTATIC="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Mic Cheque 1..2..3" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf "$source_folder" "$link_path"
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i "35i $ADD_WEBSTATIC" /etc/nginx/sites-available/default
sudo service nginx restart
