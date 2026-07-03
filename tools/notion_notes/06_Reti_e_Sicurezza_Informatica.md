# [06] Reti e Sicurezza Informatica

## 📋 Panoramica

Materia che copre i fondamenti della cybersecurity e delle reti di calcolatori. Divisa in due macro-aree: **Sicurezza Informatica** (prof. Marco Farina) — crittografia, hashing, password, certificati digitali — e **Reti** (prof. Andrea Blanchietti) — indirizzamento IPv4/IPv6, subnetting, VLAN, routing inter-VLAN.

**Tecnologie/strumenti**: OpenSSL, Python (cifrario di Cesare, entropia), Cisco Packet Tracer, JohnTheRipper, Wireshark (menzionato)

---

## 📚 Indice degli argomenti

### 1. Introduzione alla Cybersecurity

- **Triade CIA**:
  - **Confidentiality** — dati accessibili solo a soggetti autorizzati
  - **Integrity** — dati non alterati durante il ciclo di vita
  - **Availability** — dati e sistemi disponibili quando richiesti
- **Valutazione del rischio**: `r = p × d` (probabilità × danno)
- **Livelli di sicurezza**: personale, aziendale, nazionale
- **Cyberwarfare**: Stuxnet, spionaggio, sabotaggio infrastrutture, propaganda

### 2. Gestione delle Password

- **Entropia delle password**: `H = log₂(|Σ|^L) = L × log₂(|Σ|)`
- **Spazio delle chiavi** per vari alfabeti:

| Alfabeto | Cardinalità | Entropia/simbolo |
|----------|-------------|------------------|
| PIN (0-9) | 10 | 3.33 bit |
| Esadecimale | 16 | 4 bit |
| Minuscole (a-z) | 26 | 4.7 bit |
| Alfanumerico | 36 | 5.17 bit |
| Case-sensitive + numeri | 62 | 5.95 bit |
| ASCII stampabile | 94 | 6.55 bit |
| Byte (0-255) | 256 | 8 bit |

- **Password da 12 caratteri ASCII** → ~78.7 bit di entropia
- **Tecniche di intrusione**: default password, social engineering, attacchi a dizionario (`/usr/share/wordlists`), forza bruta (JohnTheRipper, AirCrack)
- **Regola pratica**: `passphrase > password complessa` (es. "correct horse battery staple" = 127 bit)

### 3. Introduzione alla Crittografia

- **Steganografia vs Crittografia**: nascondere l'esistenza del messaggio vs renderlo incomprensibile
- **Cifrario di Cesare**: sostituzione con shift `k=2`:
  ```
  meet me after the toga party → OGGV OG CHVGT VJG VQIC RCTVA
  ```
- **Spazio delle chiavi**: solo 26 possibilità → attacco brute-force banale
- **Cifratura monoalfabetica**: permutazione casuale dell'alfabeto (26! ≈ 2^88 chiavi) → vulnerabile ad analisi delle frequenze
- **Cifrario di Vigénère**: cifratura polialfabetica con chiave parola
- **Crittografia moderna (1900+)**: Bletchley Park, Shannon, DES, AES, crittografia a chiave pubblica

### 4. Crittografia DES e AES

**DES** (Data Encryption Standard):
- Chiave: 56 bit effettivi (64 bit con 8 di parità)
- Struttura: 16 round di Feistel network
- Spazio chiavi: 2^56 ≈ 7.2×10^16
- **Deep Crack (1999)**: 1536 CPU, 92 miliardi chiavi/s, 22 ore, $200K → OGGI INSICURO

**AES** (Advanced Encryption Standard):
- Vincitore del concorso NIST (2000), successore del DES
- Chiavi: 128, 192, 256 bit
- Struttura: SP-network (non Feistel), 10/12/14 round
- **AES-256**: standard attuale per dati classificati (NSA Top Secret)

