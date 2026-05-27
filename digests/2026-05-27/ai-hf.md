# Hugging Face 热门模型日报 2026-05-27

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-05-27 00:32 UTC

---

# Hugging Face 研究模型日报 | 2026-05-27

## 今日速览

本周 Hugging Face 热门模型榜单显示，**Qwen3.6 系列**持续主导多模态与视觉语言领域，多个变体（27B、35B-A3B-MoE）及社区微调版本（Uncensored、OBLITERATED）占据高下载量，反映开源 VLM 生态的活跃分化。**MiniCPM-V-4.6** 以近百万下载量巩固端侧文档理解地位，而 **DeepSeek-V4-Pro** 突破 500 万下载成为推理模型标杆。值得关注的是，**bytedance-research/Lance** 作为 any-to-any 统一架构首次进入热门榜，可能预示下一代多模态融合方向。后训练对齐领域未见专门模型上榜，但社区对"Uncensored"标签的高需求暗示对齐与能力释放之间的张力仍是研究焦点。

---

## 热门模型（按研究相关性分类）

### 🎭 多模态与视觉语言（VLM、视觉编码器、跨模态模型、图文理解）

| 模型 | 作者/数据 | 说明 |
|:---|:---|:---|
| **[bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance)**<br>👍 861 | ↓ 1,908 | ByteDance | **Any-to-any 统一生成模型**：支持图像、视频、文本的任意模态输入输出，是本周最具架构创新性的发布。对研究跨模态信息融合、统一表征学习具有重要参考价值，可能改变当前"拼接式"VLM 的设计范式。 |
| **[openbmb/MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**<br>👍 978 | ↓ 314,347 | OpenBMB | **端侧高效视觉语言模型**：MiniCPM 系列持续迭代，高下载量验证其在移动/边缘场景的实用价值。对 OCR+文档理解研究尤为关键——该系列以高分辨率图像编码和轻量架构著称，是 HMER（手写数学表达式识别）和文档版面分析的重要基线。 |
| **[Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**<br>👍 1,475 | ↓ 4,577,271 | 阿里云 | **旗舰开源 VLM**：Qwen3.6 系列的核心权重，457 万下载量体现其开源生态主导地位。视觉-语言对齐质量、多语言 OCR 能力、长上下文图文理解均为研究基准，其技术报告通常披露关键的视觉编码器设计与后训练策略。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**<br>👍 908 | ↓ 1,598,473 | HauhauCS | **MoE VLM 的激进去对齐版本**：160 万下载量揭示社区对"能力释放"的强烈需求。对**幻觉缓解研究**具有反向参考价值——该版本可能暴露原始模型的幻觉模式，为分析安全对齐如何影响多模态事实性提供对照样本。 |
| **[unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**<br>👍 502 | ↓ 735,349 | Unsloth | **MTP（Multi-Token Prediction）量化版**：Unsloth 优化的推理加速版本。MTP 机制与多模态推理的结合值得研究——视觉 token 的并行解码可能显著影响长文档理解的效率与准确性。 |
| **[unsloth/Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)**<br>👍 389 | ↓ 627,535 | Unsloth | **MoE + MTP 量化组合**：同上，MoE 稀疏激活与多 token 预测的协同优化，为高效多模态推理提供工程基准。 |
| **[numind/NuExtract3](https://huggingface.co/numind/NuExtract3)**<br>👍 160 | ↓ 20,350 | NuMind | **结构化信息提取专用 VLM**：基于 Qwen3.5 架构，聚焦文档关键信息抽取。对 OCR 后处理、版面分析到结构化输出的端到端优化有直接研究价值，是文档智能领域的垂直应用标杆。 |
| **[Jackrong/Qwopus3.6-27B-v2-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-GGUF)**<br>👍 144 | ↓ 16,379 | Jackrong | **社区优化 VLM 推理版本**：Qwopus 系列为 Qwen 的社区衍生，v2 迭代反映持续的后训练调优活动，可作为研究社区微调对视觉-语言对齐影响的案例。 |
| **[Jackrong/Qwopus3.5-9B-Coder-GGUF](https://huggingface.co/Jackrong/Qwopus3.5-9B-Coder-GGUF)**<br>👍 197 | ↓ 45,392 | Jackrong | **代码专用小型 VLM**：9B 参数+GGUF 量化，面向代码理解的多模态场景（如图表、公式截图的代码生成），对 OCR+代码的交叉研究有启发。 |
| **[CohereLabs/command-a-plus-05-2026-w4a4](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4)**<br>👍 206 | ↓ 7,769 | CohereLabs | **4-bit 量化视觉语言模型**：W4A4 极致量化下的多模态性能保持，研究压缩对视觉-语言对齐精度的影响，边缘部署与模型效率研究 relevant。 |
| **[CohereLabs/command-a-plus-05-2026-bf16](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16)**<br>👍 126 | ↓ 13,869 | CohereLabs | **BF16 精度 VLM**：同系列全精度版本，可与量化版对照研究数值精度对多模态推理（尤其是 OCR 细粒度识别）的影响。 |

### 🧠 长上下文与推理模型（扩展上下文 LLM、推理增强模型、数学模型）

| 模型 | 作者/数据 | 说明 |
|:---|:---|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**<br>👍 4,310 | ↓ 5,019,884 | DeepSeek | **开源推理模型新标杆**：502 万下载量断层领先，V4 系列的"Pro"版本暗示强化推理能力。对长上下文推理研究至关重要——DeepSeek 系列以 MLA（Multi-head Latent Attention）架构实现超长上下文的高效处理，是研究上下文压缩与推理可扩展性的核心参考。 |
| **[openbmb/MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)**<br>👍 307 | ↓ 2,409 | OpenBMB | **超轻量文本生成基座**：1B 参数的 MiniCPM5 代，虽非直接多模态，但其长文本处理能力（MiniCPM 系列通常支持 128K+ 上下文）为端侧长文档 OCR 理解提供文本解码层基础。 |
| **[tencent/Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B)**<br>👍 1,025 | ↓ 7,471 | 腾讯 | **翻译专用稠密模型**：Hy-MT2 系列聚焦机器翻译，1.8B 小参数高点赞反映专业领域效率优先趋势。对多语言 OCR 后处理、跨语言文档理解有间接支持价值。 |
| **[tencent/Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B)**<br>👍 396 | ↓ 2,091 | 腾讯 | **翻译 MoE 大模型**：30B 总参数/3B 激活的稀疏架构，多语言长文本处理能力可迁移至多语言文档理解场景。 |
| **[OBLITERATUS/Qwen3.6-27B-OBLITERATED](https://huggingface.co/OBLITERATUS/Qwen3.6-27B-OBLITERATED)**<br>👍 101 | ↓ 10,015 | OBLITERATUS | **去对齐文本模型**：纯文本生成版本，研究安全训练对基础推理能力的约束，为"对齐税"（alignment tax）的量化分析提供实验材料。 |

### 📄 OCR 与文档模型（文本识别、版面分析、文档理解、公式识别）

> *注：本周无专门 OCR/HMER 模型进入前 30，但以下多模态模型承载核心 OCR 能力*

| 模型 | 作者/数据 | 说明 |
|:---|:---|:---|
| **[openbmb/MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**<br>（重复归类） | — | **端侧文档理解首选**：MiniCPM-V 系列在学术界以高分辨率 OCR（如 1344×1344 图像编码）和表格/公式识别著称，4.6 版本迭代可能优化了 HMER 场景的性能，需关注其技术报告。 |
| **[numind/NuExtract3](https://huggingface.co/numind/NuExtract3)**<br>（重复归类） | — | **文档结构化提取**：将 OCR 输出转化为结构化数据的端到端方案，对研究"识别-理解-抽取"流水线整合有方法论意义。 |

### 🔧 Post-Training 与对齐（RLHF/DPO/SFT 模型、偏好微调模型、对齐-focused 发布）

| 模型 | 作者/数据 | 说明 |
|:---|:---|:---|
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**<br>（重复归类） | — | **激进去对齐的"反事实"样本**：160 万下载量揭示社区对原始模型对齐边界的好奇。研究者可对比其与官方版本的响应差异，量化安全对齐对知识表达、多模态事实性的影响机制。 |
| **[OBLITERATUS/Qwen3.6-27B-OBLITERATED](https://huggingface.co/OBLITERATUS/Qwen3.6-27B-OBLITERATED)**<br>（重复归类） | — | **系统提示剥离实验**：通过移除系统级安全约束研究基础模型的"原生"行为分布，为设计更精准的对齐目标函数提供参考。 |
| **[froggeric/Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)**<br>👍 423 | ↓ 0 | froggeric | **对话模板修正工具**：非模型而是基础设施，针对 Qwen 系列聊天格式的社区修复。高点赞零下载暗示研究者对官方模板设计缺陷的共识，**对话格式本身是对齐质量的关键变量**，值得形式化分析。 |

### 👁️ 幻觉缓解（事实 grounded 模型、校准置信度模型、RAG 增强模型）

> *本周无专门标注的幻觉缓解模型，但以下模型间接相关*

| 模型 | 作者/数据 | 说明 |
|:---|:---|:---|
| **[numind/NuExtract3](https://huggingface.co/numind/NuExtract3)**<br>（重复归类） | — | **结构化约束降低幻觉**：通过强制输出格式（JSON/Schema）实现"格式即对齐"，是缓解生成式模型事实幻觉的工程化路径，值得与基于 RLHF 的方法对比研究。 |
| **[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**<br>（重复归类） | — | **推理链内建事实校验**：DeepSeek 系列的深度思考模式（类似 o1 的 CoT）通过延长推理过程自我修正，是"推理时间扩展"缓解幻觉的代表架构。 |

### 🏗️ 研究基础设施（训练框架、评测套件、数据集工具）

| 模型 | 作者/数据 | 说明 |
|:---|:---|:---|
| **[bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance)**<br>（重复归类） | — | **统一多模态架构原型**：any-to-any 设计可能催生新一代训练框架，若开源训练代码将成为多模态预训练的重要基础设施。 |
| **[unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)** & **[35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)**<br>（重复归类） | — | **高效推理基础设施**：Unsloth 的 GGUF 转换与 MTP 支持代表后训练优化的工程前沿，为研究者提供低成本实验平台。 |

---

## 研究生态信号

**Qwen 家族垄断态势加剧**：本周 30 个热门模型中 8 个为 Qwen3.5/3.6 衍生（含官方、Unsloth 优化、社区微调），形成"核心权重+量化加速+去对齐实验"的三层生态，类似 Llama2 时期但迭代更快。**MiniCPM 守住端侧文档理解阵地**：OpenBMB 的双线布局（MiniCPM5 文本基座+MiniCPM-V-4.6 多模态）显示小参数高效模型的持续需求，对 OCR 研究的硬件普惠性至关重要。**对齐研究的"地下化"趋势**：官方模型强调安全，但"Uncensored""OBLITERATED"等标签高下载暗示社区对对齐机制的解构冲动，这可能分流本可用于幻觉缓解研究的算力与注意力。闭源方面，DeepSeek-V4-Pro 的 500 万下载证明顶尖推理能力仍可通过开源权重触达，但训练细节透明度下降。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance)** | **架构范式潜在变革者**。Any-to-any 统一生成若验证有效，将颠覆当前"视觉编码器+投影层+LLM"的拼接式 VLM 设计，从根本上改变 OCR/文档理解的信息流路径。建议优先分析其技术报告中的统一 tokenization 方案，评估对 HMER 等细粒度视觉任务的适配性。 |
| ⭐⭐⭐ | **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | **幻觉缓解的"负空间"研究**。160 万下载量的激进去对齐版本，可作为对照组量化安全对齐对多模态事实性的影响。建议设计实验：在相同 OCR 输入下，对比官方版与该版本的幻觉率差异，解析"对齐"与"真实"的耦合关系。 |
| ⭐⭐☆ | **[numind/NuExtract3](https://huggingface.co/numind/NuExtract3)** | **文档智能的垂直优化样本**。结构化提取任务天然需要 OCR+理解+生成的连贯能力，其训练数据构建（如何从文档版面到结构化标签）和后训练策略（如何约束输出格式降低幻觉）对 HMER 研究的下游应用有直接借鉴价值。 |

---

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*