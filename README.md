# Azure Unused Resources Checker

This project automates the process of identifying unused Azure resources, including virtual machines (VMs), disks, and public IPs, to help optimize cloud costs. It consists of a Bash script (`check_azure.sh`) and a Python script (`azure_resources.py`) that work together to perform the checks and save the results to CSV files.

---

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)

---

## Features

- Automatically installs Azure CLI if not already installed.
- Checks if the user is logged into Azure before proceeding.
- Identifies unused Azure resources:
  - Stopped or deallocated virtual machines (VMs).
  - Unattached managed disks.
  - Unused public IPs.
- Saves the results to CSV files for further analysis.

---

## Requirements

- Python 3.6 or higher
- Bash shell (Linux/macOS/WSL on Windows)
- Valid Azure account credentials

---

## Usage

### 1. Clone the repository
First, clone this repository to your local machine:

```bash
git clone git@github.com:Chethanuv/My_Projects.git
cd My_projects
az login --use-device-code
bash check_azure.sh
python3 azure_resources.py (Optional)







