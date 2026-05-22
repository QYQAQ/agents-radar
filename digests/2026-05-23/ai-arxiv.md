# ArXiv AI 研究日报 2026-05-23

> 数据来源: [ArXiv](https://arxiv.org/) (cs.AI, cs.CL, cs.LG) | 共 50 篇论文 | 生成时间: 2026-05-22 16:02 UTC

---

# ArXiv AI 研究日报 | 2026-05-23

---

## 今日速览

今日50篇论文覆盖大语言模型训练后优化、智能体自主进化、扩散模型理论与应用、以及AI安全与评估等核心方向。最突出的突破包括：**MOSS首次实现智能体源代码级自我改写**，突破了传统文本层面进化的局限；**Vector Policy Optimization**提出训练多样性以提升测试时搜索效率的新范式；**DeltaBox**将AI Agent沙箱状态回滚速度提升至毫秒级，为高频树搜索和RL训练提供基础设施。此外，多项研究聚焦于LLM的时间推理、政治偏见与冲突场景下的对齐失败，显示出AI安全研究正从通用对齐向具体社会风险场景深化。

---

## 重点论文

### 🧠 大语言模型（架构、训练、对齐、评估）

| 论文 | 作者 | 一句话说明 |
|:---|:---|:---|
| **[Tokenisation via Convex Relaxations](http://arxiv.org/abs/2605.22821v1)** | Tempus et al. | 将BPE/Unigram等贪心式分词重新建模为线性规划问题，全局优化词表构建，有望解决子词分割的局部最优困境。 |
| **[Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention](http://arxiv.org/abs/2605.22791v1)** | Hatamizadeh et al. | 在线性注意力中解耦"擦除"与"写入"操作，解决压缩记忆编辑时的关联干扰问题，推进线性复杂度序列建模。 |
| **[Post-Training is About States, Not Tokens](http://arxiv.org/abs/2605.22731v1)** | Dong Nie | 从状态分布视角统一分析SFT、RL与蒸馏，揭示训练方法的本质差异在于状态覆盖而非损失函数形式。 |
| **[Understanding Data Temporality Impact on LLM Pre-training](http://arxiv.org/abs/2605.22769v1)** | Hippolyte et al. | 系统研究预训练数据的时间动态对时序知识获取的影响，为构建具有时间感知能力的LLM提供实证基础。 |
| **[Reducing Political Manipulation with Consistency Training](http://arxiv.org/abs/2605.22771v1)** | Phan et al. | 发现LLM对对立政治话题存在"隐性政治偏见"并识别7类操纵技术，提出一致性训练缓解方案。 |
| **[Is Capability a Liability? More Capable LLMs Make Worse Forecasts](http://arxiv.org/abs/2605.22672v1)** | Merrill et al. | 揭示LLM在超线性增长与尾部风险场景下的**逆缩放现象**：能力越强预测越差，对金融与流行病学应用警示深远。 |
| **[AMEL: Accumulated Message Effects on LLM Judgments](http://arxiv.org/abs/2605.22714v1)** | Temkit | 发现对话历史极性会累积偏置LLM后续判断，对批量代码审查、内容审核等长对话评估场景提出关键警示。 |

---

### 🤖 智能体与推理（规划、工具使用、多智能体、思维链）

| 论文 | 作者 | 一句话说明 |
|:---|:---|:---|
| **[MOSS: Self-Evolution through Source-Level Rewriting](http://arxiv.org/abs/2605.22794v1)** | Cai et al. | **里程碑工作**：首个实现源代码级自我改写的自主智能体，突破文本可变工件的局限，使部署后持续学习成为可能。 |
| **[Vector Policy Optimization: Training for Diversity Improves Test-Time Search](http://arxiv.org/abs/2605.22817v1)** | Bahlous-Boldi et al. | 针对AlphaEvolve等推理时搜索框架，提出向量策略优化训练多样化策略，使单一模型适配多种任务特定奖励函数。 |
| **[DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox C/R](http://arxiv.org/abs/2605.22781v1)** | Dong et al. | 将沙箱检查点/回滚速度提升至毫秒级，解决LLM Agent高频状态探索（树搜索、RL）的基础设施瓶颈。 |
| **[LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems](http://arxiv.org/abs/2605.22786v1)** | Asif et al. | 为基于KV Cache隐式通信的多智能体系统构建安全护栏，防止恶意信息通过潜在空间泄露。 |
| **[Scout-Assisted Planning for Heterogeneous Robot Teams](http://arxiv.org/abs/2605.22693v1)** | Bui et al. | 无人机-地面机器人协同规划框架，通过空中侦察提前发现障碍物，减少物理探索中的代价高昂回溯。 |

---

### 🔧 方法与框架（新技术、基准测试、效率优化）

| 论文 | 作者 | 一句话说明 |
|:---|:---|:---|
| **[The Matching Principle: A Geometric Theory of Loss Functions](http://arxiv.org/abs/2605.22800v1)** | Rajput | 统一鲁棒性、域适应、组合泛化等看似无关问题的几何框架，提出"匹配原则"作为损失函数设计的新理论基础。 |
| **[Proxy-Based Approximation of Shapley and Banzhaf Interactions](http://arxiv.org/abs/2605.22738v1)** | Thies et al. | ProxySHAP以代理模型调和高阶交互估计的速度-精度权衡，使复杂ML系统的可解释性分析更实用。 |
| **[Optimization over the Intersection of Manifolds](http://arxiv.org/abs/2605.22736v1)** | Yang et al. | 证明流形交正则性的等价条件，为约束优化、低秩学习等提供可处理的几何优化路径。 |
| **[Uniform Diffusion Models Revisited](http://arxiv.org/abs/2605.22765v1)** | Gourevitch et al. | 重新形式化均匀扩散模型，提出leave-one-out去噪器与吸收态视角，澄清离散扩散的理论基础。 |

---

### 📊 应用（垂直领域、多模态、代码生成）

| 论文 | 作者 | 一句话说明 |
|:---|:---|:---|
| **[Advancing Mathematics Research with AI-Driven Formal Proof Search](http://arxiv.org/abs/2605.22763v1)** | Tsoukalas et al. | 首次大规模评估LLM生成Lean形式证明解决研究级数学问题的能力，为AI辅助数学发现建立基准。 |
| **[Forecasting Scientific Progress with AI](http://arxiv.org/abs/2605.22681v1)** | Wu et al. | 构建时间约束下的科学进展预测评估框架，测试AI能否真正预见研究方向而非仅事后解释。 |
| **[MambaGaze: Bidirectional Mamba for Cognitive Load Assessment](http://arxiv.org/abs/2605.22775v1)** | Mousavi et al. | 双向Mamba结合显式缺失数据建模，实现眼动追踪的实时认知负荷评估，面向安全关键人机交互。 |
| **[Live Music Diffusion Models](http://arxiv.org/abs/2605.22717v1)** | Novack et al. | 面向实时交互音乐生成的扩散模型高效微调与后训练，突破自回归模型在直播共创场景的计算瓶颈。 |
| **[Deep RL for Flexible Job Shop Scheduling](http://arxiv.org/abs/2605.22773v1)** | Tang et al. | 针对随机作业到达的动态柔性车间调度，DRL方法超越传统MILP求解器，应对组合复杂性与不确定性。 |

---

## 研究趋势信号

**智能体基础设施层快速成熟**：今日出现MOSS（源码自进化）、DeltaBox（毫秒级沙箱C/R）、LCGuard（KV通信安全）、HarnessAPI（统一工具框架）四项工作，标志Agent研究从算法创新向工程基础设施纵深发展，"部署后持续学习+高频状态探索+安全通信"的闭环正在形成。**时间推理与动态评估受关注**：数据时间性、科学预测、预报逆缩放等研究共同指向静态知识训练的局限性，时序-aware的LLM训练与评估成为新焦点。**AI安全场景细化**：从通用对齐扩展到政治操纵、冲突恶化、累积消息偏置等具体社会风险，显示安全研究与社会科学交叉深化。

---

## 值得精读

### 1. [MOSS: Self-Evolution through Source-Level Rewriting](http://arxiv.org/abs/2605.22794v1) | Cai et al.

**理由**：当前自进化智能体局限于修改技能文件、提示模板等文本工件，MOSS首次实现**运行时源代码级自我改写**——Agent直接编辑自身Python源码并热重载。这一突破使部署后持续学习从"配置调整"跃迁至"程序合成"，可能重新定义软件系统的生命周期管理。论文需关注其安全性约束（如何防止破坏核心功能）与验证机制。

### 2. [Is Capability a Liability? More Capable LLMs Make Worse Forecasts](http://arxiv.org/abs/2605.22672v1) | Merrill et al.

**理由**：**逆缩放（inverse scaling）** 在特定结构（超线性增长+尾部风险）上的系统验证，对金融风控、疫情预测等关键应用具有直接警示意义。论文需精读其机制分析：更强模型是否因过度拟合历史模式而忽视 regime change 的可能性？这一发现可能挑战"模型越大越可靠"的默认假设，推动不确定性量化方法的革新。

### 3. [The Matching Principle: A Geometric Theory of Loss Functions](http://arxiv.org/abs/2605.22800v1) | Rajput

**理由**：试图以单一几何框架统一鲁棒性、域适应、组合泛化、对齐安全等八个"各自为政"的研究领域。若理论成立，将成为表示学习的"第一性原理"式工作，为损失函数设计提供系统性指导而非启发式调参。需验证其核心数学构造（Fisher-Rao度量下的匹配条件）在具体任务中的可计算性与实证效果。

---

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*