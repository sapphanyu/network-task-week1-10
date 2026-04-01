# Automation & Cloud-Native Architecture Course

> **A 10-week journey from binary protocols to production-grade AI systems.**
> Learn how to architect distributed systems that are secure, observable, evolvable, and trustworthy.

## 📋 Course Overview

This repository contains a comprehensive course covering modern software architecture, distributed systems, cloud-native patterns, and AI governance. Each week builds on previous concepts, progressing from foundational networking to production-grade multi-agent AI systems.

### Target Audience
- Software engineers transitioning to architecture roles
- Backend developers looking to understand distributed systems
- Anyone building AI-powered production systems
- Teams needing to implement governance and compliance

---

## 🗺️ Course Structure

### **Week 01: MIME-Based Socket File Transfer**
**Foundation: Binary Protocols & Network Communication**

Learn how data moves across networks with explicit boundaries and reliable transmission.

- TCP socket programming with JSON headers
- MIME type detection and file handling
- Reliable data transfer patterns
- Client/server architecture fundamentals

📁 [week01-mime-typing/](week01-mime-typing/)

---

### **Week 02: Stateless vs Stateful Architecture**
**Session Layer: Application State Management**

Understand when systems should "remember" and when they shouldn't.

- Stateless vs stateful trade-offs
- Session management and lifecycle
- Horizontal scaling patterns
- Distributed session storage (Redis)

📁 [week02-stateless-stateful/](week02-stateless-stateful/)

---

### **Week 03: Cloud-Native Microservices**
**Distributed Systems: Service Decomposition**

Break monoliths into independently deployable services.

- Microservice architecture patterns
- Container orchestration (Docker, Kubernetes)
- Service communication (REST, gRPC, async messaging)
- Resilience patterns (circuit breakers, retries)
- Observability (logging, metrics, tracing)

📁 [week03-microservices/](week03-microservices/)

---

### **Week 04: Secure Governance & Zero-Trust**
**Security Architecture: Defense in Depth**

Security is not a feature—it's an architectural foundation.

- Zero-trust principles
- Identity & access control (OAuth 2.1, OIDC, MFA)
- Encryption strategy (at-rest, in-transit, in-use)
- Privacy by design (GDPR, PDPA compliance)
- Service mesh security (mTLS, network policies)
- Secrets management (Vault)
- Audit & compliance logging

📁 [week04-secure-governance/](week04-secure-governance/)

---

### **Week 05: Edge Bus & Back-End Bus Architecture**
**Architectural Boundaries: Public vs Private Topology**

Real systems have two faces: a safe public interface and a fast private fabric.

- Two-bus architecture pattern
- Protocol adaptation (HTTP → gRPC)
- Binary streaming optimization
- Security boundary enforcement
- Event-driven pipelines
- Cross-cutting observability

📁 [week05-edge-bus-and-back-end-bus/](week05-edge-bus-and-back-end-bus/)

---

### **Week 06: Architecture Reasoning & System Evolution**
**Engineering Leadership: Making Decisions Defensible**

Engineers build systems. Architects decide how systems are allowed to change.

- Boundary design decisions
- Trade-off analysis and documentation
- Governance as structure
- Evolution without outages
- Migration strategies
- Architecture decision records (ADRs)

📁 [week06-architecture-governance-evolution/](week06-architecture-governance-evolution/)

---

### **Week 07: AI-Native Architecture**
**Governed Autonomy: Systems That Decide**

Traditional systems execute instructions. AI-native systems make decisions.

- AI-enabled vs AI-native systems
- Autonomy levels (Level 0-3)
- Human-in-the-loop design
- Anchors & budgets for AI behavior
- Anticipative patterns
- Safe adaptation mechanisms

📁 [week07-ai-architecture/](week07-ai-architecture/)

---

### **Week 08: Multi-Agent & Collective AI Systems**
**Coordination: When Multiple AIs Work Together**

A single AI can decide. A system of AIs must coordinate.

- Single vs collective intelligence
- Agent roles & boundaries
- Coordination patterns
- Conflict resolution
- Emergent failure detection
- Collective governance

📁 [week08-multi-agent-collective-AI-systems/](week08-multi-agent-collective-AI-systems/)

---

### **Week 09: AI Audits, Accountability & Regulation**
**Trust Infrastructure: Making AI Legally Defensible**

An AI system that cannot be audited cannot be trusted.

- Auditability as architecture
- Accountability chains
- Evidence pipelines
- Regulatory compliance (GDPR, PDPA, AI Act)
- Post-incident investigation
- Bias detection and mitigation

📁 [week09-ai-audit/](week09-ai-audit/)

