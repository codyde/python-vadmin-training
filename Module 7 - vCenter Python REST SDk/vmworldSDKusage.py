import requests
import os
import urllib3
from vmware.vapi.vsphere.client import create_vsphere_client

# Ignore SSL Verification for Self Signed Certs
session = requests.session()
session.verify = False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Environmental Input
server = os.environ.get('vcenter')
username = os.environ.get('username')
password = os.environ.get('password')

# Connect to the vCenter Server
client = create_vsphere_client(server = server, username = username, password = password, session = session)

# Display VMHosts
client.vcenter.Host.list()

# Display VMs
client.vcenter.VM.list()

# Display Datastores
client.vcenter.Datastore.list()

# Display Single Datastore
client.vcenter.Datastore.get('datastore-13')

# Create Basic VM
from com.vmware.vcenter_client import VM

# Create VM Specification
vmSpec = VM.CreateSpec()

vmSpec
vmSpec.guest_os = 'WINDOWS_9_64'
vmSpec.name = 'CODE2219U'

# Create VM Placement Specification
placementSpec = VM.PlacementSpec()

#placementSpec
placementSpec.resource_pool = 'resgroup-8'
placementSpec.datastore = 'datastore-13'
placementSpec.folder = 'group-v9'

# Add Placement Specification to VM Specification 
vmSpec.placement = placementSpec

# Create new VM
newVM = client.vcenter.VM.create(vmSpec)

# Get VM Details
client.vcenter.VM.get(newVM)

# Get VM Power State
client.vcenter.vm.Power.get(newVM)

# Start VM 
client.vcenter.vm.Power.start(newVM)
client.vcenter.vm.Power.get(newVM)

# Stop VM
client.vcenter.vm.Power.stop(newVM)
client.vcenter.vm.Power.get(newVM)

# Remove VM
client.vcenter.VM.delete(newVM)
client.vcenter.VM.get(newVM)
