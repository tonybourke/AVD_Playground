

rack_id = 4
l_id = 7
r_id = 8
vlan_list_1 = "10, 20, 30, 40, 50"
vlan_list_2 = "100, 200, 300, 400"
vlan_list_3 = "1000, 1001, 1002, 1003, 1004, 1005, 1006"

while rack_id <= 25:
    file_name = "group_vars/RACK_" + str(rack_id) + ".yml"
    file = open(file_name, "w")
    file.write("network_ports:\n")
    port_id = 7
    while port_id < 15:
        file.write(f"  - switches: [clab-clos-large-leaf{l_id}, clab-clos-large-leaf{r_id}]\n")
        file.write(f"    switch_ports: [Ethernet{port_id}, Ethernet{port_id}]\n")
        file.write(f"    vlans: \"{vlan_list_1}\"\n")
        file.write(f"    enabled: true\n")
        file.write(f"    port_channel:\n") 
        file.write(f"      mode: active\n")
        port_id += 1
    while port_id < 23:
        file.write(f"  - switches: [clab-clos-large-leaf{l_id}, clab-clos-large-leaf{r_id}]\n")
        file.write(f"    switch_ports: [Ethernet{port_id}, Ethernet{port_id}]\n")
        file.write(f"    vlans: \"{vlan_list_2}\"\n")
        file.write(f"    enabled: true\n")
        file.write(f"    port_channel:\n") 
        file.write(f"      mode: active\n")
        port_id += 1
    while port_id <= 30:
        file.write(f"  - switches: [clab-clos-large-leaf{l_id}, clab-clos-large-leaf{r_id}]\n")
        file.write(f"    switch_ports: [Ethernet{port_id}, Ethernet{port_id}]\n")
        file.write(f"    vlans: \"{vlan_list_3}\"\n")
        file.write(f"    enabled: true\n")
        file.write(f"    port_channel:\n") 
        file.write(f"      mode: active\n")
        port_id += 1
    file.close
    l_id += 2
    r_id += 2
    rack_id += 1


        