```
# Cifratura AES-256-CBC con OpenSSL
openssl rand -hex 16 > iv.txt
openssl rand 32 > key.bin
KEY_HEX=$(xxd -p key.bin | tr -d '\n')
IV_HEX=$(cat iv.txt | tr -d '\n')
openssl enc -aes-256-cbc -K "$KEY_HEX" -iv "$IV_HEX" -in messaggio.txt -out messaggio.enc
```

### 5. Diffie-Hellman-Merkle Key Exchange

- **Problema**: come condividere una chiave segreta su un canale pubblico?
- **Metodo dei lucchetti** (analogia): Alice chiude con lucchetto, Bob aggiunge il suo, Alice rimuove il suo, Bob rimuove il suo
- **Puzzle di Merkle**: Bob genera 2^n puzzle con ID+chiave casuale; Alice ne sceglie uno, lo risolve e invia ID; l'attaccante deve risolvere in media 2^(n-1) puzzle
- **Diffie-Hellman** (1976, New Directions in Cryptography):
  - Basato sulla difficoltà del **logaritmo discreto**
  - `g^a mod p` scambiato pubblicamente → chiave condivisa `g^(ab) mod p`
  - Mitigazione: >2048 bit, forward secrecy

### 6. Crittografia a Chiave Pubblica e RSA

- **Cifrari simmetrici**: stessa chiave per cifrare/decifrare (permutazioni e sostituzioni)
- **Asimmetria**: chiave pubblica (cifra) + chiave privata (decifra) — basata su funzioni matematiche unidirezionali
- **RSA** (Rivest-Shamir-Adleman, 1977):
  - Basato sulla fattorizzazione del prodotto di due numeri primi grandi
  - `n = p × q`, chiave pubblica `(n, e)`, chiave privata `(n, d)`
  - `c = m^e mod n`, `m = c^d mod n`
- **Flusso**: Bob usa chiave pubblica di Alice per cifrare → solo Alice decifra con sua chiave privata

### 7. Certificati Digitali e Hashing

- **Funzioni di hash**: `H = h(M)` — mappano input arbitrario in output lunghezza fissa
- Proprietà: **non invertibile**, resistenza a collisioni, effetto valanga
- **Firma digitale**: hash del messaggio cifrato con chiave privata del mittente → verifica con chiave pubblica
- **Certificato digitale**: lega identità + chiave pubblica + firma della CA
- **PKI** (Public Key Infrastructure): gerarchia di Certificate Authority
- **Man-in-the-middle**: risolto con certificazione tramite CA
- Esempi di hash: SHA-256, SHA-3, MD5 (rotto, non usare)

### 8. Entropia e Compressione

- **Entropia di Shannon**: `H(X) = -∑ P(x) × log₂(P(x))`
- **Primo teorema di Shannon**: impossibile comprimere sotto l'entropia senza perdita
- File con solo 'a' → entropia ≈ 0 → compressione 5000:1
- File casuale → entropia ≈ 6.6 bit/simbolo → compressione trascurabile

```python
def calculate_entropy(data):
    counter = Counter(data)
    length = len(data)
    entropy = 0
    for count in counter.values():
        p = count / length
        entropy -= p * math.log2(p)
    return entropy
```

### 9. Indirizzamento IPv4

