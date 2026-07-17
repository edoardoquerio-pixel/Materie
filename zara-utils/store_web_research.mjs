import { DatabaseSync } from 'node:sqlite';

const DB = 'C:/Users/edoardo.querio/.zara/memory.db';
const db = new DatabaseSync(DB);

function store(key, value, type = 'fact', source = 'api_external_unverified', scope = 'web-research') {
  const now = new Date().toISOString();
  try {
    db.prepare(`
      INSERT INTO semantic (key, value, confidence, source, type, scope, created, updated, reinforced, decay_score)
      VALUES (?, ?, 0.8, ?, ?, ?, ?, ?, 1, 1.0)
      ON CONFLICT(key) DO UPDATE SET
        value = excluded.value, updated = excluded.updated, reinforced = reinforced + 1, decay_score = 1.0
    `).run(key, value, source, type, scope, now, now);
    return true;
  } catch (e) {
    console.error(`  ✗ ${e.message}`);
    return false;
  }
}

let total = 0;

// === AZURE ===
console.log('=== Azure ===');
const azureData = `
## Azure Pricing Models
- **Pay-as-you-go**: Pay only for what you use, no commitment
- **Reserved Instances**: 1-3 year commit, 30-72% discount
- **Spot VMs**: Up to 90% discount, interruptible workloads
- **Savings Plans**: Flexible hourly commit

## Azure Compute
- **VMs**: EC2-equivalent, per-second billing, Hybrid Benefit for Windows/Linux
- **App Service**: Managed PaaS, Free/Shared/Basic/Premium/Isolated tiers
- **Functions**: Serverless, Consumption/Premium/Dedicated plans

## Azure Storage
- **Blob**: Hot/Cool/Cold/Archive tiers, lifecycle policies
- **Disk**: Ultra/Premium SSD/Standard SSD/Standard HDD
- **Queue/Table**: NoSQL messaging and key-value

## Azure Networking
- **VNet**: Free creation, costs for VPN Gateway/VNet Peering
- **Load Balancer**: Standard tier with health probes
- **VPN Gateway**: Basic to VpnGw5 SKUs, zone-redundant

## Azure Databases
- **SQL Database**: Provisioned/Serverless, General Purpose/Business Critical/Hyperscale
- **Cosmos DB**: Serverless/Autoscale/Provisioned RU/s, multiple APIs

## Azure Identity
- **Entra ID**: Free/P1/P2 tiers, MFA, Conditional Access, PIM

## Azure Best Practices
- Use Reserved Instances for predictable workloads
- Use Spot VMs for batch/CI-CD/dev-test
- Enable auto-tuning, geo-replication, and lifecycle policies
- Right-size VMs based on actual utilization
- Use Azure Advisor for cost optimization
`.trim();
store('web:azure:overview', azureData, 'fact', 'api_external_unverified', 'web-research'); total++;

// === DOCKER ===
console.log('=== Docker ===');
const dockerData = `
## Docker Core Concepts
- **Image**: Immutable, layered package with code+dependencies
- **Container**: Isolated process, self-contained, portable
- **Volume**: Persistent data, managed by Docker, survives container removal
- **Registry**: Centralized image storage (Docker Hub, ECR, ACR, GCR)

## Essential Docker Commands
- **Lifecycle**: docker run/ps/stop/start/rm
- **Build**: docker build -t name:tag .
- **Volumes**: docker volume create/ls/inspect/rm/prune
- **Networks**: docker network create/ls/connect/disconnect

## Dockerfile Best Practices
- Use specific base image tags (not :latest)
- Chain RUN commands to reduce layers
- Order FROM least to most frequently changing (cache optimization)
- Use COPY over ADD
- Use multi-stage builds for smaller images
- Set non-root USER for security
- Use .dockerignore
- Use HEALTHCHECK

## Multi-Stage Builds
- Multiple FROM statements, each a stage
- COPY --from=build /bin/hello /bin/hello
- Build specific stage: docker build --target build
- Benefits: smaller images, separation of concerns, cleaner security

## Docker Compose
- **Structure**: services > build/image, volumes, networks, depends_on
- **Commands**: docker compose up/down/ps/logs/exec
- **Profiles**: Conditional service inclusion
- **Health checks**: test, interval, timeout, retries, start_period
- **Dev vs Prod**: Volume mounts for hot reload (dev), multi-replica (prod)

## Key Patterns
- **Dev**: Bind mounts, debug ports, verbose logging
- **Prod**: Rebuild images, health checks, resource limits, restart policies
`.trim();
store('web:docker:overview', dockerData, 'fact', 'api_external_unverified', 'web-research'); total++;

