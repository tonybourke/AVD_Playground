# leaf4

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [DNS Domain](#dns-domain)
  - [IP Name Servers](#ip-name-servers)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
  - [AAA Authentication](#aaa-authentication)
  - [AAA Authorization](#aaa-authorization)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Device Configuration](#internal-vlan-allocation-policy-device-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
  - [Router Multicast](#router-multicast)
  - [PIM Sparse Mode](#pim-sparse-mode)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management0 | OOB_MANAGEMENT | oob | MGMT | 172.20.20.14/24 | 172.20.20.1 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management0 | OOB_MANAGEMENT | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management0
   description OOB_MANAGEMENT
   no shutdown
   vrf MGMT
   ip address 172.20.20.14/24
```

### DNS Domain

DNS domain: tony.lab

#### DNS Domain Device Configuration

```eos
dns domain tony.lab
!
```

### IP Name Servers

#### IP Name Servers Summary

| Name Server | VRF | Priority |
| ----------- | --- | -------- |
| 192.168.1.9 | MGMT | - |

#### IP Name Servers Device Configuration

```eos
ip name-server vrf MGMT 192.168.1.9
```

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | UNIX-Socket | Default Services |
| ---- | ----- | ----------- | ---------------- |
| False | True | - | - |

#### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| MGMT | - | - |

#### Management API HTTP Device Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf MGMT
      no shutdown
```

## Authentication

### Local Users

#### Local Users Summary

| User | Privilege | Role | Disabled | Shell |
| ---- | --------- | ---- | -------- | ----- |
| admin | 15 | network-admin | False | - |
| tony | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 <removed>
username tony privilege 15 role network-admin nopassword
username tony ssh-key ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCUrro9HRd2CeRRS69Yn7Lz8fHfNEj3877gbXSb7eBdzMOFDMd05AWj/4reNc1hRyy8DGx/JXrfLzaJBbh9731cy+4kl2/gtIvin0T3ZWtHJ3HaBTZIRDtoI5Pgnpz1C4Zk/cQZM82RgF7SoQBCAx+dxj73FPylw8zBAtsgFl+t64L8N3atjQn7ThCc7QpPPrefh29WRchKH67Zormq6jX5bNZ/kUUw7fF2Sx4AzL9Ox5MmAiu05rvTm7+hLkahJfBghmKHzeNtZVoUkY7T0sAIQIJ+d/7xjwBrG0Lw2d89jaBmeUU3bbuIxG6nReQ7hWMlTzvxadMfyyf8y792ZRxTr93OPSGBdbS1GuZ15NM9HvP8nx+5V/Xt2fQBS+yc+NypIUwR2swUtyBrnAWYXL7KihO5BlP1JGGuGYYUUGlZlJDNNYeOT4EUhhPJ8peCHsbNqagEbxrrC9I87jKADcSJNyjYxorFN8Crh9rB8HPWFNtolTr/IrVwQliuPHSeNC0= tony@evpn-book
```

### Enable Password

Enable password has been disabled

### AAA Authentication

#### AAA Authentication Summary

| Type | Sub-type | User Stores |
| ---- | -------- | ---------- |
| Login | default | local |

#### AAA Authentication Device Configuration

```eos
aaa authentication login default local
!
```

### AAA Authorization

#### AAA Authorization Summary

| Type | User Stores |
| ---- | ----------- |
| Exec | local |

Authorization for configuration commands is disabled.

#### AAA Authorization Device Configuration

```eos
aaa authorization exec default local
!
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 16384 |

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
spanning-tree mst 0 priority 16384
```

## Internal VLAN Allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

### Internal VLAN Allocation Policy Device Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 10 | DMZ | - |
| 20 | Internal | - |
| 30 | Dev | - |
| 40 | QA | - |
| 50 | Guest | - |
| 100 | VLAN_100 | - |
| 200 | VLAN_200 | - |
| 300 | VLAN_200 | - |
| 400 | VLAN_200 | - |

### VLANs Device Configuration

```eos
!
vlan 10
   name DMZ
!
vlan 20
   name Internal
!
vlan 30
   name Dev
!
vlan 40
   name QA
!
vlan 50
   name Guest
!
vlan 100
   name VLAN_100
!
vlan 200
   name VLAN_200
!
vlan 300
   name VLAN_200
!
vlan 400
   name VLAN_200
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet3 | P2P_spine1_Ethernet6 | - | 192.168.108.13/31 | default | 1550 | False | - | - |
| Ethernet4 | P2P_spine2_Ethernet6 | - | 192.168.108.15/31 | default | 1550 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet3
   description P2P_spine1_Ethernet6
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.13/31
   pim ipv4 sparse-mode
!
interface Ethernet4
   description P2P_spine2_Ethernet6
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.15/31
   pim ipv4 sparse-mode
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 192.168.101.4/32 |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | 192.168.102.4/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | ROUTER_ID | default | - |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description ROUTER_ID
   no shutdown
   ip address 192.168.101.4/32
!
interface Loopback1
   description VXLAN_TUNNEL_SOURCE
   no shutdown
   ip address 192.168.102.4/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan10 | DMZ | VRF_A | - | False |
| Vlan20 | Internal | VRF_A | - | False |
| Vlan30 | Dev | VRF_A | - | False |
| Vlan40 | QA | VRF_A | - | False |
| Vlan50 | Guest | VRF_A | - | False |
| Vlan100 | VLAN_100 | VRF_A | - | False |
| Vlan200 | VLAN_200 | VRF_A | - | False |
| Vlan300 | VLAN_200 | VRF_A | - | False |
| Vlan400 | VLAN_200 | VRF_A | - | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan10 |  VRF_A  |  -  |  10.1.10.1/24  |  -  |  -  |  -  |
| Vlan20 |  VRF_A  |  -  |  10.1.20.1/24  |  -  |  -  |  -  |
| Vlan30 |  VRF_A  |  -  |  10.1.30.1/24  |  -  |  -  |  -  |
| Vlan40 |  VRF_A  |  -  |  10.1.40.1/24  |  -  |  -  |  -  |
| Vlan50 |  VRF_A  |  -  |  10.1.50.1/24  |  -  |  -  |  -  |
| Vlan100 |  VRF_A  |  -  |  10.1.100.1/24  |  -  |  -  |  -  |
| Vlan200 |  VRF_A  |  -  |  10.1.200.1/24  |  -  |  -  |  -  |
| Vlan300 |  VRF_A  |  -  |  10.1.31.1/24  |  -  |  -  |  -  |
| Vlan400 |  VRF_A  |  -  |  10.1.41.1/24  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan10
   description DMZ
   no shutdown
   vrf VRF_A
   ip address virtual 10.1.10.1/24
!
interface Vlan20
   description Internal
   no shutdown
   vrf VRF_A
   ip address virtual 10.1.20.1/24
!
interface Vlan30
   description Dev
   no shutdown
   vrf VRF_A
   ip address virtual 10.1.30.1/24
!
interface Vlan40
   description QA
   no shutdown
   vrf VRF_A
   ip address virtual 10.1.40.1/24
!
interface Vlan50
   description Guest
   no shutdown
   vrf VRF_A
   ip address virtual 10.1.50.1/24
!
interface Vlan100
   description VLAN_100
   no shutdown
   vrf VRF_A
   ip address virtual 10.1.100.1/24
!
interface Vlan200
   description VLAN_200
   no shutdown
   vrf VRF_A
   ip address virtual 10.1.200.1/24
!
interface Vlan300
   description VLAN_200
   no shutdown
   vrf VRF_A
   ip address virtual 10.1.31.1/24
!
interface Vlan400
   description VLAN_200
   no shutdown
   vrf VRF_A
   ip address virtual 10.1.41.1/24
```

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |

##### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 10 | 10010 | - | 239.0.0.9 |
| 20 | 10020 | - | 239.0.0.19 |
| 30 | 10030 | - | 239.0.0.29 |
| 40 | 10040 | - | 239.0.0.39 |
| 50 | 10050 | - | 239.0.0.49 |
| 100 | 10100 | - | 239.0.0.99 |
| 200 | 10200 | - | 239.0.0.199 |
| 300 | 10300 | - | 239.0.1.43 |
| 400 | 10400 | - | 239.0.1.143 |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| VRF_A | 10 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description leaf4_VTEP
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vlan 10 vni 10010
   vxlan vlan 20 vni 10020
   vxlan vlan 30 vni 10030
   vxlan vlan 40 vni 10040
   vxlan vlan 50 vni 10050
   vxlan vlan 100 vni 10100
   vxlan vlan 200 vni 10200
   vxlan vlan 300 vni 10300
   vxlan vlan 400 vni 10400
   vxlan vrf VRF_A vni 10
   vxlan vlan 10 multicast group 239.0.0.9
   vxlan vlan 20 multicast group 239.0.0.19
   vxlan vlan 30 multicast group 239.0.0.29
   vxlan vlan 40 multicast group 239.0.0.39
   vxlan vlan 50 multicast group 239.0.0.49
   vxlan vlan 100 multicast group 239.0.0.99
   vxlan vlan 200 multicast group 239.0.0.199
   vxlan vlan 300 multicast group 239.0.1.43
   vxlan vlan 400 multicast group 239.0.1.143
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### Virtual Router MAC Address

#### Virtual Router MAC Address Summary

Virtual Router MAC Address: 00:1c:73:00:00:99

#### Virtual Router MAC Address Device Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:00:99
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | False |
| VRF_A | True |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
ip routing vrf VRF_A
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |
| VRF_A | false |

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP | Exit interface | Administrative Distance | Tag | Route Name | Metric |
| --- | ------------------ | ----------- | -------------- | ----------------------- | --- | ---------- | ------ |
| MGMT | 0.0.0.0/0 | 172.20.20.1 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 172.20.20.1
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65103 | 192.168.101.4 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| maximum-paths 4 ecmp 4 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 192.168.101.101 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.102 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.108.12 | 65001 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.108.14 | 65001 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Encapsulation | Next-hop-self Source Interface |
| ---------- | -------- | ------------ | ------------- | ------------- | ------------------------------ |
| EVPN-OVERLAY-PEERS | True |  - | - | default | - |

#### Router BGP VLAN Aware Bundles

| VLAN Aware Bundle | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute | VLANs |
| ----------------- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ | ----- |
| VRF_A | 192.168.101.4:10 | 10:10 | - | - | learned<br>igmp | 10,20,30,40,50,100,200,300,400 |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute | Graceful Restart |
| --- | ------------------- | ------------ | ---------------- |
| VRF_A | 192.168.101.4:10 | connected | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65103
   router-id 192.168.101.4
   no bgp default ipv4-unicast
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 192.168.101.101 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.101 remote-as 65001
   neighbor 192.168.101.101 description spine1_Loopback0
   neighbor 192.168.101.102 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.102 remote-as 65001
   neighbor 192.168.101.102 description spine2_Loopback0
   neighbor 192.168.108.12 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.108.12 remote-as 65001
   neighbor 192.168.108.12 description spine1_Ethernet6
   neighbor 192.168.108.14 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.108.14 remote-as 65001
   neighbor 192.168.108.14 description spine2_Ethernet6
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan-aware-bundle VRF_A
      rd 192.168.101.4:10
      route-target both 10:10
      redistribute igmp
      redistribute learned
      vlan 10,20,30,40,50,100,200,300,400
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
   !
   vrf VRF_A
      rd 192.168.101.4:10
      route-target import evpn 10:10
      route-target export evpn 10:10
      router-id 192.168.101.4
      redistribute connected
```

## BFD

### Router BFD

#### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 1200 | 1200 | 3 |

#### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 1200 min-rx 1200 multiplier 3
```

## Multicast

### IP IGMP Snooping

#### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

##### IP IGMP Snooping Vlan Summary

| Vlan | IGMP Snooping | Fast Leave | Max Groups | Proxy |
| ---- | ------------- | ---------- | ---------- | ----- |
| 10 | - | - | - | - |
| 20 | - | - | - | - |
| 30 | - | - | - | - |
| 40 | - | - | - | - |
| 50 | - | - | - | - |
| 100 | - | - | - | - |
| 200 | - | - | - | - |
| 300 | - | - | - | - |
| 400 | - | - | - | - |

| Vlan | Querier Enabled | IP Address | Query Interval | Max Response Time | Last Member Query Interval | Last Member Query Count | Startup Query Interval | Startup Query Count | Version |
| ---- | --------------- | ---------- | -------------- | ----------------- | -------------------------- | ----------------------- | ---------------------- | ------------------- | ------- |
| 10 | True | 192.168.101.4 | - | - | - | - | - | - | - |
| 20 | True | 192.168.101.4 | - | - | - | - | - | - | - |
| 30 | True | 192.168.101.4 | - | - | - | - | - | - | - |
| 40 | True | 192.168.101.4 | - | - | - | - | - | - | - |
| 50 | True | 192.168.101.4 | - | - | - | - | - | - | - |
| 100 | True | 192.168.101.4 | - | - | - | - | - | - | - |
| 200 | True | 192.168.101.4 | - | - | - | - | - | - | - |
| 300 | True | 192.168.101.4 | - | - | - | - | - | - | - |
| 400 | True | 192.168.101.4 | - | - | - | - | - | - | - |

#### IP IGMP Snooping Device Configuration

```eos
!
ip igmp snooping vlan 10 querier
ip igmp snooping vlan 10 querier address 192.168.101.4
ip igmp snooping vlan 20 querier
ip igmp snooping vlan 20 querier address 192.168.101.4
ip igmp snooping vlan 30 querier
ip igmp snooping vlan 30 querier address 192.168.101.4
ip igmp snooping vlan 40 querier
ip igmp snooping vlan 40 querier address 192.168.101.4
ip igmp snooping vlan 50 querier
ip igmp snooping vlan 50 querier address 192.168.101.4
ip igmp snooping vlan 100 querier
ip igmp snooping vlan 100 querier address 192.168.101.4
ip igmp snooping vlan 200 querier
ip igmp snooping vlan 200 querier address 192.168.101.4
ip igmp snooping vlan 300 querier
ip igmp snooping vlan 300 querier address 192.168.101.4
ip igmp snooping vlan 400 querier
ip igmp snooping vlan 400 querier address 192.168.101.4
```

### Router Multicast

#### IP Router Multicast Summary

- Routing for IPv4 multicast is enabled.
- Software forwarding by the Software Forwarding Engine (SFE)

#### Router Multicast Device Configuration

```eos
!
router multicast
   ipv4
      routing
      software-forwarding sfe
```

### PIM Sparse Mode

#### Router PIM Sparse Mode

##### IP Sparse Mode Information

BFD enabled: False

##### IP Rendezvous Information

| Rendezvous Point Address | Group Address | Access Lists | Priority | Hashmask | Override |
| ------------------------ | ------------- | ------------ | -------- | -------- | -------- |
| 192.168.109.10 | 239.0.0.0/22 | - | - | - | - |

##### Router Multicast Device Configuration

```eos
!
router pim sparse-mode
   ipv4
      rp address 192.168.109.10 239.0.0.0/22
```

#### PIM Sparse Mode Enabled Interfaces

| Interface Name | VRF Name | IP Version | Border Router | DR Priority | Local Interface |
| -------------- | -------- | ---------- | ------------- | ----------- | --------------- |
| Ethernet3 | - | IPv4 | - | - | - |
| Ethernet4 | - | IPv4 | - | - | - |

## Filters

### Prefix-lists

#### Prefix-lists Summary

##### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.101.0/24 eq 32 |
| 20 | permit 192.168.102.0/24 eq 32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.101.0/24 eq 32
   seq 20 permit 192.168.102.0/24 eq 32
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-2-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY | - | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |
| VRF_A | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance VRF_A
```
