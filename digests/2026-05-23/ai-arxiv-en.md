# ArXiv AI Research Digest 2026-05-23

> Source: [ArXiv](https://arxiv.org/) (cs.AI, cs.CL, cs.LG) | 50 papers | Generated: 2026-05-23 00:30 UTC

---

# ArXiv AI Research Digest — May 23, 2026

---

## 1. Today's Highlights

Today's submissions reveal three major thrusts: **state-aware post-training paradigms** that move beyond token-level optimization to state distribution matching; **self-evolving agent architectures** capable of source-level self-modification rather than merely updating skill files; and **geometric theories of robust learning** that unify disparate problems like domain adaptation, occlusion invariance, and alignment safety under a single loss-function framework. Notably, multiple papers advance **efficient attention alternatives** (Gated DeltaNet-2, linear attention variants) and **test-time compute scaling** through diversity training rather than single-reward optimization. The field also shows growing concern with **temporal grounding** in both knowledge graphs and LLM pretraining, suggesting a shift from static to dynamic world modeling.

---

## 2. Key Papers

### 🧠 Large Language Models

**[Tokenisation via Convex Relaxations](http://arxiv.org/abs/2605.22821v1)** — Tempus et al.
Reformulates tokenization as a global linear program rather than greedy local optimization (BPE/Unigram), enabling vocabulary construction that considers the whole token space.

**[Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention](http://arxiv.org/abs/2605.22791v1)** — Hatamizadeh, Choi, Kautz.
Solves the memory editing problem in linear attention by separating forgetting and writing operations, enabling constant-memory decoding without scrambling compressed recurrent states.

**[Post-Training is About States, Not Tokens: A State Distribution View of SFT, RL, and On-Policy Distillation](http://arxiv.org/abs/2605.22731v1)** — Dong Nie.
Reframes all major post-training methods through state distribution matching rather than loss-function comparisons, revealing why certain combinations succeed or fail in practice.

**[Reducing Political Manipulation with Consistency Training](http://arxiv.org/abs/2605.22771v1)** — Phan et al.
Identifies "covert political bias"—asymmetric handling of counterpart topics—and proposes consistency training to reduce 7 categories of manipulation techniques in LLMs.

**[Understanding Data Temporality Impact on Large Language Models Pre-training](http://arxiv.org/abs/2605.22769v1)** — Hippolyte et al.
First systematic study of how pre-training dynamics affect acquisition of time-sensitive knowledge, finding that shuffled corpora create specific temporal blind spots.

**[AMEL: Accumulated Message Effects on LLM Judgments](http://arxiv.org/abs/2605.22714v1)** — Sid-ali Temkit.
Demonstrates that conversation polarity biases subsequent evaluations in LLM-as-judge deployments, with critical implications for automated content moderation and code review pipelines.

---

### 🤖 Agents & Reasoning

**[MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems](http://arxiv.org/abs/2605.22794v1)** — Cai et al.
First agent architecture capable of modifying its own source code (not just skill files) in response to runtime failures, closing the loop on true autonomous self-improvement.

**[Vector Policy Optimization: Training for Diversity Improves Test-Time Search](http://arxiv.org/abs/2605.22817v1)** — Bahlous-Boldi et al.
Trains LLMs to optimize diverse response vectors rather than single rewards, dramatically improving performance in inference-time search procedures like AlphaEvolve with varying reward functions.

**[DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback](http://arxiv.org/abs/2605.22781v1)** — Dong et al.
Enables high-frequency tree search and RL for agents by reducing sandbox checkpoint/rollback to milliseconds through copy-on-write and incremental state capture.

**[LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems](http://arxiv.org/abs/2605.22786v1)** — Asif et al.
Secures latent (KV cache) communication channels between LLM agents, which are shown to be more efficient than natural language but previously vulnerable to manipulation.

---

### 🔧 Methods & Frameworks

**[The Matching Principle: A Geometric Theory of Loss Functions for Nuisance-Robust Representation Learning](http://arxiv.org/abs/2605.22800v1)** — Vishal Rajput.
Unifies eight previously separate robustness problems (domain adaptation, occlusion invariance, alignment safety, anisotropic regularization) under a single geometric framework for loss design.

**[Proxy-Based Approximation of Shapley and Banzhaf Interactions](http://arxiv.org/abs/2605.22738v1)** — Thies et al.
ProxySHAP achieves fast, accurate higher-order feature interaction estimation, overcoming the speed-accuracy tradeoff that has limited explainability for complex model behaviors.

**[The Distillation Game: Adaptive Attacks & Efficient Defenses](http://arxiv.org/abs/2605.22737v1)** — Allouah et al.
Frames model distillation as a minimax game between utility-constrained teacher and adaptive student, yielding tractable defenses against model extraction.

---

### 📊 Applications

**[ChronoMedKG: A Temporally-Grounded Biomedical Knowledge Graph and Benchmark for Clinical Reasoning](http://arxiv.org/abs/2605.22734v1)** — Ahmed et al.
First biomedical KG encoding when diseases and symptoms manifest, enabling age-aware differential diagnosis that static KGs like PrimeKG cannot support.

**[Advancing Mathematics Research with AI-Driven Formal Proof Search](http://arxiv.org/abs/2605.22763v1)** — Tsoukalas et al.
Large-scale evaluation shows LLM-generated Lean proofs can solve 35% of advanced research-level problems, establishing formal verification as a viable path for mathematical AI assistance.

**[Superhuman Safe and Agile Racing through Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2605.22748v1)** — Geles et al.
Achieves robust physical-world racing by treating other vehicles as strategic agents rather than noise, using multi-agent RL to handle dynamic shared spaces.

---

## 3. Research Trend Signal

A clear inflection point is emerging: **from static artifacts to dynamic state management across the LLM stack**. In training, this manifests as state-distribution views of post-training (Nie) and temporal awareness in pretraining (Hippolyte et al.). In inference, it appears as millisecond-level state manipulation for search (DeltaBox) and latent-space communication between agents (LCGuard). Most strikingly, agent architectures are crossing the Rubicon from **updating external files to self-modifying source code** (MOSS), representing a qualitative shift in autonomy. Simultaneously, efficiency pressures are driving attention alternatives (Gated DeltaNet-2) and geometric unifications of robustness (Matching Principle) that may consolidate today's fragmented landscape of domain-specific fixes. The field appears to be converging on **systems that maintain, communicate, and evolve state** rather than merely generating tokens.

---

## 4. Worth Deep Reading

**[The Matching Principle](http://arxiv.org/abs/2605.22800v1)** — Rajput
This paper offers rare theoretical unification in a field drowning in ad hoc methods. By showing that domain adaptation, alignment safety, occlusion invariance, and regularization all share a geometric structure in loss-function space, it provides a principled design framework rather than yet another technique. For anyone working across multiple robustness domains, this could consolidate months of literature into a single perspective.

**[MOSS: Self-Evolution through Source-Level Rewriting](http://arxiv.org/abs/2605.22794v1)** — Cai et al.
The leap from skill-file updates to source-code self-modification is the most significant advance in agent autonomy since chain-of-thought reasoning. The technical challenges—verifying self-modifications, maintaining stability, preventing runaway evolution—are substantial and well-addressed. This is likely to define a new research subfield.

**[Vector Policy Optimization](http://arxiv.org/abs/2605.22817v1)** — Bahlous-Boldi et al.
As inference-time compute scaling becomes the dominant paradigm for improving LLM capabilities, training specifically for diverse test-time search represents a critical bridge between training and inference. The connection to AlphaEvolve and similar systems suggests immediate applicability to code generation and mathematical reasoning benchmarks where single-reward training currently limits search effectiveness.

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*