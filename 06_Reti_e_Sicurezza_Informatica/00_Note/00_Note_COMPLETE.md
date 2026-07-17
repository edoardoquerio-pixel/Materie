# Reti e Sicurezza Informatica — Note Complete

## 1. Fondamenti di Rete

**Modello OSI (7 livelli):** Physical → Data Link → Network → Transport → Session → Presentation → Application

**TCP/IP (4 livelli):** Network Interface → Internet → Transport → Application

**Protocolli principali:**
| Livello | Protocolli |
|---------|-----------|
| Application | HTTP/HTTPS, DNS, DHCP, FTP, SSH, SMTP, POP3, IMAP |
| Transport | TCP (connessione), UDP (datagram) |
| Internet | IP, ICMP, ARP, IGMP |

**Indirizzamento:**
- IPv4: 32 bit, classi A-E, CIDR, subnet mask
- IPv6: 128 bit, notazione esadecimale, autoconfigurazione
- NAT/PAT: traduzione indirizzi, port forwarding

**Topologie:** stella, bus, anello, maglia, albero

## 2. VLAN e Switching

- **VLAN (802.1Q)**: segmentazione logica della LAN, tag VLAN
- **Trunk**: multipli VLAN su stesso link
- **STP/RSTP**: prevenzione loop, ridondanza
- **LACP/Port Channel**: aggregazione link, aumento bandwidth

## 3. Routing

- **Statico**: tabelle fisse, no overhead
- **Dinamico**: 
  - OSPF: link-state, area gerarchica, convergenza veloce
  - EIGRP: Cisco proprietary, distance vector + link-state
  - BGP: path-vector, routing tra AS, politiche

## 4. Sicurezza Informatica

**Concetti:**
- CIA Triad: Confidentiality, Integrity, Availability
- AAA: Authentication, Authorization, Accounting
- Defense in depth: layer multipli di sicurezza
- Zero Trust: "never trust, always verify"

**Minacce:**
- Malware (virus, worm, trojan, ransomware, spyware)
- Phishing/Social Engineering
- DDoS/DoS
- Man-in-the-Middle
- SQL Injection, XSS, CSRF
- Supply chain attack

**Crittografia:**
| Tipo | Esempi | Utilizzo |
|------|--------|----------|
| Simmetrica | AES, DES, ChaCha20 | Dati a riposo, VPN |
| Asimmetrica | RSA, ECC, Ed25519 | TLS, Firma digitale |
| Hash | SHA-256, SHA-3, BLAKE2 | Integrità, password |

**Firewall:**
- Stateless (filtro basato su header IP/porta)
- Stateful (tracciamento connessioni)
- NGFW (ispezione applicativa, IPS, antivirus)
- WAF (protezione applicazioni web)

## 5. Protocolli di Sicurezza

- **TLS 1.3**: handshake ridotto (1-RTT), forward secrecy, AEAD
- **IPsec**: tunnel/transport mode, IKEv2, ESP/AH
- **SSH**: remote access sicuro, tunneling, SFTP
- **HTTPS**: HTTP over TLS (port 443)
- **DNSSEC**: firma DNS, catena di fiducia
- **DKIM/SPF/DMARC**: autenticazione email

## 6. Laboratori

- **Enigma/Entropia**: crittografia storica e moderna (codici, cifrari)
- **Sniffing/Network analysis**: Wireshark, tcpdump
- **Nmap**: port scanning, OS detection, service discovery
- **Firewall testing**: iptables, pfSense, Windows Defender
- **Vulnerability scanning**: OpenVAS, Nessus

## 7. Cheatsheet Comandi

```bash
# Network
ip addr / ifconfig          # Interfacce
ip route / route -n         # Tabella routing
ping -c 5 <host>            # Test connettività
traceroute / tracert <host> # Percorso pacchetti
netstat -tulpn              # Porte in ascolto
ss -tulpn                   # Modern netstat
dig <host> ANY              # DNS query
nslookup <host>             # DNS lookup
tcpdump -i eth0             # Cattura pacchetti

# Firewall (Linux)
iptables -L -n -v           # Listing regole
ufw status numbered         # Uncomplicated Firewall

# SSH
ssh user@host -p 22         # Connessione
ssh-keygen -t ed25519       # Generazione chiavi

# Scansione (nmap)
nmap -sV -sC <target>       # Service + script scan
nmap -p- <target>           # Tutte le porte
```
