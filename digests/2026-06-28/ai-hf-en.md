# Hugging Face Trending Models Digest 2026-06-28

> Source: [Hugging Face Hub](https://huggingface.co/) | 30 models | Generated: 2026-06-28 00:32 UTC

---

# Hugging Face Research Models Digest
## 2026-06-28 | Focus: Long-Context Reasoning, OCR/HMER, Multimodal Reasoning, Post-Training Alignment, Hallucination Mitigation

---

## 1. Today's Highlights

**Baidu's Unlimited-OCR** (1,137 likes, 212K downloads) dominates the OCR landscape with its feature-extraction pipeline, suggesting continued industrial investment in document understanding beyond traditional text recognition. The **Qwythos-9B-Claude-Mythos-5-1M** family (empero-ai) demonstrates strong community interest in long-context multimodal reasoning, with its GGUF variant reaching 712K downloads—indicating demand for quantized, locally-deployable vision-language models with extended context windows. **NVIDIA's LocateAnything-3B** (2,406 likes, 570K downloads) signals growing research interest in spatially-grounded multimodal understanding, directly relevant to hallucination mitigation through visual grounding. The **DeepSeek-V4-Pro-DSpark** release (deepseek-ai) with its arxiv preprint suggests continued academic-industrial collaboration on reasoning architectures. Notably, **Microsoft's FastContext-1.0-4B-SFT** explicitly targets "Explorer SubAgent" functionality, reflecting the trend toward specialized smaller models for long-context retrieval and verification tasks that can reduce hallucination in RAG pipelines.

---

## 2. Trending Models by Research Relevance

### 📄 OCR & Document Models

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** | baidu | 1,137 | 212,760 | Industrial-strength OCR with "unlimited" capacity claims—relevant for HMER researchers benchmarking against production systems; feature-extraction pipeline suggests embedding-based document retrieval applications. |

---

### 🎭 Multimodal & Vision-Language

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)** | empero-ai | 670 | 712,627 | Qwen3.5-based multimodal model with 1M context in GGUF format—high download volume indicates strong demand for accessible long-context VLMs; relevant for studying quantization effects on multimodal reasoning. |
| **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)** | empero-ai | 488 | 30,298 | Full-precision variant enabling research into native multimodal long-context capabilities without quantization artifacts. |
| **[Qwen/Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)** | Qwen | 357 | 18,872 | Qwen3.5 MoE architecture with agentic multimodal design—explicit "AgentWorld" branding suggests tool-use and environment interaction research directions. |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 2,406 | 570,466 | Spatial grounding model with image-feature-extraction pipeline—directly addresses visual hallucination through explicit localization; strong engagement suggests community prioritization of grounded VLMs. |
| **[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)** | MiniMaxAI | 1,253 | 182,714 | Dedicated minimax_m3_vl multimodal architecture—emerging player in vision-language with substantial uptake; worth monitoring for architectural innovations. |
| **[deepreinforce-ai/Ornith-1.0-9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)** | deepreinforce-ai | 166 | 1,501 | Qwen3.5-based multimodal with MIT license—rare permissively-licensed vision-language option for academic research. |
| **[deepreinforce-ai/Ornith-1.0-35B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B)** | deepreinforce-ai | 161 | 7,571 | MoE variant of Ornith family; sparse activation patterns may offer efficiency insights for large-scale multimodal deployment. |
| **[deepreinforce-ai/Ornith-1.0-397B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-397B)** | deepreinforce-ai | 120 | 463 | Extremely large MoE for scaling law studies in multimodal reasoning; low downloads reflect inference barriers but research value for architecture analysis. |
| **[HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced](https://huggingface.co/HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced)** | HauhauCS | 96 | 32,222 | Quantization-aware trained Gemma4 with vision capabilities—QAT + multimodal combination rare; useful for studying precision-recovery in visual encoders. |
| **[huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated)** | huihui-ai | 137 | 6,250 | "Abliterated" Gemma4 with unified vision-language architecture—alignment intervention study case for multimodal safety research. |
| **[Jackrong/Qwopus3.6-27B-Coder-Compat-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-Coder-Compat-MTP-GGUF)** | Jackrong | 97 | 49,935 | Qwen3.6-based with MTP (Multi-Token Prediction) and vision compatibility—MTP in multimodal context underexplored; GGUF enables local experimentation. |

---

### 🧠 Long-Context & Reasoning Models

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)** | zai-org | 2,676 | 98,994 | GLM MoE with "DSA" (likely Dynamic Sparse Attention) architecture—highest-liked text-generation model; GLM family's bidirectional prefix attention offers unique long-context inductive biases worth studying. |
| **[unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)** | unsloth | 426 | 125,230 | Unsloth-optimized quantization of GLM-5.2; efficiency-community validation of architecture's deployability. |
| **[yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)** | yuxinlu1 | 2,426 | 536,130 | Gemma-4 with explicit "reasoning" tag and coding focus; high engagement suggests code-reasoning as proxy for general reasoning evaluation. |
| **[yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)** | yuxinlu1 | 729 | 206,828 | "Agentic" and "terminal" tags with 3.5x tau2 scaling—explicit temperature/entropy manipulation for exploration; relevant for reasoning stochasticity research. |
| **[WeiboAI/VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)** | WeiboAI | 742 | 57,521 | Compact Qwen2-based model with math specialization—3B parameter efficiency study for reasoning; "vibe" suggests intuitive/creative reasoning angle. |
| **[deepseek-ai/DeepSeek-V4-Pro-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark)** | deepseek-ai | 123 | 0 | DeepSeek-V4 with "DSpark" variant and arxiv citation—fresh release with academic documentation; zero downloads suggest gated or very recent; watch for reasoning architecture details. |
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft | 365 | 6,447 | Explicit "FastContext" branding with "Explorer SubAgent"—Microsoft's entry in efficient long-context; SFT-only training enables isolation of supervised vs. RL effects. |
| **[LiquidAI/LFM2.5-230M](https://huggingface.co/LiquidAI/LFM2.5-230M)** | LiquidAI | 129 | 9,791 | Sub-1B parameter liquid architecture—extreme efficiency for long-context; "liquid" implies continuous-time or state-space approach; alternative to Transformer for context scaling. |

---

### 🔧 Post-Training & Alignment

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 2,277 | 3,331,475 | Most downloaded model in digest; "Aggressive" uncensoring with vision MoE—massive uptake indicates strong demand for alignment-removed baselines; essential for studying safety fine-tuning effects through ablation. |
| **[huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated)** | huihui-ai | 137 | 6,250 | "Abliterated" Gemma4—explicit removal of refusal behaviors; controlled study of alignment tax on coding and vision capabilities. |

---

### 👁️ Hallucination Mitigation

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 2,406 | 570,466 | Primary hallucination-mitigation signal: explicit spatial grounding architecture; "LocateAnything" directly addresses visual claim verification; strongest evidence that grounding is becoming mainstream solution. |
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft | 365 | 6,447 | "Explorer SubAgent" implies retrieval-augmented verification for long-context factuality; SFT training enables study of retrieval grounding without RL confounds. |

---

### 🏗️ Research Infrastructure

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[nvidia/GLM-5.2-NVFP4](https://huggingface.co/nvidia/GLM-5.2-NVFP4)** | nvidia | 125 | 6,464 | NVIDIA's FP4 quantization of GLM-5.2 with ModelOpt framework—sub-4-bit precision for large MoE; infrastructure for efficient long-context deployment. |
| **[nvidia/Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4)** | nvidia | 366 | 5,022,254 | Highest-download model overall; NVFP4 MoE quantization at massive scale; 5M+ downloads indicate production adoption of extreme quantization for vision-language MoE. |
| **[Comfy-Org/Krea-2](https://huggingface.co/Comfy-Org/Krea-2)** | Comfy-Org | 158 | 10 | ComfyUI integration for Krea-2; workflow infrastructure for multimodal generation pipelines. |

---

## 3. Research Ecosystem Signal

**Momentum in Qwen-Gemma-GLM tripartite competition.** The ecosystem shows clear consolidation around three model families for vision-language and reasoning: Qwen3.5/3.6 (Alibaba, empero-ai, HauhauCS, Jackrong), Gemma-4 (Google, yuxinlu1, huihui-ai), and GLM-5.2 (Zhipu, unsloth, nvidia). Qwen dominates derivative volume (uncensored, quantized, MTP variants), suggesting strongest open-weight ecosystem for fine-tuning studies. Gemma-4's "fable5-composer2.5" fine-tuning lineage indicates mature community adaptation for coding and agentic tasks. GLM-5.2's MoE-DSA architecture represents the most distinct alternative attention mechanism, potentially offering long-context efficiency advantages worth benchmarking against standard transformers.

**Open-weight vs. proprietary: asymmetric convergence.** NVIDIA's massive NVFP4 download numbers (5M+) alongside high-engagement open derivatives (HauhauCS uncensored at 3.3M) suggest open-weight models have achieved production parity for vision-language deployment, with proprietary value shifting to optimization (NVIDIA) and orchestration (Microsoft's SubAgent). However, baidu's Unlimited-OCR as closed-weight feature-extraction service indicates OCR/HMER remains commercially contested territory where architectural details are guarded.

**Post-training as primary research frontier.** The prevalence of "uncensored," "abliterated," and "QAT" variants—often with higher downloads than base models—reveals alignment and quantization as the most active research surfaces. HauhauCS's "Aggressive" vs. "Balanced" uncensoring taxonomy suggests maturation of alignment-study methodologies. The near-absence of explicit RLHF-tagged models (most are SFT or unspecified) may indicate RL's reproducibility challenges, or its absorption into proprietary pipelines. For hallucination mitigation, spatial grounding (LocateAnything-3B) and retrieval sub-agents (FastContext) represent the two emerging architectural responses, with grounding showing stronger community validation through download volume.

---

## 4. Worth Exploring

| Priority | Model | Research Rationale |
|----------|-------|-------------------|
| **1** | **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | **Hallucination mitigation through spatial grounding.** The strongest architectural signal in this digest: NVIDIA's explicit investment in visual localization as a 3B-parameter task-specific model, not merely a VLM feature. With 2,406 likes and 570K downloads, it validates community demand for grounded generation. Researchers should probe whether LocateAnything's feature-extraction embeddings can be integrated into RAG pipelines for document understanding, or whether its spatial outputs serve as direct hallucination detectors for VLMs. The 3B scale enables feasible ablation studies on grounding granularity vs. performance tradeoffs. |
| **2** | **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | **Long-context efficiency and retrieval-augmented verification.** Microsoft's "Explorer SubAgent" framing suggests a decomposition strategy for long-context reasoning that may reduce hallucination through explicit retrieval steps. The SFT-only training (no RLHF tag) is methodologically valuable: it isolates the effect of supervised retrieval training from reinforcement learning, enabling cleaner causal attribution of any factuality improvements. At 4B parameters, it's computationally accessible for replication and extension studies. Priority target for benchmarking against standard RAG and against end-to-end long-context models like Qwythos-1M. |
| **3** | **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | **Alignment ablation at production scale.** With 3.3M downloads—highest in this digest—this model represents the most accessed "alignment-removed" baseline available. The "Aggressive" descriptor (vs. sibling "Balanced") suggests systematic variation in fine-tuning intensity, offering natural experiment conditions. For hallucination researchers, uncensored models provide essential baselines to measure *alignment tax*: the performance cost of safety fine-tuning on factual accuracy. The MoE-A3B architecture (35B active 3B) enables efficiency studies of sparse expert routing in vision-language tasks. Caution: evaluate safety implications of deployment; research use for controlled comparison against aligned Qwen3.6 variants is strongly justified. |

---

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*