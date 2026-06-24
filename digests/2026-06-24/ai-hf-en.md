# Hugging Face Trending Models Digest 2026-06-24

> Source: [Hugging Face Hub](https://huggingface.co/) | 30 models | Generated: 2026-06-24 00:29 UTC

---

# Hugging Face Research Models Digest — 2026-06-24

## 1. Today's Highlights

The multimodal and document understanding landscape is accelerating rapidly, with **baidu/Unlimited-OCR** emerging as a significant open-weight OCR entry from a major industry player, signaling growing investment in open document intelligence. **google/diffusiongemma-26B-A4B-it** and **google/gemma-4-12B-it** represent Google's push toward unified any-to-any architectures, directly relevant to cross-modal reasoning and hallucination mitigation through tighter vision-language grounding. **moonshotai/Kimi-K2.7-Code** continues the trend of coding-specialized multimodal models with compressed tensor optimizations, suggesting efficiency and capability need not trade off in long-context scenarios. Meanwhile, **deepseek-ai/DeepSeek-V4-Pro** dominates engagement metrics, indicating sustained appetite for frontier reasoning models with open weights. The proliferation of Qwen3.5/3.6-derived fine-tunes (e.g., **Qwythos-9B-Claude-Mythos-5-1M**, **Qwen3.6-27B-MTP-pi-tune**) reveals vibrant community experimentation with post-training alignment and reasoning elicitation.

---

## 2. Trending Models

### 📄 OCR & Document Models

| Model | Author | Likes | Downloads | Relevance |
|-------|--------|-------|-----------|-----------|
| **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** | baidu | 472 | 8,396 | Baidu's open-weight OCR model with image-feature-extraction capabilities; trending as a rare major-industry open document understanding release, directly relevant to HMER and layout analysis research needing reproducible baselines. |
| **[datalab-to/lift](https://huggingface.co/datalab-to/lift)** | datalab-to | 135 | 3,216 | Qwen3.5-based PDF-focused image-text-to-text model; trending for specialized document understanding with implicit structure recovery, relevant to OCR post-processing and multimodal document reasoning. |

### 🎭 Multimodal & Vision-Language

| Model | Author | Likes | Downloads | Relevance |
|-------|--------|-------|-----------|-----------|
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google | 1,055 | 948,996 | Diffusion-augmented Gemma variant for image-text-to-text; trending due to its massive download volume and novel diffusion-language hybrid architecture, highly relevant to cross-modal generation and hallucination mitigation through diffusion-based grounding. |
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google | 1,154 | 1,991,703 | Google's "any-to-any" unified multimodal model; trending as the highest-download model this period, representing a paradigm shift toward single-architecture universal multimodal interfaces with implications for OCR and visual reasoning integration. |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 2,156 | 3,955,016 | Vision-enabled MoE uncensored variant; exceptionally high downloads suggest strong demand for unfiltered multimodal reasoning, though the "uncensored" tag raises alignment research questions about trade-offs between capability elicitation and safety. |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 2,315 | 274,025 | NVIDIA's visual grounding model with image-feature-extraction; trending for precise spatial reasoning in images, directly relevant to reducing hallucination in visual localization and reference resolution tasks. |
| **[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)** | MiniMaxAI | 1,220 | 131,057 | MiniMax's multimodal model with proprietary `minimax_m3_vl` architecture; trending as an emerging Chinese lab's open vision-language contribution, worth monitoring for architectural innovations in cross-modal fusion. |
| **[moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)** | moonshotai | 975 | 447,920 | Kimi coding-specialized multimodal model with compressed-tensors; trending for efficient long-context code understanding with visual components, relevant to multimodal reasoning in structured document and formula contexts. |
| **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)** | empero-ai | 212 | 1,856 | Qwen3.5-based image-text-to-text model with "Claude-Mythos" fine-tuning; niche but relevant to studying how post-training on synthetic data affects multimodal reasoning and potential hallucination patterns. |
| **[lordx64/Qwable-v1](https://huggingface.co/lordx64/Qwable-v1)** | lordx64 | 172 | 4,547 | Qwen3.5 MoE vision-language model; community fine-tune trending for experimental multimodal MoE deployments, relevant to efficiency-accuracy tradeoffs in open vision-language research. |
| **[huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated)** | huihui-ai | 112 | 3,320 | Abliterated Gemma-4 coding/vision model; "abliterated" tag indicates removal of safety refusals, making it a relevant subject for studying alignment robustness and hallucination in "unlocked" multimodal systems. |

### 🧠 Long-Context & Reasoning Models

| Model | Author | Likes | Downloads | Relevance |
|-------|--------|-------|-----------|-----------|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 5,030 | 2,245,489 | DeepSeek's latest frontier reasoning model; dominant engagement reflects its position as the open-weight reasoning benchmark, highly relevant to long-context inference, chain-of-thought reliability, and competitive pressure on proprietary systems. |
| **[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)** | zai-org | 2,195 | 40,127 | Zhipu AI's GLM-5.2 with MoE and DSA (Dynamic Sparse Attention); trending for architectural innovations in efficient long-context processing, directly relevant to scaling context windows without quadratic cost. |
| **[unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)** | unsloth | 300 | 55,820 | Unsloth's quantized GLM-5.2; high download-to-like ratio indicates strong practical adoption for local long-context deployment, relevant to accessibility of long-context research. |
| **[zai-org/GLM-5.2-FP8](https://huggingface.co/zai-org/GLM-5.2-FP8)** | zai-org | 149 | 395,290 | FP8-quantized official GLM-5.2; massive downloads suggest FP8 is becoming standard for efficient long-context inference, relevant to precision-context tradeoff research. |
| **[yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)** | yuxinlu1 | 2,237 | 456,117 | Community GGUF of Gemma-4 coding variant; highest-liked community model, trending for accessible reasoning-enhanced coding with potential document/formula applications. |
| **[WeiboAI/VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)** | WeiboAI | 664 | 41,170 | Compact 3B math-reasoning model based on Qwen2; trending for efficient reasoning at small scale, relevant to distillation and whether reasoning patterns preserve across model sizes. |
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft | 321 | 4,391 | Microsoft's Qwen3-based "Explorer SubAgent" with explicit long-context optimization; explicitly named for fast context processing, directly relevant to efficient long-context architectures and subagent decomposition research. |
| **[bytkim/Qwen3.6-27B-MTP-pi-tune-GGUF](https://huggingface.co/bytkim/Qwen3.6-27B-MTP-pi-tune-GGUF)** | bytkim | 111 | 65,765 | Multi-token prediction (MTP) fine-tune with "pi-tune" optimization; niche but relevant to training efficiency and whether MTP improves long-horizon reasoning coherence. |
| **[poolside/Laguna-M.1](https://huggingface.co/poolside/Laguna-M.1)** | poolside | 93 | 2,787 | Poolside's vLLM/SGLang-compatible model; emerging coding model with inference-engine optimizations, relevant to reasoning throughput and context management. |

### 🔧 Post-Training & Alignment

| Model | Author | Likes | Downloads | Relevance |
|-------|--------|-------|-----------|-----------|
| **[yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)** | yuxinlu1 | 445 | 96,459 | "Agentic" variant with explicit terminal/tool-use optimization; trending for post-training specialization toward autonomous behavior, relevant to alignment of agentic systems and tool hallucination. |
| **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)** | empero-ai | 186 | 27,218 | Quantized version with "reasoning" tag; the "Claude-Mythos" naming suggests synthetic Claude-style reasoning distillation, relevant to studying transfer of reasoning patterns across model families. |

### 👁️ Hallucination Mitigation

| Model | Author | Likes | Downloads | Relevance |
|-------|--------|-------|-----------|-----------|
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 2,315 | 274,025 | Visual grounding model with explicit spatial localization; strongest direct relevance to hallucination mitigation through pixel-level grounding, reducing unverified generation in visual QA. |
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google | 1,055 | 948,996 | Diffusion-based generation with language integration; diffusion architectures inherently provide iterative refinement and uncertainty quantification, potentially reducing hallucination in multimodal generation. |

### 🏗️ Research Infrastructure

| Model | Author | Likes | Downloads | Relevance |
|-------|--------|-------|-----------|-----------|
| **[LiquidAI/LFM2.5-Embedding-350M](https://huggingface.co/LiquidAI/LFM2.5-Embedding-350M)** | LiquidAI | 114 | 10,117 | Liquid Foundation Model 2.5 embedding variant; trending for non-transformer architectures in representation learning, relevant to efficient document and multimodal retrieval. |
| **[LiquidAI/LFM2.5-ColBERT-350M](https://huggingface.co/LiquidAI/LFM2.5-ColBERT-350M)** | LiquidAI | 87 | 2,534 | Late-interaction ColBERT-style retriever; emerging infrastructure for precise document retrieval with token-level matching, relevant to RAG-based hallucination mitigation. |

---

## 3. Research Ecosystem Signal

**Model family momentum** is clearly concentrating around **Qwen3.5/3.6** and **Gemma-4** as the primary open bases for community innovation, with **GLM-5.2** representing a distinct Chinese-lab alternative with architectural differentiation (DSA, MoE). The Qwen ecosystem shows particularly vibrant fine-tuning activity for multimodal and reasoning applications, while Gemma-4's "any-to-any" unified architecture is spawning derivative works across coding, vision, and agentic domains.

**Open-weight vs. proprietary dynamics** are shifting: major players (Baidu, Google, NVIDIA, Microsoft) are increasingly releasing competitive open weights in OCR and vision-language, narrowing the gap with proprietary systems. However, the highest-engagement models (**DeepSeek-V4-Pro**, **HauhauCS uncensored Qwen**) suggest demand is bifurcating between "frontier-capable" and "frontier-unrestricted" open models, complicating alignment research.

**Post-training activity for document understanding** is nascent but growing: **Unlimited-OCR** and **lift** represent early specialized entries, while most document capability is currently embedded in generalist VLMs (Gemma-4, Kimi-K2.7-Code). **Hallucination mitigation** remains primarily addressed through grounding architectures (LocateAnything) rather than explicit training methods; the absence of dedicated "hallucination-mitigated" fine-tunes in this week's trends suggests the community still relies on base model improvements and RAG rather than targeted post-training. The prevalence of "abliterated" and "uncensored" tags indicates active experimentation with alignment removal, which paradoxically creates valuable testbeds for studying robustness of hallucination mitigation techniques.

---

## 4. Worth Exploring

**[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** — As a rare open-weight OCR release from a major industry lab, this offers a reproducible baseline for HMER and document understanding research that has been historically dominated by proprietary APIs or smaller academic models. Its explicit "image-feature-extraction" architecture suggests inspectable intermediate representations, enabling research into where OCR errors originate and how they propagate to downstream multimodal systems.

**[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** — This model represents the most direct investment in visual hallucination mitigation through explicit spatial grounding. At 3B parameters, it is tractable for academic research into whether pixel-level localization constraints improve downstream VLM reliability when used as a perception module. The NVIDIA authorship suggests high-quality training infrastructure and potential integration with broader CUDA ecosystem tools.

**[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** — The explicit "FastContext" naming and "Explorer SubAgent" tag indicate Microsoft's research investment in efficient long-context decomposition. At 4B parameters, this is highly accessible for studying whether subagent architectures preserve reasoning coherence across context windows, with direct relevance to long-document OCR pipelines where information must be aggregated across distant locations.

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*