# ArXiv AI 研究日报 2026-05-23

> 数据来源: [ArXiv](https://arxiv.org/) (cs.AI, cs.CL, cs.LG) | 共 50 篇论文 | 生成时间: 2026-05-23 00:30 UTC

---

# ArXiv AI 研究日报 | 2026-05-23

---

## 今日速览

今日ArXiv共收录50篇AI核心论文，**智能体自进化与系统安全**成为最突出主题：MOSS提出首个源代码级自改写智能体框架，LCGuard为KV缓存共享建立安全屏障，DeltaBox实现毫秒级沙箱状态回滚以支撑大规模测试时搜索。**后训练范式革新**同样亮眼，"Post-Training is About States, Not Tokens"从状态分布视角统一SFT/RL/蒸馏的理论框架。此外，**tokenization基础层**出现两项重要进展——凸松弛优化与分裂树方法分别从数学基础和压缩效率角度挑战BPE霸权。

---

## 重点论文

### 🧠 大语言模型（架构、训练、对齐、评估）

| 论文 | 作者 | 一句话说明 |
|:---|:---|:---|
| **[Post-Training is About States, Not Tokens: A State Distribution View of SFT, RL, and On-Policy Distillation](http://arxiv.org/abs/2605.22731v1)** | Dong Nie | 跳出损失函数视角，从状态分布角度重新统一理解SFT、RL和蒸馏，为后训练理论提供新范式。 |
| **[Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention](http://arxiv.org/abs/2605.22791v1)** | Ali Hatamizadeh, Yejin Choi, Jan Kautz | 在线性注意力中解耦"擦除"与"写入"操作，解决压缩记忆编辑时的关联扰动难题，线性复杂度下的注意力新架构。 |
| **[Tokenisation via Convex Relaxations](http://arxiv.org/abs/2605.22821v1)** | Jan Tempus, Philip Whittington, Craig W. Schmidt et al. | 将BPE/Unigram的贪婪策略重构为线性规划全局优化问题，tokenization首次获得数学上严格的凸松弛解法。 |
| **[Tokenization with Split Trees](http://arxiv.org/abs/2605.22705v1)** | Craig W. Schmidt, Michael Krumdick, Adam Wiemerslage et al. | 提出ToaST方法，用完整二叉树递归分割pretoken，无需预定义词表即可直接优化压缩率，推理效率与灵活性兼得。 |
| **[Understanding Data Temporality Impact on Large Language Models Pre-training](http://arxiv.org/abs/2605.22769v1)** | Pilchen Hippolyte, Fabre Romain, Signe Talla Franck et al. | 系统研究预训练数据的时间动态对时序知识获取的影响，揭示shuffle策略如何冻结模型的时间感知能力。 |
| **[Reducing Political Manipulation with Consistency Training](http://arxiv.org/abs/2605.22771v1)** | Long Phan, Devin Kim, Alexander Pan et al. | 识别LLM中7类"隐蔽政治偏见"技术，通过一致性训练降低模型在政治敏感话题上的不对称操纵风险。 |
| **[AMEL: Accumulated Message Effects on LLM Judgments](http://arxiv.org/abs/2605.22714v1)** | Sid-ali Temkit | 发现对话历史极性会系统性偏置LLM作为评判者的后续判断，揭示多轮评估中的累积消息效应陷阱。 |
| **[Posterior Collapse as Automatic Spectral Pruning](http://arxiv.org/abs/2605.22691v1)** | Johannes Hirn | 证明β-VAE中的后验坍塌本质是自动谱剪枝，不同β值揭示潜变量从无用到有用的级联坍塌模式，深化生成模型可解释性。 |

### 🤖 智能体与推理（规划、工具使用、多智能体、思维链）

| 论文 | 作者 | 一句话说明 |
|:---|:---|:---|
| **[MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems](http://arxiv.org/abs/2605.22794v1)** | Qianshu Cai, Yonggang Zhang, Xianzhang Jia et al. | 突破文本可修改工件的局限，实现智能体**源代码级自改写**，部署后持续从用户交互中学习进化，终结"静态部署-等待人工修复"范式。 |
| **[LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems](http://arxiv.org/abs/2605.22786v1)** | Sadia Asif, Mohammad Mohammadi Amiri, Momin Abbas et al. | 为基于KV缓存隐式通信的多智能体系统建立安全屏障，防止恶意智能体通过潜空间通道窃取信息或注入攻击。 |
| **[DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback](http://arxiv.org/abs/2605.22781v1)** | Yunpeng Dong, Jingkai He, Yuze Hou et al. | 实现毫秒级完整沙箱状态（文件+进程内存+上下文）的checkpoint/rollback，使测试时树搜索和RL在AI Agent中真正可扩展。 |
| **[Vector Policy Optimization: Training for Diversity Improves Test-Time Search](http://arxiv.org/abs/2605.22817v1)** | Ryan Bahlous-Boldi, Isha Puri, Idan Shenfeld et al. | 训练阶段优化策略多样性而非单一奖励，使LLM在AlphaEvolve等测试时搜索中适配多样任务特定奖励函数。 |
| **[Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration](http://arxiv.org/abs/2605.22814v1)** | Lily Goli, Justin Kerr, Daniele Reda et al. | 将情景记忆与持久世界模型结合，解决好奇心驱动RL在3D环境中的灾难性遗忘与探索效率问题。 |
| **[Advancing Mathematics Research with AI-Driven Formal Proof Search](http://arxiv.org/abs/2605.22763v1)** | George Tsoukalas, Anton Kovsharov, Sergey Shirobokov et al. | 首次大规模评估LLM生成Lean形式证明解决研究级数学问题的能力，为AI辅助数学研究建立系统基准。 |

### 🔧 方法与框架（新技术、基准测试、效率优化）

| 论文 | 作者 | 一句话说明 |
|:---|:---|:---|
| **[The Matching Principle: A Geometric Theory of Loss Functions for Nuisance-Robust Representation Learning](http://arxiv.org/abs/2605.22800v1)** | Vishal Rajput | 用统一几何框架涵盖鲁棒性、域适应、光照不变性、组合泛化等看似无关的问题，揭示它们共享的结构——匹配原理。 |
| **[Proxy-Based Approximation of Shapley and Banzhaf Interactions](http://arxiv.org/abs/2605.22738v1)** | Santo M. A. R. Thies, Hubert Baniecki, R. Teal Witter et al. | ProxySHAP以可扩展方式精确估计高阶Shapley/Banzhaf交互，克服现有方法在速度与精度间的权衡困境。 |
| **[The Distillation Game: Adaptive Attacks & Efficient Defenses](http://arxiv.org/abs/2605.22737v1)** | Youssef Allouah, Mahdi Haghifam, Sanmi Koyejo et al. | 将模型蒸馏攻防建模为师生间的minimax博弈，导出效用约束下的最优防御策略，量化"有用性-可模仿性"权衡。 |
| **[HarnessAPI: A Skill-First Framework for Unified Streaming APIs and MCP Tools](http://arxiv.org/abs/2605.22733v1)** | Edwin Jose | 终结LLM工具的"双轨制"困境，单一Python函数同时暴露为HTTP端点和MCP工具，业务逻辑与协议适配彻底解耦。 |

### 📊 应用（垂直领域、多模态、代码生成）

| 论文 | 作者 | 一句话说明 |
|:---|:---|:---|
| **[Evaluating Commercial AI Chatbots as News Intermediaries](http://arxiv.org/abs/2605.22785v1)** | Mirac Suzgun, Emily Shen, Federico Bianchi et al. | 首次系统测量ChatGPT、Gemini等商业聊天机器人在14天跨语言新闻周期中的事实准确性，揭示检索-合成管道的时效性盲区。 |
| **[CogAdapt: Transferring Clinical ECG Foundation Models to Wearable Cognitive Load Assessment via Lead Adaptation](http://arxiv.org/abs/2605.22774v1)** | Amir Mousavi, Mohammad Sadegh Sirjani, Erfan Nourbakhsh et al. | 通过导联自适应将百万级临床ECG基础模型迁移至可穿戴设备，解决认知负荷评估的标注稀缺与跨被试泛化难题。 |
| **[ChronoMedKG: A Temporally-Grounded Biomedical Knowledge Graph and Benchmark for Clinical Reasoning](http://arxiv.org/abs/2605.22734v1)** | Md Shamim Ahmed, Farzaneh Firoozbakht, Lukas Galke Poech et al. | 构建首个时间感知的生物医学知识图谱，同一症状在3岁与13岁指向不同疾病，为临床时序推理提供基准。 |
| **[Forecasting Scientific Progress with Artificial Intelligence](http://arxiv.org/abs/2605.22681v1)** | Sean Wu, Pan Lu, Yupeng Chen et al. | 在受控知识约束下评估AI预测科学进展的能力，建立时间 grounded 的预测框架，探索AI能否预见自身发展轨迹。 |
| **[Superhuman Safe and Agile Racing through Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2605.22748v1)** | Ismail Geles, Leonard Bauersfeld, Markus Wulfmeier et al. | 多智能体RL在真实赛车中超越人类，关键突破是将其他车辆视为策略性参与者而非环境噪声，解决物理AI的 brittle 难题。 |

---

## 研究趋势信号

**智能体基础设施层爆发**：今日出现MOSS（自进化）、LCGuard（安全通信）、DeltaBox（状态管理）三项正交创新，标志Agent系统从"功能实现"进入"工程化运维"阶段。同时，**测试时计算扩展**成为共识——Vector Policy Optimization训练多样性策略、DeltaBox支撑毫秒级回滚搜索、Clipping Bottleneck稳定RLVR，三者共同指向"训练为搜索服务"的新范式。值得注意的是，**Tokenization基础层**在沉寂多年后迎来双突破（凸松弛+分裂树），预示预训练Pipeline的底层重构可能启动。

---

## 值得精读

### 1. [MOSS: Self-Evolution through Source-Level Rewriting](http://arxiv.org/abs/2605.22794v1)
**理由**：现有自进化智能体仅修改技能文件、提示词等"文本工件"，MOSS首次实现**运行时源代码自改写**，从根本上打破"部署即冻结"的范式。其技术路径（程序合成+差分测试+回滚保护）与哲学含义（智能体获得真正自主性）均具里程碑意义，可能重新定义Agent的维护经济学。

### 2. [Post-Training is About States, Not Tokens](http://arxiv.org/abs/2605.22731v1)
**理由**：SFT/RL/Distillation的理论分析长期被损失函数视角割裂，本文提出**状态分布视角**的统一框架，揭示三种方法本质是对状态访问分布的不同塑形。这一视角转换可能解释为何某些"理论上次优"的实践（如DPO）效果良好，并为后训练算法设计提供新原则。

### 3. [The Matching Principle](http://arxiv.org/abs/2605.22800v1)
**理由**：将鲁棒学习、域适应、组合泛化、对齐安全等**八个独立研究领域**纳入统一几何框架，声称它们共享"匹配原理"这一深层结构。若理论成立，将大幅简化方法设计空间——面对新场景时无需从零发明专用技术，而是求解匹配约束的特定实例。其野心与统一性值得验证。

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*