// === KUBERNETES ===
console.log('=== Kubernetes ===');
const k8sData = `
## Pods
- Smallest deployable unit, 1+ containers sharing network+storage
- Lifecycle: Pending → Running → Succeeded/Failed
- Probes: liveness, readiness, startup

## Deployments
- Declarative updates for Pods+ReplicaSets
- RollingUpdate (default) or Recreate strategies
- Rollout status/history/undo

## Services
- ClusterIP (internal), NodePort (static port), LoadBalancer (external LB)
- Service discovery via DNS: <service>.<ns>.svc.cluster.local

## Ingress
- HTTP/HTTPS routing with host+path rules
- Requires Ingress Controller (e.g., nginx-ingress)
- Path types: Exact, Prefix, ImplementationSpecific

## ConfigMaps & Secrets
- ConfigMaps: non-confidential key-value config
- Secrets: Opaque, TLS, dockerconfigjson types (base64)
- Mount as env vars or volumes
- Set immutable: true for performance+protection

## Namespaces
- default, kube-system, kube-public, kube-node-lease
- Not all resources are namespaced (Nodes, PVs)

## PersistentVolumes & PVCs
- PV: cluster-wide storage, PVC: storage request
- Access modes: ReadWriteOnce, ReadOnlyMany, ReadWriteMany
- Lifecycle: Provision → Bind → Use → Reclaim

## StatefulSets
- Stable network identity (pod-0, pod-1) + persistent storage
- Ordered deployment/scaling/deletion
- Requires Headless Service
- volumeClaimTemplates for per-pod PVCs

## HPA (Horizontal Pod Autoscaler)
- Scales based on CPU/memory/custom metrics
- Formula: ceil(currentReplicas * currentMetric/desiredMetric)
- Stabilization window, tolerance, behavior config

## Essential kubectl Commands
- **CRUD**: kubectl create/apply/delete/get/describe/edit
- **Logs**: kubectl logs -f --tail=100 --previous
- **Exec**: kubectl exec -it pod -- /bin/sh
- **Port-forward**: kubectl port-forward pod/service local:remote
- **Rollout**: kubectl rollout status/history/undo deployment
- **Config**: kubectl config current-context/use-context/set-context
- **Diagnostics**: kubectl top pods/nodes, kubectl explain
`.trim();
store('web:kubernetes:overview', k8sData, 'fact', 'api_external_unverified', 'web-research'); total++;

// === PYTHON PATTERNS ===
console.log('=== Python ===');
const pythonData = `
## Python Virtual Environments
- Create: python -m venv tutorial-env
- Activate: Scripts\\activate (Win) or source bin/activate (Unix)
- Deactivate: deactivate

## Pip Package Management
- Install: python -m pip install package
- Freeze: python -m pip freeze > requirements.txt
- Install from file: python -m pip install -r requirements.txt

## Type Hints
- def func(param: type) -> return_type:
- Optional, List, Dict, Union from typing
- type aliases (3.12+): type Vector = list[float]
- NewType for distinct types
- Not enforced at runtime, used by type checkers/IDEs

## List Comprehensions
- [expr for item in iterable if condition]
- Set: {x for x in iterable if condition}
- Dict: {key: value for item in iterable}
- Nested comprehensions for matrices

## Generators
- Functions with yield instead of return
- Generator expressions: sum(i*i for i in range(10))
- Memory efficient, lazy evaluation
- Auto-StopIteration when done

## Context Managers (with)
- Files: with open("file") as f:
- Custom: __enter__ / __exit__ or @contextmanager
- Automatic cleanup even on exceptions

## Decorators
- Functions that modify other functions
- @decorator syntax
- Use functools.wraps to preserve metadata
- Can accept arguments with nested wrappers

## Dataclasses
- @dataclass auto-generates __init__, __repr__, __eq__
- frozen=True for immutability, order=True for comparisons
- slots=True for memory optimization (3.10+)
- field(default_factory=list) for mutable defaults

## pathlib
- Path concatenation: Path("/dir") / "file"
- .read_text()/.write_text() for file I/O
- .glob()/.rglob() for pattern matching
- .mkdir(parents=True, exist_ok=True)

## argparse
- CLI argument parsing with auto-help
- Positional + optional arguments
- Type conversion, choices, defaults

## Common Idioms
- Tuple unpacking: x, y = (1, 2)
- Walrus operator (3.8+): :=
- Short-circuit or: a or b or default
- Multiple returns: return min, max, avg
`.trim();
store('web:python:patterns', pythonData, 'fact', 'api_external_unverified', 'web-research'); total++;

// === C#/.NET PATTERNS ===
console.log('=== C# .NET ===');
const csharpData = `
## Async/Await
- Task-based Asynchronous Pattern (TAP)
- async Task<T> with await
- await Task.WhenAll(t1, t2) for parallel
- await Task.WhenAny(tasks) for first completion
- Exception handling with try/catch inside async

## LINQ
- Query syntax: from x in collection where x > 5 select x
- Method syntax: collection.Where(x => x > 5).Select(x => x)
- Deferred execution: query is not executed until iterated
- Common: Where, Select, OrderBy, GroupBy, Sum, Average, Count, Any, All

## ASP.NET Core Minimal APIs
- app.MapGet/MapPost/MapPut/MapDelete
- Results.Ok/Created/NotFound for typed responses
- Record types for DTOs
- app.MapGroup for route grouping
- Built-in DI: AddSingleton/AddScoped/AddTransient

## Dependency Injection
- AddTransient: new instance per injection
- AddScoped: new instance per request
- AddSingleton: single instance for app lifetime
`.trim();
store('web:csharp:patterns', csharpData, 'fact', 'api_external_unverified', 'web-research'); total++;

