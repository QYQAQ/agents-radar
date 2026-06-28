# Hugging Face 热门模型日报 2026-06-28

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-28 00:32 UTC

---

# Hugging Face 研究模型日报 | 2026-06-28

## 今日速览

本周 Hugging Face 生态呈现 **OCR 与多模态深度融合**、**长上下文推理模型爆发**、**后训练对齐技术活跃** 三大趋势。百度发布的 **Unlimited-OCR** 以 21 万下载量成为文档理解领域焦点，其"无限长度"OCR 定位直接冲击长上下文文档识别瓶颈；**GLM-5.2** 系列（含 MoE 架构与 NVFP4 量化版本）与 **Qwen3.6-35B-A3B** 多模态变体显示中文模型家族在视觉-语言推理上的持续迭代；值得关注的是 **HauhauCS** 等社区微调者密集推出"Uncensored/Aggressive"变体，反映 post-training 对齐与安全性博弈已成为开源生态的核心研究战场。幻觉缓解方面虽无直接冠名模型，但 **DeepSeek-V4-Pro-DSpark** 的 arxiv 引用与 **Microsoft FastContext-1.0-4B-SFT** 的"Explorer SubAgent"标签暗示长上下文事实性检索正成为新切入点。

---

## 热门模型（按研究相关性分类）

### 📄 OCR 与文档模型

| 模型 | 作者 | 点赞 | 下载 | 研究相关性说明 |
|:---|:---|:---|:---|:---|
| **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** | baidu | 1,137 | 212,760 | **核心关注**：突破传统 OCR 上下文长度限制的"无限长度"文档识别模型，直接关联 **HMER（手写数学公式识别）与长文档版面分析** 研究；其 feature-extraction 标签暗示视觉编码器可能支持复杂文档结构（表格、公式、多栏）的层级表征，值得拆解其长序列处理机制。 |

---

### 🎭 多模态与视觉语言