- Struttura: 32 bit in 4 ottetti (notazione decimale puntata)
- **Subnet mask**: separa parte rete da parte host
- **Prefix length**: `/24` = 255.255.255.0 = 24 bit di rete
- **Indirizzi riservati**: network address (host bit = 0), broadcast (host bit = 1)
- **Host disponibili**: `2^n - 2` (tolti network e broadcast)
- **Classi legacy**: A (0-127), B (128-191), C (192-223), D (multicast), E (sperimentale)
- **Indirizzi privati** (RFC 1918):
  - Classe A: `10.0.0.0/8`
  - Classe B: `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
  - Classe C: `192.168.0.0/16`

**Calcolo subnet** (esempio):
```
192.168.10.5/24 → rete: 192.168.10.0/24, broadcast: 192.168.10.255, host: 192.168.10.1-254
172.21.152.12/16 → rete: 172.21.0.0/16, broadcast: 172.21.255.255, host: 172.21.0.1-172.21.255.254
```

### 10. VLAN (Virtual LAN)

- **Segmentazione logica** dello switch in domini di broadcast separati
- **Vantaggi**: domini broadcast più piccoli, maggiore sicurezza, efficienza IT, riduzione costi, prestazioni
- **Tipi di VLAN**:
  - **VLAN dati**: traffico utente (email, web)
  - **VLAN nativa**: frame senza tag su trunk 802.1Q
  - **VLAN di gestione**: SSH/Telnet, SVI dello switch Layer 2
  - **VLAN voce**: QoS, banda garantita, latenza <150ms
  - **VLAN predefinita (VLAN 1)**: non eliminabile, sconsigliata per gestione
- **Tag 802.1Q**: 4 byte con TPID (0x8100), priorità, CFI, VID (12 bit → 4096 VLAN)
- **VLAN multi-switch**: collegamento trunk porta-point tra switch

### 11. InterVLAN Routing

- Le VLAN sono isolate al Layer 2 → serve un **dispositivo Layer 3** per comunicare tra VLAN
- **Metodo legacy**: router con interfaccia fisica per ogni VLAN (costoso, non scalabile)
- **Router-on-a-stick**: una sola interfaccia fisica con sottointerfacce 802.1Q:
  ```
  interface GigabitEthernet0/0.10
   encapsulation dot1Q 10
   ip address 192.168.10.1 255.255.255.0
  !
  interface GigabitEthernet0/0.20
   encapsulation dot1Q 20
   ip address 192.168.20.1 255.255.255.0
  ```
- **Switch Layer 3 (SVIs)**: interfacce virtuali, routing interno allo switch

### 12. Sistemi Numerici

- **Binario (base 2)**: simboli 0,1 — potenze di 2
- **Esadecimale (base 16)**: simboli 0-9,A-F — potenze di 16
- **Conversione decimale → binario**: divisioni successive per 2
- **Conversione binario → esadecimale**: raggruppa 4 bit per cifra
  ```
  89 decimale = 1011001 binario = 0x59
  7B41 esadecimale = 31553 decimale
  ```

---

## ⚡ Punti Chiave

1. **CIA Triad** è il fondamento: nessuna sicurezza senza tutti e tre gli aspetti
2. **Entropia** misura la forza di una password — mai sotto 60 bit per account importanti
3. **Crittografia simmetrica** (AES) per volumi grandi di dati; **asimmetrica** (RSA, DH) per scambio chiavi e firme
4. **Non si scrivono algoritmi crittografici propri** — usare librerie standard (OpenSSL, Cryptography.io)
5. **Hash + chiave privata = firma digitale**; l'hash non è crittografia (non è invertibile)
6. **Niente crittografia homemade** — usa AES-256-GCM, SHA-256, x.509 con CA riconosciute
7. **Subnetting**: ricordare la formula `2^n - 2` per host utilizzabili
8. **VLAN**: isolano il traffico al Layer 2; per routing serve Layer 3 (router-on-a-stick o SVI)

---

## 📎 Risorse Collegate

- **02_Esercizi/** — Script Python (`Trova_numeri_primi.py` — numeri primi per RSA), esercizi subnetting
- **Materiale extra**: demo entropia (MD+PY), AES con OpenSSL, cifrario di Cesare, Enigma Keys
- **Lab Cisco Packet Tracer**: VLAN, InterVLAN routing (.pkt)
- **Link**: playlist cybersecurity, condivisione schermo Meet
- **Letture**: Estratto "L'arte dell'inganno" (Kevin Mitnick), paper originale RSA (Diffie-Hellman 1976)
