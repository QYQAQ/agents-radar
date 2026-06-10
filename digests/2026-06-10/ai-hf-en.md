# Hugging Face Trending Models Digest 2026-06-10

> Source: [Hugging Face Hub](https://huggingface.co/) | 30 models | Generated: 2026-06-10 00:36 UTC

---

# Hugging Face Research Models Digest — 2026-06-10

## 1. Today's Highlights

The most significant release for research is **PaddleOCR-VL-1.6**, which explicitly targets document understanding and OCR with vision-language architecture, directly relevant to HMER and layout-rich reasoning. Google's **Gemma 4** family continues its any-to-any rollout with native multimodal support and quantized GGUF variants, offering an open-weight testbed for long-context multimodal alignment. NVIDIA's **LocateAnything-3B** and **Cosmos3-Nano** signal strong momentum in spatially grounded vision models and omni-modal generation. On the reasoning side, **DeepSeek-V4-Pro** dominates engagement with 4.7K likes and 4.3M downloads, suggesting sustained interest in open-weight reasoning models. Finally, the presence of multiple aggressive fine-tunes (e.g., OBLITERATED, Uncensored HauhauCS) and thinking variants (Mellum2-12B-Thinking) underscores active community experimentation with post-training alignment and safety-hallucination tradeoffs.

---

## 2. Trending Models by Research Relevance

### 📄 OCR & Document Models

| Model | Author | Likes | Downloads | Why It Matters |
|-------|--------|-------|-----------|----------------|
| **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | PaddlePaddle | 280 | 10,139 | A vision-language OCR model built on ERNIE 4.5, trending for unified text recognition and document understanding—directly applicable to HMER, layout analysis, and multimodal document reasoning research. |

### 🎭 Multimodal & Vision-Language

| Model | Author | Likes | Downloads | Why It Matters |
|-------|--------|-------|-----------|----------------|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google | 810 | 581,354 | Native any-to-any multimodal model with strong adoption; useful for studying open-weight vision-language alignment, cross-modal transfer, and instruction tuning at 12B scale. |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 1,729 | 123,922 | Spatial grounding VLM with image-feature-extraction capabilities; highly relevant for referring expression comprehension, visual localization, and grounded multimodal reasoning. |
| **[stepfun-ai/Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)** | stepfun-ai | 358 | 46,729 | Efficient vision-language model from StepFun; worth studying for cost-accuracy tradeoffs in multimodal deployment and flash-attention style long-image reasoning. |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 1,593 | 2,983,909 | Heavily downloaded MoE vision-language fine-tune; signals community demand for studying alignment stripping, safety-hallucination boundaries, and post-training behavior in VLMs. |
| **[unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)** | unsloth | 531 | 660,140 | Quantized any-to-any Gemma 4 variant; enables accessible local research on multimodal efficiency, quantization effects on vision-language performance, and edge deployment. |
| **[google/gemma-4-12B](https://huggingface.co/google/gemma-4-12B)** | google | 479 | 122,464 | Base any-to-any Gemma 4 checkpoint; valuable as a pre-alignment baseline for studying multimodal pretraining and post-training intervention effects. |
| **[unsloth/gemma-4-12B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-12B-it-qat-GGUF)** | unsloth | 171 | 127,332 | QAT-quantized instruction-tuned Gemma 4; useful for research on quantization-aware training preserving multimodal reasoning quality. |
| **[OBLITERATUS/Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED)** | OBLITERATUS | 135 | 8,106 | Alignment-removed Gemma 4 VLM; relevant for studying hallucination, refusals, and the robustness of safety training in multimodal models. |
| **[nex-agi/Nex-N2-Pro](https://huggingface.co/nex-agi/Nex-N2-Pro)** | nex-agi | 160 | 783 | Qwen3.5 MoE-based image-text-to-text model; interesting for sparse multimodal architectures and efficient visual reasoning. |
| **[nex-agi/Nex-N2-mini](https://huggingface.co/nex-agi/Nex-N2-mini)** | nex-agi | 110 | 748 | Miniature variant of Nex-N2; useful for ablation studies on MoE routing and vision-language scaling laws. |
| **[unsloth/gemma-4-26B-A4B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-qat-GGUF)** | unsloth | 114 | 96,059 | Larger 26B-A4B MoE Gemma 4 quantized release; supports research on sparse multimodal model efficiency and long-context compression. |
| **[google/gemma-4-12B-it-qat-q4_0-gguf](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf)** | google | 114 | 63,049 | Official Google QAT q4_0 GGUF; important baseline for comparing official vs. community quantization of any-to-any models. |

### 🧠 Long-Context & Reasoning Models

| Model | Author | Likes | Downloads | Why It Matters |
|-------|--------|-------|-----------|----------------|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 4,740 | 4,302,553 | Dominant open-weight reasoning model; essential for long-context inference research, chain-of-thought evaluation, and reasoning alignment studies. |
| **[LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)** | LiquidAI | 572 | 137,138 | Liquid Foundation Model with MoE architecture; notable for recurrent-style long-context modeling and efficient reasoning at 8B scale. |
| **[JetBrains/Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)** | JetBrains | 272 | 17,571 | Explicit "thinking" variant of a code-focused MoE model; relevant for studying test-time compute, reasoning traces, and long-horizon code/math reasoning. |
| **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** | sapientinc | 733 | 133,351 | Compact 1B text model with strong uptake; potentially useful for probing whether small models can sustain long-context or structured reasoning through efficient architectures. |

### 🔧 Post-Training & Alignment

| Model | Author | Likes | Downloads | Why It Matters |
|-------|--------|-------|-----------|----------------|
| **[nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)** | nvidia | 174 | 56,864 | Massive 550B-A55B MoE from NVIDIA's Nemotron-H series; represents frontier-scale open-weight research on RLHF, synthetic data generation, and enterprise alignment. |
| **[nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4)** | nvidia | 152 | 71,818 | NVFP4-quantized Ultra variant; enables alignment and safety research on compressed frontier models with practical deployment constraints. |
| **[CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)** | CohereLabs | 155 | 1,784 | Cohere MoE code model; relevant for studying code-specific preference tuning, instruction following, and domain-specialized alignment. |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 1,593 | 2,983,909 | High-traffic uncensored fine-tune; serves as a real-world case study for alignment robustness, red-teaming, and the limits of post-training safety. |
| **[OBLITERATUS/Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED)** | OBLITERATUS | 135 | 8,106 | Alignment-removed Gemma 4; useful as a negative-control for evaluating how post-training interventions affect multimodal hallucination and truthfulness. |

### 👁️ Hallucination Mitigation

| Model | Author | Likes | Downloads | Why It Matters |
|-------|--------|-------|-----------|----------------|
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 1,729 | 123,922 | Spatially explicit grounding architecture naturally mitigates object hallucination by tying outputs to image locations; relevant for grounded generation evaluation. |
| **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | PaddlePaddle | 280 | 10,139 | Document-grounded OCR-VL design reduces transcription and structural hallucination in visually rich documents; applicable to fact-grounded document QA. |
| **[JetBrains/Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)** | JetBrains | 272 | 17,571 | Verbalized reasoning traces offer interpretability for hallucination detection and calibration in code generation tasks. |

### 🏗️ Research Infrastructure

| Model | Author | Likes | Downloads | Why It Matters |
|-------|--------|-------|-----------|----------------|
| **[unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)** / **[unsloth/gemma-4-12B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-12B-it-qat-GGUF)** / **[unsloth/gemma-4-26B-A4B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-qat-GGUF)** | unsloth | 531 / 171 / 114 | 660,140 / 127,332 / 96,059 | Unsloth's quantized Gemma 4 suite provides accessible infrastructure for reproducible research on efficient multimodal inference, quantization robustness, and long-context compression. |
| **[google/gemma-4-12B-it-qat-q4_0-gguf](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf)** | google | 114 | 63,049 | Official QAT release establishes a trusted baseline for comparing community and proprietary quantization pipelines of any-to-any models. |

---

## 3. Research Ecosystem Signal

Three interconnected trends stand out. First, **open-weight vision-language models are consolidating around unified any-to-any architectures**, with Google's Gemma 4 family and its ecosystem of official/community quantizations becoming a de facto platform for multimodal research. This mirrors earlier Llama-like dynamics but now extends to native image-text-audio modalities, lowering barriers for studies in cross-modal alignment and hallucination. Second, **OCR and document understanding are being absorbed into general VLMs rather than remaining siloed pipelines**—PaddleOCR-VL-1.6 exemplifies this convergence and offers a timely benchmark for HMER and layout-aware reasoning researchers. Third, **post-training alignment has become a contested, high-visibility research frontier**: the popularity of "uncensored" and "obliterated" fine-tunes indicates both community interest in alignment robustness and a need for better evaluation of safety-hallucination tradeoffs. NVIDIA's Nemotron-H Ultra releases, meanwhile, suggest that frontier-scale open-weight models will increasingly compete with proprietary systems on synthetic data generation and RLHF research, though access remains concentrated among well-resourced labs. The proliferation of QAT/GGUF variants also signals that **quantization-aware efficiency** is now a first-class research concern for multimodal and long-context models, not merely an engineering afterthought.

---

## 4. Worth Exploring

1. **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** — The only explicitly OCR-oriented model in this list and a rare open-weight document VLM built on a major foundation model (ERNIE 4.5). Researchers in HMER, table structure recognition, and visually grounded question answering should prioritize this for benchmarking against general VLMs. Its moderate size and PaddlePaddle ecosystem also make it suitable for fine-grained ablations on layout-aware pretraining.

2. **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** — A well-supported, natively multimodal any-to-any model with substantial download traction and an expanding quantization ecosystem. It is the most practical open testbed currently available for studying long-context multimodal reasoning, cross-modal alignment, and the effects of post-training interventions on hallucination in a unified architecture.

3. **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** — Strong engagement and a focused spatial-grounding design make this especially valuable for researchers investigating how explicit localization mechanisms reduce hallucination in VLMs. Its 3B scale permits efficient experimentation on referring expression, open-vocabulary detection, and grounded captioning tasks.

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*