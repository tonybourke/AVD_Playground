# clab-clos-large-borderleaf1

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
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
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
| Management0 | OOB_MANAGEMENT | oob | MGMT | 172.20.20.91/24 | 172.20.20.1 |

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
   ip address 172.20.20.91/24
```

### DNS Domain

DNS domain: atd.lab

#### DNS Domain Device Configuration

```eos
dns domain atd.lab
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
| arista | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 <removed>
username arista privilege 15 role network-admin nopassword
username arista ssh-key ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDaaW0yCS+kwtUVIJdwCVaw2+Ul/yYhaPXYltoVcszcEJPWCSwAmMdvrlecxcyEfrs1KJLYVLD8RwmMRlMRrteYJzmk8MGuAyNxQMcma0EWI78suzJOlxGczxwUzZY2+vYwLgWQZPYEZeScjY8ko68r+sEUmgg+y/WC+OGshtytqahs1zaJhDHwu2y3GAW9KnCA1vQL8qyaXvTKkci6+unMlwdc7jTL7bktoudWFKAAHxVtJf0SdBGvWdbbh3JgAt3mHtjKMfm+8qQgv1mfr6Sn41tLlsmn/RTsMMkDbuYVmpjXFSb6LXwf/ylx1zc/FxJHHXh4yD0wOKD3rYEIjndF7uGEqrs1BZtje50L6YPVcjUCGI9kL4R1BUI8uzTmTLATOmDJ03KAaTnXwkhlW96FQshJjiDL4K9FZUaYww6vEp2nk2XOaXxyB1JXe0/2A/H57f2wIR1TwdqAbcHOkGLqj0mS+focnRJvaxPk6ytIGmfRqF9n8K0RLMXN9s/G+sk= tony@autobox-huge
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

## Monitoring

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | 192.168.1.201:9910 | MGMT | token,/tmp/token | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | False |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=192.168.1.201:9910 -cvauth=token,/tmp/token -cvvrf=MGMT -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
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
| 1000 | VLAN_1000 | - |
| 1001 | VLAN_1001 | - |
| 1002 | VLAN_1002 | - |
| 1003 | VLAN_1003 | - |
| 1004 | VLAN_1004 | - |
| 1005 | VLAN_1005 | - |
| 1006 | VLAN_1006 | - |

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
!
vlan 1000
   name VLAN_1000
!
vlan 1001
   name VLAN_1001
!
vlan 1002
   name VLAN_1002
!
vlan 1003
   name VLAN_1003
!
vlan 1004
   name VLAN_1004
!
vlan 1005
   name VLAN_1005
!
vlan 1006
   name VLAN_1006
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
| Ethernet6 | - | - | 10.1.5.0/31 | VRF_A | - | False | - | - |

##### IPv6

| Interface | Description | Channel Group | IPv6 Address | VRF | MTU | Shutdown | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | ----------- | --------------| ------------ | --- | --- | -------- | -------------- | -------------------| ----------- | ------------ |
| Ethernet3 | P2P_clab-clos-large-spine1_Ethernet52 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet4 | P2P_clab-clos-large-spine2_Ethernet52 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet5 | P2P_clab-clos-large-spine3_Ethernet52 | - | - | default | 1550 | False | - | - | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet3
   description P2P_clab-clos-large-spine1_Ethernet52
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet4
   description P2P_clab-clos-large-spine2_Ethernet52
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet5
   description P2P_clab-clos-large-spine3_Ethernet52
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet6
   no shutdown
   no switchport
   vrf VRF_A
   ip address 10.1.5.0/31
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 192.168.101.91/32 |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | 192.168.102.91/32 |

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
   ip address 192.168.101.91/32
!
interface Loopback1
   description VXLAN_TUNNEL_SOURCE
   no shutdown
   ip address 192.168.102.91/32
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
| 10 | 10010 | - | - |
| 20 | 10020 | - | - |
| 30 | 10030 | - | - |
| 40 | 10040 | - | - |
| 50 | 10050 | - | - |
| 100 | 10100 | - | - |
| 200 | 10200 | - | - |
| 300 | 10300 | - | - |
| 400 | 10400 | - | - |
| 1000 | 11000 | - | - |
| 1001 | 11001 | - | - |
| 1002 | 11002 | - | - |
| 1003 | 11003 | - | - |
| 1004 | 11004 | - | - |
| 1005 | 11005 | - | - |
| 1006 | 11006 | - | - |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| VRF_A | 10 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description clab-clos-large-borderleaf1_VTEP
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
   vxlan vlan 1000 vni 11000
   vxlan vlan 1001 vni 11001
   vxlan vlan 1002 vni 11002
   vxlan vlan 1003 vni 11003
   vxlan vlan 1004 vni 11004
   vxlan vlan 1005 vni 11005
   vxlan vlan 1006 vni 11006
   vxlan vrf VRF_A vni 10
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
| default | True (ipv6 interfaces) |
| MGMT | False |
| VRF_A | True |

#### IP Routing Device Configuration

