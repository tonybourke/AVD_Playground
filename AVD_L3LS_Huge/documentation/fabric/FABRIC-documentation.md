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
| FABRIC | l3leaf | clab-clos-large-borderleaf1 | 172.20.20.91/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-borderleaf2 | 172.20.20.92/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf1 | 172.20.20.11/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf2 | 172.20.20.12/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf3 | 172.20.20.13/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf4 | 172.20.20.14/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf5 | 172.20.20.15/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf6 | 172.20.20.16/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf7 | 172.20.20.17/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf8 | 172.20.20.18/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf9 | 172.20.20.19/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf10 | 172.20.20.20/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf11 | 172.20.20.21/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf12 | 172.20.20.22/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf13 | 172.20.20.23/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf14 | 172.20.20.24/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf15 | 172.20.20.25/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf16 | 172.20.20.26/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf17 | 172.20.20.27/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf18 | 172.20.20.28/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf19 | 172.20.20.29/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf20 | 172.20.20.30/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf21 | 172.20.20.31/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf22 | 172.20.20.32/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf23 | 172.20.20.33/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf24 | 172.20.20.34/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf25 | 172.20.20.35/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf26 | 172.20.20.36/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf27 | 172.20.20.37/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf28 | 172.20.20.38/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf29 | 172.20.20.39/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf30 | 172.20.20.40/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf31 | 172.20.20.41/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf32 | 172.20.20.42/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf33 | 172.20.20.43/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf34 | 172.20.20.44/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf35 | 172.20.20.45/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf36 | 172.20.20.46/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf37 | 172.20.20.47/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf38 | 172.20.20.48/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf39 | 172.20.20.49/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf40 | 172.20.20.50/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf41 | 172.20.20.51/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf42 | 172.20.20.52/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf43 | 172.20.20.53/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf44 | 172.20.20.54/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf45 | 172.20.20.55/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf46 | 172.20.20.56/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf47 | 172.20.20.57/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf48 | 172.20.20.58/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf49 | 172.20.20.59/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | clab-clos-large-leaf50 | 172.20.20.60/24 | cEOS-lab | Provisioned | - |
| FABRIC | spine | clab-clos-large-spine1 | 172.20.20.101/24 | cEOS-lab | Provisioned | - |
| FABRIC | spine | clab-clos-large-spine2 | 172.20.20.102/24 | cEOS-lab | Provisioned | - |
| FABRIC | spine | clab-clos-large-spine3 | 172.20.20.103/24 | cEOS-lab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | clab-clos-large-borderleaf1 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet52 |
| l3leaf | clab-clos-large-borderleaf1 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet52 |
| l3leaf | clab-clos-large-borderleaf1 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet52 |
| l3leaf | clab-clos-large-borderleaf2 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet53 |
| l3leaf | clab-clos-large-borderleaf2 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet53 |
| l3leaf | clab-clos-large-borderleaf2 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet53 |
| l3leaf | clab-clos-large-leaf1 | Ethernet1 | mlag_peer | clab-clos-large-leaf2 | Ethernet1 |
| l3leaf | clab-clos-large-leaf1 | Ethernet2 | mlag_peer | clab-clos-large-leaf2 | Ethernet2 |
| l3leaf | clab-clos-large-leaf1 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet2 |
| l3leaf | clab-clos-large-leaf1 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet2 |
| l3leaf | clab-clos-large-leaf1 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet2 |
| l3leaf | clab-clos-large-leaf2 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet3 |
| l3leaf | clab-clos-large-leaf2 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet3 |
| l3leaf | clab-clos-large-leaf2 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet3 |
| l3leaf | clab-clos-large-leaf3 | Ethernet1 | mlag_peer | clab-clos-large-leaf4 | Ethernet1 |
| l3leaf | clab-clos-large-leaf3 | Ethernet2 | mlag_peer | clab-clos-large-leaf4 | Ethernet2 |
| l3leaf | clab-clos-large-leaf3 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet4 |
| l3leaf | clab-clos-large-leaf3 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet4 |
| l3leaf | clab-clos-large-leaf3 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet4 |
| l3leaf | clab-clos-large-leaf4 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet5 |
| l3leaf | clab-clos-large-leaf4 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet5 |
| l3leaf | clab-clos-large-leaf4 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet5 |
| l3leaf | clab-clos-large-leaf5 | Ethernet1 | mlag_peer | clab-clos-large-leaf6 | Ethernet1 |
| l3leaf | clab-clos-large-leaf5 | Ethernet2 | mlag_peer | clab-clos-large-leaf6 | Ethernet2 |
| l3leaf | clab-clos-large-leaf5 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet6 |
| l3leaf | clab-clos-large-leaf5 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet6 |
| l3leaf | clab-clos-large-leaf5 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet6 |
| l3leaf | clab-clos-large-leaf6 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet7 |
| l3leaf | clab-clos-large-leaf6 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet7 |
| l3leaf | clab-clos-large-leaf6 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet7 |
| l3leaf | clab-clos-large-leaf7 | Ethernet1 | mlag_peer | clab-clos-large-leaf8 | Ethernet1 |
| l3leaf | clab-clos-large-leaf7 | Ethernet2 | mlag_peer | clab-clos-large-leaf8 | Ethernet2 |
| l3leaf | clab-clos-large-leaf7 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet8 |
| l3leaf | clab-clos-large-leaf7 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet8 |
| l3leaf | clab-clos-large-leaf7 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet8 |
| l3leaf | clab-clos-large-leaf8 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet9 |
| l3leaf | clab-clos-large-leaf8 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet9 |
| l3leaf | clab-clos-large-leaf8 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet9 |
| l3leaf | clab-clos-large-leaf9 | Ethernet1 | mlag_peer | clab-clos-large-leaf10 | Ethernet1 |
| l3leaf | clab-clos-large-leaf9 | Ethernet2 | mlag_peer | clab-clos-large-leaf10 | Ethernet2 |
| l3leaf | clab-clos-large-leaf9 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet10 |
| l3leaf | clab-clos-large-leaf9 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet10 |
| l3leaf | clab-clos-large-leaf9 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet10 |
| l3leaf | clab-clos-large-leaf10 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet11 |
| l3leaf | clab-clos-large-leaf10 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet11 |
| l3leaf | clab-clos-large-leaf10 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet11 |
| l3leaf | clab-clos-large-leaf11 | Ethernet1 | mlag_peer | clab-clos-large-leaf12 | Ethernet1 |
| l3leaf | clab-clos-large-leaf11 | Ethernet2 | mlag_peer | clab-clos-large-leaf12 | Ethernet2 |
| l3leaf | clab-clos-large-leaf11 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet12 |
| l3leaf | clab-clos-large-leaf11 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet12 |
| l3leaf | clab-clos-large-leaf11 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet12 |
| l3leaf | clab-clos-large-leaf12 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet13 |
| l3leaf | clab-clos-large-leaf12 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet13 |
| l3leaf | clab-clos-large-leaf12 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet13 |
| l3leaf | clab-clos-large-leaf13 | Ethernet1 | mlag_peer | clab-clos-large-leaf14 | Ethernet1 |
| l3leaf | clab-clos-large-leaf13 | Ethernet2 | mlag_peer | clab-clos-large-leaf14 | Ethernet2 |
| l3leaf | clab-clos-large-leaf13 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet14 |
| l3leaf | clab-clos-large-leaf13 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet14 |
| l3leaf | clab-clos-large-leaf13 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet14 |
| l3leaf | clab-clos-large-leaf14 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet15 |
| l3leaf | clab-clos-large-leaf14 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet15 |
| l3leaf | clab-clos-large-leaf14 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet15 |
| l3leaf | clab-clos-large-leaf15 | Ethernet1 | mlag_peer | clab-clos-large-leaf16 | Ethernet1 |
| l3leaf | clab-clos-large-leaf15 | Ethernet2 | mlag_peer | clab-clos-large-leaf16 | Ethernet2 |
| l3leaf | clab-clos-large-leaf15 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet16 |
| l3leaf | clab-clos-large-leaf15 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet16 |
| l3leaf | clab-clos-large-leaf15 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet16 |
| l3leaf | clab-clos-large-leaf16 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet17 |
| l3leaf | clab-clos-large-leaf16 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet17 |
| l3leaf | clab-clos-large-leaf16 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet17 |
| l3leaf | clab-clos-large-leaf17 | Ethernet1 | mlag_peer | clab-clos-large-leaf18 | Ethernet1 |
| l3leaf | clab-clos-large-leaf17 | Ethernet2 | mlag_peer | clab-clos-large-leaf18 | Ethernet2 |
| l3leaf | clab-clos-large-leaf17 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet18 |
| l3leaf | clab-clos-large-leaf17 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet18 |
| l3leaf | clab-clos-large-leaf17 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet18 |
| l3leaf | clab-clos-large-leaf18 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet19 |
| l3leaf | clab-clos-large-leaf18 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet19 |
| l3leaf | clab-clos-large-leaf18 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet19 |
| l3leaf | clab-clos-large-leaf19 | Ethernet1 | mlag_peer | clab-clos-large-leaf20 | Ethernet1 |
| l3leaf | clab-clos-large-leaf19 | Ethernet2 | mlag_peer | clab-clos-large-leaf20 | Ethernet2 |
| l3leaf | clab-clos-large-leaf19 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet20 |
| l3leaf | clab-clos-large-leaf19 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet20 |
| l3leaf | clab-clos-large-leaf19 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet20 |
| l3leaf | clab-clos-large-leaf20 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet21 |
| l3leaf | clab-clos-large-leaf20 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet21 |
| l3leaf | clab-clos-large-leaf20 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet21 |
| l3leaf | clab-clos-large-leaf21 | Ethernet1 | mlag_peer | clab-clos-large-leaf22 | Ethernet1 |
| l3leaf | clab-clos-large-leaf21 | Ethernet2 | mlag_peer | clab-clos-large-leaf22 | Ethernet2 |
| l3leaf | clab-clos-large-leaf21 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet22 |
| l3leaf | clab-clos-large-leaf21 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet22 |
| l3leaf | clab-clos-large-leaf21 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet22 |
| l3leaf | clab-clos-large-leaf22 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet23 |
| l3leaf | clab-clos-large-leaf22 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet23 |
| l3leaf | clab-clos-large-leaf22 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet23 |
| l3leaf | clab-clos-large-leaf23 | Ethernet1 | mlag_peer | clab-clos-large-leaf24 | Ethernet1 |
| l3leaf | clab-clos-large-leaf23 | Ethernet2 | mlag_peer | clab-clos-large-leaf24 | Ethernet2 |
| l3leaf | clab-clos-large-leaf23 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet24 |
| l3leaf | clab-clos-large-leaf23 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet24 |
| l3leaf | clab-clos-large-leaf23 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet24 |
| l3leaf | clab-clos-large-leaf24 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet25 |
| l3leaf | clab-clos-large-leaf24 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet25 |
| l3leaf | clab-clos-large-leaf24 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet25 |
| l3leaf | clab-clos-large-leaf25 | Ethernet1 | mlag_peer | clab-clos-large-leaf26 | Ethernet1 |
| l3leaf | clab-clos-large-leaf25 | Ethernet2 | mlag_peer | clab-clos-large-leaf26 | Ethernet2 |
| l3leaf | clab-clos-large-leaf25 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet26 |
| l3leaf | clab-clos-large-leaf25 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet26 |
| l3leaf | clab-clos-large-leaf25 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet26 |
| l3leaf | clab-clos-large-leaf26 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet27 |
| l3leaf | clab-clos-large-leaf26 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet27 |
| l3leaf | clab-clos-large-leaf26 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet27 |
| l3leaf | clab-clos-large-leaf27 | Ethernet1 | mlag_peer | clab-clos-large-leaf28 | Ethernet1 |
| l3leaf | clab-clos-large-leaf27 | Ethernet2 | mlag_peer | clab-clos-large-leaf28 | Ethernet2 |
| l3leaf | clab-clos-large-leaf27 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet28 |
| l3leaf | clab-clos-large-leaf27 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet28 |
| l3leaf | clab-clos-large-leaf27 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet28 |
| l3leaf | clab-clos-large-leaf28 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet29 |
| l3leaf | clab-clos-large-leaf28 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet29 |
| l3leaf | clab-clos-large-leaf28 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet29 |
| l3leaf | clab-clos-large-leaf29 | Ethernet1 | mlag_peer | clab-clos-large-leaf30 | Ethernet1 |
| l3leaf | clab-clos-large-leaf29 | Ethernet2 | mlag_peer | clab-clos-large-leaf30 | Ethernet2 |
| l3leaf | clab-clos-large-leaf29 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet30 |
| l3leaf | clab-clos-large-leaf29 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet30 |
| l3leaf | clab-clos-large-leaf29 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet30 |
| l3leaf | clab-clos-large-leaf30 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet31 |
| l3leaf | clab-clos-large-leaf30 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet31 |
| l3leaf | clab-clos-large-leaf30 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet31 |
| l3leaf | clab-clos-large-leaf31 | Ethernet1 | mlag_peer | clab-clos-large-leaf32 | Ethernet1 |
| l3leaf | clab-clos-large-leaf31 | Ethernet2 | mlag_peer | clab-clos-large-leaf32 | Ethernet2 |
| l3leaf | clab-clos-large-leaf31 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet32 |
| l3leaf | clab-clos-large-leaf31 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet32 |
| l3leaf | clab-clos-large-leaf31 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet32 |
| l3leaf | clab-clos-large-leaf32 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet33 |
| l3leaf | clab-clos-large-leaf32 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet33 |
| l3leaf | clab-clos-large-leaf32 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet33 |
| l3leaf | clab-clos-large-leaf33 | Ethernet1 | mlag_peer | clab-clos-large-leaf34 | Ethernet1 |
| l3leaf | clab-clos-large-leaf33 | Ethernet2 | mlag_peer | clab-clos-large-leaf34 | Ethernet2 |
| l3leaf | clab-clos-large-leaf33 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet34 |
| l3leaf | clab-clos-large-leaf33 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet34 |
| l3leaf | clab-clos-large-leaf33 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet34 |
| l3leaf | clab-clos-large-leaf34 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet35 |
| l3leaf | clab-clos-large-leaf34 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet35 |
| l3leaf | clab-clos-large-leaf34 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet35 |
| l3leaf | clab-clos-large-leaf35 | Ethernet1 | mlag_peer | clab-clos-large-leaf36 | Ethernet1 |
| l3leaf | clab-clos-large-leaf35 | Ethernet2 | mlag_peer | clab-clos-large-leaf36 | Ethernet2 |
| l3leaf | clab-clos-large-leaf35 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet36 |
| l3leaf | clab-clos-large-leaf35 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet36 |
| l3leaf | clab-clos-large-leaf35 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet36 |
| l3leaf | clab-clos-large-leaf36 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet37 |
| l3leaf | clab-clos-large-leaf36 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet37 |
| l3leaf | clab-clos-large-leaf36 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet37 |
| l3leaf | clab-clos-large-leaf37 | Ethernet1 | mlag_peer | clab-clos-large-leaf38 | Ethernet1 |
| l3leaf | clab-clos-large-leaf37 | Ethernet2 | mlag_peer | clab-clos-large-leaf38 | Ethernet2 |
| l3leaf | clab-clos-large-leaf37 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet38 |
| l3leaf | clab-clos-large-leaf37 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet38 |
| l3leaf | clab-clos-large-leaf37 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet38 |
| l3leaf | clab-clos-large-leaf38 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet39 |
| l3leaf | clab-clos-large-leaf38 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet39 |
| l3leaf | clab-clos-large-leaf38 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet39 |
| l3leaf | clab-clos-large-leaf39 | Ethernet1 | mlag_peer | clab-clos-large-leaf40 | Ethernet1 |
| l3leaf | clab-clos-large-leaf39 | Ethernet2 | mlag_peer | clab-clos-large-leaf40 | Ethernet2 |
| l3leaf | clab-clos-large-leaf39 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet40 |
| l3leaf | clab-clos-large-leaf39 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet40 |
| l3leaf | clab-clos-large-leaf39 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet40 |
| l3leaf | clab-clos-large-leaf40 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet41 |
| l3leaf | clab-clos-large-leaf40 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet41 |
| l3leaf | clab-clos-large-leaf40 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet41 |
| l3leaf | clab-clos-large-leaf41 | Ethernet1 | mlag_peer | clab-clos-large-leaf42 | Ethernet1 |
| l3leaf | clab-clos-large-leaf41 | Ethernet2 | mlag_peer | clab-clos-large-leaf42 | Ethernet2 |
| l3leaf | clab-clos-large-leaf41 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet42 |
| l3leaf | clab-clos-large-leaf41 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet42 |
| l3leaf | clab-clos-large-leaf41 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet42 |
| l3leaf | clab-clos-large-leaf42 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet43 |
| l3leaf | clab-clos-large-leaf42 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet43 |
| l3leaf | clab-clos-large-leaf42 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet43 |
| l3leaf | clab-clos-large-leaf43 | Ethernet1 | mlag_peer | clab-clos-large-leaf44 | Ethernet1 |
| l3leaf | clab-clos-large-leaf43 | Ethernet2 | mlag_peer | clab-clos-large-leaf44 | Ethernet2 |
| l3leaf | clab-clos-large-leaf43 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet44 |
| l3leaf | clab-clos-large-leaf43 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet44 |
| l3leaf | clab-clos-large-leaf43 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet44 |
| l3leaf | clab-clos-large-leaf44 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet45 |
| l3leaf | clab-clos-large-leaf44 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet45 |
| l3leaf | clab-clos-large-leaf44 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet45 |
| l3leaf | clab-clos-large-leaf45 | Ethernet1 | mlag_peer | clab-clos-large-leaf46 | Ethernet1 |
| l3leaf | clab-clos-large-leaf45 | Ethernet2 | mlag_peer | clab-clos-large-leaf46 | Ethernet2 |
| l3leaf | clab-clos-large-leaf45 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet46 |
| l3leaf | clab-clos-large-leaf45 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet46 |
| l3leaf | clab-clos-large-leaf45 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet46 |
| l3leaf | clab-clos-large-leaf46 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet47 |
| l3leaf | clab-clos-large-leaf46 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet47 |
| l3leaf | clab-clos-large-leaf46 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet47 |
| l3leaf | clab-clos-large-leaf47 | Ethernet1 | mlag_peer | clab-clos-large-leaf48 | Ethernet1 |
| l3leaf | clab-clos-large-leaf47 | Ethernet2 | mlag_peer | clab-clos-large-leaf48 | Ethernet2 |
| l3leaf | clab-clos-large-leaf47 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet48 |
| l3leaf | clab-clos-large-leaf47 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet48 |
| l3leaf | clab-clos-large-leaf47 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet48 |
| l3leaf | clab-clos-large-leaf48 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet49 |
| l3leaf | clab-clos-large-leaf48 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet49 |
| l3leaf | clab-clos-large-leaf48 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet49 |
| l3leaf | clab-clos-large-leaf49 | Ethernet1 | mlag_peer | clab-clos-large-leaf50 | Ethernet1 |
| l3leaf | clab-clos-large-leaf49 | Ethernet2 | mlag_peer | clab-clos-large-leaf50 | Ethernet2 |
| l3leaf | clab-clos-large-leaf49 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet50 |
| l3leaf | clab-clos-large-leaf49 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet50 |
| l3leaf | clab-clos-large-leaf49 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet50 |
| l3leaf | clab-clos-large-leaf50 | Ethernet3 | spine | clab-clos-large-spine1 | Ethernet51 |
| l3leaf | clab-clos-large-leaf50 | Ethernet4 | spine | clab-clos-large-spine2 | Ethernet51 |
| l3leaf | clab-clos-large-leaf50 | Ethernet5 | spine | clab-clos-large-spine3 | Ethernet51 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 192.168.108.0/22 | 1024 | 0 | 0.0 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 192.168.101.0/24 | 256 | 55 | 21.49 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| FABRIC | clab-clos-large-borderleaf1 | 192.168.101.91/32 |
| FABRIC | clab-clos-large-borderleaf2 | 192.168.101.92/32 |
| FABRIC | clab-clos-large-leaf1 | 192.168.101.1/32 |
| FABRIC | clab-clos-large-leaf2 | 192.168.101.2/32 |
| FABRIC | clab-clos-large-leaf3 | 192.168.101.3/32 |
| FABRIC | clab-clos-large-leaf4 | 192.168.101.4/32 |
| FABRIC | clab-clos-large-leaf5 | 192.168.101.5/32 |
| FABRIC | clab-clos-large-leaf6 | 192.168.101.6/32 |
| FABRIC | clab-clos-large-leaf7 | 192.168.101.7/32 |
| FABRIC | clab-clos-large-leaf8 | 192.168.101.8/32 |
| FABRIC | clab-clos-large-leaf9 | 192.168.101.9/32 |
| FABRIC | clab-clos-large-leaf10 | 192.168.101.10/32 |
| FABRIC | clab-clos-large-leaf11 | 192.168.101.11/32 |
| FABRIC | clab-clos-large-leaf12 | 192.168.101.12/32 |
| FABRIC | clab-clos-large-leaf13 | 192.168.101.13/32 |
| FABRIC | clab-clos-large-leaf14 | 192.168.101.14/32 |
| FABRIC | clab-clos-large-leaf15 | 192.168.101.15/32 |
| FABRIC | clab-clos-large-leaf16 | 192.168.101.16/32 |
| FABRIC | clab-clos-large-leaf17 | 192.168.101.17/32 |
| FABRIC | clab-clos-large-leaf18 | 192.168.101.18/32 |
| FABRIC | clab-clos-large-leaf19 | 192.168.101.19/32 |
| FABRIC | clab-clos-large-leaf20 | 192.168.101.20/32 |
| FABRIC | clab-clos-large-leaf21 | 192.168.101.21/32 |
| FABRIC | clab-clos-large-leaf22 | 192.168.101.22/32 |
| FABRIC | clab-clos-large-leaf23 | 192.168.101.23/32 |
| FABRIC | clab-clos-large-leaf24 | 192.168.101.24/32 |
| FABRIC | clab-clos-large-leaf25 | 192.168.101.25/32 |
| FABRIC | clab-clos-large-leaf26 | 192.168.101.26/32 |
| FABRIC | clab-clos-large-leaf27 | 192.168.101.27/32 |
| FABRIC | clab-clos-large-leaf28 | 192.168.101.28/32 |
| FABRIC | clab-clos-large-leaf29 | 192.168.101.29/32 |
| FABRIC | clab-clos-large-leaf30 | 192.168.101.30/32 |
| FABRIC | clab-clos-large-leaf31 | 192.168.101.31/32 |
| FABRIC | clab-clos-large-leaf32 | 192.168.101.32/32 |
| FABRIC | clab-clos-large-leaf33 | 192.168.101.33/32 |
| FABRIC | clab-clos-large-leaf34 | 192.168.101.34/32 |
| FABRIC | clab-clos-large-leaf35 | 192.168.101.35/32 |
| FABRIC | clab-clos-large-leaf36 | 192.168.101.36/32 |
| FABRIC | clab-clos-large-leaf37 | 192.168.101.37/32 |
| FABRIC | clab-clos-large-leaf38 | 192.168.101.38/32 |
| FABRIC | clab-clos-large-leaf39 | 192.168.101.39/32 |
| FABRIC | clab-clos-large-leaf40 | 192.168.101.40/32 |
| FABRIC | clab-clos-large-leaf41 | 192.168.101.41/32 |
| FABRIC | clab-clos-large-leaf42 | 192.168.101.42/32 |
| FABRIC | clab-clos-large-leaf43 | 192.168.101.43/32 |
| FABRIC | clab-clos-large-leaf44 | 192.168.101.44/32 |
| FABRIC | clab-clos-large-leaf45 | 192.168.101.45/32 |
| FABRIC | clab-clos-large-leaf46 | 192.168.101.46/32 |
| FABRIC | clab-clos-large-leaf47 | 192.168.101.47/32 |
| FABRIC | clab-clos-large-leaf48 | 192.168.101.48/32 |
| FABRIC | clab-clos-large-leaf49 | 192.168.101.49/32 |
| FABRIC | clab-clos-large-leaf50 | 192.168.101.50/32 |
| FABRIC | clab-clos-large-spine1 | 192.168.101.101/32 |
| FABRIC | clab-clos-large-spine2 | 192.168.101.102/32 |
| FABRIC | clab-clos-large-spine3 | 192.168.101.103/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |
| 192.168.102.0/24 | 256 | 52 | 20.32 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| FABRIC | clab-clos-large-borderleaf1 | 192.168.102.91/32 |
| FABRIC | clab-clos-large-borderleaf2 | 192.168.102.92/32 |
| FABRIC | clab-clos-large-leaf1 | 192.168.102.1/32 |
| FABRIC | clab-clos-large-leaf2 | 192.168.102.1/32 |
| FABRIC | clab-clos-large-leaf3 | 192.168.102.3/32 |
| FABRIC | clab-clos-large-leaf4 | 192.168.102.3/32 |
| FABRIC | clab-clos-large-leaf5 | 192.168.102.5/32 |
| FABRIC | clab-clos-large-leaf6 | 192.168.102.5/32 |
| FABRIC | clab-clos-large-leaf7 | 192.168.102.7/32 |
| FABRIC | clab-clos-large-leaf8 | 192.168.102.7/32 |
| FABRIC | clab-clos-large-leaf9 | 192.168.102.9/32 |
| FABRIC | clab-clos-large-leaf10 | 192.168.102.9/32 |
| FABRIC | clab-clos-large-leaf11 | 192.168.102.11/32 |
| FABRIC | clab-clos-large-leaf12 | 192.168.102.11/32 |
| FABRIC | clab-clos-large-leaf13 | 192.168.102.13/32 |
| FABRIC | clab-clos-large-leaf14 | 192.168.102.13/32 |
| FABRIC | clab-clos-large-leaf15 | 192.168.102.15/32 |
| FABRIC | clab-clos-large-leaf16 | 192.168.102.15/32 |
| FABRIC | clab-clos-large-leaf17 | 192.168.102.17/32 |
| FABRIC | clab-clos-large-leaf18 | 192.168.102.17/32 |
| FABRIC | clab-clos-large-leaf19 | 192.168.102.19/32 |
| FABRIC | clab-clos-large-leaf20 | 192.168.102.19/32 |
| FABRIC | clab-clos-large-leaf21 | 192.168.102.21/32 |
| FABRIC | clab-clos-large-leaf22 | 192.168.102.21/32 |
| FABRIC | clab-clos-large-leaf23 | 192.168.102.23/32 |
| FABRIC | clab-clos-large-leaf24 | 192.168.102.23/32 |
| FABRIC | clab-clos-large-leaf25 | 192.168.102.25/32 |
| FABRIC | clab-clos-large-leaf26 | 192.168.102.25/32 |
| FABRIC | clab-clos-large-leaf27 | 192.168.102.27/32 |
| FABRIC | clab-clos-large-leaf28 | 192.168.102.27/32 |
| FABRIC | clab-clos-large-leaf29 | 192.168.102.29/32 |
| FABRIC | clab-clos-large-leaf30 | 192.168.102.29/32 |
| FABRIC | clab-clos-large-leaf31 | 192.168.102.31/32 |
| FABRIC | clab-clos-large-leaf32 | 192.168.102.31/32 |
| FABRIC | clab-clos-large-leaf33 | 192.168.102.33/32 |
| FABRIC | clab-clos-large-leaf34 | 192.168.102.33/32 |
| FABRIC | clab-clos-large-leaf35 | 192.168.102.35/32 |
| FABRIC | clab-clos-large-leaf36 | 192.168.102.35/32 |
| FABRIC | clab-clos-large-leaf37 | 192.168.102.37/32 |
| FABRIC | clab-clos-large-leaf38 | 192.168.102.37/32 |
| FABRIC | clab-clos-large-leaf39 | 192.168.102.39/32 |
| FABRIC | clab-clos-large-leaf40 | 192.168.102.39/32 |
| FABRIC | clab-clos-large-leaf41 | 192.168.102.41/32 |
| FABRIC | clab-clos-large-leaf42 | 192.168.102.41/32 |
| FABRIC | clab-clos-large-leaf43 | 192.168.102.43/32 |
| FABRIC | clab-clos-large-leaf44 | 192.168.102.43/32 |
| FABRIC | clab-clos-large-leaf45 | 192.168.102.45/32 |
| FABRIC | clab-clos-large-leaf46 | 192.168.102.45/32 |
| FABRIC | clab-clos-large-leaf47 | 192.168.102.47/32 |
| FABRIC | clab-clos-large-leaf48 | 192.168.102.47/32 |
| FABRIC | clab-clos-large-leaf49 | 192.168.102.49/32 |
| FABRIC | clab-clos-large-leaf50 | 192.168.102.49/32 |
