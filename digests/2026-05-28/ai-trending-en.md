# AI Open Source Trends 2026-05-28

> Sources: GitHub Trending + GitHub Search API | Generated: 2026-05-28 00:30 UTC

---

# AI Open Source Trends Report — Research-Focused Filter
**Date:** 2026-05-28 | **Analyst Focus:** Long-Context Reasoning, OCR/HMER, Multimodal Reasoning, Post-Training Alignment, Hallucination Mitigation

---

## 1. Today's Highlights

The most striking development is the explosive emergence of **"skill files" and agent harnesses** as a new paradigm for post-training behavioral alignment—projects like `stop-slop`, `taste-skill`, and `ECC` collectively garnered thousands of stars, signaling community demand for fine-grained control over LLM output quality without retraining. In OCR and document intelligence, **PaddleOCR** continues its dominance as a bridge between visual documents and LLMs, while **PageIndex** introduces vectorless reasoning-based RAG that could reshape how long-context systems process documents. The **Kronos** financial foundation model represents a notable expansion of domain-specific multimodal reasoning into structured time-series language. Meanwhile, **LlamaFactory**'s sustained prominence confirms efficient fine-tuning infrastructure remains critical as alignment techniques proliferate.

---

## 2. Top Projects by Category

### 📄 OCR & Document Intelligence

