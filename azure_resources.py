import json,csv,subprocess

def run_az_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True,check=True)
        return json.loads(result.stdout) if result.stdout else []
    except subprocess.CalledProcessError as e:
        print(f"Error running az command: {command}")
        print(f"Error: {e.stderr}")
        return []
    except Exception as e:  # Catch for any other errors
        print(f"General error: {e}")
        return []
    
    
def unused_vms():
    print("Checking for unused VMs...")
    command = "az vm list --show-details --query \"[?powerState == 'VM deallocated' || powerState == 'VM stopped' ].{Name:name, ResourceGroup:resourceGroup, Location:location, State:powerState}\" -o json"
    vms = run_az_command(command)
    
    with open('unused_vms.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name','ResourceGroup','Location','State']) #csv headers
        for vm in vms:
            writer.writerow([vm['Name'],vm['ResourceGroup'],vm['Location'],vm['State']])
    print("Output saved to unused_vms.csv")
            
def unused_disks():
    print("Checking for unused disks...")
    command = "az disk list --query \"[?managedBy == null].{Name:name, ResourceGroup:resourceGroup, Location:location}\" -o json"
    disks = run_az_command(command)
    
    with open('unused_disks.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name','ResourceGroup','Location']) #csv headers
        for disk in disks:
            writer.writerow([disk['Name'],disk['ResourceGroup'],disk['Location']])
    print("Output saved to unused_disks.csv")
    
            
def unused_ips():
    print("Checking for unused public-IPs...")
    command = "az network public-ip list --query \"[?ipConfiguration == null].{Name:name, ResourceGroup:resourceGroup, Location:location}\" -o json"
    ips = run_az_command(command)
    
    with open('unused_ips.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name','ResourceGroup','Location']) #csv headers
        for ip in ips:
            writer.writerow([ip['Name'],ip['ResourceGroup'],ip['Location']])
    print("Output saved to unused_ips.csv")        
            
def main():
    unused_vms()
    unused_disks()
    unused_ips()
    
if __name__ == "__main__":
    main()