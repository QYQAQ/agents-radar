# ArXiv AI Research Digest 2026-05-23

> Source: [ArXiv](https://arxiv.org/) (cs.AI, cs.CL, cs.LG) | 50 papers | Generated: 2026-05-22 16:02 UTC

---

# ArXiv AI Research Digest — May 23, 2026

---

## 1. Today's Highlights

Today's submissions reveal a strong pivot toward **state-aware post-training paradigms**, with multiple papers reframing SFT/RL/distillation through state distributions rather than token-level losses. **Self-evolving agent systems** reach a new milestone with source-level code rewriting, moving beyond text-mutable artifacts. **Linear attention architectures** continue maturing through decoupled memory mechanisms, while **safety and security concerns** escalate across multi-agent KV sharing and conflict-context deployment. Notably, **inverse capability scaling** emerges as a critical finding—more capable LLMs paradoxically worsen forecasts in high-stakes domains with regime changes.

---

## 2. Key Papers

### 🧠 Large Language Models

**[Tokenisation via Convex Relaxations](http://arxiv.org/abs/2605.22821v1)** — Tempus et al. | Replaces greedy BPE/Unigram tokenization with a global linear programming formulation, optimizing the vocabulary as a whole rather than through local decisions.

**[Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention](http://arxiv.org/abs/2605.22791v1)** — Hatamizadeh, Choi, Kautz | Solves the core challenge of compressed recurrent memory editing by separating forgetting and writing operations, advancing sub-quadratic sequence modeling.

**[Post-Training is About States, Not Tokens: A State Distribution View of SFT, RL, and On-Policy Distillation](http://arxiv.org/abs/2605.22731v1)** — Dong Nie | Reframes all major post-training methods through state distribution matching, offering a unified theoretical lens for optimization design.

**[Clipping Bottleneck: Stabilizing RLVR via Stochastic Recovery of Near-Boundary Signals](http://arxiv.org/abs/2605.22703v1)** — Yang et al. | Diagnoses and fixes a fundamental instability in GRPO-style clipped objectives that limits reasoning scaling through reinforcement learning.

**[Is Capability a Liability? More Capable Language Models Make Worse Forecasts When It Matters Most](http://arxiv.org/abs/2605.22672v1)** — Merrill, Lee, Karger | Documents dangerous inverse scaling on high-stakes forecasting tasks with tail risks, challenging assumptions about capability monotonicity.

**[Reducing Political Manipulation with Consistency Training](http://arxiv.org/abs/2605.22771v1)** — Phan et al. | Exposes covert political bias through asymmetric handling of counterpart topics and proposes consistency training as a mitigation.

**[Understanding Data Temporality Impact on Large Language Models Pre-training](http://arxiv.org/abs/2605.22769v1)** — Hippolyte et al. | First systematic study of how pre-training dynamics affect acquisition of time-sensitive knowledge, with implications for knowledge cutoff and recency bias.

**[AMEL: Accumulated Message Effects on LLM Judgments](http://arxiv.org/abs/2605.22714v1)** — Sid-ali Temkit | Reveals conversation-history polarity bias in LLM evaluators, critical for automated grading and moderation pipelines processing many items sequentially.

---

### 🤖 Agents & Reasoning

**[MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems](http://arxiv.org/abs/2605.22794v1)** — Cai et al. | Enables agents to modify their own source code rather than just skill files, closing the loop on autonomous improvement without human deployment cycles.

**[Vector Policy Optimization: Training for Diversity Improves Test-Time Search](http://arxiv.org/abs/2605.22817v1)** — Bahlous-Boldi et al. | Optimizes policies to be diverse-in-capability rather than single-reward maximizers, dramatically improving performance in inference-time search procedures like AlphaEvolve.

**[LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems](http://arxiv.org/abs/2605.22786v1)** — Asif et al. | Secures latent (KV cache) communication channels between agents against malicious manipulation, enabling faster-than-text coordination with safety guarantees.

**[DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback](http://arxiv.org/abs/2605.22781v1)** — Dong et al. | Provides the infrastructure layer for high-frequency agent exploration by achieving millisecond-level full sandbox state checkpoint/rollback.

**[Scout-Assisted Planning for Heterogeneous Robot Teams under Partially Known Environments](http://arxiv.org/abs/2605.22693v1)** — Bui et al. | Uses UAV scouts to reduce costly ground-robot backtracking in partially known environments, demonstrating physical multi-agent coordination.

---

### 🔧 Methods & Frameworks

**[The Matching Principle: A Geometric Theory of Loss Functions for Nuisance-Robust Representation Learning](http://arxiv.org/abs/2605.22800v1)** — Vishal Rajput | Unifies robustness, domain adaptation, invariance, and alignment safety under a single geometric framework of loss function design.

**[Proxy-Based Approximation of Shapley and Banzhaf Interactions](http://arxiv.org/abs/2605.22738v1)** — Thies et al. | ProxySHAP reconciles computational efficiency with accuracy for higher-order feature interactions, enabling practical explainability at scale.

**[The Distillation Game: Adaptive Attacks & Efficient Defenses](http://arxiv.org/abs/2605.22737v1)** — Allouah et al. | Frames model distillation as a minimax game between utility-constrained teacher and adaptive student, yielding tractable defense strategies.

**[Uniform Diffusion Models Revisited: Leave-One-Out Denoiser and Absorbing State Reformulation](http://arxiv.org/abs/2605.22765v1)** — Gourevitch et al. | Clarifies and improves discrete diffusion training through a leave-one-out denoiser, resolving inconsistencies in uniform diffusion reverse dynamics.

---

### 📊 Applications

**[Advancing Mathematics Research with AI-Driven Formal Proof Search](http://arxiv.org/abs/2605.22763v1)** — Tsoukalas et al. | First large-scale evaluation of LLM-generated formal proofs in Lean for solving real mathematics research problems, establishing reliability baselines.

**[Forecasting Scientific Progress with Artificial Intelligence](http://arxiv.org/abs/2605.22681v1)** — Wu et al. | Introduces temporally grounded evaluation for AI scientific forecasting under controlled knowledge constraints, testing whether AI can anticipate discovery.

**[CogAdapt: Transferring Clinical ECG Foundation Models to Wearable Cognitive Load Assessment via Lead Adaptation](http://arxiv.org/abs/2605.22774v1)** — Mousavi et al. | Adapts million-scale clinical ECG models to wearable cognitive load monitoring through lead adaptation, bridging clinical and consumer health sensing.

**[Live Music Diffusion Models: Efficient Fine-Tuning and Post-Training of Interactive Diffusion Music Generators](http://arxiv.org/abs/2605.22717v1)** — Novack et al. | Enables real-time interactive music generation through diffusion models, escaping the compute requirements of discrete autoregressive approaches.

**[Can AI Make Conflicts Worse? An Alignment Failure in LLM Deployment Across Conflict Contexts](http://arxiv.org/abs/2605.22720v1)** — Andrii Kryshtal | Documents alignment failures in conflict-zone LLM deployments where outputs may exacerbate rather than inform, calling for context-specific safety practices.

---

## 3. Research Trend Signal

Three converging directions emerge from today's corpus. **First, the "state-centric" turn in post-training**: Nie's theoretical reframing joins with DeltaBox's infrastructure and MOSS's self-modification to suggest the field is moving beyond token-level optimization toward state-space awareness in training and deployment. This mirrors broader systems-level thinking about what we actually want models to maintain across interactions. **Second, latent communication as both opportunity and attack surface**: LCGuard's protection of KV-cache channels and the broader multi-agent coordination papers indicate researchers are taking seriously the speed/efficiency gains of non-text agent communication while scrambling to secure it. **Third, capability-safety tension intensification**: Merrill et al.'s inverse scaling joins Kryshtal's conflict analysis and Phan et al.'s political manipulation work to paint a picture where raw capability gains may actively harm performance or safety in sensitive domains. This suggests the field is entering a phase where capability elicitation and risk mitigation must be co-designed rather than sequentially addressed.

---

## 4. Worth Deep Reading

**[Post-Training is About States, Not Tokens](http://arxiv.org/abs/2605.22731v1)** — This paper offers the most promising theoretical unification of post-training methods in recent months. By showing that SFT, RL, and distillation all manipulate state distributions with different implicit sampling strategies, it provides actionable guidance for hybrid method design. Essential for anyone working on training pipelines.

**[MOSS: Self-Evolution through Source-Level Rewriting](http://arxiv.org/abs/2605.22794v1)** — The leap from modifying skill files to source-level self-rewriting represents a qualitative shift in autonomous agent capabilities. The technical architecture and safety implications deserve careful study, as this may define the next phase of agent autonomy.

**[Is Capability a Liability?](http://arxiv.org/abs/2605.22672v1)** — The inverse scaling finding on high-stakes forecasting is both surprising and urgently relevant. The empirical methodology is clean, and the implications for deployment of frontier models in finance, epidemiology, and policy are profound. Required reading for AI safety and applied ML practitioners.

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*