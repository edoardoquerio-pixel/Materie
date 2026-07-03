# 21_Internet_of_Things

## 📋 Panoramica

Internet of Things — connessione di dispositivi fisici alla rete per raccolta dati, monitoraggio e automazione. Include architetture IoT, protocolli di comunicazione, cloud IoT, edge computing e sicurezza.

> ⚠️ **Nessun materiale didattico presente** in `01_Materiale/`. Questa nota è un placeholder da integrare.

## 📚 Indice degli argomenti (attesi dal syllabus)

### 1. Architetture IoT
- Modello a 3/4/5 livelli (Device, Edge, Cloud)
- IoT Reference Architecture (ISO/IEC 30141)
- Gateway IoT e protocolli fieldbus

### 2. Protocolli di Comunicazione
- **MQTT**: Pub/sub, QoS, topic, broker (Mosquitto)
- **CoAP**: UDP-based, REST-like per constrained devices
- **HTTP/HTTPS**: REST API per device
- **LoRaWAN / NB-IoT**: LPWAN per lunga distanza e basso consumo

### 3. Piattaforme Cloud IoT
- **AWS IoT Core**: Device shadow, rules engine, greengrass
- **Azure IoT Hub**: Device twin, direct methods, IoT Edge
- **GCP IoT Core** (deprecato): Alternative (Pub/Sub + Cloud IoT)

### 4. Hardware e Sensori
- **Microcontrollori**: Arduino, ESP32, STM32
- **Single Board Computer**: Raspberry Pi
- **Sensori**: Temperatura, umidità, pressione, movimento, gas, GPS

### 5. Edge Computing
- Elaborazione locale vs cloud, latenza, bandwidth
- AWS Greengrass, Azure IoT Edge
- ML on edge (TensorFlow Lite)

### 6. Sicurezza IoT
- Crittografia end-to-end, secure boot, TPM
- Firmware update (OTA)
- Vulnerabilità comuni: default password, clear-text protocols

## ⚡ Punti Chiave

- **MQTT** è il protocollo IoT standard (leggero, pub/sub, QoS 0-2)
- L'**edge computing** riduce latenza e banda verso il cloud
- La **sicurezza** è la sfida più grande (milioni di device, spesso con risorse limitate)
- **Digital Twin**: replica virtuale del dispositivo fisico nel cloud

## 📎 Risorse Collegate

- **02_Esercizi/**: —
- **03_Progetti/**: —
- **Materie collegate**: `06_Reti_e_Sicurezza_Informatica`, `14_Cloud_Azure`, `13_Cloud_AWS`
