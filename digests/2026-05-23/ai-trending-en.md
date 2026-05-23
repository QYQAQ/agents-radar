# AI Open Source Trends 2026-05-23

> Sources: GitHub Trending + GitHub Search API | Generated: 2026-05-23 14:52 UTC

---

# AI Open Source Trends Report — 2026-05-23
## Research Focus: Long-Context Reasoning, OCR/HMER, Multimodal Reasoning, Post-Training Alignment, Hallucination Mitigation

---

## 1. Today's Highlights

The most striking development is the emergence of **code knowledge graph systems** ([Understand-Anything](https://github.com/Lum1104/Understand-Anything), [codegraph](https://github.com/colbymchenry/codegraph)) that transform unstructured codebases into structured, navigable representations—directly relevant to long-context reasoning research as they reduce token consumption while preserving semantic relationships. NVIDIA's [LongLive 2.0](https://github.com/NVlabs/LongLive) for long video generation signals continued investment in temporal long-context modeling. The proliferation of **agent skill frameworks** (Karpathy skills, cybersecurity skills, .NET skills) represents an underexplored angle for post-training alignment through structured behavioral conditioning. Notably, [LlamaIndex](https://github.com/run-llama/llama_index) explicitly positions itself as an "OCR platform," confirming document intelligence as a core growth vector. However, pure research projects in hallucination mitigation and formal alignment methods remain underrepresented in today's trending data, with most activity concentrated in application-layer tooling.

---

## 2. Top Projects by Category

### 📄 OCR & Document Intelligence

| Project | Stars | Why It Matters |
|--------|-------|--------------|
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | 49,613 total | Explicitly rebranded as "the leading document agent and **OCR platform**"—central infrastructure for document understanding pipelines |
| [lancedb/lancedb](https://github.com/lancedb/lancedb) | 10,382 total | "Developer-friendly OSS embedded retrieval library for **multimodal AI**" with native document/multimodal support |
| [yichuan-w/LEANN](https://github.com/yichuan-w/LEANN) | 11,676 total | 97% storage savings for private RAG; relevant to efficient document embedding and retrieval for OCR pipelines |
| [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | 11,531 total | Code search MCP enabling "entire codebase as context"—structural document understanding at scale |

### 🎭 Multimodal Reasoning

| Project | Stars | Why It Matters |
|--------|-------|--------------|
| [huggingface/transformers](https://github.com/huggingface/transformers) | 160,901 total | Core framework for multimodal model development (text, vision, audio); foundation for VLM research |
| [lancedb/lancedb](https://github.com/lancedb/lancedb) | 10,382 total | Native multimodal retrieval infrastructure; "Search More; Manage Less" for cross-modal applications |
| [NVlabs/LongLive](https://github.com/NVlabs/LongLive) | 79 today | Long video generation = temporal multimodal reasoning; extends vision-language to extended sequences |
| [0xPlaygrounds/rig](https://github.com/0xPlaygrounds/rig) | 7,388 total | Modular LLM applications in Rust; supports multimodal pipeline construction |

### 🧠 Long-Context & Reasoning

| Project | Stars | Why It Matters |
|--------|-------|--------------|
| [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +2,331 today | Transforms code into **interactive knowledge graphs** for exploration—novel approach to structured long-context representation |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +2,434 today | "Pre-indexed code knowledge graph" with "fewer tokens, fewer tool calls, 100% local"—directly attacks context efficiency |
| [NVlabs/LongLive](https://github.com/NVlabs/LongLive) | 79 today | "LongLive 2.0: Infra - Long Video Gen"—temporal long-context generation infrastructure |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 80,795 total | High-throughput inference engine; critical for long-context serving with memory-efficient attention |
| [skyzh/tiny-llm](https://github.com/skyzh/tiny-llm) | 4,202 total | "Learning LLM inference serving" including vLLM architecture; educational foundation for context optimization |

### 🔧 Post-Training & Alignment

| Project | Stars | Why It Matters |
|--------|-------|--------------|
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | +3,152 today | Structured behavioral conditioning derived from expert observations—**implicit alignment through skill specification** |
| [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 238 today | 754 structured skills mapped to 5 frameworks; demonstrates **domain-specific post-training via skill libraries** |
| [dotnet/skills](https://github.com/dotnet/skills) | 262 today | Microsoft-backed agent skills for .NET; organizational pattern for capability elicitation |
| [open-compass/opencompass](https://github.com/open-compass/opencompass) | 7,020 total | LLM evaluation platform supporting 100+ datasets; essential alignment benchmarking infrastructure |
| [thinkwee/AwesomeOPD](https://github.com/thinkwee/AwesomeOPD) | 439 total | "Awesome List for On-Policy Distillation"—directly relevant to SFT and knowledge transfer methods |

### 👁️ Hallucination & Reliability

| Project | Stars | Why It Matters |
|--------|-------|--------------|
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | 49,613 total | Document-grounded retrieval reduces hallucination; "OCR platform" positioning emphasizes factual grounding |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 123,286 total | "Search, scrape, and clean the web for AI agents"—**data provenance and quality control** for grounding |
| [yichuan-w/LEANN](https://github.com/yichuan-w/LEANN) | 11,676 total | 100% private RAG with storage efficiency; local grounding without external API hallucination risks |

### 🏗️ Infrastructure

| Project | Stars | Why It Matters |
|--------|-------|--------------|
| [huggingface/transformers](https://github.com/huggingface/transformers) | 160,901 total | Foundational framework for model training/fine-tuning in all focus areas |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 80,795 total | Production inference for long-context and multimodal models |
| [open-compass/opencompass](https://github.com/open-compass/opencompass) | 7,020 total | Evaluation infrastructure for alignment and reasoning benchmarks |
| [skyzh/tiny-llm](https://github.com/skyzh/tiny-llm) | 4,202 total | Educational infrastructure for understanding serving optimization |
| [raw-labs/mxcp](https://github.com/raw-labs/mxcp) | 68 total | "Model eXecution + Context Protocol"—enterprise data-to-AI context management |

---

## 3. Research Trend Signal Analysis

Today's GitHub trending data reveals a **pronounced shift toward structured context representation** as the dominant paradigm for addressing long-context limitations. Rather than pursuing raw context window expansion, the community is aggressively adopting **knowledge graph intermediaries** ([Understand-Anything](https://github.com/Lum1104/Understand-Anything), [codegraph](https://github.com/colbymchenry/codegraph)) that compress and structure information for more efficient reasoning. This aligns with research trajectories in graph-based retrieval and structured reasoning, though formal evaluation of these approaches against standard long-context benchmarks remains absent.

The **skillification of agent behavior**—exemplified by Karpathy-derived skills, cybersecurity skill frameworks, and platform-specific skill repositories—represents an understudied alignment mechanism. These projects operationalize **behavioral priors through structured prompting and tool conditioning**, effectively a form of lightweight post-training alignment without gradient updates. Research opportunities exist in quantifying how skill libraries reduce hallucination and improve reasoning consistency compared to base model behavior.

OCR and document intelligence are consolidating around [LlamaIndex](https://github.com/run-llama/llama_index), which explicitly markets itself as an "OCR platform," suggesting market maturation. However, specialized HMER (Handwritten Mathematical Expression Recognition) projects remain absent from trending data, indicating either commercial consolidation or underinvestment in this critical multimodal reasoning subdomain.

Notably missing from today's trends are **explicit hallucination mitigation techniques** (e.g., self-consistency, chain-of-verification, factual grounding classifiers) and **formal alignment research implementations** (RLHF, DPO, IPO variants). The alignment activity visible is indirect—through evaluation ([OpenCompass](https://github.com/open-compass/opencompass)) and skill conditioning rather than direct preference optimization open-source releases. This suggests either research-to-code lag or proprietary concentration in these methods.

---

## 4. Research Hot Spots

- **[Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything)** & **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** — **Knowledge graphs for long-context reasoning**: These represent a testable hypothesis that structured intermediate representations outperform naive token extension. Research should evaluate graph-based context against needle-in-haystack and multi-hop reasoning benchmarks, and explore generalization from code to mathematical/scientific documents (HMER-relevant).

- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** — **Behavioral alignment via expert skill distillation**: Derived from practitioner observations of LLM failure modes, this offers a novel dataset for studying whether structured skill conditioning reduces specific reasoning errors and hallucination patterns. Comparable to Constitutional AI but with empirical rather than normative foundations.

- **[run-llama/llama_index](https://github.com/run-llama/llama_index)** — **OCR-platform positioning**: Its explicit OCR branding amid 49K stars validates document intelligence as a primary vector. Research should probe its multimodal parsing capabilities for mathematical/scientific document understanding, and benchmark against specialized HMER systems.

- **[NVlabs/LongLive](https://github.com/NVlabs/LongLive)** — **Temporal long-context for video**: Long video generation requires coherent multimodal reasoning across extended temporal sequences. Relevant to understanding how vision-language models maintain consistency, and whether temporal hallucination patterns mirror textual hallucinations.

- **[thinkwee/AwesomeOPD](https://github.com/thinkwee/AwesomeOPD)** — **On-policy distillation**: Directly relevant to efficient post-training alignment. OPD methods offer potential for aligning smaller models with verified reasoning traces, with implications for hallucination reduction through distillation from more reliable teacher distributions.

---

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*