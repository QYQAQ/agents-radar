# Hugging Face 热门模型日报 2026-06-16

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-16 00:43 UTC

---

# Hugging Face 研究模型日报 | 2026-06-16

## 今日速览

本周 Hugging Face 热门模型呈现**多模态统一架构**与**长上下文推理**双主线并进态势。Google 的 Gemma-4 系列（12B/26B）以 "any-to-any" 统一架构强势占据榜单，其原生视觉-语言融合设计为 OCR 与文档理解研究提供了新的基座选择；MiniMax-M3 与 Kimi-K2.7-Code 分别代表国产多模态与超长上下文代码推理的前沿进展，后者 256K+ 上下文窗口对 HMER（手写数学表达式识别）等需要细粒度长序列建模的任务具有直接价值。值得关注的是，**后训练对齐与幻觉缓解**正从"附加模块"演变为模型原生能力——DeepSeek-V4-Pro 的高下载量（293万）反映市场对可靠推理的需求，而微软 FastContext-1.0-4B-SFT 的"Explorer SubAgent"标签暗示了通过结构化搜索缓解幻觉的新范式。Unsloth 对主流模型的 GGUF 量化生态覆盖（Gemma-4、MiniMax-M3、Kimi-K2.7）则显著降低了研究者的实验门槛。

---

## 热门模型（按研究相关性分类）

### 🎭 多模态与视觉语言（VLM、视觉编码器、跨模态模型、图文理解）

