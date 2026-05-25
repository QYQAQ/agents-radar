# Hugging Face Trending Models Digest 2026-05-25

> Source: [Hugging Face Hub](https://huggingface.co/) | 30 models | Generated: 2026-05-25 00:31 UTC

---

# Hugging Face Research Models Digest — 2026-05-25

---

## 1. Today's Highlights

The Qwen 3.6 family dominates this week's trending list, with [Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B) amassing 1.4M downloads, signaling strong researcher interest in open-weight multimodal reasoning. Notably, [openbmb/MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6) continues gaining traction for efficient vision-language document understanding—a critical capability for OCR and HMER research. The emergence of [HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive) with 1.2M downloads reveals intense community experimentation around post-training alignment removal, raising important questions about hallucination trade-offs in uncensored models. Meanwhile, [google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it) hitting 10.4M downloads suggests Google's latest vision-language iteration is becoming a default research backbone. The any-to-any architecture of [bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance) represents a notable architectural direction for unified multimodal generation and reasoning.

---

## 2. Trending Models by Research Relevance

### 📄 OCR & Document Models

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| [openbmb/MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6) | openbmb | 918 | 269,589 | Efficient edge VLM with strong document understanding capabilities, trending for OCR-intensive tasks and formula recognition research where latency matters. |
| [numind/NuExtract3](https://huggingface.co/numind/NuExtract3) | numind | 107 | 10,998 | Structured information extraction from visual documents, directly relevant to layout analysis and document parsing research pipelines. |

### 🎭 Multimodal & Vision-Language

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| [Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B) | Qwen | 1,422 | 4,242,555 | Flagship open-weight VLM with competitive multimodal reasoning; massive adoption signals it as a primary benchmark for cross-modal research. |
| [google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it) | google | 2,762 | 10,398,435 | Google's latest vision-language iteration with highest downloads this week; important for comparing proprietary-adjacent vs. fully open VLMs. |
| [CohereLabs/command-a-plus-05-2026-w4a4](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4) | CohereLabs | 190 | 5,627 | Quantized vision-language variant from Cohere, relevant for efficient deployment of multimodal systems with constrained resources. |
| [CohereLabs/command-a-plus-05-2026-bf16](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16) | CohereLabs | 113 | 12,362 | Full-precision counterpart; pair with w4a4 variant enables systematic study of quantization effects on multimodal hallucination. |
| [bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance) | bytedance-research | 760 | 1,474 | Any-to-any multimodal architecture supporting image and video generation; novel unified framework for studying cross-modal generation vs. understanding trade-offs. |
| [unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF) | unsloth | 455 | 660,321 | Multi-token prediction variant of Qwen3.6; MTP training may improve multimodal reasoning efficiency and coherence. |
| [Jackrong/Qwopus3.5-9B-Coder-GGUF](https://huggingface.co/Jackrong/Qwopus3.5-9B-Coder-GGUF) | Jackrong | 180 | 38,937 | Community-optimized code-vision model; relevant for multimodal code generation and technical document understanding. |
| [Jackrong/Qwopus3.6-27B-v2-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-GGUF) | Jackrong | 113 | 8,300 | Iterated community fine-tune; signals active ecosystem around Qwen-based vision-language customization. |
| [meituan-longcat/LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5) | meituan-longcat | 119 | 0 | Audio-image-text-to-video generation; relevant for studying temporal coherence and cross-modal conditioning in long-form video. |

### 🧠 Long-Context & Reasoning Models

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| [deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | deepseek-ai | 4,224 | 4,666,078 | Leading reasoning-specialized LLM with massive adoption; critical benchmark for long-context inference and chain-of-thought research. |
| [NemoStation/Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B) | NemoStation | 306 | 6,032 | Video-text-to-text with 2B parameters; designed for long-form video understanding and temporal reasoning tasks. |
| [unsloth/Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF) | unsloth | 358 | 547,827 | MoE architecture with multi-token prediction; sparse activation enables efficient scaling of context length and reasoning depth. |
| [sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B) | sapientinc | 271 | 84,346 | Specialized text generation model; HRM tag suggests potential relevance for structured reasoning in human-readable mathematics. |
| [Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF) | Jackrong | 87 | 33,197 | Coder-focused MTP variant; relevant for long-context code reasoning and technical documentation processing. |

### 🔧 Post-Training & Alignment

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| [HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive) | HauhauCS | 767 | 1,220,114 | Aggressively unaligned MoE VLM with massive download volume; natural experiment for studying alignment removal effects on hallucination and capability. |
| [OBLITERATUS/Qwen3.6-27B-OBLITERATED](https://huggingface.co/OBLITERATUS/Qwen3.6-27B-OBLITERATED) | OBLITERATUS | 76 | 5,298 | Second uncensored variant this week; naming trend suggests systematic community effort to probe base model behavior post-alignment. |
| [froggeric/Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates) | froggeric | 388 | 0 | Chat template corrections for Qwen ecosystem; infrastructure for reproducible post-training alignment experiments. |

### 👁️ Hallucination Mitigation

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| [google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it) | google | 2,762 | 10,398,435 | Instruction-tuned variant with Google's alignment stack; important baseline for comparing hallucination rates against uncensored community variants. |
| [Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B) | Qwen | 1,422 | 4,242,555 | Official aligned release; essential control for isolating effects of community uncensoring on multimodal hallucination. |
| [numind/NuExtract3](https://huggingface.co/numind/NuExtract3) | numind | 107 | 10,998 | Extraction-focused design with constrained outputs; architectural approach to reducing generative hallucination in document tasks. |

### 🏗️ Research Infrastructure

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|-------------------|
| [nvidia/Nemotron-Labs-Diffusion-14B](https://huggingface.co/nvidia/Nemotron-Labs-Diffusion-14B) | nvidia | 89 | 4,071 | Diffusion-based text generation from NVIDIA; novel architecture for studying non-autoregressive approaches to reducing reasoning hallucinations. |
| [Efficient-Large-Model/SANA-WM_bidirectional](https://huggingface.co/Efficient-Large-Model/SANA-WM_bidirectional) | Efficient-Large-Model | 98 | 0 | Bidirectional video diffusion with camera control; infrastructure for studying temporal consistency as hallucination mitigation in video generation. |
| [TencentARC/Pixal3D](https://huggingface.co/TencentARC/Pixal3D) | TencentARC | 202 | 0 | Image-to-3D reconstruction; relevant for evaluating geometric hallucination in multimodal generation pipelines. |

---

## 3. Research Ecosystem Signal

The Qwen ecosystem has achieved dominant mindshare in open multimodal research, with six variants in this week's trends spanning official releases, community fine-tunes, alignment removals, and quantization experiments. This concentration enables unprecedented natural experiments: researchers can now isolate the effects of specific post-training interventions—MTP training, MoE sparsity, GGUF quantization, and alignment removal—while holding base architecture constant. The parallel emergence of two aggressive uncensored variants ([HauhauCS](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive) and [OBLITERATUS](https://huggingface.co/OBLITERATUS/Qwen3.6-27B-OBLITERATED)) with combined 1.2M+ downloads signals a significant research interest in probing the robustness-accuracy-hallucination trade-off frontier. Google's [Gemma-4](https://huggingface.co/google/gemma-4-31B-it) maintaining 10M+ downloads alongside Qwen's rise suggests a healthy competitive dynamic between proprietary-adjacent and fully open weight releases. Notably absent from trends are specialized OCR/HMER models—document understanding capabilities appear increasingly subsumed into general VLMs like [MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6), raising questions about whether dedicated formula recognition architectures remain necessary or if in-context visual reasoning suffices. The any-to-any paradigm exemplified by [Lance](https://huggingface.co/bytedance-research/Lance) may further blur these boundaries.

---

## 4. Worth Exploring

**[openbmb/MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)** — With 269K downloads and efficient edge deployment, this is the most accessible platform for studying OCR and document understanding in resource-constrained settings. Its architecture likely incorporates innovations in visual encoder compression relevant to HMER latency-accuracy trade-offs. Researchers should evaluate formula recognition performance against larger VLMs to test the "generalist vs. specialist" hypothesis.

**[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** — The 1.2M downloads for this aggressively unaligned MoE VLM make it an essential probe for hallucination research. Systematic comparison against [Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B) on multimodal benchmarks could quantify alignment's cost in factual grounding versus its benefit in refusal behavior—critical for understanding whether hallucination mitigation and helpfulness are fundamentally in tension.

**[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** — As the highest-liked model (4,224) with 4.7M downloads, this reasoning-specialized release likely incorporates architectural innovations for long-context coherence. Its performance on extended mathematical reasoning chains provides a strong baseline for evaluating whether multimodal extensions (like Qwen's vision capabilities) introduce unique long-context failure modes distinct from text-only reasoning collapse.

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*