---

### **Week 10: Capstone Project**
**Integration: Designing a Trustworthy AI System**

Prove you can design, defend, and evolve a production-grade AI system.

- Full architecture synthesis
- Design defense presentation
- Risk analysis and mitigation
- Evolution roadmap
- Professional portfolio piece

📁 [week10-capstone-project/](week10-capstone-project/)

---

## 🚀 Quick Start

### Prerequisites

**Required:**
- Docker or Podman
- Python 3.11+
- Node.js 18+
- Git

**Recommended:**
- Kubernetes (minikube or kind)
- VS Code or similar IDE
- Postman or curl for API testing

### Running the Infrastructure

The course uses a shared mockup infrastructure for testing:

```bash
# Start the mockup infrastructure
cd mockup-infra
podman-compose up -d --build

# Verify services
curl http://localhost:8080/health
```

### Week-by-Week Progression

Each week folder is self-contained with its own README:

```bash
# Example: Week 01
cd week01-mime-typing
python server/main_enhanced.py --verbose
# (in another terminal)
python client/main_enhanced.py
```

See individual week README files for specific instructions.

---

## 📚 Documentation Structure

```
automation/
├── docs/
│   ├── design/          # Architecture specifications
│   ├── development/     # Developer guides
│   ├── deployment/      # Deployment documentation
│   ├── reports/         # Test reports and summaries
│   └── guides/          # AI context and learning guides
├── scripts/             # Utility scripts
│   ├── ai_context.py           # Deployment state library
│   ├── demo-integration.py     # Integration demo launcher
│   └── verify_integration.py   # Verification tests
├── mockup-infra/        # Shared infrastructure
└── week01-10/           # Weekly course content
```

**Key Documentation:**
- [Architecture Overview](docs/design/ARCHITECTURE.md)
- [Network Architecture](docs/design/NETWORK_ARCHITECTURE_V2.md)
- [Getting Started Guide](docs/development/GETTING_STARTED.md)
- [Security Quick Reference](docs/development/SECURITY_QUICK_REFERENCE.md)
- [Documentation Index](docs/DOCUMENTATION_INDEX.md)

---

## 🔧 Infrastructure Components

### Mockup-Infra Services

The shared infrastructure provides:

- **Nginx Gateway** (Port 8080/443) - L7 reverse proxy with TLS
- **Network Isolation** - Public DMZ and private backend networks
- **Service Discovery** - DNS-based service routing
- **Observability** - Centralized logging and monitoring
- **Security** - mTLS, certificate management

See [mockup-infra/README.md](mockup-infra/README.md) for details.

---

## 🎯 Learning Path

### For Beginners
Start with Week 01-03 to build foundational knowledge:
1. Network programming basics
2. State management decisions
3. Distributed system patterns

### For Intermediate Engineers
Focus on Week 04-06 for architecture skills:
4. Security architecture
5. Boundary design
6. Architecture reasoning

### For Advanced/AI Engineers
Deep dive into Week 07-10 for AI governance:
7. AI-native systems
8. Multi-agent coordination
9. Audit and compliance
10. Capstone integration

---

## 🧪 Testing

Each week includes tests:

```bash
# Week 01: Integration tests
cd week01-mime-typing
python -m pytest tests/

# Week 02: API tests
cd week02-stateless-stateful/tests
node test-gateway-full.js

# Week 03+: See individual week READMEs
```

---

## 🤝 Contributing

This is an educational repository. Contributions welcome:

1. **Bug Fixes** - Fix errors in code or documentation
2. **Enhancements** - Improve examples or add clarifications
3. **Translations** - Help make content accessible
4. **Real-World Examples** - Share production patterns

Please open an issue before major changes.

---

## 📝 License

Educational content. Check individual files for specific licenses.

---

## 🔗 Additional Resources

- [Executive Summary](docs/reports/EXECUTIVE_SUMMARY.md) - Course overview for managers
- [Architecture Evolution](architectue_evolution/) - How the architecture progresses
- [AI Context Guide](docs/guides/AI_CONTEXT_README.md) - For AI-assisted development

---

## 🎓 Course Philosophy

> "The difference between a good engineer and a great architect is not the code they write—it's the decisions they can defend."

This course teaches you to:
- **Think in systems**, not just services
- **Design for evolution**, not just deployment
- **Build trust**, not just features
- **Govern complexity**, not just manage it

By Week 10, you'll understand not just *how* to build production systems, but *why* they're built that way—and how to explain your decisions to stakeholders, regulators, and future maintainers.

---

**Ready to start?** Begin with [Week 01: MIME-Based Socket File Transfer](week01-mime-typing/) →
