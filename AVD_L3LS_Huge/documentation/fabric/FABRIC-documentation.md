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
  - [ISIS CLNS interfaces](#isis-clns-interfaces)
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
| 192.168.110.0/22 | 1024 | 312 | 30.47 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| clab-clos-large-borderleaf1 | Ethernet3 | 192.168.110.29/31 | clab-clos-large-spine1 | Ethernet52 | 192.168.110.28/31 |
| clab-clos-large-borderleaf1 | Ethernet4 | 192.168.110.31/31 | clab-clos-large-spine2 | Ethernet52 | 192.168.110.30/31 |
| clab-clos-large-borderleaf1 | Ethernet5 | 192.168.110.33/31 | clab-clos-large-spine3 | Ethernet52 | 192.168.110.32/31 |
| clab-clos-large-borderleaf2 | Ethernet3 | 192.168.110.35/31 | clab-clos-large-spine1 | Ethernet53 | 192.168.110.34/31 |
| clab-clos-large-borderleaf2 | Ethernet4 | 192.168.110.37/31 | clab-clos-large-spine2 | Ethernet53 | 192.168.110.36/31 |
| clab-clos-large-borderleaf2 | Ethernet5 | 192.168.110.39/31 | clab-clos-large-spine3 | Ethernet53 | 192.168.110.38/31 |
| clab-clos-large-leaf1 | Ethernet3 | 192.168.108.1/31 | clab-clos-large-spine1 | Ethernet2 | 192.168.108.0/31 |
| clab-clos-large-leaf1 | Ethernet4 | 192.168.108.3/31 | clab-clos-large-spine2 | Ethernet2 | 192.168.108.2/31 |
| clab-clos-large-leaf1 | Ethernet5 | 192.168.108.5/31 | clab-clos-large-spine3 | Ethernet2 | 192.168.108.4/31 |
| clab-clos-large-leaf2 | Ethernet3 | 192.168.108.7/31 | clab-clos-large-spine1 | Ethernet3 | 192.168.108.6/31 |
| clab-clos-large-leaf2 | Ethernet4 | 192.168.108.9/31 | clab-clos-large-spine2 | Ethernet3 | 192.168.108.8/31 |
| clab-clos-large-leaf2 | Ethernet5 | 192.168.108.11/31 | clab-clos-large-spine3 | Ethernet3 | 192.168.108.10/31 |
| clab-clos-large-leaf3 | Ethernet3 | 192.168.108.13/31 | clab-clos-large-spine1 | Ethernet4 | 192.168.108.12/31 |
| clab-clos-large-leaf3 | Ethernet4 | 192.168.108.15/31 | clab-clos-large-spine2 | Ethernet4 | 192.168.108.14/31 |
| clab-clos-large-leaf3 | Ethernet5 | 192.168.108.17/31 | clab-clos-large-spine3 | Ethernet4 | 192.168.108.16/31 |
| clab-clos-large-leaf4 | Ethernet3 | 192.168.108.19/31 | clab-clos-large-spine1 | Ethernet5 | 192.168.108.18/31 |
| clab-clos-large-leaf4 | Ethernet4 | 192.168.108.21/31 | clab-clos-large-spine2 | Ethernet5 | 192.168.108.20/31 |
| clab-clos-large-leaf4 | Ethernet5 | 192.168.108.23/31 | clab-clos-large-spine3 | Ethernet5 | 192.168.108.22/31 |
| clab-clos-large-leaf5 | Ethernet3 | 192.168.108.25/31 | clab-clos-large-spine1 | Ethernet6 | 192.168.108.24/31 |
| clab-clos-large-leaf5 | Ethernet4 | 192.168.108.27/31 | clab-clos-large-spine2 | Ethernet6 | 192.168.108.26/31 |
| clab-clos-large-leaf5 | Ethernet5 | 192.168.108.29/31 | clab-clos-large-spine3 | Ethernet6 | 192.168.108.28/31 |
| clab-clos-large-leaf6 | Ethernet3 | 192.168.108.31/31 | clab-clos-large-spine1 | Ethernet7 | 192.168.108.30/31 |
| clab-clos-large-leaf6 | Ethernet4 | 192.168.108.33/31 | clab-clos-large-spine2 | Ethernet7 | 192.168.108.32/31 |
| clab-clos-large-leaf6 | Ethernet5 | 192.168.108.35/31 | clab-clos-large-spine3 | Ethernet7 | 192.168.108.34/31 |
| clab-clos-large-leaf7 | Ethernet3 | 192.168.108.37/31 | clab-clos-large-spine1 | Ethernet8 | 192.168.108.36/31 |
| clab-clos-large-leaf7 | Ethernet4 | 192.168.108.39/31 | clab-clos-large-spine2 | Ethernet8 | 192.168.108.38/31 |
| clab-clos-large-leaf7 | Ethernet5 | 192.168.108.41/31 | clab-clos-large-spine3 | Ethernet8 | 192.168.108.40/31 |
| clab-clos-large-leaf8 | Ethernet3 | 192.168.108.43/31 | clab-clos-large-spine1 | Ethernet9 | 192.168.108.42/31 |
| clab-clos-large-leaf8 | Ethernet4 | 192.168.108.45/31 | clab-clos-large-spine2 | Ethernet9 | 192.168.108.44/31 |
| clab-clos-large-leaf8 | Ethernet5 | 192.168.108.47/31 | clab-clos-large-spine3 | Ethernet9 | 192.168.108.46/31 |
| clab-clos-large-leaf9 | Ethernet3 | 192.168.108.49/31 | clab-clos-large-spine1 | Ethernet10 | 192.168.108.48/31 |
| clab-clos-large-leaf9 | Ethernet4 | 192.168.108.51/31 | clab-clos-large-spine2 | Ethernet10 | 192.168.108.50/31 |
| clab-clos-large-leaf9 | Ethernet5 | 192.168.108.53/31 | clab-clos-large-spine3 | Ethernet10 | 192.168.108.52/31 |
| clab-clos-large-leaf10 | Ethernet3 | 192.168.108.55/31 | clab-clos-large-spine1 | Ethernet11 | 192.168.108.54/31 |
| clab-clos-large-leaf10 | Ethernet4 | 192.168.108.57/31 | clab-clos-large-spine2 | Ethernet11 | 192.168.108.56/31 |
| clab-clos-large-leaf10 | Ethernet5 | 192.168.108.59/31 | clab-clos-large-spine3 | Ethernet11 | 192.168.108.58/31 |
| clab-clos-large-leaf11 | Ethernet3 | 192.168.108.61/31 | clab-clos-large-spine1 | Ethernet12 | 192.168.108.60/31 |
| clab-clos-large-leaf11 | Ethernet4 | 192.168.108.63/31 | clab-clos-large-spine2 | Ethernet12 | 192.168.108.62/31 |
| clab-clos-large-leaf11 | Ethernet5 | 192.168.108.65/31 | clab-clos-large-spine3 | Ethernet12 | 192.168.108.64/31 |
| clab-clos-large-leaf12 | Ethernet3 | 192.168.108.67/31 | clab-clos-large-spine1 | Ethernet13 | 192.168.108.66/31 |
| clab-clos-large-leaf12 | Ethernet4 | 192.168.108.69/31 | clab-clos-large-spine2 | Ethernet13 | 192.168.108.68/31 |
| clab-clos-large-leaf12 | Ethernet5 | 192.168.108.71/31 | clab-clos-large-spine3 | Ethernet13 | 192.168.108.70/31 |
| clab-clos-large-leaf13 | Ethernet3 | 192.168.108.73/31 | clab-clos-large-spine1 | Ethernet14 | 192.168.108.72/31 |
| clab-clos-large-leaf13 | Ethernet4 | 192.168.108.75/31 | clab-clos-large-spine2 | Ethernet14 | 192.168.108.74/31 |
| clab-clos-large-leaf13 | Ethernet5 | 192.168.108.77/31 | clab-clos-large-spine3 | Ethernet14 | 192.168.108.76/31 |
| clab-clos-large-leaf14 | Ethernet3 | 192.168.108.79/31 | clab-clos-large-spine1 | Ethernet15 | 192.168.108.78/31 |
| clab-clos-large-leaf14 | Ethernet4 | 192.168.108.81/31 | clab-clos-large-spine2 | Ethernet15 | 192.168.108.80/31 |
| clab-clos-large-leaf14 | Ethernet5 | 192.168.108.83/31 | clab-clos-large-spine3 | Ethernet15 | 192.168.108.82/31 |
| clab-clos-large-leaf15 | Ethernet3 | 192.168.108.85/31 | clab-clos-large-spine1 | Ethernet16 | 192.168.108.84/31 |
| clab-clos-large-leaf15 | Ethernet4 | 192.168.108.87/31 | clab-clos-large-spine2 | Ethernet16 | 192.168.108.86/31 |
| clab-clos-large-leaf15 | Ethernet5 | 192.168.108.89/31 | clab-clos-large-spine3 | Ethernet16 | 192.168.108.88/31 |
| clab-clos-large-leaf16 | Ethernet3 | 192.168.108.91/31 | clab-clos-large-spine1 | Ethernet17 | 192.168.108.90/31 |
| clab-clos-large-leaf16 | Ethernet4 | 192.168.108.93/31 | clab-clos-large-spine2 | Ethernet17 | 192.168.108.92/31 |
| clab-clos-large-leaf16 | Ethernet5 | 192.168.108.95/31 | clab-clos-large-spine3 | Ethernet17 | 192.168.108.94/31 |
| clab-clos-large-leaf17 | Ethernet3 | 192.168.108.97/31 | clab-clos-large-spine1 | Ethernet18 | 192.168.108.96/31 |
| clab-clos-large-leaf17 | Ethernet4 | 192.168.108.99/31 | clab-clos-large-spine2 | Ethernet18 | 192.168.108.98/31 |
| clab-clos-large-leaf17 | Ethernet5 | 192.168.108.101/31 | clab-clos-large-spine3 | Ethernet18 | 192.168.108.100/31 |
| clab-clos-large-leaf18 | Ethernet3 | 192.168.108.103/31 | clab-clos-large-spine1 | Ethernet19 | 192.168.108.102/31 |
| clab-clos-large-leaf18 | Ethernet4 | 192.168.108.105/31 | clab-clos-large-spine2 | Ethernet19 | 192.168.108.104/31 |
| clab-clos-large-leaf18 | Ethernet5 | 192.168.108.107/31 | clab-clos-large-spine3 | Ethernet19 | 192.168.108.106/31 |
| clab-clos-large-leaf19 | Ethernet3 | 192.168.108.109/31 | clab-clos-large-spine1 | Ethernet20 | 192.168.108.108/31 |
| clab-clos-large-leaf19 | Ethernet4 | 192.168.108.111/31 | clab-clos-large-spine2 | Ethernet20 | 192.168.108.110/31 |
| clab-clos-large-leaf19 | Ethernet5 | 192.168.108.113/31 | clab-clos-large-spine3 | Ethernet20 | 192.168.108.112/31 |
| clab-clos-large-leaf20 | Ethernet3 | 192.168.108.115/31 | clab-clos-large-spine1 | Ethernet21 | 192.168.108.114/31 |
| clab-clos-large-leaf20 | Ethernet4 | 192.168.108.117/31 | clab-clos-large-spine2 | Ethernet21 | 192.168.108.116/31 |
| clab-clos-large-leaf20 | Ethernet5 | 192.168.108.119/31 | clab-clos-large-spine3 | Ethernet21 | 192.168.108.118/31 |
| clab-clos-large-leaf21 | Ethernet3 | 192.168.108.121/31 | clab-clos-large-spine1 | Ethernet22 | 192.168.108.120/31 |
| clab-clos-large-leaf21 | Ethernet4 | 192.168.108.123/31 | clab-clos-large-spine2 | Ethernet22 | 192.168.108.122/31 |
| clab-clos-large-leaf21 | Ethernet5 | 192.168.108.125/31 | clab-clos-large-spine3 | Ethernet22 | 192.168.108.124/31 |
| clab-clos-large-leaf22 | Ethernet3 | 192.168.108.127/31 | clab-clos-large-spine1 | Ethernet23 | 192.168.108.126/31 |
| clab-clos-large-leaf22 | Ethernet4 | 192.168.108.129/31 | clab-clos-large-spine2 | Ethernet23 | 192.168.108.128/31 |
| clab-clos-large-leaf22 | Ethernet5 | 192.168.108.131/31 | clab-clos-large-spine3 | Ethernet23 | 192.168.108.130/31 |
| clab-clos-large-leaf23 | Ethernet3 | 192.168.108.133/31 | clab-clos-large-spine1 | Ethernet24 | 192.168.108.132/31 |
| clab-clos-large-leaf23 | Ethernet4 | 192.168.108.135/31 | clab-clos-large-spine2 | Ethernet24 | 192.168.108.134/31 |
| clab-clos-large-leaf23 | Ethernet5 | 192.168.108.137/31 | clab-clos-large-spine3 | Ethernet24 | 192.168.108.136/31 |
| clab-clos-large-leaf24 | Ethernet3 | 192.168.108.139/31 | clab-clos-large-spine1 | Ethernet25 | 192.168.108.138/31 |
| clab-clos-large-leaf24 | Ethernet4 | 192.168.108.141/31 | clab-clos-large-spine2 | Ethernet25 | 192.168.108.140/31 |
| clab-clos-large-leaf24 | Ethernet5 | 192.168.108.143/31 | clab-clos-large-spine3 | Ethernet25 | 192.168.108.142/31 |
| clab-clos-large-leaf25 | Ethernet3 | 192.168.108.145/31 | clab-clos-large-spine1 | Ethernet26 | 192.168.108.144/31 |
| clab-clos-large-leaf25 | Ethernet4 | 192.168.108.147/31 | clab-clos-large-spine2 | Ethernet26 | 192.168.108.146/31 |
| clab-clos-large-leaf25 | Ethernet5 | 192.168.108.149/31 | clab-clos-large-spine3 | Ethernet26 | 192.168.108.148/31 |
| clab-clos-large-leaf26 | Ethernet3 | 192.168.108.151/31 | clab-clos-large-spine1 | Ethernet27 | 192.168.108.150/31 |
| clab-clos-large-leaf26 | Ethernet4 | 192.168.108.153/31 | clab-clos-large-spine2 | Ethernet27 | 192.168.108.152/31 |
| clab-clos-large-leaf26 | Ethernet5 | 192.168.108.155/31 | clab-clos-large-spine3 | Ethernet27 | 192.168.108.154/31 |
| clab-clos-large-leaf27 | Ethernet3 | 192.168.108.157/31 | clab-clos-large-spine1 | Ethernet28 | 192.168.108.156/31 |
| clab-clos-large-leaf27 | Ethernet4 | 192.168.108.159/31 | clab-clos-large-spine2 | Ethernet28 | 192.168.108.158/31 |
| clab-clos-large-leaf27 | Ethernet5 | 192.168.108.161/31 | clab-clos-large-spine3 | Ethernet28 | 192.168.108.160/31 |
| clab-clos-large-leaf28 | Ethernet3 | 192.168.108.163/31 | clab-clos-large-spine1 | Ethernet29 | 192.168.108.162/31 |
| clab-clos-large-leaf28 | Ethernet4 | 192.168.108.165/31 | clab-clos-large-spine2 | Ethernet29 | 192.168.108.164/31 |
| clab-clos-large-leaf28 | Ethernet5 | 192.168.108.167/31 | clab-clos-large-spine3 | Ethernet29 | 192.168.108.166/31 |
| clab-clos-large-leaf29 | Ethernet3 | 192.168.108.169/31 | clab-clos-large-spine1 | Ethernet30 | 192.168.108.168/31 |
| clab-clos-large-leaf29 | Ethernet4 | 192.168.108.171/31 | clab-clos-large-spine2 | Ethernet30 | 192.168.108.170/31 |
| clab-clos-large-leaf29 | Ethernet5 | 192.168.108.173/31 | clab-clos-large-spine3 | Ethernet30 | 192.168.108.172/31 |
| clab-clos-large-leaf30 | Ethernet3 | 192.168.108.175/31 | clab-clos-large-spine1 | Ethernet31 | 192.168.108.174/31 |
| clab-clos-large-leaf30 | Ethernet4 | 192.168.108.177/31 | clab-clos-large-spine2 | Ethernet31 | 192.168.108.176/31 |
| clab-clos-large-leaf30 | Ethernet5 | 192.168.108.179/31 | clab-clos-large-spine3 | Ethernet31 | 192.168.108.178/31 |
| clab-clos-large-leaf31 | Ethernet3 | 192.168.108.181/31 | clab-clos-large-spine1 | Ethernet32 | 192.168.108.180/31 |
| clab-clos-large-leaf31 | Ethernet4 | 192.168.108.183/31 | clab-clos-large-spine2 | Ethernet32 | 192.168.108.182/31 |
| clab-clos-large-leaf31 | Ethernet5 | 192.168.108.185/31 | clab-clos-large-spine3 | Ethernet32 | 192.168.108.184/31 |
| clab-clos-large-leaf32 | Ethernet3 | 192.168.108.187/31 | clab-clos-large-spine1 | Ethernet33 | 192.168.108.186/31 |
| clab-clos-large-leaf32 | Ethernet4 | 192.168.108.189/31 | clab-clos-large-spine2 | Ethernet33 | 192.168.108.188/31 |
| clab-clos-large-leaf32 | Ethernet5 | 192.168.108.191/31 | clab-clos-large-spine3 | Ethernet33 | 192.168.108.190/31 |
| clab-clos-large-leaf33 | Ethernet3 | 192.168.108.193/31 | clab-clos-large-spine1 | Ethernet34 | 192.168.108.192/31 |
| clab-clos-large-leaf33 | Ethernet4 | 192.168.108.195/31 | clab-clos-large-spine2 | Ethernet34 | 192.168.108.194/31 |
| clab-clos-large-leaf33 | Ethernet5 | 192.168.108.197/31 | clab-clos-large-spine3 | Ethernet34 | 192.168.108.196/31 |
| clab-clos-large-leaf34 | Ethernet3 | 192.168.108.199/31 | clab-clos-large-spine1 | Ethernet35 | 192.168.108.198/31 |
| clab-clos-large-leaf34 | Ethernet4 | 192.168.108.201/31 | clab-clos-large-spine2 | Ethernet35 | 192.168.108.200/31 |
| clab-clos-large-leaf34 | Ethernet5 | 192.168.108.203/31 | clab-clos-large-spine3 | Ethernet35 | 192.168.108.202/31 |
| clab-clos-large-leaf35 | Ethernet3 | 192.168.108.205/31 | clab-clos-large-spine1 | Ethernet36 | 192.168.108.204/31 |
| clab-clos-large-leaf35 | Ethernet4 | 192.168.108.207/31 | clab-clos-large-spine2 | Ethernet36 | 192.168.108.206/31 |
| clab-clos-large-leaf35 | Ethernet5 | 192.168.108.209/31 | clab-clos-large-spine3 | Ethernet36 | 192.168.108.208/31 |
| clab-clos-large-leaf36 | Ethernet3 | 192.168.108.211/31 | clab-clos-large-spine1 | Ethernet37 | 192.168.108.210/31 |
| clab-clos-large-leaf36 | Ethernet4 | 192.168.108.213/31 | clab-clos-large-spine2 | Ethernet37 | 192.168.108.212/31 |
| clab-clos-large-leaf36 | Ethernet5 | 192.168.108.215/31 | clab-clos-large-spine3 | Ethernet37 | 192.168.108.214/31 |
| clab-clos-large-leaf37 | Ethernet3 | 192.168.108.217/31 | clab-clos-large-spine1 | Ethernet38 | 192.168.108.216/31 |
| clab-clos-large-leaf37 | Ethernet4 | 192.168.108.219/31 | clab-clos-large-spine2 | Ethernet38 | 192.168.108.218/31 |
| clab-clos-large-leaf37 | Ethernet5 | 192.168.108.221/31 | clab-clos-large-spine3 | Ethernet38 | 192.168.108.220/31 |
| clab-clos-large-leaf38 | Ethernet3 | 192.168.108.223/31 | clab-clos-large-spine1 | Ethernet39 | 192.168.108.222/31 |
| clab-clos-large-leaf38 | Ethernet4 | 192.168.108.225/31 | clab-clos-large-spine2 | Ethernet39 | 192.168.108.224/31 |
| clab-clos-large-leaf38 | Ethernet5 | 192.168.108.227/31 | clab-clos-large-spine3 | Ethernet39 | 192.168.108.226/31 |
| clab-clos-large-leaf39 | Ethernet3 | 192.168.108.229/31 | clab-clos-large-spine1 | Ethernet40 | 192.168.108.228/31 |
| clab-clos-large-leaf39 | Ethernet4 | 192.168.108.231/31 | clab-clos-large-spine2 | Ethernet40 | 192.168.108.230/31 |
| clab-clos-large-leaf39 | Ethernet5 | 192.168.108.233/31 | clab-clos-large-spine3 | Ethernet40 | 192.168.108.232/31 |
| clab-clos-large-leaf40 | Ethernet3 | 192.168.108.235/31 | clab-clos-large-spine1 | Ethernet41 | 192.168.108.234/31 |
| clab-clos-large-leaf40 | Ethernet4 | 192.168.108.237/31 | clab-clos-large-spine2 | Ethernet41 | 192.168.108.236/31 |
| clab-clos-large-leaf40 | Ethernet5 | 192.168.108.239/31 | clab-clos-large-spine3 | Ethernet41 | 192.168.108.238/31 |
| clab-clos-large-leaf41 | Ethernet3 | 192.168.108.241/31 | clab-clos-large-spine1 | Ethernet42 | 192.168.108.240/31 |
| clab-clos-large-leaf41 | Ethernet4 | 192.168.108.243/31 | clab-clos-large-spine2 | Ethernet42 | 192.168.108.242/31 |
| clab-clos-large-leaf41 | Ethernet5 | 192.168.108.245/31 | clab-clos-large-spine3 | Ethernet42 | 192.168.108.244/31 |
| clab-clos-large-leaf42 | Ethernet3 | 192.168.108.247/31 | clab-clos-large-spine1 | Ethernet43 | 192.168.108.246/31 |
| clab-clos-large-leaf42 | Ethernet4 | 192.168.108.249/31 | clab-clos-large-spine2 | Ethernet43 | 192.168.108.248/31 |
| clab-clos-large-leaf42 | Ethernet5 | 192.168.108.251/31 | clab-clos-large-spine3 | Ethernet43 | 192.168.108.250/31 |
| clab-clos-large-leaf43 | Ethernet3 | 192.168.108.253/31 | clab-clos-large-spine1 | Ethernet44 | 192.168.108.252/31 |
| clab-clos-large-leaf43 | Ethernet4 | 192.168.108.255/31 | clab-clos-large-spine2 | Ethernet44 | 192.168.108.254/31 |
| clab-clos-large-leaf43 | Ethernet5 | 192.168.109.1/31 | clab-clos-large-spine3 | Ethernet44 | 192.168.109.0/31 |
| clab-clos-large-leaf44 | Ethernet3 | 192.168.109.3/31 | clab-clos-large-spine1 | Ethernet45 | 192.168.109.2/31 |
| clab-clos-large-leaf44 | Ethernet4 | 192.168.109.5/31 | clab-clos-large-spine2 | Ethernet45 | 192.168.109.4/31 |
| clab-clos-large-leaf44 | Ethernet5 | 192.168.109.7/31 | clab-clos-large-spine3 | Ethernet45 | 192.168.109.6/31 |
| clab-clos-large-leaf45 | Ethernet3 | 192.168.109.9/31 | clab-clos-large-spine1 | Ethernet46 | 192.168.109.8/31 |
| clab-clos-large-leaf45 | Ethernet4 | 192.168.109.11/31 | clab-clos-large-spine2 | Ethernet46 | 192.168.109.10/31 |
| clab-clos-large-leaf45 | Ethernet5 | 192.168.109.13/31 | clab-clos-large-spine3 | Ethernet46 | 192.168.109.12/31 |
| clab-clos-large-leaf46 | Ethernet3 | 192.168.109.15/31 | clab-clos-large-spine1 | Ethernet47 | 192.168.109.14/31 |
| clab-clos-large-leaf46 | Ethernet4 | 192.168.109.17/31 | clab-clos-large-spine2 | Ethernet47 | 192.168.109.16/31 |
| clab-clos-large-leaf46 | Ethernet5 | 192.168.109.19/31 | clab-clos-large-spine3 | Ethernet47 | 192.168.109.18/31 |
| clab-clos-large-leaf47 | Ethernet3 | 192.168.109.21/31 | clab-clos-large-spine1 | Ethernet48 | 192.168.109.20/31 |
| clab-clos-large-leaf47 | Ethernet4 | 192.168.109.23/31 | clab-clos-large-spine2 | Ethernet48 | 192.168.109.22/31 |
| clab-clos-large-leaf47 | Ethernet5 | 192.168.109.25/31 | clab-clos-large-spine3 | Ethernet48 | 192.168.109.24/31 |
| clab-clos-large-leaf48 | Ethernet3 | 192.168.109.27/31 | clab-clos-large-spine1 | Ethernet49 | 192.168.109.26/31 |
| clab-clos-large-leaf48 | Ethernet4 | 192.168.109.29/31 | clab-clos-large-spine2 | Ethernet49 | 192.168.109.28/31 |
| clab-clos-large-leaf48 | Ethernet5 | 192.168.109.31/31 | clab-clos-large-spine3 | Ethernet49 | 192.168.109.30/31 |
| clab-clos-large-leaf49 | Ethernet3 | 192.168.109.33/31 | clab-clos-large-spine1 | Ethernet50 | 192.168.109.32/31 |
| clab-clos-large-leaf49 | Ethernet4 | 192.168.109.35/31 | clab-clos-large-spine2 | Ethernet50 | 192.168.109.34/31 |
| clab-clos-large-leaf49 | Ethernet5 | 192.168.109.37/31 | clab-clos-large-spine3 | Ethernet50 | 192.168.109.36/31 |
| clab-clos-large-leaf50 | Ethernet3 | 192.168.109.39/31 | clab-clos-large-spine1 | Ethernet51 | 192.168.109.38/31 |
| clab-clos-large-leaf50 | Ethernet4 | 192.168.109.41/31 | clab-clos-large-spine2 | Ethernet51 | 192.168.109.40/31 |
| clab-clos-large-leaf50 | Ethernet5 | 192.168.109.43/31 | clab-clos-large-spine3 | Ethernet51 | 192.168.109.42/31 |

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

### ISIS CLNS interfaces

| POD | Node | CLNS Address |
| --- | ---- | ------------ |
| FABRIC | clab-clos-large-borderleaf1 | 49.0001.1921.6810.1091.00 |
| FABRIC | clab-clos-large-borderleaf2 | 49.0001.1921.6810.1092.00 |
| FABRIC | clab-clos-large-leaf1 | 49.0001.1921.6810.1001.00 |
| FABRIC | clab-clos-large-leaf2 | 49.0001.1921.6810.1002.00 |
| FABRIC | clab-clos-large-leaf3 | 49.0001.1921.6810.1003.00 |
| FABRIC | clab-clos-large-leaf4 | 49.0001.1921.6810.1004.00 |
| FABRIC | clab-clos-large-leaf5 | 49.0001.1921.6810.1005.00 |
| FABRIC | clab-clos-large-leaf6 | 49.0001.1921.6810.1006.00 |
| FABRIC | clab-clos-large-leaf7 | 49.0001.1921.6810.1007.00 |
| FABRIC | clab-clos-large-leaf8 | 49.0001.1921.6810.1008.00 |
| FABRIC | clab-clos-large-leaf9 | 49.0001.1921.6810.1009.00 |
| FABRIC | clab-clos-large-leaf10 | 49.0001.1921.6810.1010.00 |
| FABRIC | clab-clos-large-leaf11 | 49.0001.1921.6810.1011.00 |
| FABRIC | clab-clos-large-leaf12 | 49.0001.1921.6810.1012.00 |
| FABRIC | clab-clos-large-leaf13 | 49.0001.1921.6810.1013.00 |
| FABRIC | clab-clos-large-leaf14 | 49.0001.1921.6810.1014.00 |
| FABRIC | clab-clos-large-leaf15 | 49.0001.1921.6810.1015.00 |
| FABRIC | clab-clos-large-leaf16 | 49.0001.1921.6810.1016.00 |
| FABRIC | clab-clos-large-leaf17 | 49.0001.1921.6810.1017.00 |
| FABRIC | clab-clos-large-leaf18 | 49.0001.1921.6810.1018.00 |
| FABRIC | clab-clos-large-leaf19 | 49.0001.1921.6810.1019.00 |
| FABRIC | clab-clos-large-leaf20 | 49.0001.1921.6810.1020.00 |
| FABRIC | clab-clos-large-leaf21 | 49.0001.1921.6810.1021.00 |
| FABRIC | clab-clos-large-leaf22 | 49.0001.1921.6810.1022.00 |
| FABRIC | clab-clos-large-leaf23 | 49.0001.1921.6810.1023.00 |
| FABRIC | clab-clos-large-leaf24 | 49.0001.1921.6810.1024.00 |
| FABRIC | clab-clos-large-leaf25 | 49.0001.1921.6810.1025.00 |
| FABRIC | clab-clos-large-leaf26 | 49.0001.1921.6810.1026.00 |
| FABRIC | clab-clos-large-leaf27 | 49.0001.1921.6810.1027.00 |
| FABRIC | clab-clos-large-leaf28 | 49.0001.1921.6810.1028.00 |
| FABRIC | clab-clos-large-leaf29 | 49.0001.1921.6810.1029.00 |
| FABRIC | clab-clos-large-leaf30 | 49.0001.1921.6810.1030.00 |
| FABRIC | clab-clos-large-leaf31 | 49.0001.1921.6810.1031.00 |
| FABRIC | clab-clos-large-leaf32 | 49.0001.1921.6810.1032.00 |
| FABRIC | clab-clos-large-leaf33 | 49.0001.1921.6810.1033.00 |
| FABRIC | clab-clos-large-leaf34 | 49.0001.1921.6810.1034.00 |
| FABRIC | clab-clos-large-leaf35 | 49.0001.1921.6810.1035.00 |
| FABRIC | clab-clos-large-leaf36 | 49.0001.1921.6810.1036.00 |
| FABRIC | clab-clos-large-leaf37 | 49.0001.1921.6810.1037.00 |
| FABRIC | clab-clos-large-leaf38 | 49.0001.1921.6810.1038.00 |
| FABRIC | clab-clos-large-leaf39 | 49.0001.1921.6810.1039.00 |
| FABRIC | clab-clos-large-leaf40 | 49.0001.1921.6810.1040.00 |
| FABRIC | clab-clos-large-leaf41 | 49.0001.1921.6810.1041.00 |
| FABRIC | clab-clos-large-leaf42 | 49.0001.1921.6810.1042.00 |
| FABRIC | clab-clos-large-leaf43 | 49.0001.1921.6810.1043.00 |
| FABRIC | clab-clos-large-leaf44 | 49.0001.1921.6810.1044.00 |
| FABRIC | clab-clos-large-leaf45 | 49.0001.1921.6810.1045.00 |
| FABRIC | clab-clos-large-leaf46 | 49.0001.1921.6810.1046.00 |
| FABRIC | clab-clos-large-leaf47 | 49.0001.1921.6810.1047.00 |
| FABRIC | clab-clos-large-leaf48 | 49.0001.1921.6810.1048.00 |
| FABRIC | clab-clos-large-leaf49 | 49.0001.1921.6810.1049.00 |
| FABRIC | clab-clos-large-leaf50 | 49.0001.1921.6810.1050.00 |
| FABRIC | clab-clos-large-spine1 | 49.0001.1921.6810.1101.00 |
| FABRIC | clab-clos-large-spine2 | 49.0001.1921.6810.1102.00 |
| FABRIC | clab-clos-large-spine3 | 49.0001.1921.6810.1103.00 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
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