| 模型 | 作者 | 点赞 | 下载 | 研究相关性说明 |
|:---|:---|:---|:---|:---|
| **[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)** | MiniMaxAI | 1,253 | 182,714 | 新兴多模态架构，明确标注 `minimax_m3_vl` 与 `multimodal` 标签，其视觉-语言融合方式可能提供不同于 Qwen/Gemma 的跨模态对齐范式，适合作为 **多模态推理对比基线**。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 2,277 | 3,331,475 | **现象级下载量**（330 万）揭示社区对"去对齐"视觉语言模型的强烈需求；其 `vision` + `moe` + `uncensored` 三重属性使其成为 **多模态幻觉与安全性权衡** 的极端实验样本，可研究 post-training 移除安全约束后视觉 grounding 的退化模式。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 2,406 | 570,466 | NVIDIA 官方定位模型，`image-feature-extraction` 与 `locateanything` 标签指向 **细粒度视觉定位与指代表达理解**，对评估 VLM 空间推理幻觉具有工具价值。 |
| **[HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced](https://huggingface.co/HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced)** | HauhauCS | 96 | 32,222 | QAT 量化 + 去对齐的 Gemma4 视觉变体，"Balanced"与"Aggressive"形成 **对齐强度消融对比**，适合量化后训练对多模态能力的影响研究。 |
| **[Jackrong/Qwopus3.6-27B-Coder-Compat-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-Coder-Compat-MTP-GGUF)** | Jackrong | 97 | 49,935 | `MTP`（Multi-Token Prediction）+ `vision` 组合罕见，可能探索 **视觉-代码联合推理中的并行解码策略**，对多模态推理效率研究有启发。 |
| **[deepreinforce-ai/Ornith-1.0-9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)** / **[35B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B)** / **[397B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-397B)** | deepreinforce-ai | 166/161/120 | 1,501/7,571/463 | 覆盖 9B 到 397B 的 Qwen3.5 视觉语言模型系列，MIT 许可证 + 全尺度 GGUF 化，提供 **多模态能力随规模扩展的系统性研究素材**，尤其 397B 稀疏 MoE 的幻觉模式尚未被充分分析。 |

---

### 🧠 长上下文与推理模型

| 模型 | 作者 | 点赞 | 下载 | 研究相关性说明 |
|:---|:---|:---|:---|:---|
| **[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)** | zai-org | 2,676 | 98,994 | **GLM 系列重大更新**，`glm_moe_dsa` 标签暗示 MoE + 动态稀疏注意力（DSA）架构，可能针对长上下文推理优化；作为国产开源核心基座，其 **长序列数学推理与代码生成能力** 需重点评估。 |
| **[unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)** | unsloth | 426 | 125,230 | Unsloth 快速量化适配，使 GLM-5.2 可在消费级硬件测试长上下文推理，**降低长序列研究门槛**。 |
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft | 365 | 6,447 | **直接命中研究关键词**：`Explorer SubAgent` 标签明确指向 **长上下文检索增强与事实定位**，4B 小参数设计可能探索"小模型+长上下文"vs"大模型+短上下文"的效率边界，对幻觉缓解中的证据检索机制极具参考价值。 |
| **[WeiboAI/VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)** | WeiboAI | 742 | 57,521 | `math` 标签 + 3B 极小参数，专注 **数学推理的思维链效率**，可能采用新型推理时计算扩展策略，适合作为轻量级推理基线。 |
| **[yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)** | yuxinlu1 | 2,426 | 536,130 | `fable5` + `composer2.5` + `reasoning` 复合标签暗示 **多阶段推理合成与代码生成** 的复杂后训练流程，其高下载量反映社区对"推理增强型代码模型"的偏好。 |
| **[deepseek-ai/DeepSeek-V4-Pro-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark)** | deepseek-ai | 123 | 0 | **arxiv:2606.19348** 预印本关联，零下载量暗示刚发布或受限访问；DeepSeek-V4 的 `DSpark` 变体可能聚焦 **分布式推理火花（Spark）与长上下文并行处理**，需追踪论文以确认技术细节。 |

---

### 🔧 Post-Training 与对齐

| 模型 | 作者 | 点赞 | 下载 | 研究相关性说明 |
|:---|:---|:---|:---|:---|
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 2,277 | 3,331,475 | **对齐研究的"反面教材"金矿**："Aggressive"去对齐策略的极端应用，可系统研究 **RLHF 安全约束移除后模型行为的定量变化**，包括幻觉率、事实性与有害输出的权衡曲线。 |
| **[huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated)** | huihui-ai | 137 | 6,250 | `abliterated` 标签为 **对齐消融（ablation of alignment）** 的标准化术语，该模型提供 Gemma4 代码模型的"去对齐"版本，与 HauhauCS 系列形成 **不同基座、相同目标的对照实验组**。 |
| **[Qwen/Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)** | Qwen | 357 | 18,872 | 官方 `qwen3_5_moe` + `image-text-to-text` + 隐含 Agent 能力，可能集成 **工具使用与多轮对话的强化学习**，是研究"对齐后 Agent 安全性"的官方基准。 |
| **[yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)** | yuxinlu1 | 729 | 206,828 | `agentic` + `3.5x-tau2` 参数暗示 **推理温度或采样策略的精细调优**，`terminal` 标签指向自主执行环境，是研究 **Agent 对齐与工具调用幻觉** 的实用载体。 |

---

### 👁️ 幻觉缓解（间接相关）

| 模型 | 作者 | 点赞 | 下载 | 研究相关性说明 |
|:---|:---|:---|:---|:---|
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft | 365 | 6,447 | **最接近直接相关**：`Explorer SubAgent` 架构可能实现 **长文档中的细粒度事实检索与引用生成**，是缓解生成式幻觉的"检索增强生成"路线新探索；4B 规模暗示效率优先的 grounding 策略。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 2,406 | 570,466 | 视觉定位精度是 **多模态幻觉检测的前置条件**——模型能否准确指向证据区域，直接决定其声称的可验证性；可作为 VLM 幻觉评测的辅助工具模型。 |

---

### 🏗️ 研究基础设施

| 模型 | 作者 | 点赞 | 下载 | 研究相关性说明 |
|:---|:---|:---|:---|:---|
| **[nvidia/GLM-5.2-NVFP4](https://huggingface.co/nvidia/GLM-5.2-NVFP4)** | nvidia | 125 | 6,464 | NVIDIA 官方 `ModelOpt` + `NVFP4` 4-bit 浮点量化，为 **长上下文模型的高效推理与评测** 提供硬件-算法协同基础设施，利于大规模幻觉/推理实验的成本控制。 |
| **[nvidia/Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4)** | nvidia | 366 | 5,022,254 | **500 万下载量** 的量化标杆，证明 MoE 多模态模型的 4-bit 推理已成熟，使 **Qwen3.6 全系列幻觉与对齐研究** 可在单卡运行，极大降低实验门槛。 |

---

## 研究生态信号

**Qwen/Gemma 双寡头主导多模态开源，GLM 崛起为长上下文第三极。** 本周 30 个热门模型中，Qwen3.5/3.6 衍生模型占 11 个（含官方、社区微调、量化版），Gemma4 占 4 个，两者构成视觉语言与代码推理的"基座-微调"生态核心；GLM-5.2 以 MoE+DSA 新架构入场，获 NVIDIA 官方量化背书，可能成为长上下文领域的新选项。**Post-training 对齐呈现"军备竞赛"特征**：HauhauCS、huihui-ai 等微调者系统性地对主流模型进行"去对齐"（uncensored/abliterated），下载量远超官方版本（330 万 vs 1.8 万），反映开源社区对安全约束的反弹，也为 **对齐鲁棒性、红队测试、可撤销对齐（unalignment）** 等研究提供了前所未有的实验材料。OCR 领域百度 Unlimited-OCR 的"无限长度"定位填补了长文档端到端识别的空白，但其技术细节（是否采用滑动窗口、层次化注意力或外推位置编码）尚待解析。幻觉缓解仍缺乏直接冠名模型，但 Microsoft FastContext 的"SubAgent"架构与 DeepSeek-V4 的分布式推理暗示，**"检索-生成"解耦与推理时计算扩展** 正成为间接应对路径。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| **🔥 最高** | **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** | 唯一明确突破 OCR 上下文长度限制的模型，对 **HMER 中超长公式序列、学术论文全文版面分析、古籍连续版面识别** 等任务具有直接应用价值；需验证其"无限"是营销术语还是真正的外推/压缩机制，拆解其视觉编码器与序列解码器的协同设计。 |
| **🔥 最高** | **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | 4B 参数 + "Explorer SubAgent" + SFT 的组合罕见，可能实现 **小模型驱动的长文档证据检索与事实校验**，是"以检索缓解幻觉"路线的轻量化尝试；可与 7B+ 模型对比，验证"小模型精确定位 + 大模型生成"的分层幻觉缓解架构。 |
| **🔥 高** | **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | 330 万下载量的极端去对齐样本，提供 **系统性研究对齐移除效应的稀缺材料**：可定量对比其与官方 Qwen3.6 在事实问答、视觉 grounding、多模态推理中的幻觉率差异，构建"对齐强度-幻觉模式-安全性"的三维分析框架，对 post-training 对齐的鲁棒性研究具有范式意义。 |

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*