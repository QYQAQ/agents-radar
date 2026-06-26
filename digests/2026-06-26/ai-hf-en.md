# Hugging Face Trending Models Digest 2026-06-26

> Source: [Hugging Face Hub](https://huggingface.co/) | 30 models | Generated: 2026-06-26 00:35 UTC

---

# Hugging Face Research Models Digest — 2026-06-26

## 1. Today's Highlights

The most significant release for OCR/HMER research is **baidu/Unlimited-OCR**, a purpose-built image-text-to-text model achieving 890 weekly likes and 70K+ downloads, suggesting strong demand for unified document understanding beyond legacy pipeline approaches. **moonshotai/Kimi-K2.7-Code** (992 likes, 502K downloads) represents a major vision-language advance with its compressed-tensor architecture and image-feature-extraction capabilities, relevant to multimodal reasoning and potential hallucination in code-grounded visual tasks. The **deepseek-ai/DeepSeek-V4-Pro** dominates overall engagement (5,061 likes, 1.88M downloads) with its conversational text-generation focus, though its implications for long-context reasoning warrant attention given DeepSeek's historical strength in extended context windows. Notably, **google/gemma-4-12B-it** debuts as an "any-to-any" unified model, signaling a trend toward modality-agnostic architectures that could reshape how we approach cross-modal hallucination mitigation. The proliferation of uncensored/abliterated variants (HauhauCS, huihui-ai) raises alignment research concerns about post-training safety degradation in widely downloaded models.

---

## 2. Trending Models by Research Relevance

### 📄 OCR & Document Models

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|------------------|
| **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** | baidu | 890 | 70,743 | End-to-end image-text-to-text OCR model trending as a potential successor to pipeline-based HMER systems, eliminating the traditional detection-recognition separation that compounds error propagation in mathematical formula recognition. |
| **[datalab-to/lift](https://huggingface.co/datalab-to/lift)** | datalab-to | 152 | 5,189 | Qwen3.5-based PDF-focused image-text-to-text model for document understanding, relevant to layout-aware OCR and structured document parsing research with limited but specialized uptake. |

### 🎭 Multimodal & Vision-Language

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|------------------|
| **[moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)** | moonshotai | 992 | 502,106 | Kimi K2.5-architecture vision-language model with compressed-tensor efficiency and image-feature-extraction, trending for code-grounded multimodal reasoning and potential study of compression effects on cross-modal alignment. |
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google | 1,176 | 2,187,644 | "Any-to-any" unified Gemma4 architecture representing a paradigm shift toward modality-agnostic VLMs, critical for studying unified vs. modular approaches to multimodal hallucination and reasoning transfer. |
| **[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)** | MiniMaxAI | 1,241 | 154,350 | Proprietary-family multimodal model (minimax_m3_vl) with strong engagement, offering a comparison point for open-weight multimodal architectures in vision-language reasoning benchmarks. |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 2,363 | 407,838 | NVIDIA's image-feature-extraction and grounding model, highly relevant for spatial reasoning in multimodal contexts and as a component for hallucination-reduced visual grounding systems. |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 2,234 | 3,520,206 | Most-downloaded model this period; uncensored Qwen3.6 MoE vision model represents a natural experiment in alignment-stripped multimodal behavior, useful for studying safety-hallucination tradeoffs at scale. |
| **[HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced](https://huggingface.co/HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced)** | HauhauCS | 83 | 15,128 | QAT-quantized uncensored Gemma4 vision variant, enabling study of quantization-robustness interactions with multimodal alignment in resource-constrained deployments. |
| **[Jackrong/Qwopus3.6-27B-Coder-Compat-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-Coder-Compat-MTP-GGUF)** | Jackrong | 90 | 19,382 | Multi-token prediction (MTP) vision-enabled Qwen coder with GGUF quantization, relevant for efficient multimodal code generation and speculative decoding research in visual programming contexts. |

### 🧠 Long-Context & Reasoning Models

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|------------------|
| **[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)** | zai-org | 2,476 | 67,107 | GLM MoE with DSA (Dynamic Sparse Attention) architecture, likely incorporating long-context innovations given GLM family history; top-liked model this week for potential next-generation context scaling. |
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 5,061 | 1,878,217 | DeepSeek V4 conversational architecture with established long-context heritage; highest absolute engagement, critical for benchmarking extended-context reasoning and retrieval-augmented generation performance. |
| **[yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)** | yuxinlu1 | 2,363 | 495,813 | Heavily fine-tuned Gemma4 coder with "fable5-composer2.5" composite training, trending for specialized reasoning with potential long-context code comprehension applications. |
| **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)** | empero-ai | 390 | 10,160 | Qwen3.5-based 1M context window model (implied by "1M" suffix), directly relevant to ultra-long-context reasoning research and efficient attention mechanisms at extreme sequence lengths. |
| **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)** | empero-ai | 476 | 134,294 | Quantized variant of the 1M-context Qwythos, enabling accessible long-context research on consumer hardware with significant download traction. |
| **[WeiboAI/VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)** | WeiboAI | 715 | 51,717 | Compact Qwen2-based math-specialized model, trending for efficient reasoning and potential study of capability scaling in small-parameter regimes for mathematical proof generation. |
| **[Chunjiang-Intelligence/DeepSeek-v4-Fable](https://huggingface.co/Chunjiang-Intelligence/DeepSeek-v4-Fable)** | Chunjiang-Intelligence | 90 | 646 | Cybersecurity-focused DeepSeek V4 variant, niche but relevant for studying domain-specific reasoning and potential security-hallucination interactions in specialized contexts. |

### 🔧 Post-Training & Alignment

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|------------------|
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT-SFT)** | microsoft | 345 | 5,276 | Explicitly SFT-tuned Qwen3 model with "Explorer SubAgent" architecture, representing Microsoft's supervised alignment approach for tool-use and agentic behavior with context-efficient design. |
| **[huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated)** | huihui-ai | 127 | 4,874 | "Abliterated" (alignment-removed) Gemma4 coder, trending as a case study for reverse-engineering post-training effects and studying base model vs. aligned behavior in code generation. |
| **[deepreinforce-ai/Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)** | deepreinforce-ai | 80 | 0 | Reinforcement learning-branded 35B model (name suggests ornithology/reinforcement connection), zero downloads but worth monitoring for explicit RLHF/DPO methodology disclosures. |

### 👁️ Hallucination Mitigation

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|------------------|
| **[nvidia/Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4)** | nvidia | 340 | 4,602,255 | Highest-download model this period; NVIDIA's NVFP4-optimized Qwen3.6 MoE with ModelOpt toolchain, enabling study of low-precision inference effects on calibration and confidence-based hallucination detection. |
| **[Qwen/Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)** | Qwen | 239 | 3,389 | Official Qwen3.5 MoE agent-world model, potentially incorporating tool-use grounding mechanisms relevant to factuality and retrieval-based hallucination reduction in agentic systems. |

### 🏗️ Research Infrastructure

| Model | Author | Likes | Downloads | Research Relevance |
|-------|--------|-------|-----------|------------------|
| **[unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)** | unsloth | 384 | 88,915 | Unsloth's optimized GGUF conversion of GLM-5.2, infrastructure-critical for efficient long-context and MoE research deployment with established quantization tooling. |
| **[nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)** | nvidia | 695 | 50,553 | Cache-aware streaming ASR with Nemotron 3.5 architecture, relevant to multimodal speech-text alignment and real-time hallucination in streaming transcription contexts. |

---

## 3. Research Ecosystem Signal

The Qwen family (3.5/3.6) has achieved dominant ecosystem centrality, serving as the base for OCR (datalab-to/lift), ultra-long-context (Qwythos-1M), vision-language (HauhauCS variants), and agentic grounding (Qwen-AgentWorld) applications—suggesting Qwen's architectural decisions have become a de facto standard for downstream research, similar to Llama's position in 2024. This concentration creates both efficiency (shared tooling, unified evaluation) and risk (systematic failure modes propagating across derivative models). The "uncensored" phenomenon deserves particular scrutiny: HauhauCS's aggressive alignment removal achieved 3.5M downloads, indicating substantial demand for unfiltered models that complicates safety research—researchers studying hallucination mitigation now face a bifurcated ecosystem where alignment-stripped variants may become the default deployment choice. Google's "any-to-any" Gemma4 architecture and Baidu's unified OCR represent converging trends toward modality collapse in model design, potentially obsoleting specialized HMER pipelines. Open-weight models are increasingly competitive with proprietary systems in multimodal reasoning (MiniMax-M3, Kimi-K2.7-Code), though NVIDIA's optimization dominance (NVFP4, LocateAnything) suggests hardware-software co-design remains a proprietary moat. The proliferation of composite fine-tuning recipes ("fable5-composer2.5") indicates maturation in post-training orchestration but limited transparency in exact methodological contributions.

---

## 4. Worth Exploring

**[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** — As the only purpose-built OCR model in this cohort with significant traction, it offers a rare opportunity to study whether end-to-end image-text-to-text architectures can finally surpass the detection-recognition pipeline paradigm that has dominated HMER since the 2010s. Its 70K+ downloads suggest sufficient community adoption for reproducible benchmarking against specialized models like Nougat or GOT-OCR2. Researchers should evaluate its performance on formula-heavy scientific documents to assess unified-architecture limitations in fine-grained symbol recognition.

**[moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)** — The compressed-tensor architecture (502K downloads) represents a significant efficiency innovation for multimodal deployment, but more critically for hallucination research, its code-grounded visual training creates a controlled setting to study whether structured reasoning domains (code) reduce cross-modal hallucination compared to open-ended captioning. The image-feature-extraction pipeline enables component-level analysis of where vision-language alignment fails.

**[empero-ai/Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)** — With explicit 1M context window claims and both full-precision and GGUF variants, this is the most accessible model for rigorous long-context research since Gemini's context-window claims. The 9B parameter scale enables experiments on consumer hardware, while the Claude-Mythos naming suggests distillation or synthetic data from Claude outputs—raising important questions about whether long-context capabilities transfer through distillation and how synthetic training data affects hallucination at extreme sequence lengths.

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*