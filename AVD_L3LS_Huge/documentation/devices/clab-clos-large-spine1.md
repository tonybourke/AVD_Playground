# clab-clos-large-spine1

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [DNS Domain](#dns-domain)
  - [IP Name Servers](#ip-name-servers)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
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
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router ISIS](#router-isis)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management0 | oob_management | oob | MGMT | 172.20.20.101/24 | 172.20.20.1 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management0 | oob_management | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management0
   description oob_management
   no shutdown
   vrf MGMT
   ip address 172.20.20.101/24
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

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | - |

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

STP mode: **none**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
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

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet2 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF1_Ethernet3 | routed | - | 192.168.108.0/31 | default | 1550 | False | - | - |
| Ethernet3 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF2_Ethernet3 | routed | - | 192.168.108.6/31 | default | 1550 | False | - | - |
| Ethernet4 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF3_Ethernet3 | routed | - | 192.168.108.12/31 | default | 1550 | False | - | - |
| Ethernet5 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF4_Ethernet3 | routed | - | 192.168.108.18/31 | default | 1550 | False | - | - |
| Ethernet6 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF5_Ethernet3 | routed | - | 192.168.108.24/31 | default | 1550 | False | - | - |
| Ethernet7 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF6_Ethernet3 | routed | - | 192.168.108.30/31 | default | 1550 | False | - | - |
| Ethernet8 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF7_Ethernet3 | routed | - | 192.168.108.36/31 | default | 1550 | False | - | - |
| Ethernet9 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF8_Ethernet3 | routed | - | 192.168.108.42/31 | default | 1550 | False | - | - |
| Ethernet10 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF9_Ethernet3 | routed | - | 192.168.108.48/31 | default | 1550 | False | - | - |
| Ethernet11 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF10_Ethernet3 | routed | - | 192.168.108.54/31 | default | 1550 | False | - | - |
| Ethernet12 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF11_Ethernet3 | routed | - | 192.168.108.60/31 | default | 1550 | False | - | - |
| Ethernet13 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF12_Ethernet3 | routed | - | 192.168.108.66/31 | default | 1550 | False | - | - |
| Ethernet14 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF13_Ethernet3 | routed | - | 192.168.108.72/31 | default | 1550 | False | - | - |
| Ethernet15 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF14_Ethernet3 | routed | - | 192.168.108.78/31 | default | 1550 | False | - | - |
| Ethernet16 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF15_Ethernet3 | routed | - | 192.168.108.84/31 | default | 1550 | False | - | - |
| Ethernet17 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF16_Ethernet3 | routed | - | 192.168.108.90/31 | default | 1550 | False | - | - |
| Ethernet18 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF17_Ethernet3 | routed | - | 192.168.108.96/31 | default | 1550 | False | - | - |
| Ethernet19 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF18_Ethernet3 | routed | - | 192.168.108.102/31 | default | 1550 | False | - | - |
| Ethernet20 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF19_Ethernet3 | routed | - | 192.168.108.108/31 | default | 1550 | False | - | - |
| Ethernet21 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF20_Ethernet3 | routed | - | 192.168.108.114/31 | default | 1550 | False | - | - |
| Ethernet22 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF21_Ethernet3 | routed | - | 192.168.108.120/31 | default | 1550 | False | - | - |
| Ethernet23 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF22_Ethernet3 | routed | - | 192.168.108.126/31 | default | 1550 | False | - | - |
| Ethernet24 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF23_Ethernet3 | routed | - | 192.168.108.132/31 | default | 1550 | False | - | - |
| Ethernet25 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF24_Ethernet3 | routed | - | 192.168.108.138/31 | default | 1550 | False | - | - |
| Ethernet26 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF25_Ethernet3 | routed | - | 192.168.108.144/31 | default | 1550 | False | - | - |
| Ethernet27 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF26_Ethernet3 | routed | - | 192.168.108.150/31 | default | 1550 | False | - | - |
| Ethernet28 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF27_Ethernet3 | routed | - | 192.168.108.156/31 | default | 1550 | False | - | - |
| Ethernet29 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF28_Ethernet3 | routed | - | 192.168.108.162/31 | default | 1550 | False | - | - |
| Ethernet30 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF29_Ethernet3 | routed | - | 192.168.108.168/31 | default | 1550 | False | - | - |
| Ethernet31 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF30_Ethernet3 | routed | - | 192.168.108.174/31 | default | 1550 | False | - | - |
| Ethernet32 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF31_Ethernet3 | routed | - | 192.168.108.180/31 | default | 1550 | False | - | - |
| Ethernet33 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF32_Ethernet3 | routed | - | 192.168.108.186/31 | default | 1550 | False | - | - |
| Ethernet34 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF33_Ethernet3 | routed | - | 192.168.108.192/31 | default | 1550 | False | - | - |
| Ethernet35 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF34_Ethernet3 | routed | - | 192.168.108.198/31 | default | 1550 | False | - | - |
| Ethernet36 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF35_Ethernet3 | routed | - | 192.168.108.204/31 | default | 1550 | False | - | - |
| Ethernet37 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF36_Ethernet3 | routed | - | 192.168.108.210/31 | default | 1550 | False | - | - |
| Ethernet38 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF37_Ethernet3 | routed | - | 192.168.108.216/31 | default | 1550 | False | - | - |
| Ethernet39 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF38_Ethernet3 | routed | - | 192.168.108.222/31 | default | 1550 | False | - | - |
| Ethernet40 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF39_Ethernet3 | routed | - | 192.168.108.228/31 | default | 1550 | False | - | - |
| Ethernet41 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF40_Ethernet3 | routed | - | 192.168.108.234/31 | default | 1550 | False | - | - |
| Ethernet42 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF41_Ethernet3 | routed | - | 192.168.108.240/31 | default | 1550 | False | - | - |
| Ethernet43 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF42_Ethernet3 | routed | - | 192.168.108.246/31 | default | 1550 | False | - | - |
| Ethernet44 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF43_Ethernet3 | routed | - | 192.168.108.252/31 | default | 1550 | False | - | - |
| Ethernet45 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF44_Ethernet3 | routed | - | 192.168.109.2/31 | default | 1550 | False | - | - |
| Ethernet46 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF45_Ethernet3 | routed | - | 192.168.109.8/31 | default | 1550 | False | - | - |
| Ethernet47 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF46_Ethernet3 | routed | - | 192.168.109.14/31 | default | 1550 | False | - | - |
| Ethernet48 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF47_Ethernet3 | routed | - | 192.168.109.20/31 | default | 1550 | False | - | - |
| Ethernet49 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF48_Ethernet3 | routed | - | 192.168.109.26/31 | default | 1550 | False | - | - |
| Ethernet50 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF49_Ethernet3 | routed | - | 192.168.109.32/31 | default | 1550 | False | - | - |
| Ethernet51 | P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF50_Ethernet3 | routed | - | 192.168.109.38/31 | default | 1550 | False | - | - |
| Ethernet52 | P2P_LINK_TO_CLAB-CLOS-LARGE-BORDERLEAF1_Ethernet3 | routed | - | 192.168.110.28/31 | default | 1550 | False | - | - |
| Ethernet53 | P2P_LINK_TO_CLAB-CLOS-LARGE-BORDERLEAF2_Ethernet3 | routed | - | 192.168.110.34/31 | default | 1550 | False | - | - |

##### ISIS

| Interface | Channel Group | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | Authentication Mode |
| --------- | ------------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------- |
| Ethernet2 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet3 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet4 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet5 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet6 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet7 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet8 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet9 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet10 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet11 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet12 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet13 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet14 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet15 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet16 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet17 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet18 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet19 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet20 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet21 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet22 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet23 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet24 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet25 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet26 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet27 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet28 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet29 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet30 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet31 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet32 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet33 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet34 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet35 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet36 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet37 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet38 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet39 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet40 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet41 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet42 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet43 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet44 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet45 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet46 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet47 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet48 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet49 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet50 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet51 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet52 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet53 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet2
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF1_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.0/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet3
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF2_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.6/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet4
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF3_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.12/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet5
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF4_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.18/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet6
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF5_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.24/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet7
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF6_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.30/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet8
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF7_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.36/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet9
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF8_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.42/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet10
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF9_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.48/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet11
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF10_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.54/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet12
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF11_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.60/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet13
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF12_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.66/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet14
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF13_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.72/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet15
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF14_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.78/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet16
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF15_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.84/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet17
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF16_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.90/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet18
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF17_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.96/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet19
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF18_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.102/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet20
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF19_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.108/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet21
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF20_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.114/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet22
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF21_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.120/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet23
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF22_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.126/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet24
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF23_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.132/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet25
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF24_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.138/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet26
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF25_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.144/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet27
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF26_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.150/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet28
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF27_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.156/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet29
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF28_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.162/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet30
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF29_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.168/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet31
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF30_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.174/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet32
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF31_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.180/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet33
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF32_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.186/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet34
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF33_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.192/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet35
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF34_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.198/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet36
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF35_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.204/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet37
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF36_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.210/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet38
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF37_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.216/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet39
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF38_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.222/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet40
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF39_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.228/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet41
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF40_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.234/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet42
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF41_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.240/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet43
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF42_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.246/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet44
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF43_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.108.252/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet45
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF44_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.109.2/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet46
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF45_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.109.8/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet47
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF46_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.109.14/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet48
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF47_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.109.20/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet49
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF48_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.109.26/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet50
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF49_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.109.32/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet51
   description P2P_LINK_TO_CLAB-CLOS-LARGE-LEAF50_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.109.38/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet52
   description P2P_LINK_TO_CLAB-CLOS-LARGE-BORDERLEAF1_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.110.28/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet53
   description P2P_LINK_TO_CLAB-CLOS-LARGE-BORDERLEAF2_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ip address 192.168.110.34/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.101.101/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |

##### ISIS

| Interface | ISIS instance | ISIS metric | Interface mode |
| --------- | ------------- | ----------- | -------------- |
| Loopback0 | EVPN_UNDERLAY | - | passive |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 192.168.101.101/32
   isis enable EVPN_UNDERLAY
   isis passive
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | False |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |

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

### Router ISIS

#### Router ISIS Summary

| Settings | Value |
| -------- | ----- |
| Instance | EVPN_UNDERLAY |
| Net-ID | 49.0001.1921.6810.1101.00 |
| Type | level-2 |
| Router-ID | 192.168.101.101 |
| Log Adjacency Changes | True |

#### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |
| Ethernet2 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet3 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet4 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet5 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet6 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet7 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet8 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet9 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet10 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet11 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet12 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet13 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet14 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet15 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet16 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet17 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet18 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet19 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet20 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet21 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet22 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet23 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet24 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet25 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet26 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet27 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet28 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet29 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet30 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet31 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet32 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet33 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet34 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet35 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet36 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet37 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet38 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet39 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet40 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet41 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet42 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet43 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet44 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet45 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet46 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet47 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet48 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet49 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet50 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet51 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet52 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet53 | EVPN_UNDERLAY | 50 | point-to-point |
| Loopback0 | EVPN_UNDERLAY | - | passive |

#### ISIS IPv4 Address Family Summary

| Settings | Value |
| -------- | ----- |
| IPv4 Address-family Enabled | True |
| Maximum-paths | 4 |

#### Router ISIS Device Configuration

```eos
!
router isis EVPN_UNDERLAY
   net 49.0001.1921.6810.1101.00
   is-type level-2
   router-id ipv4 192.168.101.101
   log-adjacency-changes
   !
   address-family ipv4 unicast
      maximum-paths 4
   !
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65001 | 192.168.101.101 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| maximum-paths 4 ecmp 4 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Next-hop unchanged | True |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 192.168.101.1 | 65100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.2 | 65100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.3 | 65102 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.4 | 65102 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.5 | 65104 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.6 | 65104 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.7 | 65106 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.8 | 65106 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.9 | 65108 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.10 | 65108 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.11 | 65110 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.12 | 65110 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.13 | 65112 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.14 | 65112 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.15 | 65114 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.16 | 65114 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.17 | 65116 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.18 | 65116 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.19 | 65118 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.20 | 65118 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.21 | 65120 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.22 | 65120 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.23 | 65122 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.24 | 65122 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.25 | 65124 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.26 | 65124 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.27 | 65126 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.28 | 65126 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.29 | 65128 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.30 | 65128 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.31 | 65130 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.32 | 65130 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.33 | 65132 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.34 | 65132 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.35 | 65134 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.36 | 65134 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.37 | 65136 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.38 | 65136 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.39 | 65138 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.40 | 65138 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.41 | 65140 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.42 | 65140 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.43 | 65142 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.44 | 65142 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.45 | 65144 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.46 | 65144 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.47 | 65146 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.48 | 65146 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.49 | 65148 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.50 | 65148 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.91 | 65190 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.101.92 | 65191 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Encapsulation |
| ---------- | -------- | ------------- |
| EVPN-OVERLAY-PEERS | True | default |

#### Router BGP Device Configuration

```eos
!
router bgp 65001
   router-id 192.168.101.101
   maximum-paths 4 ecmp 4
   no bgp default ipv4-unicast
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS next-hop-unchanged
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor 192.168.101.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.1 remote-as 65100
   neighbor 192.168.101.1 description clab-clos-large-leaf1
   neighbor 192.168.101.2 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.2 remote-as 65100
   neighbor 192.168.101.2 description clab-clos-large-leaf2
   neighbor 192.168.101.3 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.3 remote-as 65102
   neighbor 192.168.101.3 description clab-clos-large-leaf3
   neighbor 192.168.101.4 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.4 remote-as 65102
   neighbor 192.168.101.4 description clab-clos-large-leaf4
   neighbor 192.168.101.5 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.5 remote-as 65104
   neighbor 192.168.101.5 description clab-clos-large-leaf5
   neighbor 192.168.101.6 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.6 remote-as 65104
   neighbor 192.168.101.6 description clab-clos-large-leaf6
   neighbor 192.168.101.7 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.7 remote-as 65106
   neighbor 192.168.101.7 description clab-clos-large-leaf7
   neighbor 192.168.101.8 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.8 remote-as 65106
   neighbor 192.168.101.8 description clab-clos-large-leaf8
   neighbor 192.168.101.9 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.9 remote-as 65108
   neighbor 192.168.101.9 description clab-clos-large-leaf9
   neighbor 192.168.101.10 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.10 remote-as 65108
   neighbor 192.168.101.10 description clab-clos-large-leaf10
   neighbor 192.168.101.11 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.11 remote-as 65110
   neighbor 192.168.101.11 description clab-clos-large-leaf11
   neighbor 192.168.101.12 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.12 remote-as 65110
   neighbor 192.168.101.12 description clab-clos-large-leaf12
   neighbor 192.168.101.13 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.13 remote-as 65112
   neighbor 192.168.101.13 description clab-clos-large-leaf13
   neighbor 192.168.101.14 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.14 remote-as 65112
   neighbor 192.168.101.14 description clab-clos-large-leaf14
   neighbor 192.168.101.15 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.15 remote-as 65114
   neighbor 192.168.101.15 description clab-clos-large-leaf15
   neighbor 192.168.101.16 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.16 remote-as 65114
   neighbor 192.168.101.16 description clab-clos-large-leaf16
   neighbor 192.168.101.17 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.17 remote-as 65116
   neighbor 192.168.101.17 description clab-clos-large-leaf17
   neighbor 192.168.101.18 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.18 remote-as 65116
   neighbor 192.168.101.18 description clab-clos-large-leaf18
   neighbor 192.168.101.19 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.19 remote-as 65118
   neighbor 192.168.101.19 description clab-clos-large-leaf19
   neighbor 192.168.101.20 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.20 remote-as 65118
   neighbor 192.168.101.20 description clab-clos-large-leaf20
   neighbor 192.168.101.21 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.21 remote-as 65120
   neighbor 192.168.101.21 description clab-clos-large-leaf21
   neighbor 192.168.101.22 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.22 remote-as 65120
   neighbor 192.168.101.22 description clab-clos-large-leaf22
   neighbor 192.168.101.23 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.23 remote-as 65122
   neighbor 192.168.101.23 description clab-clos-large-leaf23
   neighbor 192.168.101.24 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.24 remote-as 65122
   neighbor 192.168.101.24 description clab-clos-large-leaf24
   neighbor 192.168.101.25 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.25 remote-as 65124
   neighbor 192.168.101.25 description clab-clos-large-leaf25
   neighbor 192.168.101.26 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.26 remote-as 65124
   neighbor 192.168.101.26 description clab-clos-large-leaf26
   neighbor 192.168.101.27 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.27 remote-as 65126
   neighbor 192.168.101.27 description clab-clos-large-leaf27
   neighbor 192.168.101.28 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.28 remote-as 65126
   neighbor 192.168.101.28 description clab-clos-large-leaf28
   neighbor 192.168.101.29 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.29 remote-as 65128
   neighbor 192.168.101.29 description clab-clos-large-leaf29
   neighbor 192.168.101.30 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.30 remote-as 65128
   neighbor 192.168.101.30 description clab-clos-large-leaf30
   neighbor 192.168.101.31 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.31 remote-as 65130
   neighbor 192.168.101.31 description clab-clos-large-leaf31
   neighbor 192.168.101.32 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.32 remote-as 65130
   neighbor 192.168.101.32 description clab-clos-large-leaf32
   neighbor 192.168.101.33 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.33 remote-as 65132
   neighbor 192.168.101.33 description clab-clos-large-leaf33
   neighbor 192.168.101.34 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.34 remote-as 65132
   neighbor 192.168.101.34 description clab-clos-large-leaf34
   neighbor 192.168.101.35 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.35 remote-as 65134
   neighbor 192.168.101.35 description clab-clos-large-leaf35
   neighbor 192.168.101.36 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.36 remote-as 65134
   neighbor 192.168.101.36 description clab-clos-large-leaf36
   neighbor 192.168.101.37 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.37 remote-as 65136
   neighbor 192.168.101.37 description clab-clos-large-leaf37
   neighbor 192.168.101.38 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.38 remote-as 65136
   neighbor 192.168.101.38 description clab-clos-large-leaf38
   neighbor 192.168.101.39 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.39 remote-as 65138
   neighbor 192.168.101.39 description clab-clos-large-leaf39
   neighbor 192.168.101.40 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.40 remote-as 65138
   neighbor 192.168.101.40 description clab-clos-large-leaf40
   neighbor 192.168.101.41 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.41 remote-as 65140
   neighbor 192.168.101.41 description clab-clos-large-leaf41
   neighbor 192.168.101.42 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.42 remote-as 65140
   neighbor 192.168.101.42 description clab-clos-large-leaf42
   neighbor 192.168.101.43 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.43 remote-as 65142
   neighbor 192.168.101.43 description clab-clos-large-leaf43
   neighbor 192.168.101.44 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.44 remote-as 65142
   neighbor 192.168.101.44 description clab-clos-large-leaf44
   neighbor 192.168.101.45 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.45 remote-as 65144
   neighbor 192.168.101.45 description clab-clos-large-leaf45
   neighbor 192.168.101.46 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.46 remote-as 65144
   neighbor 192.168.101.46 description clab-clos-large-leaf46
   neighbor 192.168.101.47 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.47 remote-as 65146
   neighbor 192.168.101.47 description clab-clos-large-leaf47
   neighbor 192.168.101.48 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.48 remote-as 65146
   neighbor 192.168.101.48 description clab-clos-large-leaf48
   neighbor 192.168.101.49 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.49 remote-as 65148
   neighbor 192.168.101.49 description clab-clos-large-leaf49
   neighbor 192.168.101.50 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.50 remote-as 65148
   neighbor 192.168.101.50 description clab-clos-large-leaf50
   neighbor 192.168.101.91 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.91 remote-as 65190
   neighbor 192.168.101.91 description clab-clos-large-borderleaf1
   neighbor 192.168.101.92 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.92 remote-as 65191
   neighbor 192.168.101.92 description clab-clos-large-borderleaf2
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
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

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
```
