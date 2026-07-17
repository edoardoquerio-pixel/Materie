# Cloud Computing Fundamentals — Speech (20 min)

## 1. Introduction

Good morning everyone. Today we are talking about Cloud Computing — one of the most transformative technologies of the last twenty years. It's not just a technical topic: it's a paradigm shift in how we think about, build, and use computing resources. We'll start with the basics and gradually work our way up to more advanced concepts like Serverless and Cloud-Native applications.

---

## 2. What is Cloud Computing and how does it work?

Let's start with a definition. Cloud Computing is a model that enables on-demand network access to a shared pool of configurable computing resources — servers, storage, databases, networks, software, analytics — that can be provisioned and released with minimal management effort or provider interaction.

In plain English: instead of physically owning your computers and servers, you rent them from someone else, use them over the Internet, and pay only for what you consume.

How does it actually work? There are three main actors: the **cloud provider** (AWS, Azure, Google Cloud), the **customer** (a company or developer), and the **end user**. The provider owns and manages massive data centers spread across the globe. The customer runs applications and stores data on them without worrying about the underlying hardware. The end user interacts with these applications without knowing — and without needing to know — where the data physically resides.

The magic lies in three essential characteristics. First: **on-demand self-service**. You can provision resources in a few clicks or a single API call, without talking to a salesperson. Second: **broad network access**. Resources are accessible from any device connected to the Internet. Third: **resource pooling**. The provider serves many customers from the same physical infrastructure, achieving economies of scale that translate to lower costs for everyone.

Two more characteristics define the cloud experience: **rapid elasticity** — if your application sees a traffic spike, the cloud automatically adds more resources; when traffic drops, it releases them — and **measured service**, meaning you pay per use like electricity or gas. No fixed bills, no wasted capacity.

---

## 3. The evolution from traditional data centres to the cloud

To understand why the cloud is so revolutionary, let's look at where we came from.

Until the early 2000s, if a company wanted a web application, it bought physical servers. It needed to find space in a data centre — often a purpose-built facility with cooling, UPS units, physical security. It had to configure networking, storage, backups. It had to forecast future load and purchase hardware months in advance. If the peak was higher than expected? The application crashed. If it was lower? Servers sat idle, money wasted.

Then came **virtualization**. A single physical server could host multiple virtual machines, each with its own operating system. This improved resource utilization, but the real leap was **public cloud**. In 2006 Amazon launched AWS with services like S3 for storage and EC2 for compute. The idea that infrastructure is no longer something you own, but a service you consume, was born.

Today we are on the third or fourth generation: infrastructure is programmable via API, managed with code (Infrastructure as Code), and orchestrated by Kubernetes. The data centre is no longer a place — it's an abstraction.

---

## 4. Service models: IaaS, PaaS and SaaS

The cloud is divided into three main service models, each representing a different level of abstraction and responsibility.

**IaaS — Infrastructure as a Service.** This is the model closest to traditional hardware. The provider gives you virtual machines, storage, and networking, and you install the operating system, middleware, and applications on top. You have maximum control, but also maximum management responsibility. Examples: AWS EC2, Google Compute Engine, Azure Virtual Machines. Who uses it? System administrators, companies migrating existing workloads without modifying them.

**PaaS — Platform as a Service.** Here the provider also manages the operating system, runtimes, and middleware. You bring only your code and data. You deploy an application without worrying about security patches, system updates, or infrastructure scaling. Examples: Google App Engine, Heroku, Azure App Services. Who uses it? Developers who want to focus on code, not infrastructure.

**SaaS — Software as a Service.** The finished product, ready to use. The provider manages everything: hardware, platform, application, data. You open a browser and use the software. You install nothing, you manage nothing. Examples: Gmail, Microsoft 365, Salesforce, Dropbox. Who uses it? Everyone — every end user.

There's a useful metaphor: IaaS is like buying land and construction materials. PaaS is like renting a house that's already built but empty. SaaS is like renting a house that's already furnished with utilities connected. Each model balances control and convenience differently — choose what fits your needs.

---

## 5. Public, Private, Hybrid and Multi-Cloud

Not all cloud is the same. There are different deployment models.

**Public Cloud.** The infrastructure is owned by the provider, located in its data centres, and shared among multiple customers. Advantages: no upfront capital expenditure, maximum elasticity, pay only for use. Disadvantages: reduced control, potential regulatory compliance issues for sensitive data.

**Private Cloud.** The infrastructure is dedicated to a single organization. It can be on-premise or managed by a third-party provider. Advantages: full control, security, compliance. Disadvantages: high initial costs, internal maintenance, limited elasticity based on available physical resources.

**Hybrid Cloud.** Combines public and private cloud, with orchestration between the two. Data and applications can move between environments. The classic example: a banking application runs on private cloud for sensitive data but scales to public cloud during traffic spikes without exposing critical data. Advantages: flexibility, security, cost optimization. Disadvantages: higher operational complexity.

**Multi-Cloud.** You use multiple public cloud providers simultaneously — AWS for compute, Azure for Active Directory, Google Cloud for machine learning. Advantages: avoid vendor lock-in, choose the best service for each need. Disadvantages: significant management complexity, need to maintain skills across multiple constantly-evolving platforms.

