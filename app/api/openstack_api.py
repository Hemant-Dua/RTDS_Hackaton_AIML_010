import openstack
from app.config import OPENSTACK_CREDENTIALS

# Initialize OpenStack connection
conn = openstack.connect(**OPENSTACK_CREDENTIALS)

async def openstack_action(intent: str, params: dict):
    if intent == "create_vm":
        return await create_vm(params)
    elif intent == "resize_vm":
        return await resize_vm(params)
    elif intent == "delete_vm":
        return await delete_vm(params)
    else:
        return {"error": "Unknown action"}

async def create_vm(params: dict):
    # Example OpenStack call for creating a VM
    vm = conn.compute.create_server(name=params['name'], flavor=params['flavor'], image=params['image'])
    return {"status": "VM Created", "vm_id": vm.id}

async def resize_vm(params: dict):
    # Example OpenStack call to resize a VM
    server = conn.compute.get_server(params['vm_id'])
    conn.compute.resize_server(server, flavor=params['new_flavor'])
    return {"status": "VM Resized", "vm_id": server.id}

async def delete_vm(params: dict):
    # Example OpenStack call to delete a VM
    server = conn.compute.get_server(params['vm_id'])
    conn.compute.delete_server(server)
    return {"status": "VM Deleted"}
