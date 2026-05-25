# Hugging Face 热门模型日报 2026-05-25

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-05-25 00:31 UTC

---

# Hugging Face 研究模型日报 | 2026-05-25

---

## 今日速览

本周 Hugging Face 生态呈现**多模态统一化**与**长上下文军备竞赛**两大趋势。字节跳动的 **Lance** 以 any-to-any 架构实现图像-视频-文本统一生成，标志多模态模型向全模态原生架构演进；**Qwen3.6** 系列（27B/35B-A3B）持续主导视觉语言开源生态，其 MTP（Multi-Token Prediction）变体与超长上下文能力成为研究焦点。Google **Gemma-4-31B-it** 以千万级下载量验证开源 VLM 的商业落地潜力，而 **MiniCPM-V-4.6** 则延续端侧高效多模态路线。值得注意的是，**HauhauCS** 等社区微调版本的高下载量（120万+）反映出后训练对齐与去幻觉化需求的旺盛，但专用 OCR/HMER 模型本周缺席热门榜单，文档理解仍依附于通用 VLM 的隐式能力。

---

## 热门模型

### 🎭 多模态与视觉语言（VLM、视觉编码器、跨模态模型、图文理解）

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance)** | bytedance-research | 760 | 1,474 | **原生 any-to-any 架构**，统一处理文本/图像/视频生成与理解，打破模态间人工边界，为跨模态推理研究提供新基线。 |
| **[openbmb/MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)** | openbmb | 918 | 269,589 | 端侧高效 VLM 新迭代，以极小激活参数实现强视觉理解，**OCR 密集型场景**的端侧部署理想研究对象。 |
| **[Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)** | Qwen | 1,422 | 4,242,555 | Qwen3.6 系列旗舰开源权重，**image-text-to-text** 任务标杆，其视觉编码器设计与长上下文融合机制值得多模态推理深度剖析。 |
| **[unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)** | unsloth | 455 | 660,321 | **MTP（Multi-Token Prediction）** 量化版，推测解码加速视觉语言推理，对多模态模型效率-精度权衡研究具工具价值。 |
| **[unsloth/Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)** | unsloth | 358 | 547,827 | MoE 架构 MTP 量化版，35B 总参数/3B 激活参数，**稀疏激活+多模态**的扩展性研究样本。 |
| **[google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)** | google | 2,762 | 10,398,435 | 本周下载量冠军，Gemma-4 视觉指令微调版，**开源 VLM 中工业验证最充分**，其多语言 OCR 与文档理解能力待学术评测。 |
| **[CohereLabs/command-a-plus-05-2026-bf16](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16)** | CohereLabs | 113 | 12,362 | Cohere 视觉语言模型 bf16 版，**企业级对话+视觉理解**，对齐策略与幻觉控制机制不透明但性能强劲。 |
| **[CohereLabs/command-a-plus-05-2026-w4a4](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4)** | CohereLabs | 190 | 5,627 | 4-bit 激活/权重量化版，极端压缩下的多模态能力保留，**量化对视觉特征精度损失**的研究案例。 |
| **[numind/NuExtract3](https://huggingface.co/numind/NuExtract3)** | numind | 107 | 10,998 | 基于 Qwen3.5 的**结构化信息抽取专用 VLM**，image-to-text 任务定位，文档关键信息提取与版面理解的轻量研究入口。 |
| **[Jackrong/Qwopus3.6-27B-v2-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-GGUF)** | Jackrong | 113 | 8,300 | 社区 Qwen3.6 视觉 GGUF 变体，**多模态模型开源量化生态**的活跃信号。 |
| **[Jackrong/Qwopus3.5-9B-Coder-GGUF](https://huggingface.co/Jackrong/Qwopus3.5-9B-Coder-GGUF)** | Jackrong | 180 | 38,937 | 代码导向视觉语言模型，**图表/公式/代码截图理解**的潜在 OCR 替代方案。 |

### 🧠 长上下文与推理模型（扩展上下文 LLM、推理增强模型、数学模型）

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 4,224 | 4,666,078 | 本周点赞冠军，**长上下文推理旗舰**，V4 系列 Pro 版在文本生成任务中隐含超长上下文与复杂推理能力，多模态扩展值得追踪。 |
| **[NemoStation/Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)** | NemoStation | 306 | 6,032 | **video-text-to-text** 专用模型，2B 参数实现视频长序列理解，时序推理与视觉信息融合的轻量化研究对象。 |
| **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** | sapientinc | 271 | 84,346 | HRM（Human Resource Model?）文本生成模型，1B 参数极高下载量，**长文档生成或结构化输出**的隐性能力待验证。 |
| **[nvidia/Nemotron-Labs-Diffusion-14B](https://huggingface.co/nvidia/Nemotron-Labs-Diffusion-14B)** | nvidia | 89 | 4,071 | NVIDIA 实验室扩散模型，text-generation 标签下的**扩散语言模型**，非自回归生成对长上下文连贯性的潜在优势。 |

### 🔧 Post-Training 与对齐（RLHF/DPO/SFT 模型、偏好微调模型、对齐-focused 发布）

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 767 | 1,220,114 | **本周下载量黑马（120万+）**，激进去审查版 Qwen3.6 MoE，反映社区对**对齐边界与有用性权衡**的极端实验需求，安全研究反面教材。 |
| **[froggeric/Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)** | froggeric | 388 | 0 | Qwen 聊天模板修正集合，**对齐基础设施的社区维护**，模板工程对指令遵循质量的隐性影响值得系统研究。 |
| **[OBLITERATUS/Qwen3.6-27B-OBLITERATED](https://huggingface.co/OBLITERATUS/Qwen3.6-27B-OBLITERATED)** | OBLITERATUS | 76 | 5,298 | "抹除"版 Qwen3.6，**去对齐化实验**，与 HauhauCS 共同构成后训练对齐可逆性研究的社区数据集。 |

### 👁️ 幻觉缓解（事实 grounded 模型、校准置信度模型、RAG 增强模型）

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[numind/NuExtract3](https://huggingface.co/numind/NuExtract3)** | numind | 107 | 10,998 | 结构化抽取任务天然要求**输出与输入视觉内容严格对齐**，其幻觉率可作为文档理解 VLM 的基准测试。 |
| **[google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)** | google | 2,762 | 10,398,435 | Google 官方 it 版通常集成**事实性校准与拒绝机制**，千万级部署量的幻觉反馈数据具有研究价值。 |

### 🏗️ 研究基础设施（上述领域的训练框架、评测套件、数据集工具）

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[Supertone/supertonic-3](https://huggingface.co/Supertone/supertonic-3)** | Supertone | 645 | 43,119 | 语音合成基础设施，非直接相关但**any-to-any 时代的音频模态扩展**参考。 |
| **[circlestone-labs/Anima](https://huggingface.co/circlestone-labs/Anima)** | circlestone-labs | 1,531 | 637,329 | ComfyUI 生态核心节点，**多模态生成工作流基础设施**，视觉研究者的工程工具。 |
| **[SulphurAI/Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)** | SulphurAI | 1,322 | 1,331,058 | 文本到视频基础模型，**百万级下载的生成基础设施**，时序一致性幻觉研究的实验平台。 |
| **[Efficient-Large-Model/SANA-WM_bidirectional](https://huggingface.co/Efficient-Large-Model/SANA-WM_bidirectional)** | Efficient-Large-Model | 98 | 0 | 双向 SANA 视频生成，**相机控制与运动一致性**，视频生成幻觉（物理规律违背）的控制研究。 |

---

## 研究生态信号

**Qwen 生态霸权巩固**：Qwen3.5/3.6 系列占据 30 个热门模型中的 8 个（含社区变体），形成事实上的开源多模态基础设施。其 MTP、MoE、视觉融合等技术的快速迭代，使 Qwen 成为 OCR/VLM/长上下文研究的默认基线。Google Gemma-4 以 1000 万+ 下载量证明开源权重的商业可行性，但技术透明度不及 Qwen。**专用 OCR/HMER 模型缺席**本周热门榜，文档理解仍被通用 VLM 的隐式能力覆盖，学术领域需警惕"通用吞噬专用"的能力评估偏差。后训练对齐领域呈现**两极化**：官方版本强化安全对齐，而 HauhauCS/OBLITERATUS 等社区变体以百万下载量践行"对齐可逆性"实验，形成独特的自然对照研究生态。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance)** | **any-to-any 原生架构的首个热门开源实现**，打破"图像理解+图像生成"分离范式。其统一表征空间对 OCR（文本作为图像-语言中间态）、跨模态推理（公式→LaTeX→渲染图像）具有重构潜力，建议优先分析其 tokenizer 与模态桥接机制。 |
| ⭐⭐⭐ | **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | **120万下载的激进去对齐化实验**，为幻觉缓解研究提供反向样本。可系统对比其与官方 Qwen3.6 在文档理解任务中的幻觉率差异，量化"过度对齐"与"事实准确性"的权衡边界，是对齐研究的天然消融实验。 |
| ⭐⭐ | **[numind/NuExtract3](https://huggingface.co/numind/NuExtract3)** | **轻量级文档结构化抽取专用 VLM**，107 点赞/1.1万下载的"小而美"存在。可直接作为 OCR 后处理 pipeline 的替代方案，评测其在发票、表格、学术论文版面的抽取幻觉率，填补本周无专用 OCR 模型的空白。 |

---

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*