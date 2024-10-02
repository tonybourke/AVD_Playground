
left_id = 21
right_id = left_id + 1
mlag_id = 1

# MLAG Connections 

print("# MLAG Connections")
while left_id < 51:
    print(f"    - endpoints: [\"leaf{left_id}:eth{mlag_id}\", \"leaf{right_id}:eth{mlag_id}\"]")
    

    if mlag_id == 1:
        mlag_id = 2
    else:
        left_id = left_id + 2
        right_id = right_id + 2
        mlag_id = 1
print("")
print("# Spines connections")


leaf_id = 21
spine_id = 0
port_id = leaf_id + 1
while spine_id < 3:
    spine_id = spine_id + 1
    while leaf_id <= 50:
        print(f"     - endpoints: [\"leaf{leaf_id}:eth3\", \"spine{spine_id}:eth{port_id}\"]")
        leaf_id = leaf_id + 1
        port_id = port_id + 1
    leaf_id = 21
    port_id = leaf_id + 1
    print("")


# Section for containerlab

leaf_id = 21
while leaf_id <= 50:
    mgmt_ip = leaf_id + 10
    print(f"leaf{leaf_id}:")
    print("  kind: ceos")
    print("  image: ceos:4.32.0F")
    print(f"  mgmt-ipv4: 172.20.20.{mgmt_ip}")
    leaf_id += 1

# Section for AVD

mlag_group = 1
leaf_id = 1
mgmt_ip = leaf_id + 10
int_id = 2

while mlag_group <= 25:
    print(f"- group: mlag{mlag_group}")
    print(f"  nodes:")
    print(f"    - name: clab-clos-large-leaf{leaf_id}")
    print(f"      id: {leaf_id}")
    print(f"      mgmt_ip: 172.20.20.{mgmt_ip}/24")
    print(f"      uplink_switch_interfaces: [Ethernet{int_id}, Ethernet{int_id}, Ethernet{int_id}]")
    leaf_id += 1
    mgmt_ip += 1
    int_id += 1
    print(f"    - name: clab-clos-large-leaf{leaf_id}")
    print(f"      id: {leaf_id}")
    print(f"      mgmt_ip: 172.20.20.{mgmt_ip}/24")
    print(f"      uplink_switch_interfaces: [Ethernet{int_id}, Ethernet{int_id}, Ethernet{int_id}]")
    int_id += 1
    leaf_id += 1
    mgmt_ip += 1
    mlag_group += 1




rack_id = 1
l = 1
r = 2
while rack_id <= 25:
    print(f"RACK_{rack_id}:")
    print(f"  hosts:")
    print(f"    clab-clos-large-leaf[{l}:{r}]:")
    l += 2
    r += 2
    rack_id += 1