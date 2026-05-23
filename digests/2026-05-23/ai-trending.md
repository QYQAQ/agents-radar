# AI 开源趋势日报 2026-05-23

> 数据来源: GitHub Trending + GitHub Search API | 生成时间: 2026-05-23 14:52 UTC

---

# AI 开源趋势日报（2026-05-23）

## 研究方向聚焦：长上下文推理、OCR/HMER、多模态推理、Post-Training 对齐、幻觉缓解

---

## 第一步：相关性筛选结果

经严格筛选，以下项目与研究方向**直接相关**：

| 项目 | 相关维度 | 相关性说明 |
|:---|:---|:---|
| **run-llama/llama_index** | OCR/文档智能、多模态推理 | 明确标注"OCR platform"，文档理解与多模态RAG核心基础设施 |
| **NVlabs/LongLive** | 长上下文与推理 | NVIDIA长视频生成，直接关联长上下文建模与推理 |
| **yichuan-w/LEANN** | 长上下文与推理、基础设施 | 97%存储节省的本地RAG，长上下文压缩与高效检索 |
| **open-compass/opencompass** | 基础设施、幻觉与可靠性 | LLM评测平台，覆盖多模态与对齐评测 |
| **jingyaogong/minimind** | 基础设施、Post-Training与对齐 | 从零训练LLM的完整pipeline，含SFT/RLHF教学 |
| **testtimescaling/testtimescaling.github.io** | 长上下文与推理、Post-Training与对齐 | Test-Time Scaling综述，推理时计算扩展与对齐 |
| **EgoAlpha/prompt-in-context-learning** | 长上下文与推理 | 上下文学习(ICL)前沿资源，长上下文利用策略 |
| **galilai-group/stable-pretraining** | Post-Training与对齐、基础设施 | 稳定预训练库，世界模型训练，关联对齐稳定性 |
| **thinkwee/AwesomeOPD** | Post-Training与对齐 | On-Policy Distillation，在线对齐与知识蒸馏 |
| **0xPlaygrounds/rig** | 基础设施 | Rust LLM应用框架，模块化推理架构 |
| **skyzh/tiny-llm** | 长上下文与推理、基础设施 | Apple Silicon上的vLLM实现，推理服务优化 |
| **zilliztech/claude-context** | 长上下文与推理 | 代码库级上下文检索，长上下文工程实践 |
| **topoteretes/cognee** | 长上下文与推理 | AI Agent记忆控制平面，长期记忆与上下文管理 |
| **Y-Research-SBU/PosterGen** | 多模态推理 | CVPR 2026 Findings，学术海报生成，视觉-文本对齐 |

**排除项目**：通用Agent框架（AutoGPT、OpenHands等）、聊天UI（OpenWebUI、Cherry Studio）、纯商业应用（FinceptTerminal）、前端工具、视频下载器（yt-dlp）、安全技能库等非研究核心项目。

---

## 第二步：分类详情

---

## 1. 今日速览

今日热榜呈现**"长上下文工程化"与"推理时计算扩展"**两大核心动向：NVIDIA的LongLive 2.0推动长视频生成基础设施迭代；Test-Time Scaling综述项目登榜标志社区对推理时对齐策略的高度关注；LlamaIndex持续强化其OCR+文档智能定位；LEANN以97%存储压缩实现本地长上下文RAG，凸显边缘侧长上下文需求；minimind与stable-pretraining等训练框架则为post-training对齐提供了更稳定的基础设施底座。

---

## 2. 各维度热门项目

### 📄 OCR 与文档智能

