# Hugging Face Trending Models Digest 2026-06-30

> Source: [Hugging Face Hub](https://huggingface.co/) | 30 models | Generated: 2026-06-30 00:33 UTC

---

# Hugging Face Research Models Digest — 2026-06-30

## 1. Today's Highlights

This week's trending releases are dominated by **Qwen3.5/3.6 and GLM-5.2 MoE variants**, reflecting strong momentum in open-weight multimodal reasoning and long-context modeling. **baidu/Unlimited-OCR** stands out as the only explicitly OCR-focused model in the top tier, signaling continued commercial and research interest in unified document understanding. **NVIDIA's LocateAnything-3B** and **NVFP4-optimized Qwen/GLM checkpoints** highlight a growing infrastructure trend: vision-language and reasoning models being packaged with efficient deployment formats for edge and interactive applications. Meanwhile, the proliferation of **"Uncensored" and "Fable" fine-tunes** (HauhauCS, Chunjiang-Intelligence, yuxinlu1) underscores active post-training alignment experimentation, though often with reduced safety emphasis. For hallucination research, the absence of explicitly fact-grounded or calibration-focused releases is notable—most mitigation work appears embedded in base model training rather than standalone artifacts.

---

## 2. Trending Models by Research Relevance

### 📄 OCR & Document Models

| Model | Author | Likes | Downloads | Why It Matters |
|-------|--------|-------|-----------|----------------|
| [baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR) | baidu | 1,368 | 362,945 | A high-download Baidu OCR model for image-text-to-text tasks, directly relevant to document understanding, layout parsing, and formula/HMER recognition pipelines. |

---

### 🎭 Multimodal & Vision-Language

| Model | Author | Likes | Downloads | Why It Matters |
|-------|--------|-------|-----------|----------------|
| [empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF) | empero-ai | 943 | 907,682 | A heavily downloaded quantized Qwen3.5-based multimodal model with 1M context, relevant to vision-language reasoning and long-context image-text understanding. |
| [empero-ai/Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M) | empero-ai | 558 | 79,540 | The full-precision counterpart, useful for studying multimodal long-context behavior and post-training transfer effects. |
| [deepreinforce-ai/Ornith-1.0-9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B) | deepreinforce-ai | 274 | 19,170 | A Qwen3.5-based image-text-to-text model, relevant for analyzing open-weight multimodal architectures and their reasoning-grounding tradeoffs. |
| [deepreinforce-ai/Ornith-1.0-35B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B) | deepreinforce-ai | 239 | 38,857 | Larger MoE-based multimodal variant, useful for scaling studies in vision-language reasoning. |
| [deepreinforce-ai/Ornith-1.0-397B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-397B) | deepreinforce-ai | 166 | 1,622 | A very large open-weight multimodal MoE, relevant for frontier-scale multimodal reasoning and hallucination benchmarking. |
| [HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced](https://huggingface.co/HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced) | HauhauCS | 107 | 46,053 | A QAT-quantized Gemma4 vision model, relevant for efficient multimodal deployment and post-training alignment analysis. |
| [nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B) | nvidia | 2,481 | 728,320 | A high-traction NVIDIA vision-language model for localization and grounding, directly relevant to reducing spatial/visual hallucinations. |

---

### 🧠 Long-Context & Reasoning Models

| Model | Author | Likes | Downloads | Why It Matters |
|-------|--------|-------|-----------|----------------|
| [zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2) | zai-org | 2,934 | 133,350 | The top-liked release this week, a MoE+DSA text-generation model, relevant to long-context and reasoning architecture research. |
| [Qwen/Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B) | Qwen | 435 | 26,223 | A Qwen3.5 MoE positioned as a world model for agents, relevant to long-horizon reasoning and interactive multimodal agents. |
| [yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF) | yuxinlu1 | 2,501 | 561,577 | A popular coding/reasoning fine-tune of Gemma-4, useful for studying reasoning transfer and code-grounded hallucination. |
| [yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF) | yuxinlu1 | 843 | 241,409 | An agentic reasoning variant, relevant to tool-use reasoning and long-context agent planning. |
| [WeiboAI/VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B) | WeiboAI | 749 | 63,449 | A compact Qwen2-based math/reasoning model, relevant to efficient reasoning and small-model hallucination studies. |
| [deepseek-ai/DeepSeek-V4-Pro-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark) | deepseek-ai | 211 | 5,460 | DeepSeek's latest Pro reasoning model, relevant for comparing proprietary-scale reasoning with open-weight alternatives. |
| [deepseek-ai/DeepSeek-V4-Flash-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-DSpark) | deepseek-ai | 95 | 2,239 | A faster DeepSeek-V4 variant, useful for latency-sensitive reasoning and inference-time scaling research. |
| [Chunjiang-Intelligence/DeepSeek-v4-Fable](https://huggingface.co/Chunjiang-Intelligence/DeepSeek-v4-Fable) | Chunjiang-Intelligence | 130 | 1,463 | A fine-tuned DeepSeek-V4 variant, relevant for studying post-training specialization and its effect on reasoning fidelity. |
| [LiquidAI/LFM2.5-230M](https://huggingface.co/LiquidAI/LFM2.5-230M) | LiquidAI | 151 | 15,463 | A small liquid foundation model, relevant to efficient sequence modeling and alternative long-context architectures. |

---

### 🔧 Post-Training & Alignment

| Model | Author | Likes | Downloads | Why It Matters |
|-------|--------|-------|-----------|----------------|
| [HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive) | HauhauCS | 2,332 | 3,089,944 | The most-downloaded model this period, an aggressively uncensored Qwen3.6 MoE fine-tune, relevant for studying alignment removal and safety-reward tradeoffs. |
| [HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced](https://huggingface.co/HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced) | HauhauCS | 107 | 46,053 | A "balanced" uncensored Gemma4 vision model, useful for comparing alignment-preserving vs. alignment-removing post-training strategies. |
| [yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF) | yuxinlu1 | 2,501 | 561,577 | A "Fable"-style coding fine-tune, relevant to domain-specific SFT and its impact on reasoning and truthfulness. |
| [Chunjiang-Intelligence/DeepSeek-v4-Fable](https://huggingface.co/Chunjiang-Intelligence/DeepSeek-v4-Fable) | Chunjiang-Intelligence | 130 | 1,463 | A cybersecurity-tuned DeepSeek-V4, relevant to specialized post-training and potential capability elicitation. |

---

### 👁️ Hallucination Mitigation

| Model | Author | Likes | Downloads | Why It Matters |
|-------|--------|-------|-----------|----------------|
| [nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B) | nvidia | 2,481 | 728,320 | Strong visual grounding capabilities make it relevant for mitigating object/spatial hallucinations in VLMs. |
| [baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR) | baidu | 1,368 | 362,945 | Document-grounded OCR output can serve as a retrieval basis for reducing hallucination in document QA pipelines. |

---

### 🏗️ Research Infrastructure

| Model | Author | Likes | Downloads | Why It Matters |
|-------|--------|-------|-----------|----------------|
| [unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF) | unsloth | 464 | 164,180 | Unsloth's quantized GLM-5.2, relevant for efficient inference research and reproducible long-context evaluation. |
| [nvidia/GLM-5.2-NVFP4](https://huggingface.co/nvidia/GLM-5.2-NVFP4) | nvidia | 169 | 81,944 | NVIDIA's 4-bit floating-point optimized GLM-5.2, relevant to model compression and deployment of large reasoning models. |
| [nvidia/Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4) | nvidia | 378 | 5,392,518 | The highest-downloaded infrastructure release, an NVFP4-optimized Qwen MoE, relevant to efficient serving of multimodal reasoning models. |
| [unsloth/Qwen-AgentWorld-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen-AgentWorld-35B-A3B-GGUF) | unsloth | 113 | 116,693 | A GGUF release of Qwen's agent-world model, useful for local reproducibility and agent benchmarking. |
| [nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) | nvidia | 742 | 76,154 | A streaming ASR model, relevant to multimodal speech-text pipelines and real-time document/audio understanding. |

---

## 3. Research Ecosystem Signal

The ecosystem this week is defined by three converging trends. First, **Qwen and GLM model families are consolidating dominance** in open-weight multimodal reasoning, with multiple fine-tune communities (empero-ai, deepreinforce-ai, HauhauCS, yuxinlu1) building derivative variants on top of Qwen3.5/3.6 and GLM-5.2 MoE backbones. Second, **efficient deployment formats are becoming first-class research artifacts**: NVFP4 and GGUF releases from NVIDIA and Unsloth are among the highest-downloaded models, suggesting that compression and inference efficiency are now central to research reproducibility rather than afterthoughts. Third, **post-training alignment is being actively contested**—the popularity of "Uncensored" and "Fable" fine-tunes indicates a large experimental community probing the boundaries of safety tuning, though this comes at the cost of reduced focus on explicit hallucination mitigation. For OCR and document understanding, **baidu/Unlimited-OCR remains a singular commercial-grade open release**, while NVIDIA's LocateAnything-3B points to visual grounding as the most promising near-term lever for reducing multimodal hallucinations.

---

## 4. Worth Exploring

1. **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** — With 728K downloads and strong community traction, this is the most promising open model for researchers studying visual grounding and spatial hallucination mitigation. Its localization capabilities can serve as a benchmark or component for grounded VLM pipelines.

2. **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** — As the only top-tier OCR-specific model, it is essential for document understanding, HMER, and retrieval-augmented document QA research. Its high download count suggests robust production readiness worth dissecting.

3. **[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)** — The most-liked new release, this MoE+DSA text-generation model is a strong candidate for long-context reasoning benchmarks and architecture studies, particularly when compared against Qwen3.5/3.6 and DeepSeek-V4 families.

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*