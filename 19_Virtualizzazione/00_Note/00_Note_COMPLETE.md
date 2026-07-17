# Virtualizzazione — Note Complete

## 1. Concetti Base

- **Hypervisor**: software che crea e gestisce VM
  - **Type 1 (bare-metal)**: Hyper-V, ESXi, KVM, Xen — diretto su hardware
  - **Type 2 (hosted)**: VirtualBox, VMware Workstation — sopra OS host
- **Host**: macchina fisica che esegue hypervisor
- **Guest**: VM che esegue su hypervisor
- **Virtualizzazione vs Container**: hypervisor virtualizza hardware, container virtualizza OS

## 2. Docker

**Vedi 17_Container_Docker_Kubernetes per dettaglio completo.**
- Docker Engine: daemon + CLI + REST API
- Container runtime: containerd, runc
- Networking: bridge, host, overlay, macvlan
- Volumes: dati persistenti fuori dal container

## 3. Hyper-V (Windows)

- Ruolo Windows: `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V`
- **Generation 1**: BIOS, legacy device support
- **Generation 2**: UEFI, Secure Boot, hot add/remove
- **VHDX**: disco virtuale, max 64TB, resize online
- **Checkpoint**: snapshot VM (production/standard)
- **Hyper-V Manager**: GUI amministrazione
- **PowerShell**: `New-VM`, `Start-VM`, `Get-VM`, `Set-VM`
- **Nested virtualization**: VM dentro VM (WSL2, Docker Desktop)

## 4. VirtualBox (Cross-platform)

- Open source, Oracle
- **Guest Additions**: driver display, mouse integrato, clipboard, shared folder
- **Reti**: NAT (default), Bridged, Host-only, Internal, NAT Network
- **Snapshot**: stato VM salvabile/ripristinabile
- **Export/Import**: OVA/OVF format
- **VBoxManage**: CLI

## 5. VMware vSphere

- **ESXi**: Type 1 hypervisor
- **vCenter**: management centralizzato (cluster, HA, DRS, vMotion)
- **vSphere Client**: GUI management
- **vSAN**: storage software-defined
- **NSX**: virtual networking, micro-segmentation

## 6. Terraform (HCL)

```hcl
# Provisioning VM su vSphere
resource "vsphere_virtual_machine" "vm" {
  name             = "webserver"
  resource_pool_id = data.vsphere_compute_cluster.cluster.resource_pool_id
  datastore_id     = data.vsphere_datastore.datastore.id

  num_cpus = 2
  memory   = 4096
  guest_id = "ubuntu64Guest"

  network_interface {
    network_id = data.vsphere_network.network.id
  }

  disk {
    label = "disk0"
    size  = 50
  }
}
```

**Provider comuni:** vSphere, AWS, Azure, GCP, Docker, Kubernetes, Proxmox

## 7. Proxmox VE

- **Type**: Debian-based, KVM (VM) + LXC (container)
- **Storage**: ZFS, LVM, Ceph, NFS, iSCSI
- **Cluster**: multi-node, HA, migration live
- **Backup**: vzdump, Proxmox Backup Server (deduplication)
- **Web GUI**: management via browser, API REST

## 8. Concetti Avanzati

- **CPU Pinning**: assegnazione core dedicati a VM
- **NUMA**: ottimizzazione memoria per VM large
- **Memory Ballooning**: overcommit RAM host→guest
- **Storage Pass-through**: disco fisico intero a VM
- **SR-IOV**: NIC virtuale con performance near-native
- **Live Migration**: VM spostata tra host senza downtime
- **FT (Fault Tolerance)**: VM duplicata su host diverso (VMware)
