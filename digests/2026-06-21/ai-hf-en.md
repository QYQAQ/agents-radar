# Hugging Face Trending Models Digest 2026-06-21

> Source: [Hugging Face Hub](https://huggingface.co/) | 30 models | Generated: 2026-06-21 00:37 UTC

---

# Hugging Face Research Models Digest — 2026-06-21

---

## 1. Today's Highlights

The **Google Gemma-4** family continues to dominate with its unified any-to-any architecture, now heavily fine-tuned for coding and agentic workflows—relevant for multimodal reasoning benchmarks. **MiniMax-M3** and **Kimi-K2.7-Code** signal strong progress in vision-language integration with extended context handling, critical for document understanding and HMER evaluation. **DeepSeek-V4-Pro** leads raw engagement (4,985 likes, 2.8M downloads), suggesting open-weight reasoning models are consolidating around MoE architectures. Notably, **datalab-to/lift** appears purpose-built for PDF document understanding, directly addressing OCR pipeline gaps. The proliferation of GGUF quantized variants (unsloth, yuxinlu1, Jackrong) indicates robust community investment in efficient deployment of alignment-tuned models.

---

## 2. Trending Models

### 📄 OCR & Document Models

| Model | Author | Likes | Downloads | Relevance |
|-------|--------|-------|-----------|-----------|
| [**datalab-to/lift**](https://huggingface.co/datalab-to/lift) | datalab-to | 86 | 0 | Purpose-built PDF document understanding model leveraging Qwen3.5 architecture; directly relevant for layout analysis and formula recognition research despite zero downloads indicating fresh release. |

### 🎭 Multimodal & Vision-Language

| Model | Author | Likes | Downloads | Relevance |
|-------|--------|-------|-----------|-----------|
| [**MiniMaxAI/MiniMax-M3**](https://huggingface.co/MiniMaxAI/MiniMax-M3) | MiniMaxAI | 1,159 | 85,771 | Native image-text-to-text model with strong multimodal architecture; trending for cross-modal reasoning and visual question answering research. |
| [**google/diffusiongemma-26B-A4B-it**](https://huggingface.co/google/diffusiongemma-26B-A4B-it) | google | 1,022 | 673,464 | Diffusion-based Gemma variant for image-text-to-text; notable for generative multimodal alignment and hallucination-prone generation studies. |
| [**moonshotai/Kimi-K2.7-Code**](https://huggingface.co/moonshotai/Kimi-K2.7-Code) | moonshotai | 929 | 317,963 | Image-text-to-text with code specialization; strong candidate for multimodal mathematical reasoning and HMER benchmark evaluation. |
| [**nvidia/LocateAnything-3B**](https://huggingface.co/nvidia/LocateAnything-3B) | nvidia | 2,216 | 235,606 | Visual grounding and localization model; excellent for studying spatial reasoning and reducing object hallucination in VLMs. |
| [**google/gemma-4-12B-it**](https://huggingface.co/google/gemma-4-12B-it) | google | 1,106 | 1,696,240 | Unified any-to-any architecture; flagship model for studying multimodal tokenization and cross-modal transfer in open weights. |
| [**prefeitura-rio/Rio-3.5-Open-397B**](https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B) | prefeitura-rio | 327 | 190,694 | Massive 397B MoE vision-language model; relevant for scaling laws in multimodal reasoning and document understanding. |
| [**HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive**](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive) | HauhauCS | 2,040 | 3,812,636 | High-engagement uncensored vision model; useful for studying alignment trade-offs and safety hallucination in post-training ablation. |
| [**Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF**](https://huggingface.co/Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF) | Jackrong | 269 | 168,502 | Multi-token prediction vision-language model; MTP objective may reduce autoregressive hallucination in structured outputs like math formulas. |
| [**DavidAU/Qwen3.6-40B-Claude-4.6-Opus-Deckard-Heretic-Uncensored-Thinking-NEO-CODE-Di-IMatrix-MAX-GGUF**](https://huggingface.co/DavidAU/Qwen3.6-40B-Claude-4.6-Opus-Deckard-Heretic-Uncensored-Thinking-NEO-CODE-Di-IMatrix-MAX-GGUF) | DavidAU | 411 | 587,521 | Extreme fine-tune with "thinking" and code specialization; natural experiment for studying emergence vs. fine-tuning in reasoning traces. |
| [**bosonai/higgs-audio-v3-tts-4b**](https://huggingface.co/bosonai/higgs-audio-v3-tts-4b) | bosonai | 496 | 72,225 | Audio-text-speech model on Qwen3 backbone; relevant for multimodal alignment beyond vision, including speech-based document accessibility. |

### 🧠 Long-Context & Reasoning Models

| Model | Author | Likes | Downloads | Relevance |
|-------|--------|-------|-----------|-----------|
| [**zai-org/GLM-5.2**](https://huggingface.co/zai-org/GLM-5.2) | zai-org | 1,686 | 19,683 | GLM MoE with DSA (Dynamic Sparse Attention); architecture explicitly designed for long-context efficiency and reasoning scalability. |
| [**WeiboAI/VibeThinker-3B**](https://huggingface.co/WeiboAI/VibeThinker-3B) | WeiboAI | 511 | 16,270 | Compact math-specialized model; strong candidate for studying reasoning emergence in small-scale HMER and equation solving. |
| [**deepseek-ai/DeepSeek-V4-Pro**](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | deepseek-ai | 4,985 | 2,797,050 | Dominant open-weight reasoning model; benchmark leader for long-context mathematical reasoning and chain-of-thought evaluation. |
| [**microsoft/FastContext-1.0-4B-SFT**](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT) | microsoft | 244 | 1,998 | Explicitly named for context efficiency; Explorer SubAgent tag suggests agentic long-context decomposition research. |
| [**CohereLabs/North-Mini-Code-1.0**](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) | CohereLabs | 467 | 18,783 | Cohere MoE code model; relevant for comparing reasoning architectures across model families in controlled benchmarks. |

### 🔧 Post-Training & Alignment

| Model | Author | Likes | Downloads | Relevance |
|-------|--------|-------|-----------|-----------|
| [**yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF**](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF) | yuxinlu1 | 1,983 | 312,332 | Multi-stage fine-tuned Gemma (Fable5 + Composer2.5); exemplifies complex post-training stacking for coding alignment. |
| [**yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF**](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF) | yuxinlu1 | 183 | 6,307 | Agentic variant with "tau2" scaling; explicit exploration of inference-time compute scaling for alignment. |
| [**unsloth/GLM-5.2-GGUF**](https://huggingface.co/unsloth/GLM-5.2-GGUF) | unsloth | 205 | 22,586 | Community-optimized quantization of GLM-5.2; infrastructure for efficient alignment research and RLHF deployment. |
| [**bytkim/Qwen3.6-27B-MTP-pi-tune-GGUF**](https://huggingface.co/bytkim/Qwen3.6-27B-MTP-pi-tune-GGUF) | bytkim | 97 | 20,465 | Multi-token prediction with "pi-tune" method; novel post-training objective for reducing exposure bias in reasoning. |

### 👁️ Hallucination Mitigation

| Model | Author | Likes | Downloads | Relevance |
|-------|--------|-------|-----------|-----------|
| [**nvidia/LocateAnything-3B**](https://huggingface.co/nvidia/LocateAnything-3B) | nvidia | 2,216 | 235,606 | Visual grounding explicitly trains against spatial hallucination; strong baseline for object hallucination benchmarks. |
| [**Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF**](https://huggingface.co/Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF) | Jackrong | 269 | 168,502 | MTP training reduces token-level prediction error; hypothesized to decrease structural hallucination in code/math generation. |

### 🏗️ Research Infrastructure

| Model | Author | Likes | Downloads | Relevance |
|-------|--------|-------|-----------|-----------|
| [**unsloth/Kimi-K2.7-Code-GGUF**](https://huggingface.co/unsloth/Kimi-K2.7-Code-GGUF) | unsloth | 146 | 37,260 | Compressed-tensors + GGUF conversion; infrastructure for efficient evaluation of long-context vision models. |
| [**LiquidAI/LFM2.5-Embedding-350M**](https://huggingface.co/LiquidAI/LFM2.5-Embedding-350M) | LiquidAI | 81 | 6,128 | Liquid neural network embeddings; alternative architecture for studying context-dependent representation stability. |
| [**zai-org/SCAIL-2**](https://huggingface.co/zai-org/SCAIL-2) | zai-org | 241 | 0 | Character animation video model; relevant for temporal consistency and cross-frame hallucination research. |

---

## 3. Research Ecosystem Signal

**Qwen and Gemma families are consolidating as dominant open-weight backbones** for multimodal and reasoning research, with Qwen3.5/3.6 variants appearing in 10+ models versus Gemma-4's unified architecture push. The **MoE paradigm is now default** for large models (GLM-5.2, DeepSeek-V4-Pro, Rio-3.5, Cohere North), suggesting efficiency-aware scaling is the central research challenge. **Vision-language integration is maturing beyond simple captioning**: Kimi-K2.7-Code and MiniMax-M3 emphasize code-grounded visual reasoning, while LocateAnything-3B targets spatial precision—both directly address hallucination in structured outputs critical for HMER.

Post-training activity reveals **aggressive stacking of specialized datasets** (Fable5, Composer2.5, tau2 scaling) and **uncensored fine-tuning as a natural experiment** in alignment removal—HauhauCS and DavidAU models collectively exceed 4.4M downloads, indicating substantial demand for studying safety-performance trade-offs. The **GGUF ecosystem** (unsloth, llama.cpp community) has matured into a genuine research infrastructure, enabling efficient hallucination and reasoning studies on consumer hardware. Notably, **explicit document/OCR models remain underrepresented**: only `datalab-to/lift` targets PDF understanding directly, suggesting a persistent gap between general VLMs and specialized document intelligence—precisely where HMER and formula recognition research must intervene.

---

## 4. Worth Exploring

| Model | Priority | Research Rationale |
|-------|----------|-------------------|
| [**datalab-to/lift**](https://huggingface.co/datalab-to/lift) | **High** | Sole explicit PDF/document model in trending list; critical for establishing whether general VLMs (Qwen/Gemma) have subsumed specialized OCR or whether architecture-specific document understanding remains necessary. Evaluate against HMER benchmarks to test formula recognition boundaries. |
| [**nvidia/LocateAnything-3B**](https://huggingface.co/nvidia/LocateAnything-3B) | **High** | 2,216 likes with explicit visual grounding objective; ideal for studying whether spatial calibration techniques transfer to reducing hallucination in mathematical diagram understanding. Compact size enables controlled ablation studies. |
| [**zai-org/GLM-5.2**](https://huggingface.co/zai-org/GLM-5.2) | **Medium-High** | DSA (Dynamic Sparse Attention) architecture is a genuine architectural alternative to standard transformers for long-context; compare against Qwen/Gemma families on document-length reasoning tasks to assess efficiency-reasoning trade-offs. FP8 variant available for memory-constrained evaluation. |

---

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*