The trend today? According to industry reports, over 80% of enterprises already adopt a multi-cloud or hybrid approach. Plain public or private cloud is no longer enough — you need a strategy.

---

## 6. Advantages and disadvantages

Let's look at the pros and cons in a balanced way.

**Advantages.** First is economic: no upfront CapEx. Instead of millions in hardware, you pay monthly OpEx. Second: elasticity. If your startup grows 1000% in a week, the cloud doesn't stop you. If traffic drops, you don't pay for idle resources. Third: time-to-market. A development team can launch a production infrastructure in minutes instead of weeks. Fourth: security. The major providers invest billions in physical and logical security — amounts no average company can match. Fifth: disaster recovery. Data is replicated across multiple geographic regions. A fire in one data centre? Services continue from another location.

**Disadvantages.** First: unpredictable costs. If you don't monitor usage, the bill at the end of the month can surprise you. Second: connectivity dependency. No Internet, no work. Third: vendor lock-in. Once you build your architecture on AWS's proprietary services, migrating elsewhere becomes complex and expensive. Fourth: reduced control. If AWS has an outage, your service is down — and there's nothing you can do about it. Fifth: compliance. Certain sectors — healthcare, finance, public administration — have strict regulatory requirements about where and how data can reside. Not everything can go to the cloud.

The key? Evaluate case by case. There is no universal answer: every workload has its ideal environment.

---

## 7. Edge Computing vs Cloud Computing

So far we've talked about data travelling to centralized data centres. But there's a problem: latency.

Think of a self-driving car. If it needs to stop for an obstacle, it cannot wait for data to go to a regional cloud and come back. It needs milliseconds, not hundreds of milliseconds. Enter **Edge Computing**: processing happens close to the data source — on the device itself, on a local gateway, or on an edge server at a network point of presence.

Cloud computing is centralized, powerful, ideal for heavy processing and historical data. Edge computing is distributed, fast, ideal for real-time applications like IoT, autonomous vehicles, augmented reality, and smart manufacturing.

They are not competing — they are complementary. The modern architecture is often a continuum: edge devices collect data and make quick decisions, intermediate nodes aggregate, the central cloud handles complex analytics and machine learning. The typical example: a smart thermostat adjusts temperature locally but sends usage data to the cloud to improve prediction algorithms.

The growth of IoT and 5G is accelerating edge computing. Gartner predicts that by 2028, 75% of enterprise-generated data will be processed outside centralized data centres.

---

## 8. Serverless Computing

Another step forward in abstraction: **Serverless Computing**. The name is misleading — servers are definitely there — but the developer doesn't see them, doesn't manage them, doesn't configure them. You just write functions, upload them to the cloud, and say "run this function when X happens."

Imagine you want to resize an image every time one is uploaded. With a traditional approach, you keep a server running waiting for requests. With serverless, you write a function of a few lines, connect it to an upload event, and the cloud runs the function only when needed. If zero requests come in, you pay nothing. If a million come in, the cloud scales automatically.

Major providers: AWS Lambda, Azure Functions, Google Cloud Functions.

Advantages: no server management, automatic scaling, pay only for execution time — down to the millisecond. Perfect for intermittent workloads, microservices, webhooks, mobile application backends.

Disadvantages: cold starts — if a function hasn't been called for a while, the next invocation takes hundreds of milliseconds extra. Execution time limits — Lambda functions time out after 15 minutes. Difficult local debugging. Testing complexity.

Serverless doesn't replace everything, but for certain categories of problems, it's hard to beat in terms of efficiency and cost.

---

## 9. Cloud-Native Applications

Last topic: **Cloud-Native applications**. Running on the cloud is not enough to be cloud-native. A traditional application simply migrated to a virtual machine doesn't leverage the cloud — it lives there, but doesn't use its potential.

A cloud-native application is designed from the ground up for the cloud. It rests on four pillars.

First: **microservices**. The application is broken into many small, independent services, each with its own responsibility. Not a single monolithic block, but dozens or hundreds of components communicating via APIs.

Second: **containers**. Each microservice runs in a container — lightweight, isolated, reproducible. Docker is the standard, Kubernetes the de facto orchestrator.

Third: **DevOps and Continuous Delivery**. Deployments are frequent, automated, repeatable. Infrastructure is code. Testing and security are integrated into the development pipeline.

Fourth: **resilience and observability**. The application assumes components will fail — and is designed accordingly with retries, circuit breakers, graceful degradation. And it must be observable: centralized logging, metrics, distributed tracing.

Examples of cloud-native architectures: Netflix, Spotify, Uber. They couldn't exist without the cloud — their scale and speed of innovation demand these technologies.

---

## 10. Conclusion

To close: cloud computing is not just a technology — it's a new way of thinking about IT. It's moving from ownership to access, from fixed capacity to elasticity, from hardware to software.

We've covered the foundations: what it is and how it works. The historical evolution from traditional data centres. The three service models — IaaS, PaaS, SaaS. The deployment models — public, private, hybrid, multi-cloud. Advantages and disadvantages. And then the frontiers: edge computing, serverless, cloud-native.

The final message is this: the cloud is not a destination, it's a journey. Companies don't "finish" migrating to the cloud — they continuously evolve how they use it. And understanding these fundamentals gives you the tools to be part of that evolution.

Thank you.
