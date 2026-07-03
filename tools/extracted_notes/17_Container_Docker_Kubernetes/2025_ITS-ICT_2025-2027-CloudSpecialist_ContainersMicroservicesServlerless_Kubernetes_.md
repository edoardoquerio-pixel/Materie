# ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless kubernetes intro

Fonte: `ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless kubernetes intro.pdf`

Software Developer
Unità Formativa (UF): Containers, Microservizi -
Serverless
Docente: Denis Maggiorotto
Titolo argomento: Introduzione a kubernetes

Kubernetes

L’orchestratore di container per eccellenza

Dal monolite ai micro servizi

154

Lo sviluppo diventa agile

155

Waterfall Vs Agile

156

Il movimento DevOps

157

I principi del DevOps (CALMS)

158

Gli strumenti del DevOps (solo una piccola parte)

159

Le applicazioni diventano multi container (microservices)

160

Troppi container?

161

Perché Kubernetes

162

Cos’è Kubernetes

Kubernetes is an open source
container orchestration engine for 
automating deployment, scaling, 
and management of containerized 
applications. 
The open source project is hosted 
by the Cloud Native Computing 
Foundation.

163

Kubernetes dal 2017 è il secondo progetto OO dopo Linux

164

LAB

https://github.com/sunnyvale-academy/ITS-ICT_Containers

Lab 

18 – Kubernetes

165

L’architettura di 
Kubernetes ed il Pod

L’architettura di Kubernetes

167

L’architettura di Kubernetes

168

L’architettura di Kubernetes

169

L’architettura di Kubernetes

170

Eseguire un’applicazione su Kubernetes

171

Kubernetes APIs

172

Kubernetes APIs

173

Kubernetes APIs

174

Kubernetes APIs

175

Minikube

176

Pods

177

Multi container Pods

E’ possibile inserire più di un 
Container all’interno del Pod.

Questa pratica è utile per 
avere uno o più Containers che 
supportano il Container 
principale (Sidecar pattern)

178

Pods replicas

Quando il carico utente 
aumenta, la pratica comune è 
quella di aumentare il fattore 
di replica dei Pod (le istanze) e 
non il numero di container in 
un singolo Pod

179

Running the first Pod

180

Running the first Pod

181

Pods con YAML

Ogni risorsa Kubernetes
può esser descritta in 
YAML, la cui struttura di 
base è formata dalle 
seguenti chiavi (tutte 
obbligatorie) 

182

Pods con YAML

apiVersion rappresenta la versione delle API che useremo per creare la nostra 
risorsa (in questo caso un Pod). E’ necessario specificare l’apiVersion corretta per 
ogni risorsa (vedi tabella).

183

Pods con YAML

kind rappresenta il tipo di risorsa da creare. In questo caso il Pod

184

Pods con YAML

metadata racchiude delle informazioni fondamentali per il Pod. Qui vediamo il 
nome (obbligatorio) ed una label (app). Parleremo delle label in seguito.

185

Pods con YAML

spec (specification) racchiude i containers che il Pod avrà al suo interno. La 
struttura di spec dipende dal tipo di risorsa (in questo caso Pod).

186

Pods con YAML

$ kubectl create –f pod-definition.yml

187

Altri Pods con YAML

Single container

Multi container

188

LAB

https://github.com/sunnyvale-academy/ITS-ICT_Containers

Lab 

19 – Pod

189

ReplicationController, 
ReplicaSet e Deployment

Pod lifecycle (Pod status)

191

ReplicationController (deprecato in favore di ReplicaSet)

192

ReplicationController

193

ReplicationController

194

ReplicationController

Per specificare il numero di repliche aggiungiamo:

195

ReplicationController

$ kubectl create –f rc-definition.yml

$ kubectl get replicationcontroller

$ kubectl get pods

196

LAB

https://github.com/sunnyvale-academy/ITS-ICT_Containers

Lab 

20 – ReplicationController

197

ReplicaSet

198

ReplicaSet

Con il Selector, 
ReplicaSet può anche 
gestire Pod che non ha 
creato

199

ReplicaSet

$ kubectl create –f replicaset-definition-definition.yml

$ kubectl get replicaset

$ kubectl get pods

200

Labels and Selectors

201

Labels and Selectors

tier

tier

202

Labels and Selectors

203

Labels and Selectors

204

Labels and Selectors

205

Scaling

$ kubectl replace –f 
replicaset-definition.yml

206

Scaling

$ kubectl scale –replicas=6 replicaset-definition.yml

$ kubectl scale –replicas=6 replicaset myapp-replicaset

207

LAB

https://github.com/sunnyvale-academy/ITS-ICT_Containers

Lab 

21 – ReplicaSet

208