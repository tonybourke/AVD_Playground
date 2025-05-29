# FABRIC

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| FABRIC | l3leaf | leaf1 | 172.20.20.11/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf2 | 172.20.20.12/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf3 | 172.20.20.13/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf4 | 172.20.20.14/24 | cEOS-lab | Provisioned | - |
| FABRIC | spine | spine1 | 172.20.20.101/24 | cEOS-lab | Provisioned | - |
| FABRIC | spine | spine2 | 172.20.20.102/24 | cEOS-lab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | leaf1 | Ethernet3 | spine | spine1 | Ethernet3 |
| l3leaf | leaf1 | Ethernet4 | spine | spine2 | Ethernet3 |
| l3leaf | leaf2 | Ethernet3 | spine | spine1 | Ethernet4 |
| l3leaf | leaf2 | Ethernet4 | spine | spine2 | Ethernet4 |
| l3leaf | leaf3 | Ethernet3 | spine | spine1 | Ethernet5 |
| l3leaf | leaf3 | Ethernet4 | spine | spine2 | Ethernet5 |
| l3leaf | leaf4 | Ethernet3 | spine | spine1 | Ethernet6 |
| l3leaf | leaf4 | Ethernet4 | spine | spine2 | Ethernet6 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 192.168.108.0/22 | 1024 | 16 | 1.57 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| leaf1 | Ethernet3 | 192.168.108.1/31 | spine1 | Ethernet3 | 192.168.108.0/31 |
| leaf1 | Ethernet4 | 192.168.108.3/31 | spine2 | Ethernet3 | 192.168.108.2/31 |
| leaf2 | Ethernet3 | 192.168.108.5/31 | spine1 | Ethernet4 | 192.168.108.4/31 |
| leaf2 | Ethernet4 | 192.168.108.7/31 | spine2 | Ethernet4 | 192.168.108.6/31 |
| leaf3 | Ethernet3 | 192.168.108.9/31 | spine1 | Ethernet5 | 192.168.108.8/31 |
| leaf3 | Ethernet4 | 192.168.108.11/31 | spine2 | Ethernet5 | 192.168.108.10/31 |
| leaf4 | Ethernet3 | 192.168.108.13/31 | spine1 | Ethernet6 | 192.168.108.12/31 |
| leaf4 | Ethernet4 | 192.168.108.15/31 | spine2 | Ethernet6 | 192.168.108.14/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 192.168.101.0/24 | 256 | 6 | 2.35 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| FABRIC | leaf1 | 192.168.101.1/32 |
| FABRIC | leaf2 | 192.168.101.2/32 |
| FABRIC | leaf3 | 192.168.101.3/32 |
| FABRIC | leaf4 | 192.168.101.4/32 |
| FABRIC | spine1 | 192.168.101.101/32 |
| FABRIC | spine2 | 192.168.101.102/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |
| 192.168.102.0/24 | 256 | 4 | 1.57 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| FABRIC | leaf1 | 192.168.102.1/32 |
| FABRIC | leaf2 | 192.168.102.2/32 |
| FABRIC | leaf3 | 192.168.102.3/32 |
| FABRIC | leaf4 | 192.168.102.4/32 |
