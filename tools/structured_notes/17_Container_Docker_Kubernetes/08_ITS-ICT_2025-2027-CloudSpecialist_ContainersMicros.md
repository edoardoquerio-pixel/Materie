# ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless networking

## Panoramica
Unità Formativa (UF): Containers Microservizi

## Argomenti trattati
Cloud, Reti, Docker, Data Analytics, Git

---
## Appunti

Cloud Specialist
Unità Formativa (UF): Containers Microservizi
Docente: Denis Maggiorotto
Titolo argomento: Container networking
Gestione della rete
all'interno dei container
$ docker run -d --net none busybox sleep 1000
3a82e2e4537ac9cde52fb69c3a471fd4809817a6165983f0bf5af08d67eeebe3
$ docker exec -it
3a82e2e4537ac9cde52fb69c3a471fd4809817a6165983f0bf5af08d67eeebe3
/ # ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
ping: sendto: Network is unreachable
lo Link encap:Local Loopback
inet addr:127.0.0.1 Mask:255.0.0.0
UP LOOPBACK RUNNING MTU:65536 Metric:1
$ docker network ls
NETWORK ID NAME DRIVER SCOPE
8dae0c4d0380 bridge bridge
22530231e5cd host
bd5e44929d16 none null
$ docker run -d --name container_1 busybox sleep 1000
34886a41f5212abd8cd3aa4062479028899e78f32b44103bade6b67d88b76f75
$ docker exec -it container_1 ifconfig
eth0 Link encap:Ethernet HWaddr 02:42:AC:11:00:02
inet addr:172.17.0.2 Bcast:172.17.255.255 Mask:255.255.0.0
UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1
RX packets:10 errors:0 dropped:0 overruns:0 frame:0
TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:0
RX bytes:796 (796.0 B) TX bytes:0 (0.0 B)
lo Link encap:Local Loopback
inet addr:127.0.0.1 Mask:255.0.0.0
UP LOOPBACK RUNNING MTU:65536 Metric:1
RX packets:0 errors:0 dropped:0 overruns:0 frame:0
TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:1000
RX bytes:0 (0.0 B) TX bytes:0 (0.0 B)
$ docker run -d --name container_2 busybox sleep 1000
c8c34dad781a7a5778852de2e40fe922f6b4113759b94928d81c4753f7631b9a
$ docker exec -it container_2 ifconfig
eth0 Link encap:Ethernet HWaddr 02:42:AC:11:00:04
inet addr:172.17.0.4 Bcast:172.17.255.255 Mask:255.255.0.0
UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1
RX packets:10 errors:0 dropped:0 overruns:0 frame:0
TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:0
RX bytes:796 (796.0 B) TX bytes:0 (0.0 B)
lo Link encap:Local Loopback
inet addr:127.0.0.1 Mask:255.0.0.0
UP LOOPBACK RUNNING MTU:65536 Metric:1
RX packets:0 errors:0 dropped:0 overruns:0 frame:0
TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:1000
RX bytes:0 (0.0 B) TX bytes:0 (0.0 B)
$ docker exec -it container_1 ping 172.17.0.4
PING 172.17.0.4 (172.17.0.4): 56 data bytes
64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.069 ms
64 bytes from 172.17.0.4: seq=1 ttl=64 time=0.076 ms
--- 172.17.0.4 ping statistics ---
$ docker exec -it container_1 ping 172.17.0.4
PING 172.17.0.4 (172.17.0.4): 56 data bytes
64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.069 ms
64 bytes from 172.17.0.4: seq=1 ttl=64 time=0.076 ms
--- 172.17.0.4 ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 0.069/0.072/0.076 ms
$ docker exec -it container_1 ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=117 time=33.251 ms
--- 8.8.8.8 ping statistics ---
1 packets transmitted, 1 packets received, 0% packet loss
round-trip min/avg/max = 33.251/33.251/33.251 ms
$ docker exec -it container_1 ping 172.17.0.4
PING 172.17.0.4 (172.17.0.4): 56 data bytes
$ docker exec -it container_1 ping 172.17.0.4
64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.069 ms
$ docker exec -it container_1 ping 172.17.0.4
PING 172.17.0.4 (172.17.0.4): 56 data bytes
$ docker exec -it container_1 ping 172.17.0.4

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 2025_ITS-ICT_2025-2027-CloudSpecialist_ContainersMicroservicesServlerless_networking.md*