| 模型 | 作者/数据 | 核心说明与研究相关性 |
|:---|:---|:---|
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google \| 👍 876 \| ⬇️ 311,788 | **扩散+语言统一架构**：26B 参数、A4B 激活的稀疏 MoE 设计，将扩散模型的细粒度视觉生成能力与文本推理融合。对 **HMER 研究**极具价值——数学公式渲染的像素级精确性可反向提升公式识别模型的训练数据质量；其 image-text-to-text 范式也为"公式图像→LaTeX"的端到端研究提供新基线。 |
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google \| 👍 1,029 \| ⬇️ 1,160,435 | **原生 any-to-any 统一模型**：官方指令版，支持文本、图像、视频任意模态输入输出。对 **OCR/文档理解**研究的核心意义在于：摒弃了传统"视觉编码器+投影层+LLM"的拼接架构，视觉特征与语言 token 在统一空间表示，可能根本性改善文档版面分析中的跨模态对齐问题。百万级下载量验证其作为研究基座的生态位。 |
| **[google/gemma-4-12B](https://huggingface.co/google/gemma-4-12B)** | google \| 👍 549 \| ⬇️ 250,498 | **Gemma-4 基座版**：any-to-any 预训练权重，适合研究者进行 **post-training 对齐**实验（如针对文档领域的 DPO/RLHF）。相比指令版，更便于探究原生多模态预训练表示与下游 OCR 任务的迁移规律。 |
| **[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)** | MiniMaxAI \| 👍 800 \| ⬇️ 14,312 | **国产多模态 MoE 旗舰**：标签显式标注"multimodal"与"agent"能力，800 点赞与相对较低下载量形成反差，暗示研究社区关注度高于实际部署。其视觉-语言融合机制对 **中文文档 OCR** 研究具有独特价值——MiniMax 在中文场景的理解优势可能迁移至古籍、手写体等低资源文档识别任务。 |
| **[moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)** | moonshotai \| 👍 740 \| ⬇️ 56,750 | **超长上下文代码多模态模型**：Kimi 系列的 2.7 代代码特化版，标签含"image-feature-extraction"与"compressed-tensors"，暗示视觉-代码联合推理与上下文压缩技术。对 **HMER 与数学推理**研究的关键价值：代码生成任务所需的结构化长序列推理，与数学公式识别中的层级结构解析（如分式嵌套、矩阵环境）高度同构；其上下文压缩技术可能解决手写公式图像的高分辨率长序列瓶颈。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia \| 👍 2,054 \| ⬇️ 86,968 | **视觉定位专用模型**：本周点赞冠军（2054），"LocateAnything"命名暗示开放词汇目标定位与视觉 grounding 能力。对 **OCR 研究**的间接价值：文档理解中的关键元素定位（如表格单元格、公式编号、图表标题）可借鉴其视觉-语言空间对齐机制；3B 轻量参数适合作为文档版面分析的视觉 backbone 嵌入更大系统。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS \| 👍 1,844 \| ⬇️ 2,697,882 | **社区激进微调版 Qwen3.6-VL**：下载量惊人（270万），"Aggressive"标签暗示对齐约束的显著解除。对 **幻觉缓解研究**的警示意义：该模型的流行反衬出当前 VLMs 在安全回答与真实能力间的张力；研究者可将其作为"对齐失败"的负面案例，探究 uncensored 微调对视觉 grounding 忠实性的侵蚀机制。 |
| **[unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)** | unsloth \| 👍 613 \| ⬇️ 980,781 | **Gemma-4 高效量化版**：近百万下载的社区优化版本，保留 image-text-to-text 能力。对 **OCR/HMER 研究**的实用价值：使单卡/边缘设备上的文档理解实验成为可能，便于研究者快速验证 Gemma-4 架构在公式识别、表格解析等任务上的零样本/少样本表现。 |
| **[unsloth/MiniMax-M3-GGUF](https://huggingface.co/unsloth/MiniMax-M3-GGUF)** | unsloth \| 👍 80 \| ⬇️ 14,799 | **MiniMax-M3 量化适配**：标签含"multimodal"与"agent"，参数效率优化后适合 **多模态对齐实验**的快速迭代。 |
| **[Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF)** | Jackrong \| 👍 201 \| ⬇️ 62,469 | **Qwopus 代码视觉模型**："MTP"（Multi-Token Prediction）标签与"vision"能力结合，暗示代码生成中的视觉辅助。对 **HMER 研究**的启发：数学公式的 token 化表示与代码 AST 的结构相似性，MTP 技术可能提升公式 LaTeX 序列的生成效率。 |
| **[Jackrong/Qwopus3.6-27B-v2-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-MTP-GGUF)** | Jackrong \| 👍 310 \| ⬇️ 184,446 | **Qwopus v2 迭代版**：更高下载量反映社区认可，v2 改进可能涉及视觉-代码对齐稳定性，值得对比研究。 |
| **[DavidAU/Qwen3.6-40B-Claude-4.6-Opus-Deckard-Heretic-Uncensored-Thinking-NEO-CODE-Di-IMatrix-MAX-GGUF](https://huggingface.co/DavidAU/Qwen3.6-40B-Claude-4.6-Opus-Deckard-Heretic-Uncensored-Thinking-NEO-CODE-Di-IMatrix-MAX-GGUF)** | DavidAU \| 👍 354 \| ⬇️ 369,526 | **极端融合微调实验**：名称堆砌"Claude-4.6-Opus""Thinking""NEO-CODE"等概念，"Heretic"标签暗示对齐突破。对 **幻觉缓解研究**的方法论价值：作为社区"蒸馏+融合+解除对齐"的极端案例，可用于量化分析多层后训练叠加对模型校准（calibration）的破坏程度。 |

### 🧠 长上下文与推理模型（扩展上下文 LLM、推理增强模型、数学模型）

| 模型 | 作者/数据 | 核心说明与研究相关性 |
|:---|:---|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai \| 👍 4,862 \| ⬇️ 2,934,763 | **本周绝对顶流**：点赞与下载双冠，"conversational"标签下的 Pro 版本暗示推理能力强化。对 **长上下文推理与幻觉缓解**的双重价值：DeepSeek 系列以推理链忠实性著称，V4-Pro 的 MoE 架构（deepseek_v4）与超长上下文训练使其成为 **文档级多跳推理** 的理想基座——可直接测试其在长文档中跨页引用公式、表格的准确性，为幻觉缓解研究提供高天花板基准。 |
| **[yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)** | yuxinlu1 \| 👍 577 \| ⬇️ 20,207 | **社区代码推理融合版**：融合 Fable5 与 Composer2.5 的代码能力至 Gemma-4。对 **HMER 研究**的直接关联：代码生成所需的结构化推理与数学公式识别的 LaTeX 生成任务高度同构；该模型的社区高点赞反映"视觉+代码"融合范式的研究热度。 |
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft \| 👍 101 \| ⬇️ 13 | **微软轻量长上下文 SFT 实验**："Explorer SubAgent"标签极具研究新意——暗示通过**子代理探索机制**扩展有效上下文，而非单纯增加序列长度。对 **长上下文推理与幻觉缓解**的前沿价值：若"SubAgent"实现为递归式上下文检索与验证，则可能根本性改变长文档理解的幻觉模式，值得密切追踪其技术披露。4B 参数适合作为研究假设的快速验证平台。 |
| **[silx-ai/Quasar-Preview](https://huggingface.co/silx-ai/Quasar-Preview)** | silx-ai \| 👍 81 \| ⬇️ 363 | **"quasar_long" 长上下文专用标签**：明确指向长文本优化，低下载高标签特异性使其成为 **长上下文研究**的潜在早期信号。需关注其是否采用稀疏注意力或上下文压缩等创新机制。 |

### 🔧 Post-Training 与对齐（RLHF/DPO/SFT 模型、偏好微调模型、对齐-focused 发布）

| 模型 | 作者/数据 | 核心说明与研究相关性 |
|:---|:---|:---|
| **[CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)** | CohereLabs \| 👍 388 \| ⬇️ 11,145 | **Cohere MoE 代码对齐模型**：cohere2_moe 架构的代码特化 SFT 版本。对 **对齐研究**的参考价值：Cohere 在指令跟随与安全性间的平衡策略已知较为保守，其代码领域的对齐方法可能揭示"能力-安全"帕累托前沿在结构化输出任务上的特殊形态。 |
| **[prefeitura-rio/Rio-3.5-Open-397B](https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B)** | prefeitura-rio \| 👍 302 \| ⬇️ 188,723 | **巴西政府开源 397B MoE 巨模型**：qwen3_5_moe 架构，官方机构发布的开放权重。对 **对齐研究**的独特意义：政府背景模型的对齐目标（公共服务、多语言公平性）与商业模型差异显著，可作为 **多文化语境下幻觉缓解** 的跨域研究素材——检验 Qwen3.5 架构在葡萄牙语文档理解中的校准表现。 |
| **[OBLITERATUS/Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED)** | OBLITERATUS \| 👍 324 \| ⬇️ 70,732 | **Gemma-4 激进解除对齐**："OBLITERATED"命名与 gemma4_unified 标签的矛盾组合。对 **幻觉缓解研究**的对比实验价值：与官方 gemma-4-12B-it 形成严格对照，可量化测量对齐移除对视觉-语言 grounding 忠实性的影响，特别是文档理解中的事实坚持度。 |
| **[unsloth/diffusiongemma-26B-A4B-it-GGUF](https://huggingface.co/unsloth/diffusiongemma-26B-A4B-it-GGUF)** | unsloth \| 👍 275 \| ⬇️ 107,243 | **DiffusionGemma 量化版**：使扩散-语言统一模型的后训练实验民主化。研究者可探索针对 **HMER 数据生成** 的 LoRA 微调：利用其扩散能力生成多样化手写公式样本，再用于训练判别式识别模型。 |
| **[unsloth/gemma-4-12B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-12B-it-qat-GGUF)** | unsloth \| 👍 241 \| ⬇️ 288,390 | **QAT（量化感知训练）版本**：相比标准 GGUF，QAT 保留更多精度。对 **后训练对齐研究**的意义：量化损伤与对齐效果的交互作用尚属研究空白，该模型可作为"低比特对齐是否可行"的实验入口。 |

### 👁️ 幻觉缓解（事实 grounded 模型、校准置信度模型、RAG 增强模型）

| 模型 | 作者/数据 | 核心说明与研究相关性 |
|:---|:---|:---|
| **[nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)** | nvidia \| 👍 422 \| ⬇️ 5,200 | **流式 ASR 专用小模型**：nemotron-3.5 系列的流式语音识别变体。对 **幻觉缓解的跨模态启发**：ASR 中的"流式"约束与 LLM 的"实时生成"场景同构，其 "cache-aware" 设计（标签明确标注）可能为 **长文档生成中的事实一致性维护** 提供技术借鉴——如何在增量解码中保持跨段落的事实连贯。 |
| **[nex-agi/Nex-N2-Pro](https://huggingface.co/nex-agi/Nex-N2-Pro)** / **[nex-agi/Nex-N2-mini](https://huggingface.co/nex-agi/Nex-N2-mini)** | nex-agi \| 👍 287/217 \| ⬇️ 3,681/8,260 | **Nex 系列 MoE 模型**：qwen3_5_moe 架构的双规模发布。对 **幻觉缓解研究**的潜在价值：Pro/mini 对比可分离"模型容量"与"架构设计"对 grounding 能力的影响，若其技术报告披露训练细节，可探究 MoE 路由稀疏性是否意外导致事实检索的不稳定性。 |

### 🏗️ 研究基础设施（训练框架、评测套件、数据集工具）

| 模型 | 作者/数据 | 核心说明与研究相关性 |
|:---|:---|:---|
| **[unsloth](https://huggingface.co/unsloth) 系列量化模型** | unsloth \| 多模型 | **社区量化基础设施**：本周 Unsloth 覆盖 Gemma-4、MiniMax-M3、Kimi-K2.7、DiffusionGemma 等主流架构的 GGUF/QAT 版本，形成 **多模态研究的标准化实验平台**。对 OCR/HMER 研究的生态价值：大幅降低视觉-语言模型的实验门槛，使学术机构单卡资源即可验证假设；其量化一致性（同一工具链处理多架构）便于控制实验中的"基础设施变量"。 |

---

## 研究生态信号

**Gemma-4 统一架构**正成为多模态 OCR/文档理解的新事实标准，其 "any-to-any" 设计消解了传统 VLM 的模态拼接裂缝，可能使版面分析、公式识别等任务的端到端优化首次成为可能。国产模型呈现 **"长上下文"（Kimi）与"多模态 MoE"（MiniMax、Qwen3.5/3.6）双轨并进**，且社区微调活跃度极高（HauhauCS、Jackrong、DavidAU 等），但 "uncensored" 标签的泛滥暗示 **对齐研究与安全部署间的张力正在加剧**——研究者需警惕此类模型作为基准的可靠性污染。开源权重在视觉语言领域已逼近闭源可用性（Gemma-4 百万下载 vs MiniMax 社区版），但 **幻觉缓解仍缺乏标准化评测**：微软 FastContext 的 "SubAgent" 探索与 DeepSeek-V4-Pro 的推理链忠实性，或预示下一波研究将从"生成能力"转向"验证能力"的架构创新。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | **"

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*