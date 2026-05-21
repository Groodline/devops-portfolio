#!/usr/bin/env bash
set -e

SITE_DIR="/var/www/devops-static-site"
NGINX_CONF="/etc/nginx/sites-available/devops-static-site"
NGINX_ENABLED="/etc/nginx/sites-enabled/devops-static-site"

echo "Creating site directory..."
sudo mkdir -p "$SITE_DIR"

echo "Copying index.html..."
sudo cp index.html "$SITE_DIR/index.html"

echo "Copying Nginx config..."
sudo cp nginx/devops-static-site.conf "$NGINX_CONF"

echo "Enabling Nginx site..."
sudo ln -sf "$NGINX_CONF" "$NGINX_ENABLED"

echo "Testing Nginx config..."
sudo nginx -t

echo "Reloading Nginx..."
sudo systemctl reload nginx

echo "Done. Open your server IP or domain in browser."
