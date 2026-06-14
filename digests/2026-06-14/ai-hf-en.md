# Hugging Face Trending Models Digest 2026-06-14

> Source: [Hugging Face Hub](https://huggingface.co/) | 30 models | Generated: 2026-06-14 00:35 UTC

---

# Hugging Face Research Models Digest — June 14, 2026

## 1. Today's Highlights

The **Gemma 4** family dominates this week's trending list with unprecedented momentum, particularly the **google/gemma-4-12B-it** surpassing 1M downloads, signaling strong researcher interest in unified any-to-any architectures for multimodal reasoning. **DeepSeek-V4-Pro** leads in raw engagement with 4,813 likes and 3.25M downloads, suggesting continued appetite for open-weight reasoning models with strong long-context capabilities. Notably, **nvidia/LocateAnything-3B** emerges as a specialized vision-language model for spatial grounding, relevant to document layout understanding and visual grounding tasks that underpin OCR/HMER pipelines. The proliferation of uncensored/abliterated fine-tunes (e.g., **HauhauCS/Qwen3.6-35B-A3B-Uncensored**, **Jiunsong/supergemma4-26b-uncensored**) raises important questions about post-training alignment trade-offs and safety-aware hallucination mitigation research. Meanwhile, **moonshotai/Kimi-K2.7-Code** and **MiniMaxAI/MiniMax-M3** indicate sustained investment in long-context multimodal code understanding, with potential applications for structured document and formula recognition.

---

## 2. Trending Models by Research Relevance

### 📄 OCR & Document Models
*No direct OCR/HMER-specialized models in this week's top 30; however, several multimodal models with document understanding capabilities are noted below.*

### 🎭 Multimodal & Vision-Language

| Model | Author | Likes | Downloads | Why It Matters |
|-------|--------|-------|-----------|--------------|
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google | 705 | 92,080 | Diffusion-based generative VLM combining image generation with text understanding; relevant to studying hallucination in generative multimodal outputs and cross-modal alignment. |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 1,959 | 69,443 | Spatial grounding VLM for open-vocabulary localization; directly applicable to document layout analysis, figure/table detection, and visual grounding for OCR pipelines. |
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google | 995 | 1,005,883 | Unified any-to-any multimodal model with massive adoption; its architecture and 1M+ download volume make it critical for benchmarking multimodal reasoning and studying unified perception-language alignment. |
| **[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)** | MiniMaxAI | 413 | 1,031 | Compact multimodal model with competitive vision-language performance; useful for studying efficient cross-modal architectures and resource-constrained document understanding. |
| **[google/gemma-4-12B](https://huggingface.co/google/gemma-4-12B)** | google | 533 | 207,338 | Base any-to-any Gemma 4 variant; essential for studying pre-training vs. instruction-tuned multimodal behavior and alignment dynamics. |
| **[ByteDance/Bernini-R](https://huggingface.co/ByteDance/Bernini-R)** | ByteDance | 235 | 426 | Image-text-to-video generation with spatial reasoning; relevant to understanding temporal and spatial coherence in multimodal generation, with implications for hallucination mitigation in dynamic visual content. |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 1,761 | 2,411,202 | High-engagement uncensored vision-language MoE; critical negative example for studying alignment degradation, safety-hallucination trade-offs, and post-training robustness in multimodal systems. |
| **[Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF)** | Jackrong | 157 | 11,291 | Code-vision multimodal model with GGUF quantization; relevant to document-code hybrid understanding and efficient deployment of structured document parsers. |

### 🧠 Long-Context & Reasoning Models

| Model | Author | Likes | Downloads | Why It Matters |
|-------|--------|-------|-----------|--------------|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 4,813 | 3,250,404 | Leading open-weight reasoning model with exceptional engagement; its architecture and scaling properties are directly relevant to long-context inference, chain-of-thought reliability, and reasoning hallucination studies. |
| **[moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)** | moonshotai | 515 | 1,689 | Long-context code-focused multimodal model from Kimi family; explicitly designed for extended context processing and structured reasoning, with direct applications to mathematical formula understanding and HMER. |
| **[CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)** | CohereLabs | 355 | 6,533 | MoE-based code model with efficient long-context handling; relevant to studying sparse expert routing for reasoning tasks and computational efficiency in extended sequence modeling. |
| **[nex-agi/Nex-N2-Pro](https://huggingface.co/nex-agi/Nex-N2-Pro)** | nex-agi | 236 | 3,092 | Qwen3.5 MoE-based reasoning model; useful for analyzing mixture-of-experts dynamics in multimodal reasoning and context-dependent expert specialization. |
| **[XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash)** | XiaomiMiMo | 106 | 3,590 | Agent-oriented reasoning model with FP4 quantization; relevant to studying reasoning reliability in tool-augmented systems and low-precision inference effects on hallucination. |
| **[prefeitura-rio/Rio-3.5-Open-397B](https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B)** | prefeitura-rio | 110 | 5,943 | Massive 397B parameter open MoE; scale makes it notable for studying emergent long-context capabilities and efficiency- reasoning trade-offs in extreme-scale models. |

### 🔧 Post-Training & Alignment

| Model | Author | Likes | Downloads | Why It Matters |
|-------|--------|-------|-----------|--------------|
| **[OBLITERATUS/Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED)** | OBLITERATUS | 277 | 50,289 | Abliterated/uncensored Gemma 4 variant; directly relevant to studying alignment removal techniques, their effects on helpfulness-harmlessness trade-offs, and unintended hallucination consequences of "de-alignment." |
| **[huihui-ai/Huihui-gemma-4-12B-it-abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-it-abliterated)** | huihui-ai | 152 | 8,270 | Another abliterated Gemma 4 fine-tune; useful for comparative analysis of different alignment removal methods and their differential impact on multimodal truthfulness. |
| **[Jiunsong/supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)** | Jiunsong | 818 | 98,892 | High-engagement uncensored 26B Gemma 4; the popularity of such models demands rigorous study of post-training alignment fragility and methods for robust preference learning. |

### 👁️ Hallucination Mitigation

| Model | Author | Likes | Downloads | Why It Matters |
|-------|--------|-------|-----------|--------------|
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google | 705 | 92,080 | *(Cross-listed)* Diffusion-based generation inherently enables iterative refinement; its architecture offers a natural testbed for studying generation-time hallucination reduction through denoising guidance. |
| **[nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)** | nvidia | 400 | 3,975 | Streaming ASR with cache-aware processing; relevant to real-time hallucination mitigation in speech-to-text, with techniques transferable to streaming document understanding. |

### 🏗️ Research Infrastructure

| Model | Author | Likes | Downloads | Why It Matters |
|-------|--------|-------|-----------|--------------|
| **[unsloth/diffusiongemma-26B-A4B-it-GGUF](https://huggingface.co/unsloth/diffusiongemma-26B-A4B-it-GGUF)** | unsloth | 246 | 42,885 | GGUF-quantized DiffusionGemma; Unsloth's optimization infrastructure enables efficient research on large multimodal models with reduced computational barriers. |
| **[unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)** | unsloth | 580 | 872,895 | High-volume GGUF distribution of Gemma 4; critical infrastructure for accessible hallucination and alignment research on unified multimodal architectures. |
| **[unsloth/gemma-4-12B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-12B-it-qat-GGUF)** | unsloth | 213 | 227,830 | QAT-optimized Gemma 4; quantization-aware training preserves more alignment properties than post-hoc quantization, making it valuable for studying compression-alignment interactions. |
| **[unsloth/gemma-4-26B-A4B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-qat-GGUF)** | unsloth | 151 | 260,757 | Larger QAT variant; enables scale-dependent studies of alignment preservation under quantization. |

---

## 3. Research Ecosystem Signal

**Gemma 4's dominance** represents the most significant ecosystem shift: Google's unified any-to-any architecture has achieved both mass adoption (1M+ downloads for 12B-it) and extensive community modification, creating an unprecedented natural experiment in alignment robustness. The sheer volume of abliterated/uncensored fine-tunes—**OBLITERATED**, **abliterated**, **supergemma4-uncensored**, **HauhauCS Aggressive**—signals that post-training alignment remains fragile and easily reversed, demanding new technical approaches to "unaligned" robustness rather than mere preference optimization. This tension between open-weight accessibility and alignment durability is particularly acute in vision-language models, where multimodal hallucinations can be visually persuasive and harder to detect.

**Open-weight momentum continues to concentrate** in Chinese-origin model families (DeepSeek, Qwen/Kimi/MiniMax derivatives) with Western labs (Google, NVIDIA, Cohere) competing through architectural differentiation—unified any-to-any, spatial grounding, MoE efficiency—rather than scale alone. The **absence of dedicated OCR/HMER models** in this week's trending list is notable: document understanding appears increasingly subsumed into general multimodal architectures, raising questions about whether specialized formula recognition requires continued independent development or benefits from unified pre-training. For hallucination mitigation specifically, the research community faces a paradox: the most-downloaded "research" models are often deliberately de-aligned, suggesting that safety research itself requires engagement with adversarially modified systems.

---

## 4. Worth Exploring

**[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** — **Highest priority for OCR/HMER researchers.** This spatial grounding model offers explicit open-vocabulary localization with strong engagement (1,959 likes), suggesting reliable performance. For formula recognition, its grounding mechanism can be adapted to detect and localize mathematical expressions within document layouts, serving as a preprocessing module for specialized HMER encoders. Its 3B scale enables efficient experimentation with document-specific fine-tuning.

**[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** — **Essential baseline for multimodal alignment research.** With 1M+ downloads and unified any-to-any architecture, this is becoming a de facto standard for comparing hallucination mitigation techniques across modalities. Researchers should establish its baseline performance on document understanding benchmarks before and after alignment interventions, using the proliferating abliterated variants as counterfactuals.

**[moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)** — **Strategic for long-context reasoning research.** The Kimi family's established long-context reputation, combined with this code-focused multimodal variant, makes it ideal for studying how extended context windows affect structured reasoning reliability—directly relevant to parsing long documents with interleaved formulas, tables, and explanatory text. Its relatively low download count (1,689) suggests underexplored potential for document understanding fine-tuning.

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*