// === CLOUD COMPARISON ===
console.log('=== Cloud Comparison ===');
const cloudComparison = `
## Market Positions
- AWS (2006): Market leader ~33%, broadest services
- Azure (2010): Second, fastest growing, best enterprise/Microsoft integration
- GCP (2008): Third, leading AI/ML and data analytics

## Compute Equivalents
- AWS EC2 → Azure VMs → GCP Compute Engine
- AWS Lambda → Azure Functions → GCP Cloud Functions
- AWS ECS/EKS → Azure AKS → GCP GKE
- AWS Fargate → Azure Container Apps → GCP Cloud Run

## Storage
- AWS S3 → Azure Blob → GCP Cloud Storage
- AWS EBS → Azure Disk → GCP Persistent Disk
- AWS RDS → Azure SQL/Cosmos DB → GCP Cloud SQL/Spanner
- AWS DynamoDB → Azure Cosmos DB → GCP Firestore/Bigtable
- AWS Redshift → Azure Synapse → GCP BigQuery

## AI/ML
- AWS SageMaker/Bedrock → Azure ML/Azure OpenAI → GCP Vertex AI
- GCP leads with TensorFlow and custom TPUs
- Azure leads with OpenAI integration (GPT models)
- AWS broadest pre-built AI services

## Global Infrastructure
- AWS: 36 regions, 114+ AZs, 600+ edge locations
- Azure: 60+ regions, 126+ AZs
- GCP: 40+ regions, 121+ AZs, 187+ edge

## Pricing Differences
- AWS: pay-as-you-go, Reserved (1-3yr), Spot (90% off)
- Azure: same + Hybrid Benefit for Windows/SQL
- GCP: same + Sustained Use auto-discounts (up to 30%)

## When to Choose Each
- AWS: broadest catalog, any workload
- Azure: Microsoft ecosystem, hybrid cloud, enterprise
- GCP: AI/ML, data analytics, startups
- Multi-cloud common: leverage each platform's strengths
`.trim();
store('web:cloud:comparison', cloudComparison, 'fact', 'api_external_unverified', 'web-research'); total++;

// === WORKFLOW: Docker compose patterns ===
const dockerComposePatterns = `
## Docker Compose Dev Pattern
- Bind mount volumes for hot reload
- Debug ports exposed
- Verbose logging
- Unrestricted resources
- Example: npm run dev

## Docker Compose Prod Pattern
- Rebuild images (no bind mounts)
- Health checks required
- Resource limits (CPU/memory)
- restart: unless-stopped
- External volumes for persistence
- Multiple replicas

## Common Compose Patterns
- depends_on with condition: service_healthy
- Profiles for conditional service inclusion
- env_file for environment variables
- .dockerignore to exclude unnecessary files from build context
`.trim();
store('web:docker:compose-patterns', dockerComposePatterns, 'workflow', 'api_external_unverified', 'web-research'); total++;

// === WORKFLOW: Kubernetes deployment patterns ===
const k8sDeployPatterns = `
## Kubernetes Deployment Best Practices
- Always set resource requests and limits
- Use liveness + readiness probes
- Use ConfigMaps/Secrets for configuration
- Use RollingUpdate strategy for zero-downtime
- Set pod anti-affinity for HA
- Use Namespaces for environment isolation
- Use RBAC for access control
- Enable encryption at rest for Secrets in etcd

## Common kubectl Workflow
1. kubectl apply -f manifests/
2. kubectl rollout status deployment/myapp
3. kubectl get pods -w
4. kubectl logs -f deployment/myapp
5. kubectl port-forward service/myapp 8080:80
`.trim();
store('web:kubernetes:deploy-patterns', k8sDeployPatterns, 'workflow', 'api_external_unverified', 'web-research'); total++;

// === ARCHITECTURE: Azure services map ===
const azureArch = `
## Azure Architecture Patterns
- **IaaS**: VMs + VNet + Load Balancer + Storage
- **PaaS**: App Service + SQL Database + Azure Functions
- **Serverless**: Functions + Cosmos DB + Blob Storage (event-driven)
- **Microservices**: AKS + Service Bus + API Management
- **Hybrid**: VPN Gateway + Azure Arc + SQL Managed Instance
- **DR**: Geo-replication + Traffic Manager + Azure Site Recovery
`.trim();
store('web:azure:architecture', azureArch, 'architecture', 'api_external_unverified', 'web-research'); total++;

console.log(`\n=== Done! Stored ${total} web research items ===`);
db.close();
