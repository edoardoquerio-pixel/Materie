# risoluzione problema rete Debian

**File:** `risoluzione problema rete Debian.txt`
**Tipo:** `.txt`
**Dimensione:** 0.4 KB
**Ultima modifica:** 02/07/2026 09:22

---

# risoluzione problema rete Debian 3
# tira su l'interfaccia a mano con l'IP tipico di VirtualBox NAT:

sudo ip link set enp0s3 up
sudo ip addr add 10.0.2.15/24 dev enp0s3
sudo ip route add default via 10.0.2.2
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf

# verifica:

ping -c 2 8.8.8.8

# risoluzione permanente (basta reinstallare il client dhcp):
sudo apt install isc-dhcp-client -y

sudo systemctl restart networking

