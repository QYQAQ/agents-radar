# Hugging Face Trending Models Digest 2026-06-13

> Source: [Hugging Face Hub](https://huggingface.co/) | 30 models | Generated: 2026-06-13 00:38 UTC

---

# Hugging Face Research Models Digest — 2026-06-13

## 1. Today's Highlights

The most significant development this week is the emergence of **Google's Gemma 4 family** as a dominant open-weight any-to-any architecture, with the 12B and 26B variants showing substantial adoption across both research and fine-tuning communities—directly relevant to multimodal reasoning and post-training alignment studies. **DeepSeek-V4-Pro** leads all models with 4.8K likes and 3.4M downloads, signaling continued momentum for open-weight reasoning-optimized LLMs that support long-context inference. Notably, **NVIDIA's LocateAnything-3B** demonstrates strong vision-language localization capabilities with 149K downloads, while the proliferation of **abliterated/uncensored Gemma 4 derivatives** (e.g., HauhauCS's Qwen3.6 variant, huihui-ai's abliterated release) raises important research questions about post-training alignment robustness and safety filter circumvention. The absence of dedicated OCR/HMER models in this week's top-30 suggests either consolidation into general VLMs or underrepresentation of specialized document models in community engagement metrics.

---

## 2. Trending Models by Research Relevance

### 📄 OCR & Document Models
*No dedicated OCR/HMER models appear in this week's top-30 trending list. Document understanding capabilities appear increasingly subsumed into general multimodal architectures.*

### 🎭 Multimodal & Vision-Language

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google | 967 | 911,544 | Google's unified any-to-any architecture with native image-text-to-text capabilities; trending due to strong performance on visual reasoning benchmarks and open-weight accessibility for multimodal research. |
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google | 614 | 20,669 | Diffusion-based autoregressive vision-language model merging generative and discriminative capabilities; relevant for studying unified multimodal architectures that blur generation-understanding boundaries. |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 1,925 | 149,206 | Lightweight visual grounding model with precise localization; trending for efficient vision-language tasks and relevant to spatial reasoning and referring expression comprehension research. |
| **[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)** | MiniMaxAI | 252 | 442 | Compact multimodal model with competitive vision-language performance; worth monitoring for efficiency-multimodal tradeoff studies despite lower download traction. |
| **[ByteDance/Bernini-R](https://huggingface.co/ByteDance/Bernini-R)** | ByteDance | 229 | 373 | Image-text-to-video generation model with Apache 2.0 licensing; relevant for extending multimodal understanding into temporal/video reasoning domains. |
| **[unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)** | unsloth | 570 | 836,531 | Quantized deployment-optimized Gemma 4 variant; massive download volume indicates strong demand for accessible multimodal inference, relevant for edge deployment of VLMs. |

### 🧠 Long-Context & Reasoning Models

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 4,796 | 3,384,418 | Leading open-weight reasoning model with extended context and strong mathematical capabilities; dominant download volume confirms its position as primary research substrate for long-context and reasoning studies. |
| **[moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)** | moonshotai | 337 | 0 | Long-context code-specialized model from Moonshot AI; zero downloads suggest gated or preview status, but architecture relevant for studying code-specific reasoning with extended context windows. |
| **[CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)** | CohereLabs | 335 | 4,054 | MoE-based code generation model; relevant for studying mixture-of-experts efficiency in reasoning tasks and long-context code understanding. |
| **[XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash)** | XiaomiMiMo | 97 | 2,607 | Agent-optimized reasoning model with FP4 quantization; emerging research signal for agentic long-context execution with compressed representations. |

### 🔧 Post-Training & Alignment

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 1,722 | 2,393,894 | Aggressively uncensored MoE vision-language model with extraordinary download volume; critical research artifact for studying alignment failure modes and post-training safety filter robustness. |
| **[huihui-ai/Huihui-gemma-4-12B-it-abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-it-abliterated)** | huihui-ai | 147 | 8,013 | Abliterated (alignment-stripped) Gemma 4 variant; directly relevant to studying post-training alignment removal techniques and their effects on multimodal behavior. |
| **[OBLITERATUS/Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED)** | OBLITERATUS | 254 | 43,578 | Another alignment-removed Gemma 4 derivative; trending downloads indicate active community interest in "unaligned" base models for research or application. |

### 👁️ Hallucination Mitigation

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[google/gemma-4-12B](https://huggingface.co/google/gemma-4-12B)** | google | 527 | 198,271 | Base any-to-any model without instruction tuning; useful as controlled baseline for studying how post-training alignment affects hallucination rates in multimodal settings versus instruction-tuned variants. |
| **[google/gemma-4-12B-it-qat-q4_0-gguf](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf)** | google | 133 | 175,635 | Officially quantized aware trained (QAT) variant; quantization-aware training may preserve calibration properties relevant to confidence estimation and hallucination detection. |

### 🏗️ Research Infrastructure

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| **[unsloth/diffusiongemma-26B-A4B-it-GGUF](https://huggingface.co/unsloth/diffusiongemma-26B-A4B-it-GGUF)** | unsloth | 214 | 17,666 | Community-optimized quantization of DiffusionGemma; infrastructure for studying compressed multimodal diffusion architectures. |
| **[unsloth/gemma-4-12B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-12B-it-qat-GGUF)** | unsloth | 206 | 208,889 | Third-party QAT GGUF enabling accessible Gemma 4 research; high download volume supports broad reproducibility of multimodal alignment studies. |
| **[unsloth/gemma-4-26B-A4B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-qat-GGUF)** | unsloth | 148 | 221,174 | Larger variant infrastructure; enables scaling studies in quantized multimodal reasoning with strong community adoption. |

---

## 3. Research Ecosystem Signal

The current ecosystem reveals three dominant trends relevant to our research priorities. **First, the Google Gemma 4 family has achieved rapid ascendancy as the primary open-weight any-to-any architecture**, with both official releases and community derivatives (GGUF, abliterated, uncensored) proliferating across the top-30. This mirrors and extends the earlier Llama ecosystem pattern, but with native multimodal capabilities—suggesting that unified vision-language architectures are becoming the default research substrate, potentially marginalizing specialized OCR models unless they demonstrate clear superiority on document-specific benchmarks.

**Second, the alignment robustness problem is becoming empirically tractable** through the natural experiment of abliterated/uncensored derivatives. The extraordinary download volume of HauhauCS's uncensored Qwen3.6 (2.4M) versus official models indicates substantial demand for "unaligned" weights, creating both research opportunity and ethical urgency. For hallucination mitigation research, these models provide valuable negative controls—comparing their factuality against aligned variants could yield quantitative measures of alignment's epistemic benefits.

**Third, long-context reasoning remains concentrated in Chinese lab outputs** (DeepSeek, Moonshot/Kimi, MiniMax, Qwen derivatives) with Western contributions lagging in this specific dimension. DeepSeek-V4-Pro's dominance confirms that open-weight reasoning models have achieved mainstream research adoption, but the absence of explicit long-context document understanding models in the trending list suggests either capability consolidation or a measurement gap in how Hugging Face engagement captures specialized research use.

---

## 4. Worth Exploring

**[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** — This model merits immediate attention for OCR/HMER researchers because visual grounding precision directly enables structured document understanding: accurate localization of formula regions, table cells, and text blocks is prerequisite for downstream recognition. At 3B parameters with 149K downloads, it offers an efficient, well-adopted baseline for studying how spatial reasoning capabilities transfer to document layout analysis tasks, potentially complementing or replacing heavier general VLMs in resource-constrained document processing pipelines.

**[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** — With 3.4M downloads and the highest likes in the dataset, this is the dominant open substrate for long-context reasoning research. For our focus areas, it offers explicit value: (a) extended context enables full-document OCR+reasoning without chunking, (b) strong math performance suggests robust symbolic reasoning for formula understanding, and (c) its conversational format supports studying hallucination in reasoning chains. Comparative evaluation against Gemma 4 on document-heavy benchmarks would yield actionable insights into architecture-specific tradeoffs.

**[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** — The official instruction-tuned any-to-any model represents the most controlled environment for studying post-training alignment effects in multimodal settings. Its availability in base, instruction-tuned, and quantized variants (including official QAT and community GGUFs) enables systematic ablation studies: comparing hallucination rates, calibration quality, and document understanding accuracy across the alignment spectrum. The 911K downloads ensure reproducibility and community benchmark saturation, making it the reference point for 2026 multimodal research.

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*