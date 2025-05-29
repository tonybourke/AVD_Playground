# clab-clos-large-spine2

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
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
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
| Management0 | OOB_MANAGEMENT | oob | MGMT | 172.20.20.102/24 | 172.20.20.1 |

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
   ip address 172.20.20.102/24
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

##### IPv6

| Interface | Description | Channel Group | IPv6 Address | VRF | MTU | Shutdown | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | ----------- | --------------| ------------ | --- | --- | -------- | -------------- | -------------------| ----------- | ------------ |
| Ethernet2 | P2P_clab-clos-large-leaf1_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet3 | P2P_clab-clos-large-leaf2_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet4 | P2P_clab-clos-large-leaf3_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet5 | P2P_clab-clos-large-leaf4_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet6 | P2P_clab-clos-large-leaf5_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet7 | P2P_clab-clos-large-leaf6_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet8 | P2P_clab-clos-large-leaf7_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet9 | P2P_clab-clos-large-leaf8_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet10 | P2P_clab-clos-large-leaf9_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet11 | P2P_clab-clos-large-leaf10_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet12 | P2P_clab-clos-large-leaf11_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet13 | P2P_clab-clos-large-leaf12_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet14 | P2P_clab-clos-large-leaf13_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet15 | P2P_clab-clos-large-leaf14_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet16 | P2P_clab-clos-large-leaf15_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet17 | P2P_clab-clos-large-leaf16_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet18 | P2P_clab-clos-large-leaf17_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet19 | P2P_clab-clos-large-leaf18_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet20 | P2P_clab-clos-large-leaf19_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet21 | P2P_clab-clos-large-leaf20_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet22 | P2P_clab-clos-large-leaf21_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet23 | P2P_clab-clos-large-leaf22_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet24 | P2P_clab-clos-large-leaf23_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet25 | P2P_clab-clos-large-leaf24_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet26 | P2P_clab-clos-large-leaf25_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet27 | P2P_clab-clos-large-leaf26_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet28 | P2P_clab-clos-large-leaf27_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet29 | P2P_clab-clos-large-leaf28_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet30 | P2P_clab-clos-large-leaf29_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet31 | P2P_clab-clos-large-leaf30_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet32 | P2P_clab-clos-large-leaf31_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet33 | P2P_clab-clos-large-leaf32_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet34 | P2P_clab-clos-large-leaf33_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet35 | P2P_clab-clos-large-leaf34_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet36 | P2P_clab-clos-large-leaf35_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet37 | P2P_clab-clos-large-leaf36_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet38 | P2P_clab-clos-large-leaf37_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet39 | P2P_clab-clos-large-leaf38_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet40 | P2P_clab-clos-large-leaf39_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet41 | P2P_clab-clos-large-leaf40_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet42 | P2P_clab-clos-large-leaf41_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet43 | P2P_clab-clos-large-leaf42_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet44 | P2P_clab-clos-large-leaf43_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet45 | P2P_clab-clos-large-leaf44_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet46 | P2P_clab-clos-large-leaf45_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet47 | P2P_clab-clos-large-leaf46_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet48 | P2P_clab-clos-large-leaf47_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet49 | P2P_clab-clos-large-leaf48_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet50 | P2P_clab-clos-large-leaf49_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet51 | P2P_clab-clos-large-leaf50_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet52 | P2P_clab-clos-large-borderleaf1_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |
| Ethernet53 | P2P_clab-clos-large-borderleaf2_Ethernet4 | - | - | default | 1550 | False | - | - | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet2
   description P2P_clab-clos-large-leaf1_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet3
   description P2P_clab-clos-large-leaf2_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet4
   description P2P_clab-clos-large-leaf3_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet5
   description P2P_clab-clos-large-leaf4_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet6
   description P2P_clab-clos-large-leaf5_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet7
   description P2P_clab-clos-large-leaf6_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet8
   description P2P_clab-clos-large-leaf7_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet9
   description P2P_clab-clos-large-leaf8_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet10
   description P2P_clab-clos-large-leaf9_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet11
   description P2P_clab-clos-large-leaf10_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet12
   description P2P_clab-clos-large-leaf11_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet13
   description P2P_clab-clos-large-leaf12_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet14
   description P2P_clab-clos-large-leaf13_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet15
   description P2P_clab-clos-large-leaf14_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet16
   description P2P_clab-clos-large-leaf15_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet17
   description P2P_clab-clos-large-leaf16_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet18
   description P2P_clab-clos-large-leaf17_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet19
   description P2P_clab-clos-large-leaf18_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet20
   description P2P_clab-clos-large-leaf19_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet21
   description P2P_clab-clos-large-leaf20_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet22
   description P2P_clab-clos-large-leaf21_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet23
   description P2P_clab-clos-large-leaf22_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet24
   description P2P_clab-clos-large-leaf23_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet25
   description P2P_clab-clos-large-leaf24_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet26
   description P2P_clab-clos-large-leaf25_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet27
   description P2P_clab-clos-large-leaf26_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet28
   description P2P_clab-clos-large-leaf27_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet29
   description P2P_clab-clos-large-leaf28_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet30
   description P2P_clab-clos-large-leaf29_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet31
   description P2P_clab-clos-large-leaf30_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet32
   description P2P_clab-clos-large-leaf31_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet33
   description P2P_clab-clos-large-leaf32_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet34
   description P2P_clab-clos-large-leaf33_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet35
   description P2P_clab-clos-large-leaf34_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet36
   description P2P_clab-clos-large-leaf35_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet37
   description P2P_clab-clos-large-leaf36_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet38
   description P2P_clab-clos-large-leaf37_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet39
   description P2P_clab-clos-large-leaf38_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet40
   description P2P_clab-clos-large-leaf39_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet41
   description P2P_clab-clos-large-leaf40_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet42
   description P2P_clab-clos-large-leaf41_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet43
   description P2P_clab-clos-large-leaf42_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet44
   description P2P_clab-clos-large-leaf43_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet45
   description P2P_clab-clos-large-leaf44_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet46
   description P2P_clab-clos-large-leaf45_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet47
   description P2P_clab-clos-large-leaf46_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet48
   description P2P_clab-clos-large-leaf47_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet49
   description P2P_clab-clos-large-leaf48_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet50
   description P2P_clab-clos-large-leaf49_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet51
   description P2P_clab-clos-large-leaf50_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet52
   description P2P_clab-clos-large-borderleaf1_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
