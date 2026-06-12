# Hugging Face Trending Models Digest 2026-06-12

> Source: [Hugging Face Hub](https://huggingface.co/) | 30 models | Generated: 2026-06-12 00:38 UTC

---

# Hugging Face Research Models Digest — 2026-06-12

## 1. Today's Highlights

The **Google Gemma-4 family** dominates this week's trending list with multiple variants (12B, 26B-A4B) in both base and instruction-tuned forms, signaling a major push toward unified any-to-any multimodal architectures that natively handle vision, text, and potentially structured document inputs. **DeepSeek-V4-Pro** leads in absolute engagement with 4.7M+ likes and 4M downloads, suggesting continued appetite for open-weight reasoning models with strong long-context capabilities. Notably, **sapientinc/HRM-Text-1B** emerges as a specialized handwriting recognition and mathematical expression model (HRM), directly relevant to OCR/HMER research. The proliferation of "abliterated" and "uncensored" fine-tunes (e.g., Huihui-gemma-4-12B-it-abliterated, HauhauCS Qwen3.6 variant) indicates active community experimentation with post-training alignment removal, raising important questions for hallucination mitigation and safety research. NVIDIA's **LocateAnything-3B** and **Nemotron-3.5-Ultra** series demonstrate enterprise investment in grounded multimodal understanding and scalable alignment, respectively.

---

## 2. Trending Models by Research Relevance

### 📄 OCR & Document Models

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** | sapientinc | 749 | 134,752 | Dedicated handwriting recognition and mathematical expression (HRM) model; directly addresses HMER benchmarks and document understanding for educational/scientific content. |

---

### 🎭 Multimodal & Vision-Language

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google | 939 | 675,936 | Unified any-to-any architecture supporting seamless image-text interleaving; critical for studying native multimodal reasoning without modality-specific adapters. |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 1,869 | 131,794 | Open-vocabulary visual grounding model enabling precise spatial localization from natural language; advances grounded multimodal understanding and reduces referential hallucinations. |
| **[stepfun-ai/Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)** | stepfun-ai | 368 | 50,187 | Efficient vision-language model with competitive performance; useful for studying speed-accuracy tradeoffs in deployed multimodal systems. |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 1,675 | 3,057,541 | Aggressively uncensored MoE vision-language model; serves as a negative alignment baseline for studying hallucination propensity and safety filter bypassing in VLMs. |
| **[ByteDance/Bernini-R](https://huggingface.co/ByteDance/Bernini-R)** | ByteDance | 222 | 305 | Image-text-to-video generation with explicit rendering control; relevant for studying temporal consistency and cross-modal grounding in generative video. |

---

### 🧠 Long-Context & Reasoning Models

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 4,781 | 4,061,006 | Flagship reasoning model with extended context and chain-of-thought capabilities; benchmark for long-context retrieval and complex mathematical reasoning research. |
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google | 486 | 0 | Diffusion-based language model at 26B active/4B activated parameters; novel architecture for studying non-autoregressive reasoning and iterative refinement in long-form generation. |
| **[CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)** | CohereLabs | 307 | 1,859 | MoE code generation model; relevant for studying structured reasoning in long-context programming tasks and tool-use planning. |
| **[LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)** | LiquidAI | 594 | 142,134 | Liquid neural network architecture with 8B total/1B active parameters; explores continuous-time dynamics for potentially more efficient long-context processing. |

---

### 🔧 Post-Training & Alignment

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[huihui-ai/Huihui-gemma-4-12B-it-abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-it-abliterated)** | huihui-ai | 143 | 6,400 | Systematically removes refusal behaviors from Gemma-4; explicit dataset for studying alignment fickleness and the robustness of safety fine-tuning in multimodal models. |
| **[OBLITERATUS/Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED)** | OBLITERATUS | 234 | 14,838 | Aggressive alignment stripping of unified any-to-any model; natural experiment for measuring how multimodal capabilities degrade or hallucinate without safety constraints. |
| **[nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)** | nvidia | 198 | 59,066 | 550B-parameter (55B active) enterprise model with explicit alignment training; represents state-of-the-art in scalable RLHF and synthetic data generation for alignment research. |
| **[nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4)** | nvidia | 168 | 91,117 | Quantized variant of Nemotron-3 Ultra; enables studying alignment preservation under aggressive 4-bit floating-point compression. |

---

### 👁️ Hallucination Mitigation

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 1,869 | 131,794 | Explicit visual grounding reduces object hallucination by requiring pixel-level evidence; directly testable against standard VLM hallucination benchmarks. |
| **[google/gemma-4-12B](https://huggingface.co/google/gemma-4-12B)** | google | 516 | 140,221 | Base any-to-any model without instruction tuning; essential control for isolating the contribution of post-training alignment to hallucination rates in multimodal settings. |

---

### 🏗️ Research Infrastructure

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)** | unsloth | 561 | 711,706 | Optimized GGUF quantization of Gemma-4; enables accessible local evaluation of multimodal alignment and hallucination at reduced precision. |
| **[unsloth/gemma-4-12B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-12B-it-qat-GGUF)** | unsloth | 200 | 148,252 | QAT-quantized variant with claimed minimal accuracy loss; infrastructure for studying quantization's impact on long-context multimodal reasoning. |
| **[unsloth/gemma-4-26B-A4B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-qat-GGUF)** | unsloth | 142 | 129,110 | Extended to 26B MoE architecture; tests whether QAT preserves mixture-of-experts routing quality in multimodal contexts. |

---

## 3. Research Ecosystem Signal

The **Gemma-4 family** represents the most significant structural shift in open multimodal research, replacing patchwork encoder-decoder designs with unified "any-to-any" processing that natively interleaves vision and language tokens. This architecture is particularly promising for OCR/HMER as it eliminates the modality alignment bottleneck that plagues conventional VLMs on structured documents and mathematical notation. The simultaneous release of base, instruction-tuned, quantized, and aggressively fine-tuned variants creates an unprecedented natural experiment for alignment researchers: we can now measure how the same underlying multimodal capabilities respond to different post-training regimes.

Open-weight models continue to close the gap with proprietary systems in vision-language tasks, though **Nemotron-3 Ultra** demonstrates that enterprise-scale alignment (550B parameters, synthetic data pipelines) still offers advantages in controllability. The explosion of "abliterated" community fine-tunes—particularly for multimodal models—reveals a tension: safety alignment for VLMs remains brittle, and visual inputs provide additional attack surfaces for jailbreaking. For hallucination mitigation specifically, **LocateAnything-3B**'s grounding-first approach suggests a promising architectural direction beyond post-hoc fact-checking, though its 3B scale limits complex reasoning. The near-absence of dedicated document-OCR models (only **HRM-Text-1B**) in a top-30 list otherwise dominated by generalist VLMs indicates that specialized OCR/HMER remains underrepresented in mainstream hub activity, presenting an opportunity for targeted research contributions.

---

## 4. Worth Exploring

**[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** — This is the only explicitly HMER-focused model in the trending list and warrants immediate attention for handwriting recognition researchers. At 1B parameters, it is tractable for fine-tuning experiments and ablation studies, and its 134K downloads suggest active community validation. Researchers should evaluate it against CROHME, HME100K, and emerging handwritten-text benchmarks to assess whether compact specialized models outperform generalist VLMs (like Gemma-4) on formula recognition, or if unified architectures have subsumed this niche.

**[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** — The grounding mechanism in this model offers a concrete architectural approach to hallucination mitigation that goes beyond training-data or alignment interventions. Researchers should test whether requiring explicit spatial localization before generating descriptions reduces object hallucination on POPE, MMMU, and custom document-grounding benchmarks. Its 1,869 likes and 131K downloads indicate strong community interest, and its moderate size enables efficient experimentation with integration into larger pipelines.

**[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** — As the flagship open any-to-any model, this is essential infrastructure for comparing unified versus modular multimodal architectures. Researchers should specifically probe its performance on long-document understanding (arXiv papers, textbooks with interleaved figures) and measure whether native token interleaving improves cross-modal attention for OCR-rich tasks compared to adapter-based approaches. The availability of base, instruction, quantized, and abliterated variants enables controlled studies of alignment's impact on multimodal hallucination.

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*