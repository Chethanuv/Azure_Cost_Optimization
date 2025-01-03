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
    command = "az vm list --show-details --query \"[?powerState == 'VM deallocated' || powerState == 'VM stopped' ].{Name:name, ResourceGroup:resourceGroup, Location:location, State:powerState,SKU:hardwareProfile.vmSize, SizeInGB:storageProfile.osDisk.diskSizeGb}\" -o json"
    vms = run_az_command(command)
    
    with open('unused_vms.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name','ResourceGroup','Location','State','SKU','OSDiskSize']) #csv headers
        for vm in vms:
            writer.writerow([vm['Name'],vm['ResourceGroup'],vm['Location'],vm['State'],vm['SKU'],vm['SizeInGB']])
    print("Output saved to unused_vms.csv")
            
def unused_disks():
    print("Checking for unused disks...")
    command = "az disk list --query \"[?managedBy == null].{Name:name, ResourceGroup:resourceGroup, Location:location, SKU:sku.name, SizeInGB:diskSizeGB}\" -o json"
    disks = run_az_command(command)
    
    with open('unused_disks.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name','ResourceGroup','Location','SKU','Size']) #csv headers
        for disk in disks:
            writer.writerow([disk['Name'],disk['ResourceGroup'],disk['Location'],disk['SKU'],disk['SizeInGB']])
    print("Output saved to unused_disks.csv")
    
            
def unused_ips():
    print("Checking for unused public-IPs...")
    command = "az network public-ip list --query \"[?ipConfiguration == null].{Name:name, ResourceGroup:resourceGroup, Location:location, Type:sku.name, AllocationMethod:publicIPAllocationMethod}\" -o json"
    ips = run_az_command(command)
    
    with open('unused_ips.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name','ResourceGroup','Location','SKU','Type']) #csv headers
        for ip in ips:
            writer.writerow([ip['Name'],ip['ResourceGroup'],ip['Location'],ip['Type'],ip['AllocationMethod']])
    print("Output saved to unused_ips.csv")        
            
def main():
    unused_vms()
    unused_disks()
    unused_ips()
    
if __name__ == "__main__":
    main()