!
interface Ethernet53
   description P2P_clab-clos-large-borderleaf2_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
   pim ipv4 sparse-mode
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 192.168.101.102/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | ROUTER_ID | default | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description ROUTER_ID
   no shutdown
   ip address 192.168.101.102/32
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
| default | True (ipv6 interfaces) |
| MGMT | False |

#### IP Routing Device Configuration

```eos
!
ip routing ipv6 interfaces
no ip routing vrf MGMT
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | false |

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
| 65001 | 192.168.101.102 |

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

##### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

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

#### BGP Neighbor Interfaces

| Neighbor Interface | VRF | Peer Group | Remote AS | Peer Filter |
| ------------------ | --- | ---------- | --------- | ----------- |
| Ethernet2 | default | IPv4-UNDERLAY-PEERS | 65100 | - |
| Ethernet3 | default | IPv4-UNDERLAY-PEERS | 65100 | - |
| Ethernet4 | default | IPv4-UNDERLAY-PEERS | 65102 | - |
| Ethernet5 | default | IPv4-UNDERLAY-PEERS | 65102 | - |
| Ethernet6 | default | IPv4-UNDERLAY-PEERS | 65104 | - |
| Ethernet7 | default | IPv4-UNDERLAY-PEERS | 65104 | - |
| Ethernet8 | default | IPv4-UNDERLAY-PEERS | 65106 | - |
| Ethernet9 | default | IPv4-UNDERLAY-PEERS | 65106 | - |
| Ethernet10 | default | IPv4-UNDERLAY-PEERS | 65108 | - |
| Ethernet11 | default | IPv4-UNDERLAY-PEERS | 65108 | - |
| Ethernet12 | default | IPv4-UNDERLAY-PEERS | 65110 | - |
| Ethernet13 | default | IPv4-UNDERLAY-PEERS | 65110 | - |
| Ethernet14 | default | IPv4-UNDERLAY-PEERS | 65112 | - |
| Ethernet15 | default | IPv4-UNDERLAY-PEERS | 65112 | - |
| Ethernet16 | default | IPv4-UNDERLAY-PEERS | 65114 | - |
| Ethernet17 | default | IPv4-UNDERLAY-PEERS | 65114 | - |
| Ethernet18 | default | IPv4-UNDERLAY-PEERS | 65116 | - |
| Ethernet19 | default | IPv4-UNDERLAY-PEERS | 65116 | - |
| Ethernet20 | default | IPv4-UNDERLAY-PEERS | 65118 | - |
| Ethernet21 | default | IPv4-UNDERLAY-PEERS | 65118 | - |
| Ethernet22 | default | IPv4-UNDERLAY-PEERS | 65120 | - |
| Ethernet23 | default | IPv4-UNDERLAY-PEERS | 65120 | - |
| Ethernet24 | default | IPv4-UNDERLAY-PEERS | 65122 | - |
| Ethernet25 | default | IPv4-UNDERLAY-PEERS | 65122 | - |
| Ethernet26 | default | IPv4-UNDERLAY-PEERS | 65124 | - |
| Ethernet27 | default | IPv4-UNDERLAY-PEERS | 65124 | - |
| Ethernet28 | default | IPv4-UNDERLAY-PEERS | 65126 | - |
| Ethernet29 | default | IPv4-UNDERLAY-PEERS | 65126 | - |
| Ethernet30 | default | IPv4-UNDERLAY-PEERS | 65128 | - |
| Ethernet31 | default | IPv4-UNDERLAY-PEERS | 65128 | - |
| Ethernet32 | default | IPv4-UNDERLAY-PEERS | 65130 | - |
| Ethernet33 | default | IPv4-UNDERLAY-PEERS | 65130 | - |
| Ethernet34 | default | IPv4-UNDERLAY-PEERS | 65132 | - |
| Ethernet35 | default | IPv4-UNDERLAY-PEERS | 65132 | - |
| Ethernet36 | default | IPv4-UNDERLAY-PEERS | 65134 | - |
| Ethernet37 | default | IPv4-UNDERLAY-PEERS | 65134 | - |
| Ethernet38 | default | IPv4-UNDERLAY-PEERS | 65136 | - |
| Ethernet39 | default | IPv4-UNDERLAY-PEERS | 65136 | - |
| Ethernet40 | default | IPv4-UNDERLAY-PEERS | 65138 | - |
| Ethernet41 | default | IPv4-UNDERLAY-PEERS | 65138 | - |
| Ethernet42 | default | IPv4-UNDERLAY-PEERS | 65140 | - |
| Ethernet43 | default | IPv4-UNDERLAY-PEERS | 65140 | - |
| Ethernet44 | default | IPv4-UNDERLAY-PEERS | 65142 | - |
| Ethernet45 | default | IPv4-UNDERLAY-PEERS | 65142 | - |
| Ethernet46 | default | IPv4-UNDERLAY-PEERS | 65144 | - |
| Ethernet47 | default | IPv4-UNDERLAY-PEERS | 65144 | - |
| Ethernet48 | default | IPv4-UNDERLAY-PEERS | 65146 | - |
| Ethernet49 | default | IPv4-UNDERLAY-PEERS | 65146 | - |
| Ethernet50 | default | IPv4-UNDERLAY-PEERS | 65148 | - |
| Ethernet51 | default | IPv4-UNDERLAY-PEERS | 65148 | - |
| Ethernet52 | default | IPv4-UNDERLAY-PEERS | 65190 | - |
| Ethernet53 | default | IPv4-UNDERLAY-PEERS | 65191 | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Encapsulation | Next-hop-self Source Interface |
| ---------- | -------- | ------------ | ------------- | ------------- | ------------------------------ |
| EVPN-OVERLAY-PEERS | True |  - | - | default | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65001
   router-id 192.168.101.102
   no bgp default ipv4-unicast
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS next-hop-unchanged
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 192.168.101.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.1 remote-as 65100
   neighbor 192.168.101.1 description clab-clos-large-leaf1_Loopback0
   neighbor 192.168.101.2 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.2 remote-as 65100
   neighbor 192.168.101.2 description clab-clos-large-leaf2_Loopback0
   neighbor 192.168.101.3 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.3 remote-as 65102
   neighbor 192.168.101.3 description clab-clos-large-leaf3_Loopback0
   neighbor 192.168.101.4 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.4 remote-as 65102
   neighbor 192.168.101.4 description clab-clos-large-leaf4_Loopback0
   neighbor 192.168.101.5 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.5 remote-as 65104
   neighbor 192.168.101.5 description clab-clos-large-leaf5_Loopback0
   neighbor 192.168.101.6 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.6 remote-as 65104
   neighbor 192.168.101.6 description clab-clos-large-leaf6_Loopback0
   neighbor 192.168.101.7 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.7 remote-as 65106
   neighbor 192.168.101.7 description clab-clos-large-leaf7_Loopback0
   neighbor 192.168.101.8 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.8 remote-as 65106
   neighbor 192.168.101.8 description clab-clos-large-leaf8_Loopback0
   neighbor 192.168.101.9 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.9 remote-as 65108
   neighbor 192.168.101.9 description clab-clos-large-leaf9_Loopback0
   neighbor 192.168.101.10 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.10 remote-as 65108
   neighbor 192.168.101.10 description clab-clos-large-leaf10_Loopback0
   neighbor 192.168.101.11 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.11 remote-as 65110
   neighbor 192.168.101.11 description clab-clos-large-leaf11_Loopback0
   neighbor 192.168.101.12 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.12 remote-as 65110
   neighbor 192.168.101.12 description clab-clos-large-leaf12_Loopback0
   neighbor 192.168.101.13 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.13 remote-as 65112
   neighbor 192.168.101.13 description clab-clos-large-leaf13_Loopback0
   neighbor 192.168.101.14 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.14 remote-as 65112
   neighbor 192.168.101.14 description clab-clos-large-leaf14_Loopback0
   neighbor 192.168.101.15 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.15 remote-as 65114
   neighbor 192.168.101.15 description clab-clos-large-leaf15_Loopback0
   neighbor 192.168.101.16 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.16 remote-as 65114
   neighbor 192.168.101.16 description clab-clos-large-leaf16_Loopback0
   neighbor 192.168.101.17 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.17 remote-as 65116
   neighbor 192.168.101.17 description clab-clos-large-leaf17_Loopback0
   neighbor 192.168.101.18 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.18 remote-as 65116
   neighbor 192.168.101.18 description clab-clos-large-leaf18_Loopback0
   neighbor 192.168.101.19 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.19 remote-as 65118
   neighbor 192.168.101.19 description clab-clos-large-leaf19_Loopback0
   neighbor 192.168.101.20 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.20 remote-as 65118
   neighbor 192.168.101.20 description clab-clos-large-leaf20_Loopback0
   neighbor 192.168.101.21 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.21 remote-as 65120
   neighbor 192.168.101.21 description clab-clos-large-leaf21_Loopback0
   neighbor 192.168.101.22 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.22 remote-as 65120
   neighbor 192.168.101.22 description clab-clos-large-leaf22_Loopback0
   neighbor 192.168.101.23 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.23 remote-as 65122
   neighbor 192.168.101.23 description clab-clos-large-leaf23_Loopback0
   neighbor 192.168.101.24 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.24 remote-as 65122
   neighbor 192.168.101.24 description clab-clos-large-leaf24_Loopback0
   neighbor 192.168.101.25 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.25 remote-as 65124
   neighbor 192.168.101.25 description clab-clos-large-leaf25_Loopback0
   neighbor 192.168.101.26 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.26 remote-as 65124
   neighbor 192.168.101.26 description clab-clos-large-leaf26_Loopback0
   neighbor 192.168.101.27 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.27 remote-as 65126
   neighbor 192.168.101.27 description clab-clos-large-leaf27_Loopback0
   neighbor 192.168.101.28 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.28 remote-as 65126
   neighbor 192.168.101.28 description clab-clos-large-leaf28_Loopback0
   neighbor 192.168.101.29 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.29 remote-as 65128
   neighbor 192.168.101.29 description clab-clos-large-leaf29_Loopback0
   neighbor 192.168.101.30 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.30 remote-as 65128
   neighbor 192.168.101.30 description clab-clos-large-leaf30_Loopback0
   neighbor 192.168.101.31 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.31 remote-as 65130
   neighbor 192.168.101.31 description clab-clos-large-leaf31_Loopback0
   neighbor 192.168.101.32 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.32 remote-as 65130
   neighbor 192.168.101.32 description clab-clos-large-leaf32_Loopback0
   neighbor 192.168.101.33 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.33 remote-as 65132
   neighbor 192.168.101.33 description clab-clos-large-leaf33_Loopback0
   neighbor 192.168.101.34 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.34 remote-as 65132
   neighbor 192.168.101.34 description clab-clos-large-leaf34_Loopback0
   neighbor 192.168.101.35 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.35 remote-as 65134
   neighbor 192.168.101.35 description clab-clos-large-leaf35_Loopback0
   neighbor 192.168.101.36 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.36 remote-as 65134
   neighbor 192.168.101.36 description clab-clos-large-leaf36_Loopback0
   neighbor 192.168.101.37 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.37 remote-as 65136
   neighbor 192.168.101.37 description clab-clos-large-leaf37_Loopback0
   neighbor 192.168.101.38 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.38 remote-as 65136
   neighbor 192.168.101.38 description clab-clos-large-leaf38_Loopback0
   neighbor 192.168.101.39 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.39 remote-as 65138
   neighbor 192.168.101.39 description clab-clos-large-leaf39_Loopback0
   neighbor 192.168.101.40 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.40 remote-as 65138
   neighbor 192.168.101.40 description clab-clos-large-leaf40_Loopback0
   neighbor 192.168.101.41 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.41 remote-as 65140
   neighbor 192.168.101.41 description clab-clos-large-leaf41_Loopback0
   neighbor 192.168.101.42 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.42 remote-as 65140
   neighbor 192.168.101.42 description clab-clos-large-leaf42_Loopback0
   neighbor 192.168.101.43 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.43 remote-as 65142
   neighbor 192.168.101.43 description clab-clos-large-leaf43_Loopback0
   neighbor 192.168.101.44 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.44 remote-as 65142
   neighbor 192.168.101.44 description clab-clos-large-leaf44_Loopback0
   neighbor 192.168.101.45 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.45 remote-as 65144
   neighbor 192.168.101.45 description clab-clos-large-leaf45_Loopback0
   neighbor 192.168.101.46 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.46 remote-as 65144
   neighbor 192.168.101.46 description clab-clos-large-leaf46_Loopback0
   neighbor 192.168.101.47 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.47 remote-as 65146
   neighbor 192.168.101.47 description clab-clos-large-leaf47_Loopback0
   neighbor 192.168.101.48 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.48 remote-as 65146
   neighbor 192.168.101.48 description clab-clos-large-leaf48_Loopback0
   neighbor 192.168.101.49 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.49 remote-as 65148
   neighbor 192.168.101.49 description clab-clos-large-leaf49_Loopback0
   neighbor 192.168.101.50 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.50 remote-as 65148
   neighbor 192.168.101.50 description clab-clos-large-leaf50_Loopback0
   neighbor 192.168.101.91 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.91 remote-as 65190
   neighbor 192.168.101.91 description clab-clos-large-borderleaf1_Loopback0
   neighbor 192.168.101.92 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.92 remote-as 65191
   neighbor 192.168.101.92 description clab-clos-large-borderleaf2_Loopback0
   redistribute connected route-map RM-CONN-2-BGP
   neighbor interface Ethernet2 peer-group IPv4-UNDERLAY-PEERS remote-as 65100
   neighbor interface Ethernet3 peer-group IPv4-UNDERLAY-PEERS remote-as 65100
   neighbor interface Ethernet4 peer-group IPv4-UNDERLAY-PEERS remote-as 65102
   neighbor interface Ethernet5 peer-group IPv4-UNDERLAY-PEERS remote-as 65102
   neighbor interface Ethernet6 peer-group IPv4-UNDERLAY-PEERS remote-as 65104
   neighbor interface Ethernet7 peer-group IPv4-UNDERLAY-PEERS remote-as 65104
   neighbor interface Ethernet8 peer-group IPv4-UNDERLAY-PEERS remote-as 65106
   neighbor interface Ethernet9 peer-group IPv4-UNDERLAY-PEERS remote-as 65106
   neighbor interface Ethernet10 peer-group IPv4-UNDERLAY-PEERS remote-as 65108
   neighbor interface Ethernet11 peer-group IPv4-UNDERLAY-PEERS remote-as 65108
   neighbor interface Ethernet12 peer-group IPv4-UNDERLAY-PEERS remote-as 65110
   neighbor interface Ethernet13 peer-group IPv4-UNDERLAY-PEERS remote-as 65110
   neighbor interface Ethernet14 peer-group IPv4-UNDERLAY-PEERS remote-as 65112
   neighbor interface Ethernet15 peer-group IPv4-UNDERLAY-PEERS remote-as 65112
   neighbor interface Ethernet16 peer-group IPv4-UNDERLAY-PEERS remote-as 65114
   neighbor interface Ethernet17 peer-group IPv4-UNDERLAY-PEERS remote-as 65114
   neighbor interface Ethernet18 peer-group IPv4-UNDERLAY-PEERS remote-as 65116
   neighbor interface Ethernet19 peer-group IPv4-UNDERLAY-PEERS remote-as 65116
   neighbor interface Ethernet20 peer-group IPv4-UNDERLAY-PEERS remote-as 65118
   neighbor interface Ethernet21 peer-group IPv4-UNDERLAY-PEERS remote-as 65118
   neighbor interface Ethernet22 peer-group IPv4-UNDERLAY-PEERS remote-as 65120
   neighbor interface Ethernet23 peer-group IPv4-UNDERLAY-PEERS remote-as 65120
   neighbor interface Ethernet24 peer-group IPv4-UNDERLAY-PEERS remote-as 65122
   neighbor interface Ethernet25 peer-group IPv4-UNDERLAY-PEERS remote-as 65122
   neighbor interface Ethernet26 peer-group IPv4-UNDERLAY-PEERS remote-as 65124
   neighbor interface Ethernet27 peer-group IPv4-UNDERLAY-PEERS remote-as 65124
   neighbor interface Ethernet28 peer-group IPv4-UNDERLAY-PEERS remote-as 65126
   neighbor interface Ethernet29 peer-group IPv4-UNDERLAY-PEERS remote-as 65126
   neighbor interface Ethernet30 peer-group IPv4-UNDERLAY-PEERS remote-as 65128
   neighbor interface Ethernet31 peer-group IPv4-UNDERLAY-PEERS remote-as 65128
   neighbor interface Ethernet32 peer-group IPv4-UNDERLAY-PEERS remote-as 65130
   neighbor interface Ethernet33 peer-group IPv4-UNDERLAY-PEERS remote-as 65130
   neighbor interface Ethernet34 peer-group IPv4-UNDERLAY-PEERS remote-as 65132
   neighbor interface Ethernet35 peer-group IPv4-UNDERLAY-PEERS remote-as 65132
   neighbor interface Ethernet36 peer-group IPv4-UNDERLAY-PEERS remote-as 65134
   neighbor interface Ethernet37 peer-group IPv4-UNDERLAY-PEERS remote-as 65134
   neighbor interface Ethernet38 peer-group IPv4-UNDERLAY-PEERS remote-as 65136
   neighbor interface Ethernet39 peer-group IPv4-UNDERLAY-PEERS remote-as 65136
   neighbor interface Ethernet40 peer-group IPv4-UNDERLAY-PEERS remote-as 65138
   neighbor interface Ethernet41 peer-group IPv4-UNDERLAY-PEERS remote-as 65138
   neighbor interface Ethernet42 peer-group IPv4-UNDERLAY-PEERS remote-as 65140
   neighbor interface Ethernet43 peer-group IPv4-UNDERLAY-PEERS remote-as 65140
   neighbor interface Ethernet44 peer-group IPv4-UNDERLAY-PEERS remote-as 65142
   neighbor interface Ethernet45 peer-group IPv4-UNDERLAY-PEERS remote-as 65142
   neighbor interface Ethernet46 peer-group IPv4-UNDERLAY-PEERS remote-as 65144
   neighbor interface Ethernet47 peer-group IPv4-UNDERLAY-PEERS remote-as 65144
   neighbor interface Ethernet48 peer-group IPv4-UNDERLAY-PEERS remote-as 65146
   neighbor interface Ethernet49 peer-group IPv4-UNDERLAY-PEERS remote-as 65146
   neighbor interface Ethernet50 peer-group IPv4-UNDERLAY-PEERS remote-as 65148
   neighbor interface Ethernet51 peer-group IPv4-UNDERLAY-PEERS remote-as 65148
   neighbor interface Ethernet52 peer-group IPv4-UNDERLAY-PEERS remote-as 65190
   neighbor interface Ethernet53 peer-group IPv4-UNDERLAY-PEERS remote-as 65191
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS next-hop address-family ipv6 originate
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
| Ethernet2 | - | IPv4 | - | - | - |
| Ethernet3 | - | IPv4 | - | - | - |
| Ethernet4 | - | IPv4 | - | - | - |
| Ethernet5 | - | IPv4 | - | - | - |
| Ethernet6 | - | IPv4 | - | - | - |
| Ethernet7 | - | IPv4 | - | - | - |
| Ethernet8 | - | IPv4 | - | - | - |
| Ethernet9 | - | IPv4 | - | - | - |
| Ethernet10 | - | IPv4 | - | - | - |
| Ethernet11 | - | IPv4 | - | - | - |
| Ethernet12 | - | IPv4 | - | - | - |
| Ethernet13 | - | IPv4 | - | - | - |
| Ethernet14 | - | IPv4 | - | - | - |
| Ethernet15 | - | IPv4 | - | - | - |
| Ethernet16 | - | IPv4 | - | - | - |
| Ethernet17 | - | IPv4 | - | - | - |
| Ethernet18 | - | IPv4 | - | - | - |
| Ethernet19 | - | IPv4 | - | - | - |
| Ethernet20 | - | IPv4 | - | - | - |
| Ethernet21 | - | IPv4 | - | - | - |
| Ethernet22 | - | IPv4 | - | - | - |
| Ethernet23 | - | IPv4 | - | - | - |
| Ethernet24 | - | IPv4 | - | - | - |
| Ethernet25 | - | IPv4 | - | - | - |
| Ethernet26 | - | IPv4 | - | - | - |
| Ethernet27 | - | IPv4 | - | - | - |
| Ethernet28 | - | IPv4 | - | - | - |
| Ethernet29 | - | IPv4 | - | - | - |
| Ethernet30 | - | IPv4 | - | - | - |
| Ethernet31 | - | IPv4 | - | - | - |
| Ethernet32 | - | IPv4 | - | - | - |
| Ethernet33 | - | IPv4 | - | - | - |
| Ethernet34 | - | IPv4 | - | - | - |
| Ethernet35 | - | IPv4 | - | - | - |
| Ethernet36 | - | IPv4 | - | - | - |
| Ethernet37 | - | IPv4 | - | - | - |
| Ethernet38 | - | IPv4 | - | - | - |
| Ethernet39 | - | IPv4 | - | - | - |
| Ethernet40 | - | IPv4 | - | - | - |
| Ethernet41 | - | IPv4 | - | - | - |
| Ethernet42 | - | IPv4 | - | - | - |
| Ethernet43 | - | IPv4 | - | - | - |
| Ethernet44 | - | IPv4 | - | - | - |
| Ethernet45 | - | IPv4 | - | - | - |
| Ethernet46 | - | IPv4 | - | - | - |
| Ethernet47 | - | IPv4 | - | - | - |
| Ethernet48 | - | IPv4 | - | - | - |
| Ethernet49 | - | IPv4 | - | - | - |
| Ethernet50 | - | IPv4 | - | - | - |
| Ethernet51 | - | IPv4 | - | - | - |
| Ethernet52 | - | IPv4 | - | - | - |
| Ethernet53 | - | IPv4 | - | - | - |

## Filters

### Prefix-lists

#### Prefix-lists Summary

##### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.101.0/24 eq 32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.101.0/24 eq 32
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

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
```
