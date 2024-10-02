import yaml
import pyeapi

switch_file = open('switches.yml', 'r')
pyeapi.load_config('eapi.conf')

switch_dict = yaml.safe_load(switch_file)

connect = pyeapi.connect_to('clab-clos-large-leaf1')
running_config = connect.enable(["show running-config | json"])
print(running_config[0]['result'])
config_json = connect.enable(["show vlan | json"])

config_vlan = config_json[0]['result']['vlans']
is_svi = False
is_vxlan = False

for vlan in config_vlan:
    print(vlan)
    for interface in config_vlan[vlan]['interfaces']:
        if interface == 'Cpu':
            is_svi = True
        if interface == 'Vxlan1':
            is_vxlan = True
    print(f"VLAN {vlan} SVI: {is_svi}")
    print(f"VLAN {vlan} stretched: {is_svi}")
    

# for switch in switch_dict['switches']:
#     print(switch)
#     connect = pyeapi.connect_to(switch)
#     config_json = connect.enable(["show running-config | json"])
#     print(config_json[0]['result'])