```eos
!
ip routing ipv6 interfaces
no ip routing vrf MGMT
ip routing vrf VRF_A
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | false |
| VRF_A | false |

#### IPv6 Routing Device Configuration

```eos
!
ipv6 unicast-routing
```

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
| 65190 | 192.168.101.91 |

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
| 192.168.101.103 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.1.5.1 | 1 | VRF_A | - | - | - | - | - | - | - | - | - |

#### BGP Neighbor Interfaces

| Neighbor Interface | VRF | Peer Group | Remote AS | Peer Filter |
| ------------------ | --- | ---------- | --------- | ----------- |
| Ethernet3 | default | IPv4-UNDERLAY-PEERS | 65001 | - |
| Ethernet4 | default | IPv4-UNDERLAY-PEERS | 65001 | - |
| Ethernet5 | default | IPv4-UNDERLAY-PEERS | 65001 | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Encapsulation | Next-hop-self Source Interface |
| ---------- | -------- | ------------ | ------------- | ------------- | ------------------------------ |
| EVPN-OVERLAY-PEERS | True |  - | - | default | - |

#### Router BGP VLAN Aware Bundles

| VLAN Aware Bundle | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute | VLANs |
| ----------------- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ | ----- |
| VLAN_1000 | 192.168.101.91:11000 | 11000:11000 | - | - | learned | 1000 |
| VLAN_1001 | 192.168.101.91:11001 | 11001:11001 | - | - | learned | 1001 |
| VLAN_1002 | 192.168.101.91:11002 | 11002:11002 | - | - | learned | 1002 |
| VLAN_1003 | 192.168.101.91:11003 | 11003:11003 | - | - | learned | 1003 |
| VLAN_1004 | 192.168.101.91:11004 | 11004:11004 | - | - | learned | 1004 |
| VLAN_1005 | 192.168.101.91:11005 | 11005:11005 | - | - | learned | 1005 |
| VLAN_1006 | 192.168.101.91:11006 | 11006:11006 | - | - | learned | 1006 |
| VRF_A | 192.168.101.91:10 | 10:10 | - | - | learned | 10,20,30,40,50,100,200,300,400 |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute | Graceful Restart |
| --- | ------------------- | ------------ | ---------------- |
| VRF_A | 192.168.101.91:10 | connected | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65190
   router-id 192.168.101.91
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
   neighbor 192.168.101.101 description clab-clos-large-spine1_Loopback0
   neighbor 192.168.101.102 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.102 remote-as 65001
   neighbor 192.168.101.102 description clab-clos-large-spine2_Loopback0
   neighbor 192.168.101.103 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.103 remote-as 65001
   neighbor 192.168.101.103 description clab-clos-large-spine3_Loopback0
   redistribute connected route-map RM-CONN-2-BGP
   neighbor interface Ethernet3 peer-group IPv4-UNDERLAY-PEERS remote-as 65001
   neighbor interface Ethernet4 peer-group IPv4-UNDERLAY-PEERS remote-as 65001
   neighbor interface Ethernet5 peer-group IPv4-UNDERLAY-PEERS remote-as 65001
   !
   vlan-aware-bundle VLAN_1000
      rd 192.168.101.91:11000
      route-target both 11000:11000
      redistribute learned
      vlan 1000
   !
   vlan-aware-bundle VLAN_1001
      rd 192.168.101.91:11001
      route-target both 11001:11001
      redistribute learned
      vlan 1001
   !
   vlan-aware-bundle VLAN_1002
      rd 192.168.101.91:11002
      route-target both 11002:11002
      redistribute learned
      vlan 1002
   !
   vlan-aware-bundle VLAN_1003
      rd 192.168.101.91:11003
      route-target both 11003:11003
      redistribute learned
      vlan 1003
   !
   vlan-aware-bundle VLAN_1004
      rd 192.168.101.91:11004
      route-target both 11004:11004
      redistribute learned
      vlan 1004
   !
   vlan-aware-bundle VLAN_1005
      rd 192.168.101.91:11005
      route-target both 11005:11005
      redistribute learned
      vlan 1005
   !
   vlan-aware-bundle VLAN_1006
      rd 192.168.101.91:11006
      route-target both 11006:11006
      redistribute learned
      vlan 1006
   !
   vlan-aware-bundle VRF_A
      rd 192.168.101.91:10
      route-target both 10:10
      redistribute learned
      vlan 10,20,30,40,50,100,200,300,400
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS next-hop address-family ipv6 originate
   !
   vrf VRF_A
      rd 192.168.101.91:10
      route-target import evpn 10:10
      route-target export evpn 10:10
      router-id 192.168.101.91
      neighbor 10.1.5.1 remote-as 1
      redistribute connected
      !
      address-family ipv4
         neighbor 10.1.5.1 activate
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

#### IP IGMP Snooping Device Configuration

```eos
```

### Router Multicast

#### IP Router Multicast Summary

- Routing for IPv4 multicast is enabled.

#### Router Multicast Device Configuration

```eos
!
router multicast
   ipv4
      routing
```

### PIM Sparse Mode

#### PIM Sparse Mode Enabled Interfaces

| Interface Name | VRF Name | IP Version | Border Router | DR Priority | Local Interface |
| -------------- | -------- | ---------- | ------------- | ----------- | --------------- |
| Ethernet3 | - | IPv4 | - | - | - |
| Ethernet4 | - | IPv4 | - | - | - |
| Ethernet5 | - | IPv4 | - | - | - |

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