| 项目 | Stars | 今日新增 | 一句话说明 |
|:---|:---|:---|:---|
| **[run-llama/llama_index](https://github.com/run-llama/llama_index)** | 49,613 | — | **文档Agent与OCR平台**，支持多模态文档解析、向量化检索与RAG pipeline，是文档智能领域的核心基础设施，今日在vector-db主题中保持高活跃度 |
| **[yichuan-w/LEANN](https://github.com/yichuan-w/LEANN)** | 11,676 | — | **[MLsys2026] RAG on Everything**，以97%存储压缩实现本地设备上的高效文档检索，直接解决长文档OCR后的存储与检索瓶颈 |
| **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** | 11,531 | — | **代码搜索MCP**，将完整代码库作为上下文，本质是结构化文档的长上下文检索工程，对大规模技术文档理解有借鉴意义 |

### 🎭 多模态推理

| 项目 | Stars | 今日新增 | 一句话说明 |
|:---|:---|:---|:---|
| **[run-llama/llama_index](https://github.com/run-llama/llama_index)** | 49,613 | — | **多模态文档Agent**，支持图像、文本、表格的联合推理与跨模态检索，VLM应用的关键中间件 |
| **[Y-Research-SBU/PosterGen](https://github.com/Y-Research-SBU/PosterGen)** | 235 | — | **CVPR 2026 Findings**，学术海报生成模型，涉及视觉-文本布局理解与生成式多模态对齐，HMER相关技术可迁移 |
| **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | 17,470 | — | **Agent记忆控制平面**，支持多模态信息的长期记忆编码与上下文重构，跨模态记忆管理的基础设施 |

### 🧠 长上下文与推理

| 项目 | Stars | 今日新增 | 一句话说明 |
|:---|:---|:---|:---|
| **[NVlabs/LongLive](https://github.com/NVlabs/LongLive)** | — | +79 | **LongLive 2.0: 长视频生成基础设施**，NVIDIA官方项目，长时序一致性推理与上下文保持的核心技术，直接关联长上下文建模 |
| **[testtimescaling/testtimescaling.github.io](https://github.com/testtimescaling/testtimescaling.github.io)** | 98 | — | **Test-Time Scaling综述**，系统梳理LLM推理时计算扩展的what/how/where/how well，长上下文推理优化的关键理论资源 |
| **[yichuan-w/LEANN](https://github.com/yichuan-w/LEANN)** | 11,676 | — | **97%存储节省的本地RAG**，长上下文压缩与高效检索的工程突破，边缘部署场景的核心使能技术 |
| **[skyzh/tiny-llm](https://github.com/skyzh/tiny-llm)** | 4,202 | — | **Apple Silicon上的vLLM实现**，针对长上下文推理服务的系统级优化，含KV Cache管理与内存高效调度 |
| **[EgoAlpha/prompt-in-context-learning](https://github.com/EgoAlpha/prompt-in-context-learning)** | 2,235 | — | **上下文学习前沿资源**，长上下文利用策略与示例选择，ICL效率优化的研究入口 |
| **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | 17,470 | — | **Agent记忆控制平面**，6行代码实现AI Agent的长期记忆管理，解决上下文窗口外的信息持久化问题 |

### 🔧 Post-Training 与对齐

| 项目 | Stars | 今日新增 | 一句话说明 |
|:---|:---|:---|:---|
| **[jingyaogong/minimind](https://github.com/jingyaogong/minimind)** | 50,450 | — | **2小时从零训练64M参数LLM**，完整覆盖预训练→SFT→RLHF pipeline，post-training对齐的教学级实现 |
| **[thinkwee/AwesomeOPD](https://github.com/thinkwee/AwesomeOPD)** | 439 | — | **On-Policy Distillation综述**，在线策略蒸馏前沿，DPO/RLHF的替代与补充方向，对齐效率优化的关键资源 |
| **[testtimescaling/testtimescaling.github.io](https://github.com/testtimescaling.github.io)** | 98 | — | **推理时对齐策略综述**，Test-Time Scaling与推理时偏好优化，post-training向inference-time迁移的理论基础 |
| **[galilai-group/stable-pretraining](https://github.com/galilai-group/stable-pretraining)** | 234 | — | **稳定预训练库**，世界模型训练的可靠性工程，为后续对齐阶段提供更稳定的初始化基础 |
| **[0xPlaygrounds/rig](https://github.com/0xPlaygrounds/rig)** | 7,388 | — | **Rust LLM应用框架**，模块化推理架构，支持可插拔的对齐策略与推理时干预 |

### 👁️ 幻觉与可靠性

| 项目 | Stars | 今日新增 | 一句话说明 |
|:---|:---|:---|:---|
| **[open-compass/opencompass](https://github.com/open-compass/opencompass)** | 7,020 | — | **LLM评测平台**，覆盖100+数据集的多维评测，含幻觉检测、事实性验证与可信度校准基准 |
| **[run-llama/llama_index](https://github.com/run-llama/llama_index)** | 49,613 | — | **RAG事实 grounding**，通过检索增强生成缓解幻觉，文档级事实验证的核心工程实践 |
| **[yichuan-w/LEANN](https://github.com/yichuan-w/LEANN)** | 11,676 | — | **100%私有RAG**，本地部署消除外部API的不确定性，提升生成内容的可追溯性与可靠性 |

### 🏗️ 基础设施

| 项目 | Stars | 今日新增 | 一句话说明 |
|:---|:---|:---|:---|
| **[run-llama/llama_index](https://github.com/run-llama/llama_index)** | 49,613 | — | **文档智能基础设施**，OCR+RAG+Agent的完整技术栈，研究到产品的关键桥梁 |
| **[jingyaogong/minimind](https://github.com/jingyaogong/minimind)** | 50,450 | — | **轻量LLM训练框架**，完整pipeline开源，对齐算法快速验证的理想沙盒 |
| **[open-compass/opencompass](https://github.com/open-compass/opencompass)** | 7,020 | — | **评测基础设施**，支持多模态模型与对齐方法的系统性评估 |
| **[skyzh/tiny-llm](https://github.com/skyzh/tiny-llm)** | 4,202 | — | **推理服务教学框架**，长上下文KV Cache优化与调度策略的实验平台 |
| **[0xPlaygrounds/rig](https://github.com/0xPlaygrounds/rig)** | 7,388 | — | **Rust LLM工程框架**，类型安全的模型调用与工具编排，对齐策略的模块化实现 |
| **[galilai-group/stable-pretraining](https://github.com/galilai-group/stable-pretraining)** | 234 | — | **稳定训练基础设施**，减少预训练不稳定性导致的下游对齐困难 |

---

## 3. 研究趋势信号分析

今日数据揭示三个关键趋势：**其一，长上下文正从"模型能力"转向"系统工程"**——NVlabs/LongLive、LEANN、zilliztech/claude-context等项目聚焦上下文压缩、检索增强与记忆管理，而非单纯扩展窗口长度，表明社区认识到"有效利用"比"无限延长"更具实用价值。**其二，Test-Time Scaling成为对齐新前沿**——testtimescaling.github.io的登榜与thinkwee/AwesomeOPD的活跃，显示研究重心正从训练时RLHF/DPO向推理时计算扩展与在线策略优化迁移，这与DeepSeek-R1、OpenAI o系列模型的发布逻辑一致。**其三，OCR/文档智能与多模态推理的基建化**——LlamaIndex明确 rebranding 为"OCR platform"，标志文档理解从单一功能进化为Agent核心能力，而Y-Research-SBU/PosterGen等CVPR工作则显示视觉-文本对齐仍在向细粒度场景渗透。值得注意的是，**HMER（手写数学表达式识别）专项开源项目仍显稀缺**，今日数据中无直接对应，表明该领域仍以学术闭源为主，存在显著开源空白。

---

## 4. 研究关注热点

- **[testtimescaling/testtimescaling.github.io](https://github.com/testtimescaling/testtimescaling.github.io)** — **推理时对齐的理论基础**
  - **理由**：首篇系统性Test-Time Scaling综述，直接关联长上下文推理优化与post-training向inference-time的范式转移
  - **相关性**：为幻觉缓解提供新路径（推理时自我修正）、为长上下文利用提供计算分配策略

- **[yichuan-w/LEANN](https://github.com/yichuan-w/LEANN)** — **边缘侧长上下文RAG**
  - **理由**：97%存储压缩+本地部署，解决长文档OCR后的实际部署瓶颈，MLsys2026收录验证其系统创新性
  - **相关性**：OCR/HMER场景的海量公式/符号数据亟需此类压缩检索技术

- **[NVlabs/LongLive](https://github.com/NVlabs/LongLive)** — **长时序一致性生成**
  - **理由**：NVIDIA官方长视频生成2.0，长上下文保持与一致性推理的工业级实践
  - **相关性**：视频级长上下文技术可迁移至长文档、长公式序列的连贯理解

- **[thinkwee/AwesomeOPD](https://github.com/thinkwee/AwesomeOPD)** — **在线策略蒸馏**
  - **理由**：On-Policy Distillation作为DPO/RLHF的轻量替代，降低对齐成本与稳定性风险
  - **相关性**：为HMER/OCR模型的领域适配提供高效对齐方案，减少幻觉

- **[jingyaogong/minimind](https://github.com/jingyaogong/minimind)** — **对齐算法快速验证平台**
  - **理由**：50K+ stars的轻量训练框架，完整SFT/RLHF pipeline，2小时可复现
  - **相关性**： ideal沙盒用于测试新型幻觉缓解策略与多模态对齐方法

---

*报告生成时间：2026-05-23 | 数据覆盖：GitHub Trending + AI主题搜索（7天活跃）*

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*