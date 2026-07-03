# [17] Container Docker Kubernetes

## 📋 Panoramica

Materia su containerizzazione e orchestrazione. Copre Docker (immagini, container, Compose) e Kubernetes (pod, deployment, service, scaling). Repository come submodule Git separato.

**Tecnologie**: Docker, Docker Compose, Kubernetes (kubectl, YAML), Draw.io (diagrams)

---

## 📚 Indice degli argomenti

### 1. Docker — Fondamenti

- **Cos'è un container**: processo isolato, stesso kernel dell'host, leggero vs VM
- **Immagine vs Container**: immagine = template, container = istanza in esecuzione
- **Dockerfile**: ricetta per costruire un'immagine

### 2. Docker — Comandi Principali

```bash
docker build -t mia-app:latest .    # costruisci immagine
docker run -d -p 8080:80 mia-app    # avvia container
docker ps                           # container attivi
docker images                       # immagini locali
docker exec -it <id> /bin/sh        # shell nel container
docker logs <id>                    # log container
docker stop <id>                    # ferma container
docker compose up -d                # multi-container
```

### 3. Docker Compose

```yaml
version: '3'
services:
  web:
    build: ./app
    ports:
      - "8080:80"
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secret
    volumes:
      - pgdata:/var/lib/postgresql/data
volumes:
  pgdata:
```

### 4. Kubernetes — Architettura

- **Cluster**: Master node (control plane) + Worker nodes
- **Componenti master**: API Server, Scheduler, Controller Manager, etcd
- **Componenti worker**: Kubelet, kube-proxy, container runtime

### 5. Kubernetes — Oggetti Principali

- **Pod**: unità minima, 1+ container
- **Deployment**: gestione repliche, rolling update, rollback
- **Service**: astrazione di rete, bilanciamento carico (ClusterIP, NodePort, LoadBalancer)
- **ConfigMap / Secret**: configurazione e dati sensibili
- **Ingress**: routing HTTP/HTTPS esterno
- **PersistentVolume (PV/PVC)**: storage persistente

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
```

### 6. Kubernetes — Comandi

```bash
kubectl get pods                    # lista pod
kubectl get nodes                   # nodi cluster
kubectl apply -f deployment.yaml    # deploy
kubectl delete pod <nome>           # elimina pod
kubectl logs <pod>                  # log
kubectl scale deployment/nginx --replicas=5
kubectl expose deployment/nginx --port=80 --type=LoadBalancer
```

---

## ⚡ Punti Chiave

1. **Container ≠ VM**: condividono il kernel host, avvio in secondi, leggeri
2. **Immutabilità**: le immagini non si modificano, si ricostruiscono
3. **K8s desidera stato dichiarativo**: scrivi YAML, K8s lo realizza
4. **Health check**: liveness + readiness probe per resilienza
5. **Mai hardcodare credenziali**: sempre Secret + ConfigMap
6. **Submodule**: `17_Container_Docker_Kubernetes/` è su repo separato — `git submodule update --init --recursive`

---

## 📎 Risorse Collegate

- **labs/** — Laboratori Docker e Kubernetes
- **assignments/** — Assignment pratici
- **01_Materiale/** — Slide e risorse
- **appendices/** — Approfondimenti
