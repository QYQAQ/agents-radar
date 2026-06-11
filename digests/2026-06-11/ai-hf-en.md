# Hugging Face Trending Models Digest 2026-06-11

> Source: [Hugging Face Hub](https://huggingface.co/) | 30 models | Generated: 2026-06-11 00:37 UTC

---

# Hugging Face Research Models Digest — June 11, 2026

---

## 1. Today's Highlights

Google's **Gemma 4** family dominates this week's releases with unified any-to-any architectures, signaling a major push toward native multimodal reasoning without modality-specific adapters. **DeepSeek-V4-Pro** leads engagement with 4.76M weekly downloads, suggesting continued demand for open-weight reasoning models with strong long-context capabilities. Notably, **sapientinc/HRM-Text-1B** emerges as a specialized OCR-adjacent model for handwritten recognition and mathematical expression, filling a critical gap in the HMER ecosystem. NVIDIA's **LocateAnything-3B** introduces grounded visual localization that could reduce hallucination in vision-language tasks through explicit spatial reasoning. The proliferation of quantized GGUF variants (Unsloth, Google official) indicates infrastructure maturation for deploying multimodal models with reduced hallucination risks via deterministic inference.

---

## 2. Trending Models by Research Relevance

### 📄 OCR & Document Models

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** | sapientinc | 739 | 134,752 | Dedicated handwritten recognition and mathematical expression model (HRM-Text tag); directly addresses HMER with 1B-parameter efficiency for formula recognition and document understanding research. |

### 🎭 Multimodal & Vision-Language

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google | 885 | 675,936 | Native any-to-any unified architecture enabling seamless image-text-to-text reasoning; critical for studying emergent cross-modal capabilities and unified multimodal representation learning. |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 1,803 | 131,794 | Grounded visual localization with image-feature-extraction; reduces referential hallucination by explicitly grounding language in visual coordinates. |
| **[stepfun-ai/Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)** | stepfun-ai | 363 | 50,187 | Vision-language model with Step-3.7 architecture; offers alternative multimodal design for comparative studies in efficient visual reasoning. |
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google | 213 | 0 | Novel diffusion-based Gemma variant for image-text-to-text; explores generative multimodal alignment with 26B MoE parameters. |
| **[ByteDance/Bernini-R](https://huggingface.co/ByteDance/Bernini-R)** | ByteDance | 210 | 305 | Image-text-to-video generation with Bernini renderer; relevant for temporal multimodal consistency and video hallucination research. |

### 🧠 Long-Context & Reasoning Models

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 4,758 | 4,061,006 | DeepSeek V4 architecture with proven long-context scaling; highest engagement signals research community validation for reasoning and extended-context benchmarks. |
| **[LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)** | LiquidAI | 581 | 142,134 | Liquid Foundation Model 2.5 with MoE (8B active/1B total); explores alternative long-context architectures with linear attention mechanisms. |
| **[JetBrains/Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)** | JetBrains | 281 | 18,273 | Explicit "Thinking" variant with 12B-A2.5B MoE; designed for step-by-step reasoning traceability and chain-of-thought verification. |
| **[CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)** | CohereLabs | 255 | 1,859 | Cohere2 MoE architecture optimized for code; relevant for structured reasoning and long-context program synthesis evaluation. |

### 🔧 Post-Training & Alignment

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 1,630 | 3,057,541 | Aggressive uncensored Qwen3.6 MoE variant; high engagement reflects active community experimentation with safety-removed baselines for alignment research—critical for studying reward hacking and value erosion. |
| **[huihui-ai/Huihui-gemma-4-12B-it-abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-it-abliterated)** | huihui-ai | 135 | 6,400 | Explicitly "abliterated" Gemma 4 with safety training removed; controlled comparison for studying alignment robustness and refusal behavior in multimodal settings. |
| **[OBLITERATUS/Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED)** | OBLITERATUS | 212 | 14,838 | Parallel safety-removal effort on Gemma 4; enables cross-study validation of alignment intervention effects on any-to-any models. |

### 👁️ Hallucination Mitigation

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 1,803 | 131,794 | Spatial grounding architecture explicitly designed to reduce object hallucination through pixel-level localization supervision; directly applicable to hallucination quantification research. |
| **[google/gemma-4-12B-it-qat-q4_0-gguf](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf)** | google | 123 | 96,749 | Official QAT-quantized variant with deterministic inference; quantization-aware training reduces stochastic output variance, enabling reproducible hallucination studies. |
| **[unsloth/gemma-4-12B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-12B-it-qat-GGUF)** | unsloth | 187 | 148,252 | Community QAT implementation with verified equivalence claims; supports cross-validation of quantization effects on multimodal hallucination rates. |

### 🏗️ Research Infrastructure

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)** | unsloth | 548 | 711,706 | Most-downloaded Gemma 4 variant; infrastructure for efficient multimodal deployment and reproducible evaluation pipelines. |
| **[unsloth/gemma-4-12B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-12B-it-qat-GGUF)** | unsloth | 187 | 148,252 | QAT-quantized any-to-any model; enables controlled studies of compression vs. hallucination tradeoffs in unified multimodal architectures. |
| **[unsloth/gemma-4-26B-A4B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-qat-GGUF)** | unsloth | 129 | 129,110 | Scaled QAT variant with MoE; infrastructure for parameter-efficiency studies in multimodal reasoning at 26B scale. |

---

## 3. Research Ecosystem Signal

**Gemma 4** has rapidly established itself as the dominant open-weight family for multimodal reasoning research, with Google releasing unified any-to-any architectures alongside official quantized variants—suggesting intentional ecosystem cultivation for reproducible science. The parallel emergence of multiple "abliterated" safety-removed fine-tunes (HauhauCS, huihui-ai, OBLITERATUS) within weeks of release indicates both (a) vulnerability of current alignment techniques to community removal, and (b) active demand for unaligned baselines in mechanistic interpretability and red-teaming research. **DeepSeek-V4-Pro's** 4M+ downloads confirm that Chinese open-weight models remain competitive with Western counterparts in reasoning benchmarks, while **NVIDIA's LocateAnything** represents a notable proprietary-to-open shift in grounded vision, potentially reducing reliance on closed APIs for hallucination-critical applications. The **HRM-Text-1B** release is particularly significant as one of few specialized HMER models in a landscape dominated by generalist VLMs, suggesting renewed recognition that document understanding requires dedicated architectures. Quantization infrastructure (QAT-GGUF variants from both Google and Unsloth) is maturing specifically for multimodal deployment, enabling researchers to isolate whether hallucination stems from model capacity or inference stochasticity.

---

## 4. Worth Exploring

### **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**
**Why study it:** Explicit spatial grounding with 1,803 likes but only 131K downloads (low adoption relative to engagement) suggests underexplored potential. For hallucination researchers, it offers a controlled architecture to test whether pixel-level supervision reduces object hallucination compared to standard VLMs—directly testable against Gemma 4 on grounded captioning benchmarks.

### **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**
**Why study it:** The sole dedicated HMER model in this cohort with strong download traction (134K). Generalist multimodal models consistently underperform on handwritten mathematical expressions; this 1B-parameter specialist enables ablation studies on whether scale or architecture specialization drives OCR performance, with direct implications for efficient document AI.

### **[JetBrains/Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)**
**Why study it:** Explicit "Thinking" designation with MoE architecture from a non-traditional AI lab (JetBrains). Offers fresh perspective on reasoning trace transparency—comparing its step-by-step outputs against DeepSeek-V4-Pro's implicit reasoning could yield insights on whether explicit thinking tokens reduce logical hallucination in long-context chains, particularly for code and structured reasoning tasks.

---

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*