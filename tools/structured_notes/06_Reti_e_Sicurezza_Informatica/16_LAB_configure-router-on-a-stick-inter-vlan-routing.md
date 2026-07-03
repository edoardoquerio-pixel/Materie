# LAB configure-router-on-a-stick-inter-vlan-routing

## Panoramica
Lab - Configure Router-on-a-Stick Inter-VLAN Routing

## Argomenti trattati
Generale

---
## Appunti

Lab - Configure Router-on-a-Stick Inter-VLAN Routing
Addressing Table
Default Gateway
Interface Assigned
S1: F0/2-4, F0/7-24, G0/1-2
S2: F0/2-17, F0/19-24, G0/1-2
© 2013 - 2019 Cisco and/or its affiliates. All rights reserved. Cisco Public
www.netacad.com
Lab - Configure Router-on-a-Stick Inter-VLAN Routing
Part 1: Build the Network and Configure Basic Device Settings
Part 2: Create VLANs and Assign Switch Ports
Part 3: Configure an 802.1Q Trunk between the Switches
Part 4: Configure Inter-VLAN Routing on the Router
Part 5: Verify Inter-VLAN Routing is working
Background / Scenario
Modern switches use virtual local-area networks (VLANs) to provide segmentation services traditionally
provided by routers in LAN configurations. VLANs address scalability, security, and network management. In
general, VLANs make it easier to design a network to support the goals of an organization. Communication
between VLANs requires a device operating at Layer 3 of the OSI model. Routers in VLAN topologies provide
additional security and traffic flow management.
VLAN trunks are used to span VLANs across multiple devices. Trunks allow the traffic from multiple VLANS to
travel over a single link, while keeping the VLAN identification and segmentation intact. A particular kind of
inter-VLAN routing, called “Router-On-A-Stick”, uses a trunk from the router to the switch to enable all VLANs
to pass to the router.
In this lab, you will create VLANs on both switches in the topology, assign VLANs to switch access ports,
verify that VLANs are working as expected, create VLAN trunks between the two switches and between S1
and R1, and configure Inter-VLAN routing on R1 to allow hosts in different VLANs to communicate, regardless
of which subnet the host resides.
Note: The routers used with CCNA hands-on labs are Cisco 4221 with Cisco IOS XE Release 16.9.4
(universalk9 image). The switches used in the labs are Cisco Catalyst 2960s with Cisco IOS Release 15.2(2)
(lanbasek9 image). Other routers, switches, and Cisco IOS versions can be used. Depending on the model
and Cisco IOS version, the commands available and the output produced might vary from what is shown in
the labs. Refer to the Router Interface Summary Table at the end of the lab for the correct interface identifiers.
Note: Ensure that the routers and switches have been erased and have no startup configurations. If you are
unsure, contact your instructor.
Required Resources
• 1 Router (Cisco 4221 with Cisco IOS XE Release 16.9.4 universal image or comparable)
• 2 Switches (Cisco 2960 with Cisco IOS Release 15.2(2) lanbasek9 image or comparable)
• 2 PCs (Windows with a terminal emulation program, such as Tera Term)
• Console cables to configure the Cisco IOS devices via the console ports
• Ethernet cables as shown in the topology
Part 1: Build the Network and Configure Basic Device Settings
In Part 1, you will set up the network topology and configure basic settings on the PC hosts and switches.
Step 1: Cable the network as shown in the topology.
Attach the devices as shown in the topology diagram, and cable as necessary.
© 2013 - 2019 Cisco and/or its affiliates. All rights reserved. Cisco Public
www.netacad.com
Lab - Configure Router-on-a-Stick Inter-VLAN Routing
Step 2: Configure basic settings for the router.
Open configuration window
a. Console into the router and enable privileged EXEC mode.
b. Enter configuration mode.
c. Assign a device name to the router.
d. Disable DNS lookup to prevent the router from attempting to translate incorrectly entered commands as
though they were host names.
e. Assign class as the privileged EXEC encrypted password.
f. Assign cisco as the console password and enable login.
g. Assign cisco as the VTY password and enable login.
h. Encrypt the plaintext passwords.
i. Create a banner that warns anyone accessing the device that unauthorized access is prohibited.
j. Save the running configuration to the startup configuration file.
k. Set the clock on the router.
Note: Use the question mark (?) to help with the correct sequence of parameters needed to execute this
Close configuration window
Step 3: Configure basic settings for each switch.
Open configuration window
a. Console into the switch and enable privileged EXEC mode.
b. Enter configuration mode.
c. Assign a device name to the switch.
d. Disable DNS lookup to prevent the router from attempting to translate incorrectly entered commands as
though they were host names.
e. Assign class as the privileged EXEC encrypted password.
f. Assign cisco as the console password and enable login.
g. Assign cisco as the vty password and enable login.
h. Encrypt the plaintext passwords.
i. Create a banner that warns anyone accessing the device that unauthorized access is prohibited.
j. Set the clock on the switch.
Note: Use the question mark (?) to help with the correct sequence of parameters needed to ex ecute this
k. Copy the running configuration to the startup configuration.
Close configuration window

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_LAB_configure-router-on-a-stick-inter-vlan-routing.md*
