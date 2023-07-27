from collections import defaultdict

from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager

def get_hosts_from_group():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources="/home/sasano8/projects/jetson-sample/infratool/inventry/hosts.development.yml")
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # Get hosts from specific group
    for group, hosts in inventory.get_groups_dict().items():
        if group == "all":
            continue
        
        yield group, hosts


def make_spec():
    data = defaultdict(set)
    for group, hosts in get_hosts_from_group():
        for host in hosts:
            data[host].add(group)
    "ungrouped"
            
    return data


data = dict(make_spec())
print(data)
