#!/usr/bin/env bash
set -e

echo "Updating packages..."
sudo apt update

echo "Installing required packages..."
sudo apt install -y ca-certificates curl git ufw

echo "Installing Docker..."
curl -fsSL https://get.docker.com | sh

echo "Adding current user to docker group..."
sudo usermod -aG docker "$USER"

echo "Enabling firewall..."
sudo ufw allow OpenSSH
sudo ufw allow 80/tcp
sudo ufw --force enable

echo "Done. Re-login to SSH for docker group changes to apply."