| Project | Stars | Why It Matters |
|--------|-------|--------------|
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | 78,717 total | Bridges images/PDFs to structured LLM-ready data with 100+ language support; essential pipeline component for multimodal document understanding |
| [PageIndex](https://github.com/VectifyAI/PageIndex) | 32,240 total | **Vectorless, reasoning-based RAG** — eliminates embedding storage bottlenecks, directly relevant to long-context document processing efficiency |
| [RAGFlow](https://github.com/infiniflow/ragflow) | 81,377 total | Fuses RAG with agent capabilities; its OCR + deep document understanding pipeline addresses hallucination-prone retrieval gaps |
| [LlamaIndex](https://github.com/run-llama/llama_index) | 49,706 total | Explicitly positions as "document agent and OCR platform"; advanced indexing for long-context ingestion |

### 🎭 Multimodal Reasoning

| Project | Stars | Why It Matters |
|--------|-------|--------------|
| [Kronos](https://github.com/shiyu-coder/Kronos) | 401 today | Foundation model for "language of financial markets" — domain-specific multimodal reasoning over structured numerical + textual time series |
| [Transformers](https://github.com/huggingface/transformers) | 160,994 total | Core infrastructure for VLM development; supports multimodal model training/inference pipelines |
| [LlamaFactory](https://github.com/hiyouga/LlamaFactory) | 71,657 total | Unified fine-tuning for 100+ LLMs & VLMs (ACL 2024); critical for multimodal alignment experiments |

### 🧠 Long-Context & Reasoning

| Project | Stars | Why It Matters |
|--------|-------|--------------|
| [PageIndex](https://github.com/VectifyAI/PageIndex) | 32,240 total | Vectorless reasoning-based indexing enables longer effective context by reducing retrieval noise and storage overhead |
| [claude-context](https://github.com/zilliztech/claude-context) | 11,604 total | Code search MCP making "entire codebase the context" — tackles context window limitations via intelligent compression |
| [mem0](https://github.com/mem0ai/mem0) | 56,905 total | Universal memory layer for agents; persistent context across sessions addresses long-context state management |
| [memvid](https://github.com/memvid/memvid) | 15,579 total | Serverless single-file memory layer; simplifies long-term memory for agent reasoning loops |

### 🔧 Post-Training & Alignment

| Project | Stars | Why It Matters |
|--------|-------|--------------|
| [stop-slop](https://github.com/hardikpandya/stop-slop) | 664 today | **Skill file for removing AI tells from prose** — lightweight behavioral alignment without model retraining |
| [taste-skill](https://github.com/Leonxlnx/taste-skill) | 2,715 today | Prevents "boring, generic slop" generation; emergent pattern of taste/preference injection via prompting infrastructure |
| [ECC](https://github.com/affaan-m/ECC) | 2,062 today (+196,003 topic:llm) | "Agent harness performance optimization" with skills, instincts, memory, security — comprehensive alignment framework |
| [LlamaFactory](https://github.com/hiyouga/LlamaFactory) | 71,657 total | Efficient fine-tuning hub supporting RLHF/DPO/SFT; practical alignment infrastructure |
| [OpenHands](https://github.com/OpenHands/OpenHands) | 75,067 total | AI-driven development with implicit alignment through human feedback loops in coding tasks |

### 👁️ Hallucination & Reliability

| Project | Stars | Why It Matters |
|--------|-------|--------------|
| [stop-slop](https://github.com/hardikpandya/stop-slop) | 664 today | Directly targets output quality degradation — hallucination-like "AI tells" in generated prose |
| [taste-skill](https://github.com/Leonxlnx/taste-skill) | 2,715 today | Generic/boring outputs correlate with mode collapse; taste injection as hallucination mitigation strategy |
| [RAGFlow](https://github.com/infiniflow/ragflow) | 81,377 total | "Deep document understanding" with traceable retrieval — grounding mechanism for factuality |
| [graphify](https://github.com/safishamsi/graphify) | 55,016 total | Queryable knowledge graphs from heterogeneous data; structured grounding against hallucination |

### 🏗️ Infrastructure (Training/Inference/Eval for Focus Areas)

| Project | Stars | Why It Matters |
|--------|-------|--------------|
| [vLLM](https://github.com/vllm-project/vllm) | 81,183 total | High-throughput inference engine; enables efficient serving of long-context and multimodal models |
| [OpenCompass](https://github.com/open-compass/opencompass) | 7,037 total | LLM evaluation platform with 100+ datasets; critical for benchmarking reasoning and alignment progress |
| [txtai](https://github.com/neuml/txtai) | 12,611 total | All-in-one framework for semantic search and LLM orchestration; supports multimodal workflows |
| [tiny-llm](https://github.com/skyzh/tiny-llm) | 4,211 total | Educational vLLM+Qwen implementation; demystifies inference optimization for researchers |

---

## 3. Research Trend Signal Analysis

Today's data reveals a **tectonic shift toward "skill-based alignment"** — lightweight, composable behavioral modifiers that operate above the base model layer. The viral success of `stop-slop`, `taste-skill`, and `ECC` (collectively ~5,400+ stars today) indicates researcher and practitioner frustration with generic model outputs, driving demand for **post-hoc preference injection** without costly retraining. This parallels academic interest in inference-time alignment and context steering, but manifests as practical, shareable artifacts rather than theoretical frameworks.

In OCR and document intelligence, **vectorless RAG** (`PageIndex`, 32K stars) signals emerging skepticism toward embedding-based retrieval for long documents, favoring reasoning-centric approaches that preserve linguistic structure. This aligns with recent advances in long-context transformers (e.g., Kimi-K2.5, GLM-5 mentioned in Ollama) where direct context processing reduces retrieval dependency. The sustained prominence of `PaddleOCR` and `LlamaIndex`'s explicit "document agent + OCR" rebranding confirms document understanding as a **bottleneck capability** for multimodal systems.

Notably absent from today's trending list are explicit **HMER (Handwritten Mathematical Expression Recognition)** projects and dedicated **vision-language model** repositories—suggesting either maturity consolidation (into PaddleOCR-like general tools) or underinvestment relative to agent infrastructure. The `Kronos` financial language model represents an interesting **domain-specific multimodal** direction, applying sequence reasoning to structured market data rather than generic visual QA.

The proliferation of **agent memory systems** (`mem0`, `memvid`, `claude-mem`) indicates long-context research is migrating from "bigger windows" to "smarter compression and recall" — a necessary evolution as context lengths plateau against attention costs.

---

## 4. Research Hot Spots

- **Skill-File Alignment Ecosystem** (`stop-slop`, `taste-skill`, `ECC`, `Anthropic-Cybersecurity-Skills`)
  - *Relevance:* Emergent infrastructure for behavioral alignment without gradient updates. Research opportunity: formalize these ad-hoc "skills" into measurable preference optimization objectives, connect to DPO/RLHF theory.

- **Vectorless Reasoning RAG** (`PageIndex`)
  - *Relevance:* Eliminates embedding storage (97% savings claimed by `LEANN`). Critical for scaling long-context systems to enterprise document corpora; investigate compatibility with recent work on reasoning-based retrieval (e.g., Search-o1, DeepSeek-R1-style methods).

- **Domain-Specific Multimodal Foundation Models** (`Kronos`)
  - *Relevance:* Financial markets as structured multimodal domain (time series + news + reports). Template for HMER-adjacent domains (mathematical proof assistants, scientific notation) where visual-symbolic grounding is critical.

- **Agent Memory & Persistent Context** (`mem0`, `memvid`, `claude-mem`, `thedotmack/claude-mem`)
  - *Relevance:* Long-context research must address cross-session state. These systems implement compression and relevance scoring—directly applicable to evaluating long-context model performance beyond single-session benchmarks.

- **OCR-to-LLM Pipeline Robustness** (`PaddleOCR`, `RAGFlow`)
  - *Relevance:* Hallucination mitigation depends on faithful document ingestion. Research gap: systematic evaluation of how OCR errors propagate through multimodal reasoning chains, and alignment techniques to make models robust to recognition noise.

---

*Report compiled from GitHub trending data 2026-05-28. Projects selected by strict relevance to declared research directions; general agent frameworks, CRM tools, language learning guides, and infrastructure without direct research connection excluded.*

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*