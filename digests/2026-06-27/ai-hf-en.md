# Hugging Face Trending Models Digest 2026-06-27

> Source: [Hugging Face Hub](https://huggingface.co/) | 30 models | Generated: 2026-06-27 00:33 UTC

---

# Hugging Face Research Models Digest — June 27, 2026

## 1. Today's Highlights

Baidu's **Unlimited-OCR** leads document understanding innovation with 134K downloads, signaling strong demand for open-weight OCR systems that handle unconstrained text recognition scenarios. NVIDIA's **LocateAnything-3B** and **Qwen3.6-35B-A3B-NVFP4** demonstrate the industry's push toward efficient multimodal architectures with optimized inference formats. The emergence of **Ornith-1.0** (397B parameter variant) and **GLM-5.2** with MoE-DSA architectures indicates sustained investment in scaling reasoning capabilities while maintaining deployment efficiency. Notably, **MiniMax-M3** and fine-tuned variants like **Gemma-4-12B-agentic-fable5** reflect vigorous community activity in post-training alignment for specialized multimodal and agentic applications. The prevalence of GGUF/quantized releases (8 of 30 models) underscores researchers' prioritization of accessible, deployable long-context and reasoning models.

---

## 2. Trending Models by Research Relevance

### 📄 OCR & Document Models

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| [**baidu/Unlimited-OCR**](https://huggingface.co/baidu/Unlimited-OCR) | baidu | 1,040 | 134,146 | General-purpose OCR with "unlimited" scope, trending for open-weight document understanding without domain constraints—directly relevant to HMER and unconstrained text recognition research. |
| [**datalab-to/lift**](https://huggingface.co/datalab-to/lift) | datalab-to | 158 | 6,054 | PDF-focused image-text-to-text model built on Qwen3.5, trending for structured document extraction and layout-aware reasoning tasks. |

### 🎭 Multimodal & Vision-Language

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| [**nvidia/LocateAnything-3B**](https://huggingface.co/nvidia/LocateAnything-3B) | nvidia | 2,383 | 494,756 | Visual grounding model with image-feature-extraction pipeline, trending for precise spatial reasoning in VLM architectures—highly relevant to reducing object hallucination in multimodal systems. |
| [**MiniMaxAI/MiniMax-M3**](https://huggingface.co/MiniMaxAI/MiniMax-M3) | MiniMaxAI | 1,246 | 169,951 | Native multimodal model (MiniMax-M3-VL) with strong adoption, trending as a competitive open-weight alternative to proprietary VLMs for cross-modal research. |
| [**empero-ai/Qwythos-9B-Claude-Mythos-5-1M**](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M) | empero-ai | 446 | 20,346 | Vision-enabled Qwen3.5 derivative with 1M context, trending for long-context multimodal reasoning experiments. |
| [**Jackrong/Qwopus3.6-27B-Coder-Compat-MTP-GGUF**](https://huggingface.co/Jackrong/Qwopus3.6-27B-Coder-Compat-MTP-GGUF) | Jackrong | 93 | 35,027 | Multi-token prediction (MTP) vision-language model, trending for efficient multimodal code generation and speculative decoding research. |
| [**HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced**](https://huggingface.co/HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced) | HauhauCS | 91 | 23,772 | Quantization-aware trained (QAT) Gemma-4 with vision, trending for studying multimodal model calibration and efficient deployment. |
| [**huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated**](https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated) | huihui-ai | 135 | 5,445 | Abliterated (refusal-removed) vision-language coder, trending for studying alignment trade-offs in multimodal systems. |
| [**deepreinforce-ai/Ornith-1.0-9B**](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B) / [**-35B**](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B) / [**-397B**](https://huggingface.co/deepreinforce-ai/Ornith-1.0-397B) | deepreinforce-ai | 112-121 | 218-1,005 | Qwen3.5-based multimodal family with extreme scale variation (9B to 397B), trending for scaling law research in vision-language architectures. |

### 🧠 Long-Context & Reasoning Models

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| [**zai-org/GLM-5.2**](https://huggingface.co/zai-org/GLM-5.2) | zai-org | 2,589 | 83,589 | GLM-MoE-DSA architecture with sparse attention, trending for efficient long-context processing and reasoning—directly relevant to context scaling research. |
| [**empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF**](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF) | empero-ai | 583 | 486,810 | Quantized 1M-context reasoning model with high download volume, trending for accessible long-context experimentation. |
| [**WeiboAI/VibeThinker-3B**](https://huggingface.co/WeiboAI/VibeThinker-3B) | WeiboAI | 731 | 54,638 | Compact math-specialized Qwen2 model, trending for efficient reasoning distillation and STEM task evaluation. |
| [**yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF**](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF) | yuxinlu1 | 2,398 | 516,333 | Heavily downloaded coding-reasoning hybrid, trending for agentic coding with extended reasoning chains. |
| [**yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF**](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF) | yuxinlu1 | 684 | 186,663 | "Tau2" temperature-scaled agentic variant, trending for controllable reasoning generation and tool-use research. |
| [**LiquidAI/LFM2.5-230M**](https://huggingface.co/LiquidAI/LFM2.5-230M) | LiquidAI | 112 | 8,286 | Ultra-efficient liquid foundation model, trending for memory-efficient long-context and continuous-time reasoning research. |
| [**microsoft/FastContext-1.0-4B-SFT**](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT) | microsoft | 355 | 5,735 | Microsoft SFT-tuned fast context model, trending for supervised fine-tuning approaches to context efficiency. |

### 🔧 Post-Training & Alignment

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| [**HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive**](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive) | HauhauCS | 2,263 | 3,453,492 | Most-downloaded model in digest; "aggressive" uncensored MoE with vision, trending for studying extreme alignment removal and its multimodal implications. |
| [**Qwen/Qwen-AgentWorld-35B-A3B**](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B) | Qwen | 320 | 13,186 | Official Qwen agent-tuned MoE, trending for legitimate multi-agent alignment and tool-use preference optimization research. |
| [**Chunjiang-Intelligence/DeepSeek-v4-Fable**](https://huggingface.co/Chunjiang-Intelligence/DeepSeek-v4-Fable) | Chunjiang-Intelligence | 107 | 1,103 | Cybersecurity-focused DeepSeek-v4 variant, trending for domain-specific alignment and safety evaluation in specialized contexts. |

### 👁️ Hallucination Mitigation

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| [**nvidia/LocateAnything-3B**](https://huggingface.co/nvidia/LocateAnything-3B) | nvidia | 2,383 | 494,756 | Visual grounding with explicit localization, trending as an architectural approach to reducing spatial and object hallucinations in VLMs. |
| [**nvidia/nemotron-3.5-asr-streaming-0.6b**](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) | nvidia | 707 | 56,434 | Streaming ASR with Nemotron backbone, relevant to temporal hallucination mitigation in audio-text alignment. |

### 🏗️ Research Infrastructure

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| [**unsloth/GLM-5.2-GGUF**](https://huggingface.co/unsloth/GLM-5.2-GGUF) | unsloth | 410 | 107,553 | Community-optimized quantization of GLM-5.2, trending for efficient inference research and reproducible long-context evaluation. |
| [**nvidia/Qwen3.6-35B-A3B-NVFP4**](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4) | nvidia | 361 | 4,812,629 | NVIDIA's NVFP4-optimized MoE with highest downloads, trending for hardware-software co-design in efficient model serving. |
| [**nvidia/GLM-5.2-NVFP4**](https://huggingface.co/nvidia/GLM-5.2-NVFP4) | nvidia | 87 | 441 | NVIDIA's GLM-5.2 ModelOpt variant, trending for studying compression-aware evaluation of reasoning architectures. |

---

## 3. Research Ecosystem Signal

The Qwen family (3.5/3.6) has emerged as the dominant substrate for research derivatives, with 8+ fine-tuned/quantized variants in this digest alone—indicating a mature, accessible base for OCR, multimodal, and alignment experiments. NVIDIA's aggressive optimization pipeline (NVFP4, LocateAnything) signals proprietary hardware-software integration becoming a key differentiator in efficient vision-language deployment. The contrast between official releases (Qwen-AgentWorld, MiniMax-M3) and "uncensored" community forks (HauhauCS variants) reveals a bifurcated alignment research landscape: legitimate preference tuning versus adversarial safety evaluation. Notably, document understanding remains underrepresented beyond Unlimited-OCR and lift, suggesting an opportunity for specialized HMER and layout-analysis models. The Gemma-4 ecosystem's coding-focused fine-tunes (yuxinlu1, huihui-ai) demonstrates strong community investment in agentic reasoning, though mathematical/scientific OCR variants remain scarce. Long-context research is increasingly democratized through GGUF quantization, but native context extension architectures (GLM-5.2's DSA, Liquid's LFM) represent the frontier for efficient scaling.

---

## 4. Worth Exploring

**[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** — Essential for hallucination mitigation researchers: its explicit visual grounding architecture provides a controlled testbed for studying how spatial localization mechanisms reduce object hallucination in VLMs. The 494K downloads indicate robust community validation for reproducible experiments.

**[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** — Critical for HMER and document understanding researchers: as a leading open-weight "unlimited" scope OCR system, it offers a baseline for comparing constrained vs. unconstrained text recognition, with particular relevance to formula recognition and degenerate document analysis where commercial systems fail.

**[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)** — Foundational for long-context researchers: the MoE-DSA (sparse attention) architecture represents a distinct approach to context scaling from pure transformer extensions, enabling ablation studies between sparse and dense attention mechanisms for reasoning tasks. Pair with [unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF) for efficient evaluation pipelines.

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*