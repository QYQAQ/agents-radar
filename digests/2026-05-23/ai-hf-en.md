# Hugging Face Trending Models Digest 2026-05-23

> Source: [Hugging Face Hub](https://huggingface.co/) | 30 models | Generated: 2026-05-22 16:02 UTC

---

# Hugging Face Trending Models Digest — May 23, 2026

---

## 1. Today's Highlights

The Hugging Face ecosystem is experiencing explosive momentum around **Qwen 3.6** and **DeepSeek-V4** model families, with Alibaba's Qwen3.6-35B-A3B MoE model crossing nearly 6 million downloads. Google's [gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it) dominates raw adoption with over 10 million downloads, signaling strong enterprise appetite for open-weight multimodal models. The community quantization scene remains vibrant through [unsloth](https://huggingface.co/unsloth)'s GGUF releases, while generative media sees breakthrough interest in [SulphurAI's text-to-video model](https://huggingface.co/SulphurAI/Sulphur-2-base) with 1.2M+ downloads. Notably, ByteDance's [Lance](https://huggingface.co/bytedance-research/Lance) represents a rare "any-to-any" architecture push, and [DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) has become the most liked model this week with 4,140 likes despite being a full proprietary-weight release.

---

## 2. Trending Models

### 🧠 Language Models (LLMs, chat models, instruction-tuned)

| Model | Author | Likes | Downloads | Why It's Trending |
|-------|--------|-------|-----------|-------------------|
| **[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 4,140 | 4,287,396 | Flagship reasoning model from DeepSeek's V4 family, dominating engagement with highest likes this week. |
| **[DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)** | deepseek-ai | 1,185 | 2,556,531 | Distilled fast variant balancing performance and inference speed for production deployments. |
| **[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)** | Qwen | 1,860 | 5,978,432 | Mixture-of-Experts multimodal LLM with exceptional download velocity; flagship of Alibaba's ecosystem. |
| **[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)** | Qwen | 1,385 | 4,049,995 | Dense variant of Qwen 3.6 series, proving strong demand for mid-scale capable open weights. |
| **[google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)** | google | 2,728 | 10,283,716 | Google's latest Gemma iteration leads absolute downloads, signaling broad enterprise and consumer adoption. |
| **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** | sapientinc | 235 | 72,470 | Specialized HR/people-analytics text model carving out vertical domain niche. |

### 🎨 Multimodal & Generation (image, video, audio, text-to-X)

| Model | Author | Likes | Downloads | Why It's Trending |
|-------|--------|-------|-----------|-------------------|
| **[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)** | SulphurAI | 1,260 | 1,249,582 | Breakout text-to-video model with massive download surge; community's current open video generation favorite. |
| **[bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance)** | bytedance-research | 620 | 1,001 | Ambitious any-to-any multimodal architecture from ByteDance research, early but conceptually significant. |
| **[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)** | openbmb | 899 | 221,612 | Efficient vision-language model with strong performance-per-parameter ratio for edge deployment. |
| **[HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)** | HiDream-ai | 421 | 22,783 | Hybrid image-text-to-image model leveraging Qwen3 VL for enhanced prompt adherence and editing. |
| **[circlestone-labs/Anima](https://huggingface.co/circlestone-labs/Anima)** | circlestone-labs | 1,489 | 602,483 | ComfyUI-native diffusion model with strong community traction for anime and stylized generation. |
| **[TencentARC/Pixal3D](https://huggingface.co/TencentARC/Pixal3D)** | TencentARC | 186 | 0 | Research-stage image-to-3D reconstruction with MIT license, positioned for generative 3D workflows. |
| **[SANA-WM_bidirectional](https://huggingface.co/Efficient-Large-Model/SANA-WM_bidirectional)** | Efficient-Large-Model | 78 | 0 | Bidirectional image-to-video with camera control, pushing controllable video generation boundaries. |
| **[Supertonic-3](https://huggingface.co/Supertone/supertonic-3)** | Supertone | 563 | 37,545 | Professional-grade Korean TTS from Supertone with ONNX optimization for production voice applications. |
| **[Dramabox](https://huggingface.co/ResembleAI/Dramabox)** | ResembleAI | 224 | 1,354 | Expressive voice cloning and dramatic TTS, targeting entertainment and gaming use cases. |
| **[scenema-audio](https://huggingface.co/ScenemaAI/scenema-audio)** | ScenemaAI | 119 | 441 | Diffusion-based text-to-audio with voice cloning, emerging contender in generative audio space. |

### 🔧 Specialized Models (code, math, medical, embeddings)

| Model | Author | Likes | Downloads | Why It's Trending |
|-------|--------|-------|-----------|-------------------|
| **[tencent/Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B)** | tencent | 264 | 564 | Compact Hunyuan translation specialist, part of Tencent's MT2 series for multilingual NLP. |
| **[tencent/Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B)** | tencent | 145 | 224 | Large MoE translation model; lower downloads suggest inference cost barriers for translation tasks. |
| **[NemoStation/Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)** | NemoStation | 242 | 4,002 | Video-text-to-text model built on Qwen3.5, enabling video understanding and captioning applications. |
| **[microsoft/Fara-7B](https://huggingface.co/microsoft/Fara-7B)** | microsoft | 594 | 15,399 | Microsoft multimodal model on Qwen2.5-VL backbone, likely research-oriented with strong academic interest. |
| **[numind/NuExtract3](https://huggingface.co/numind/NuExtract3)** | numind | 68 | 7,576 | Information extraction specialist with vision-language capabilities, practical for document AI pipelines. |
| **[Cactus-Compute/needle](https://huggingface.co/Cactus-Compute/needle)** | Cactus-Compute | 117 | 328 | JAX-based encoder-decoder with function calling and tool-use, exploring alternative frameworks to PyTorch. |
| **[internlm/Intern-S2-Preview](https://huggingface.co/internlm/Intern-S2-Preview)** | internlm | 93 | 2,294 | Preview of InternLM's S2 series, maintaining presence in competitive multimodal landscape. |

### 📦 Fine-tunes & Quantizations (community fine-tunes, GGUF, AWQ)

| Model | Author | Likes | Downloads | Why It's Trending |
|-------|--------|-------|-----------|-------------------|
| **[unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)** | unsloth | 402 | 532,255 | Unsloth's GGUF quantization with Multi-Token Prediction, enabling fast local inference of Qwen 3.6. |
| **[unsloth/Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)** | unsloth | 325 | 466,060 | MoE model GGUF conversion, pushing boundaries of runnable local models despite architectural complexity. |
| **[Jackrong/Qwopus3.5-9B-Coder-GGUF](https://huggingface.co/Jackrong/Qwopus3.5-9B-Coder-GGUF)** | Jackrong | 157 | 28,599 | Community code-specialized GGUF with TGI compatibility, filling niche for local coding assistants. |
| **[froggeric/Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)** | froggeric | 362 | 0 | MLX-optimized chat template fixes for Qwen 3.5, addressing Apple Silicon ecosystem needs despite zero downloads (recent upload). |
| **[CohereLabs/command-a-plus-05-2026-w4a4](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4)** | CohereLabs | 167 | 2,127 | INT4-quantized Cohere Command A with vision, experimental 4-bit weight compression for edge deployment. |
| **[CohereLabs/command-a-plus-05-2026-bf16](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16)** | CohereLabs | 102 | 11,950 | Full BF16 Cohere vision model, higher downloads showing preference for quality over extreme quantization. |

---

## 3. Ecosystem Signal

**Qwen and DeepSeek have cemented themselves as the dominant open-weight model families**, with Alibaba's Qwen3.6 series showing remarkable ecosystem breadth—spanning dense and MoE variants, official releases, and massive third-party quantization activity. Google's Gemma-4 leads in raw adoption volume, suggesting its enterprise-friendly licensing and integration with Google Cloud infrastructure drives production deployment. The quantization community, led by [unsloth](https://huggingface.co/unsloth), has matured significantly: GGUF releases now routinely achieve 500K+ downloads, with Multi-Token Prediction emerging as a key optimization technique for local inference. 

A notable tension exists between **open-weight accessibility and proprietary API competition**: DeepSeek's V4-Pro and Flash releases attract enormous engagement despite being "merely" weight releases rather than training-open models, while Cohere's quantized experiments suggest proprietary labs are testing how far compression can extend their reach. The "any-to-any" architecture of [Lance](https://huggingface.co/bytedance-research/Lance) and the camera-controllable video generation of [SANA-WM](https://huggingface.co/Efficient-Large-Model/SANA-WM_bidirectional) point toward **increasing modality fusion** as the next frontier, though practical adoption lags behind language-centric models. Community fine-tuning shows signs of specialization—coding, HR, chat templates—rather than generic instruction tuning, indicating market maturation.

---

## 4. Worth Exploring

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** — With 4,140 likes and 4.2M downloads, this is the week's clear engagement leader. Worth studying for its reasoning capabilities and as a benchmark for whether open-weight releases can sustain momentum against API-only competitors. The Pro/Flash dual release strategy offers natural A/B testing for latency-quality tradeoffs.

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)** — The breakout generative video model with 1.2M downloads from a relatively unknown lab. Its diffusers+GGUF compatibility and endpoint-ready tagging suggest production viability rare in open video generation. Critical to test whether quality matches download velocity, or if this represents speculative caching.

**[unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)** — Represents the state-of-the-art in consumer-accessible large models. The Multi-Token Prediction optimization and 532K downloads indicate this is becoming a default local inference target. Worth comparing against the MoE variant to understand whether dense or sparse architectures better serve quantized deployment.

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*