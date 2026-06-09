# Hugging Face Trending Models Digest 2026-06-09

> Source: [Hugging Face Hub](https://huggingface.co/) | 30 models | Generated: 2026-06-09 00:30 UTC

---

# Hugging Face Research Models Digest — 2026-06-09

## 1. Today's Highlights

The most significant development for OCR and document understanding researchers is **PaddlePaddle/PaddleOCR-VL-1.6**, which leverages the ERNIE4.5 architecture for unified visual-language document processing, representing a major upgrade in the PaddleOCR ecosystem. **google/gemma-4-12B** and its variants (including QAT-quantized GGUF releases) signal Google's push toward efficient any-to-any multimodal architectures, with substantial community adoption evidenced by 645K+ downloads for the Unsloth GGUF variant. **nvidia/LocateAnything-3B** introduces open-vocabulary spatial localization capabilities that could enhance grounding for document layout analysis and reduce hallucination in visual reasoning. The dominance of **DeepSeek-V4-Pro** (4.7K likes, 5.4M downloads) and its Flash variant underscores continued demand for efficient, reasoning-capable LLMs with strong long-context performance.

---

## 2. Trending Models by Research Relevance

### 📄 OCR & Document Models

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | PaddlePaddle | 277 | 9,924 | Unified visual-language OCR built on ERNIE4.5; directly advances HMER and document understanding with end-to-end text recognition, layout analysis, and formula recognition capabilities in a single architecture. |

### 🎭 Multimodal & Vision-Language

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 1,617 | 121,594 | Open-vocabulary visual grounding model that enables precise spatial localization from natural language, directly applicable to reducing grounding hallucinations in document and scene understanding. |
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google | 750 | 554,173 | Native any-to-any multimodal architecture supporting seamless image-text interleaving; relevant for studying cross-modal reasoning and unified multimodal representation learning. |
| **[unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)** | unsloth | 500 | 645,263 | Efficiently quantized Gemma-4 enabling accessible edge deployment of multimodal reasoning; useful for benchmarking vision-language performance under compression. |
| **[google/gemma-4-12B](https://huggingface.co/google/gemma-4-12B)** | google | 450 | 117,509 | Base any-to-any model for researchers studying pre-training dynamics of unified multimodal architectures without instruction tuning artifacts. |
| **[stepfun-ai/Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)** | stepfun-ai | 351 | 45,535 | Efficient vision-language model with competitive performance; relevant for studying cost-effective multimodal deployment and reasoning acceleration. |
| **[unsloth/gemma-4-12B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-12B-it-qat-GGUF)** | unsloth | 146 | 121,399 | Quantization-aware trained Gemma-4 preserving multimodal capabilities; important for studying QAT effects on vision-language task performance. |
| **[unsloth/gemma-4-26B-A4B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-qat-GGUF)** | unsloth | 100 | 87,455 | Larger sparse (MoE) variant with QAT quantization; enables research on scaling efficient multimodal architectures with mixture-of-experts routing. |
| **[google/gemma-4-12B-it-qat-q4_0-gguf](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf)** | google | 97 | 52,386 | Official Google QAT release establishing quantization baselines for reproducible multimodal efficiency research. |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 1,553 | 3,036,465 | Community-modified vision-language MoE with aggressive uncensoring; caution advised for alignment research, but relevant for studying safety-utility tradeoffs in open VLMs. |
| **[nex-agi/Nex-N2-Pro](https://huggingface.co/nex-agi/Nex-N2-Pro)** | nex-agi | 116 | 716 | Qwen3.5-based MoE with vision capabilities; emerging architecture for studying efficient multimodal scaling. |

### 🧠 Long-Context & Reasoning Models

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 4,720 | 5,399,597 | State-of-the-art reasoning LLM with exceptional long-context handling and mathematical reasoning; premier model for benchmarking extended-context inference and chain-of-thought reliability. |
| **[deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)** | deepseek-ai | 1,446 | 3,262,529 | Distilled efficient variant maintaining strong reasoning; ideal for studying reasoning compression and latency-accuracy tradeoffs in long-context settings. |
| **[JetBrains/Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)** | JetBrains | 259 | 17,448 | Explicit "thinking" mode architecture for observable reasoning processes; directly relevant to studying reasoning transparency and intermediate step verification for hallucination reduction. |
| **[LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)** | LiquidAI | 548 | 135,131 | Liquid foundation model with state-space-inspired architecture; explores alternative long-context mechanisms beyond attention, potentially offering sub-quadratic scaling for extended sequences. |
| **[unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)** | unsloth | 695 | 1,186,648 | Multi-token prediction Qwen variant in efficient format; MTP training shows promise for accelerating reasoning and improving long-horizon coherence. |

### 🔧 Post-Training & Alignment

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** | sapientinc | 726 | 163,953 | Specialized text model with explicit human reward modeling alignment; relevant for studying reward hacking mitigation and stable preference optimization at smaller scales. |
| **[nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)** | nvidia | 165 | 55,910 | Massive 550B parameter model (55B active) with sophisticated post-training; NVIDIA's alignment pipeline offers insights into scaling RLHF for frontier models. |
| **[nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4)** | nvidia | 145 | 66,219 | NVFP4-quantized variant enabling practical deployment of ultra-scale aligned models; studies quantization-robustness of RLHF-trained policies. |

### 👁️ Hallucination Mitigation

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 1,617 | 121,594 | Explicit visual grounding reduces hallucination by constraining generation to verified spatial locations; applicable to grounded document QA and fact-checking. |
| **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | PaddlePaddle | 277 | 9,924 | OCR-grounded generation ensures textual outputs are anchored to recognized document content, mitigating confabulation in document understanding. |

### 🏗️ Research Infrastructure

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[nvidia/Cosmos3-Nano](https://huggingface.co/nvidia/Cosmos3-Nano)** | nvidia | 203 | 34,104 | Compact world foundation model for physical AI; infrastructure for studying multimodal pre-training and video-world model alignment. |
| **[nvidia/Cosmos3-Super](https://huggingface.co/nvidia/Cosmos3-Super)** | nvidia | 157 | 27,548 | Larger Cosmos variant establishing scaling laws for world models; relevant for long-horizon reasoning and simulation-grounded hallucination reduction. |

---

## 3. Research Ecosystem Signal

The vision-language model landscape is consolidating around **unified any-to-any architectures**, with Google's Gemma-4 family representing the most significant open-weight push into native multimodality—challenging the previous paradigm of bolted-on vision encoders. The proliferation of QAT-quantized GGUF variants (three Gemma-4 releases, all with 50K+ downloads) indicates strong researcher demand for **efficient, reproducible multimodal baselines** that preserve performance under compression. In OCR and document understanding, PaddlePaddle's ERNIE4.5-based PaddleOCR-VL-1.6 signals China's continued investment in unified document intelligence, though download volumes suggest it has not yet achieved broad adoption outside specialized use cases.

For alignment research, the contrast is striking: **DeepSeek-V4's massive organic traction** (5.4M downloads) versus **NVIDIA's Nemotron-3 Ultra** (55K downloads despite 550B parameters) suggests that efficiency and accessibility trump raw scale for community engagement. The emergence of explicit "thinking" architectures (Mellum2, DeepSeek's reasoning modes) points to a methodological shift toward **interpretable reasoning as an alignment tool**—making cognitive processes observable rather than treating models as black boxes. Notably absent from this trending list are dedicated hallucination mitigation models, suggesting the field has shifted toward **integrated solutions** (grounding, reasoning transparency) rather than standalone anti-hallucination systems. The uncensored Qwen3.6 variant's alarming 3M+ downloads raises urgent questions about safety-utility tradeoffs in open post-training.

---

## 4. Worth Exploring

**[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** — This is the most significant OCR-specific release in this cohort, integrating ERNIE4.5's multimodal capabilities into a mature document understanding framework. Researchers in HMER and document intelligence should prioritize this for benchmarking against specialized formula recognition and layout analysis tasks, as it likely represents the state-of-the-art in unified OCR-VL architectures.

**[JetBrains/Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)** — The explicit "thinking" mode offers a rare opportunity to study reasoning processes directly, making it invaluable for hallucination research. Unlike opaque chain-of-thought, this architecture may expose where and how models confabulate, enabling targeted intervention. Its modest size (12B total, 2.5B active) makes it feasible for mechanistic interpretability studies.

**[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** — With unmatched community validation (4.7K likes, 5.4M downloads), this is the definitive baseline for long-context reasoning research. Its efficiency innovations (likely including MLA and other architectural optimizations) make it practical for extended-context experiments that would be prohibitive with other frontier models. Essential for anyone studying reasoning reliability across long horizons or developing hallucination benchmarks for mathematical and logical reasoning.

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*