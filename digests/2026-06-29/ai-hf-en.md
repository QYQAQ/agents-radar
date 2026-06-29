# Hugging Face Trending Models Digest 2026-06-29

> Source: [Hugging Face Hub](https://huggingface.co/) | 30 models | Generated: 2026-06-29 00:34 UTC

---

# Hugging Face Research Models Digest — June 29, 2026

## 1. Today's Highlights

Baidu's **Unlimited-OCR** leads document understanding with 295K downloads, signaling continued demand for robust OCR systems that likely handle complex layouts and mathematical content. The **GLM-5.2** family from Zhipu AI (with NVIDIA NVFP4 optimizations) demonstrates MoE+DSA architecture maturation for long-context reasoning. NVIDIA's **LocateAnything-3B** and **Qwen3.6-35B-A3B-NVFP4** highlight the vision-language convergence, with the latter reaching 5.2M downloads for optimized multimodal deployment. Microsoft's **FastContext-1.0-4B-SFT** explicitly targets extended context through SFT, directly relevant to long-context research. Notably, uncensored fine-tunes like HauhauCS's variants suggest active post-training alignment experimentation, though this raises questions about safety-hallucination trade-offs.

---

## 2. Trending Models by Research Relevance

### 📄 OCR & Document Models

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** | baidu | 1,230 | 295,064 | Production-scale OCR with "unlimited" capacity claims; likely advances HMER and dense document layout parsing—critical for benchmarking formula recognition and table understanding. |

### 🎭 Multimodal & Vision-Language

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)** | empero-ai | 795 | 831,529 | High-download Qwen3.5-based vision model with 1M context; merges Claude-style reasoning with efficient quantization for multimodal deployment research. |
| **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)** | empero-ai | 525 | 52,492 | Full-precision variant enabling study of quantization effects on multimodal reasoning and hallucination. |
| **[Qwen/Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)** | Qwen | 397 | 23,697 | Official Qwen3.5 MoE with agent-world grounding; explicit agentic multimodal design may reduce tool-use hallucination. |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 2,302 | 3,248,724 | Massive-download uncensored VLM; natural experiment for studying alignment removal effects on multimodal truthfulness and hallucination rates. |
| **[HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced](https://huggingface.co/HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced)** | HauhauCS | 100 | 40,820 | QAT-quantized uncensored Gemma4 vision model; enables comparison of quantization-aware training vs. post-hoc quantization on multimodal calibration. |
| **[deepreinforce-ai/Ornith-1.0-9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)** | deepreinforce-ai | 233 | 5,814 | Qwen3.5-based image-text-to-text; smaller scale for controlled multimodal hallucination studies. |
| **[deepreinforce-ai/Ornith-1.0-35B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B)** | deepreinforce-ai | 203 | 19,635 | Larger Ornith variant with MoE; scales multimodal reasoning for long-context document analysis. |
| **[deepreinforce-ai/Ornith-1.0-397B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-397B)** | deepreinforce-ai | 145 | 1,116 | Extreme-scale open multimodal model; rare opportunity to study emergent reasoning-hallucination dynamics at 397B parameters. |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 2,434 | 646,451 | Visual grounding model; strong spatial reasoning foundation reduces referential hallucination in VLM pipelines. |

### 🧠 Long-Context & Reasoning Models

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)** | zai-org | 2,815 | 118,651 | GLM MoE+DSA architecture; "Dual-Stream Attention" likely enables efficient long-context processing with explicit reasoning pathways. |
| **[unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)** | unsloth | 442 | 146,023 | Optimized deployment variant; enables long-context inference efficiency research on consumer hardware. |
| **[yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)** | yuxinlu1 | 2,471 | 549,926 | High-download code-reasoning model; "fable5-composer" suggests structured reasoning traces for hallucination analysis in code generation. |
| **[yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)** | yuxinlu1 | 792 | 225,822 | Agentic variant with "tau2" temperature scaling; explicit exploration of inference-time reasoning calibration. |
| **[WeiboAI/VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)** | WeiboAI | 743 | 59,337 | Small math-specialized model; efficient testbed for studying reasoning-hallucination trade-offs in constrained compute. |
| **[deepseek-ai/DeepSeek-V4-Pro-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark)** | deepseek-ai | 178 | 373 | DeepSeek V4 with "DSpark"—likely distilled reasoning spark; academic preprint attached for reproducibility. |
| **[deepseek-ai/DeepSeek-V4-Flash-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-DSpark)** | deepseek-ai | 76 | 24 | Faster variant; enables latency-sensitive long-context applications with reasoning preservation. |
| **[Chunjiang-Intelligence/DeepSeek-v4-Fable](https://huggingface.co/Chunjiang-Intelligence/DeepSeek-v4-Fable)** | Chunjiang-Intelligence | 124 | 1,409 | Community fine-tune with "cybersecurity" focus; tests domain-specific reasoning robustness. |

### 🔧 Post-Training & Alignment

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft | 369 | 6,779 | Explicitly SFT-tuned for "Explorer SubAgent" long-context retrieval; direct study of supervised alignment for context extension. |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 2,302 | 3,248,724 | "Aggressive" uncensoring via alignment removal; natural ablation for studying RLHF/DPO necessity in multimodal settings. |
| **[HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced](https://huggingface.co/HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced)** | HauhauCS | 100 | 40,820 | "Balanced" uncensored variant; comparative study with "Aggressive" reveals alignment sensitivity to post-training intensity. |

### 👁️ Hallucination Mitigation

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[Qwen/Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)** | Qwen | 397 | 23,697 | "World-model" grounding via agentic feedback loops; explicit architectural intervention for grounding hallucination reduction. |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 2,434 | 646,451 | Spatial grounding encoder; reduces visual referential hallucination when composed with VLMs. |
| **[yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)** | yuxinlu1 | 792 | 225,822 | "Tau2" suggests calibrated confidence; agentic loop with explicit temperature scaling for uncertainty-aware generation. |

### 🏗️ Research Infrastructure

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[nvidia/GLM-5.2-NVFP4](https://huggingface.co/nvidia/GLM-5.2-NVFP4)** | nvidia | 154 | 45,762 | NVIDIA's FP4-optimized GLM-5.2 via ModelOpt; enables precision-format studies for long-context model deployment. |
| **[nvidia/Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4)** | nvidia | 371 | 5,235,413 | Highest-download model in digest; production validation of 4-bit multimodal MoE inference, critical for hallucination studies under quantization. |
| **[unsloth/Qwen-AgentWorld-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen-AgentWorld-35B-A3B-GGUF)** | unsloth | 95 | 79,503 | Unsloth-optimized world-model; efficient inference for scalable hallucination evaluation pipelines. |

---

## 3. Research Ecosystem Signal

**Qwen3.5/3.6 and GLM-5.2** have emerged as dominant open-weight families for multimodal and long-context research, with Qwen's MoE architecture (A3B active parameters) enabling efficient scaling experiments. The proliferation of **uncensored fine-tunes** (HauhauCS, empero-ai) represents an uncontrolled natural experiment in alignment removal—researchers can now directly measure hallucination rate changes when safety training is stripped, though ethical deployment requires caution. NVIDIA's aggressive **NVFP4/ModelOpt** push (5.2M downloads for Qwen3.6-NVFP4) signals industry prioritization of quantization-aware inference; this demands urgent study of whether 4-bit compression amplifies multimodal hallucination. Notably, **explicit reasoning architectures** (DSpark, Fable, Composer, AgentWorld) are replacing opaque scaling—models now advertise structured cognition, enabling mechanistic interpretability of reasoning failures. The gap between open-weight and proprietary systems is narrowing in vision-language, but **document-level OCR+reasoning** remains underrepresented beyond Baidu's entry, suggesting opportunity for HMER-focused releases.

---

## 4. Worth Exploring

| Model | Research Priority |
|-------|-----------------|
| **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** | **Critical for HMER benchmarking.** 295K downloads suggest production robustness; evaluate on arXiv formula recognition, table extraction, and multi-page document chains to test long-context OCR coherence. Compare against Pix2Struct and Donut successors for layout-aware reasoning. |
| **[Qwen/Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)** | **Hallucination mitigation via world-modeling.** The "AgentWorld" grounding mechanism offers a rare architectural intervention to study: ablate the feedback loop to measure hallucination reduction versus standard Qwen3.5. Test on multi-turn visual reasoning with external tool verification. |
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | **Controlled long-context alignment.** At 4B parameters with explicit SFT for "Explorer SubAgent," this enables affordable study of: (a) context extension via supervised training versus position interpolation, (b) retrieval-augmented hallucination in long documents, (c) sub-agent decomposition for faithful generation. Ideal for academic labs without cluster access. |

---

*Digest compiled from Hugging Face Hub trending data. Models selected for relevance to OCR/HMER, multimodal reasoning, long-context processing, post-training alignment, and hallucination mitigation research.*

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*