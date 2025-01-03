#!/bin/bash

# Check if Azure CLI is installed
echo "Checking if Azure CLI is installed..."
if ! command -v az &> /dev/null; then
    echo -n "Azure CLI is not installed. Do you want to install it? (y/n): "
    read -r response 
        
    if [ "$response" = "y" ]; then
        echo "Installing Azure CLI..."
        curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
    else
        echo "Exiting..."
        exit 1
    fi
fi
echo "Azure CLI is installed."

# Check if logged in to Azure
echo "Checking if logged in to Azure..."
if ! az account show &> /dev/null; then
    echo "Please login to Azure first using: 'az login --use-device-code' and re-run the script."
    exit 1
fi
echo "Logged in to Azure."
# Run the Python script
python3 azure_resources.py