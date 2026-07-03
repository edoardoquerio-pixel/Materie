# [19] Virtualizzazione

## 📋 Panoramica

Materia sulla virtualizzazione di sistemi: memoria, networking, VM e infrastruttura virtuale. Include laboratori pratici con OpenStack e microservizi containerizzati con Docker + Terraform.

**Tecnologie**: VMware/Hyper-V (concetti), OpenStack, Docker, Terraform (OpenTofu), Python, Node.js

---

## 📚 Indice degli argomenti

### 1. Fondamenti di Virtualizzazione

- **Hypervisor**: Tipo 1 (bare-metal: VMware ESXi, Hyper-V, KVM) vs Tipo 2 (hosted: VirtualBox)
- **Virtualizzazione della memoria**: MMU virtuale, shadow page table, hardware-assisted (Intel EPT/AMD NPT)
- **Virtualizzazione di networking**: vSwitch, VLAN, NIC teaming, SR-IOV
- **Overhead**: confronto prestazioni native vs virtualizzate

### 2. VM e OpenStack

- **OpenStack**: cloud OS open-source
  - **Nova**: compute
  - **Neutron**: networking
  - **Cinder**: block storage
  - **Glance**: immagini
  - **Keystone**: identity
  - **Horizon**: dashboard
- **Flavors**: template di risorse (CPU, RAM, disk)
- **Tenant/Project**: isolamento multi-tenant

### 3. Docker e Microservizi

- **Esempi pratici** nella cartella `ITS-Docker/`:
  - `LISTA/`: container Python (Flask) per CRUD
  - `API/`: Docker Compose multi-container con Python + dipendenze
- **Microservizi** (Terraform + Docker):
  - `users/`: microservizio utenti (Node.js + JSON)
  - `post/`: microservizio post (Node.js + JSON)
  - `threads/`: microservizio thread (Node.js + JSON)
- **Terraform per Docker**:

```hcl
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.9.0"
    }
  }
}

resource "docker_container" "app" {
  name  = "microservizio-app"
  image = docker_image.app.image_id
  ports {
    internal = 3000
    external = 3000
  }
}
```

### 4. WSA-Lab (Windows Server App + Docker + Terraform)

- Progetto completo: applicazione Python containerizzata
- Infrastruttura come codice con Terraform
- `main.tf` + `outputs.tf` per provisioning automatizzato

---

## ⚡ Punti Chiave

1. **Hypervisor Tipo 1** per produzione (minore overhead, maggiore sicurezza)
2. **OpenStack** è complesso ma è lo standard open-source per cloud privato
3. **Docker per sviluppo, K8s per produzione**: Compose per locale, orchestrazione per cluster
4. **Terraform**: stato dichiarativo desiderato, piano prima di applicare
5. **Microservizi**: ogni servizio ha il suo DB, comunicano via API

---

## 📎 Risorse Collegate

- **02_Esercizi/** — Laboratori virtualizzazione
- **03_Progetti/** — Microservizi Docker, Terraform, OpenStack lab
- **WSA-lab/** — Progetto completo Windows Server App (Docker + Terraform + Python)
- **ITS-Docker/** — Esempi Docker Compose e container singoli
