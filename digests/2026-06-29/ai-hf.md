# Hugging Face 热门模型日报 2026-06-29

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-29 00:34 UTC

---

# Hugging Face 研究模型日报 | 2026-06-29

## 今日速览

本周 Hugging Face 生态呈现 **OCR 与多模态推理深度耦合**、**长上下文模型向 Agentic 场景渗透** 的显著趋势。百度发布的 **Unlimited-OCR** 以近 30 万周下载量成为文档理解领域焦点，其"unlimited"命名暗示对超长文档或无限序列的 OCR 能力突破；**nvidia/LocateAnything-3B** 与 **Qwen-AgentWorld-35B-A3B** 则分别代表了视觉 grounding 与 world-model 架构在多模态推理中的新方向。后训练对齐方面，**HauhauCS** 系列的"Uncensored-Aggressive"与"Balanced"双路线发布，以及 **microsoft/FastContext-1.0-4B-SFT** 的"Explorer SubAgent"标签，揭示了 SFT 阶段对长上下文 Agent 行为对齐的探索。值得关注的是，**DeepSeek-V4** 系列同时出现 Pro 与 Flash 两版 DSpark 变体，可能指向推理效率与深度思考的后训练权衡。

---

## 热门模型

### 📄 OCR 与文档模型

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** | baidu | 1,230 | 295,064 | **核心关注**：百度开源的 OCR 模型，"unlimited"标签与超高下载量暗示其对超长文档、连续版面或流式文本的识别突破，直接关联 HMER（手写数学表达式识别）与复杂文档结构理解研究；feature-extraction 任务标签表明可能提供可插拔的视觉编码器。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 2,434 | 646,451 | **核心关注**：NVIDIA 的视觉定位模型，image-feature-extraction 与 image-text-to-text 双任务设计，支持"anything"级别的细粒度视觉 grounding，对 OCR 中的区域检测、公式定位及版面分析具有直接迁移价值。 |

---

### 🎭 多模态与视觉语言

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)** | empero-ai | 525 | 52,492 | Qwen3.5 架构的 9B 多模态模型，"Mythos-5-1M"命名暗示百万级多模态指令微调，image-text-to-text 任务支持图文推理，适合作为 VLM 后训练对齐的研究基座。 |
| **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)** | empero-ai | 795 | 831,529 | 上述模型的 GGUF 量化版，下载量激增 16 倍，反映边缘部署对多模态推理的旺盛需求；量化后仍保留 reasoning 标签，值得研究量化对视觉推理能力的损伤。 |
| **[Qwen/Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)** | Qwen | 397 | 23,697 | Qwen 官方 35B-A3B MoE 架构的 world-model 变体，image-text-to-text 任务标签与"AgentWorld"命名表明多模态 Agent 环境交互能力，是研究 VLM 与具身智能交叉的关键节点。 |
| **[HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced](https://huggingface.co/HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced)** | HauhauCS | 100 | 40,820 | Gemma-4 12B 的 QAT（量化感知训练）多模态版本，"Balanced"与"Uncensored"路线对比，为研究 VLM 后训练中安全性-有用性权衡提供对照实验素材。 |
| **[deepreinforce-ai/Ornith-1.0-35B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B)** / **[9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)** / **[397B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-397B)** | deepreinforce-ai | 203/233/145 | 19,635/5,814/1,116 | 覆盖 9B-397B 的 Ornith 系列，qwen3_5_moe 架构，image-text-to-text 任务，MIT 许可证，397B 的超大 MoE 规模可能探索稀疏激活下的多模态涌现能力。 |
| **[deepreinforce-ai/Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)** / **[9B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)** | deepreinforce-ai | 407/273 | 79,630/36,846 | Ornith 系列的 GGUF 部署版本，endpoints_compatible 标签表明推理服务优化，适合研究多模态模型的高效服务化与幻觉缓解的实时干预。 |

---

### 🧠 长上下文与推理模型

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)** | zai-org | 2,815 | 118,651 | GLM 系列第五代 5.2 版本，glm_moe_dsa 标签中的 DSA（Dynamic Sparse Attention）暗示长上下文动态稀疏注意力机制，是研究超长序列建模效率的核心模型。 |
| **[unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)** | unsloth | 442 | 146,023 | Unsloth 优化的 GLM-5.2 GGUF 版，结合 Unsloth 的内存高效训练技术，为长上下文模型的低成本微调与推理提供基础设施。 |
| **[nvidia/GLM-5.2-NVFP4](https://huggingface.co/nvidia/GLM-5.2-NVFP4)** | nvidia | 154 | 45,762 | NVIDIA 的 NVFP4 量化版 GLM-5.2，Model Optimizer/ModelOpt 标签，探索 4-bit 浮点量化对长上下文注意力精度的保留程度，直接影响长文本推理的可靠性。 |
| **[yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)** | yuxinlu1 | 2,471 | 549,926 | Gemma-4 12B 的代码推理特化版，"fable5-composer2.5"命名暗示多阶段合成数据训练，reasoning 标签与超高下载量表明代码推理作为通用推理能力代理的验证路径。 |
| **[yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)** | yuxinlu1 | 792 | 225,822 | 上述模型的 Agentic 升级版，"3.5x-tau2"可能指温度采样或思考深度参数，terminal 标签表明面向命令行 Agent 场景，是研究长上下文工具使用与推理规划的关键。 |
| **[WeiboAI/VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)** | WeiboAI | 743 | 59,337 | 3B 小参数数学推理模型，qwen2 基座，math 标签，探索小模型通过特定训练范式获得推理能力，对研究推理能力的参数效率与蒸馏策略具有参考价值。 |
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft | 369 | 6,779 | 微软 4B 长上下文 SFT 模型，"Explorer SubAgent"标签与 qwen3 基座，明确指向长上下文场景下的 Agent 行为对齐，是研究 SFT 阶段如何塑造长文本 Agent 决策偏好的重要样本。 |
| **[LiquidAI/LFM2.5-230M](https://huggingface.co/LiquidAI/LFM2.5-230M)** | LiquidAI | 141 | 12,384 | 230M 超小参数的 LFM（Liquid Foundation Model）2.5 版，liquid 标签暗示连续时间状态空间模型，可能为长上下文建模提供不同于 Transformer 的替代架构。 |
| **[deepseek-ai/DeepSeek-V4-Pro-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark)** / **[Flash-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-DSpark)** | deepseek-ai | 178/76 | 373/24 | DeepSeek-V4 的 DSpark 变体双发，Pro 与 Flash 可能分别对应深度思考与快速响应的后训练路径，arxiv 标签表明有配套论文，是研究推理时计算扩展与效率权衡的难得对照。 |
| **[Chunjiang-Intelligence/DeepSeek-v4-Fable](https://huggingface.co/Chunjiang-Intelligence/DeepSeek-v4-Fable)** | Chunjiang-Intelligence | 124 | 1,409 | DeepSeek-v4 的第三方 Fable 微调版，cybersecurity 标签，研究垂直领域微调对基础模型长上下文推理与幻觉特性的影响。 |

---

### 🔧 Post-Training 与对齐

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 2,302 | 3,248,724 | **本周下载冠军**，Qwen3.6 35B-A3B MoE 的"Uncensored-Aggressive"对齐版本，gguf/vision/moe 多标签叠加，极端下载量反映社区对后训练"去抑制"的强烈需求，同时是研究对齐过度与幻觉风险加剧关系的危险样本。 |
| **[HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced](https://huggingface.co/HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced)** | HauhauCS | 100 | 40,820 | 同一作者的"Balanced"路线，与 Aggressive 版形成对照，QAT 量化感知训练与 vision 能力结合，为研究多模态模型后训练中安全性-性能帕累托前沿提供实验组。 |
| **[unsloth/Qwen-AgentWorld-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen-AgentWorld-35B-A3B-GGUF)** | unsloth | 95 | 79,503 | Unsloth 优化的 Qwen-AgentWorld GGUF，world-model 标签与 unsloth 的高效训练技术结合，支持低成本复现多模态 Agent 对齐流程。 |

---

### 👁️ 幻觉缓解

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** | baidu | 1,230 | 295,064 | OCR 领域的幻觉缓解关键基线：文档理解的幻觉常源于字符误识或版面解析错误，该模型的高下载量与 feature-extraction 设计，为研究"识别-理解"级联系统中的误差传播与校准提供基础。 |
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft | 369 | 6,779 | "Explorer SubAgent"暗示主动探索与信息核实行为，可能通过 SFT 注入长上下文检索增强机制，直接关联 RAG 增强的幻觉缓解研究。 |
| **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)** | empero-ai | 525 | 52,492 | "Mythos"命名与百万级数据训练，可能包含对抗性幻觉数据构造，适合作为 VLM 幻觉检测与置信度校准的测试平台。 |

---

### 🏗️ 研究基础设施

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)** / **[Qwen-AgentWorld-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen-AgentWorld-35B-A3B-GGUF)** | unsloth | 442/95 | 146,023/79,503 | Unsloth 持续提供主流长上下文/多模态模型的 GGUF 优化版本，降低研究门槛，其技术栈本身即是高效后训练与部署的研究对象。 |
| **[nvidia/Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4)** | nvidia | 371 | 5,235,413 | NVIDIA 官方 NVFP4 量化实现，Model Optimizer/ModelOpt 工具链输出，超 500 万下载量，为研究量化对 MoE 多模态模型推理可靠性的影响提供标准化基准。 |
| **[nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)** | nvidia | 734 | 67,419 | Nemotron 3.5 ASR 流式模型，虽为语音任务，但 streaming 架构与 0.6B 小参数设计，其流式处理技术可迁移至实时 OCR 与文档流理解场景。 |

---

## 研究生态信号

**Qwen 与 GLM 家族主导多模态长上下文生态**：Qwen3.5/3.6 系列（AgentWorld、Ornith、Qwythos、HauhauCS 微调）与 GLM-5.2（zai-org、NVIDIA NVFP4、Unsloth GGUF）形成双核心，MoE 架构成为 35B+ 模型的默认选择，A3B 激活参数设计平衡推理成本与性能。开源权重在 VLM 领域持续强势，但百度 Unlimited-OCR、NVIDIA LocateAnything 等厂商模型的专有架构（如 feature-extraction 任务）暗示核心 OCR 编码器仍存闭源壁垒。后训练对齐呈现**极端分化**：HauhauCS "Aggressive"路线以 320 万下载验证"去抑制"市场需求，而"Balanced"路线与微软 FastContext 的"SubAgent"探索，反映学术与工业界对对齐目标的认知分裂。文档理解方面，OCR 与 VLM 的边界持续模糊——Unlimited-OCR 的 image-text-to-text 任务标签与 LocateAnything 的 grounding 能力，表明"识别即理解"的端到端范式正在取代传统级联流水线。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| **🔥 最高** | **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** | 295K 周下载的 OCR 现象级模型，"unlimited"命名与 feature-extraction 设计直指长文档/无限序列 OCR 瓶颈；对 HMER 研究而言，其视觉编码器是否支持数学符号的细粒度特征提取、是否开源权重可微调，是验证 OCR-VLM 融合假设的关键。建议优先测试其对手写公式、复杂版面的 zero-shot 能力。 |
| **🔥 最高** | **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | 320 万下载的"Uncensored-Aggressive" MoE VLM，是研究**对齐过度→幻觉加剧**因果链的极端样本。其 vision + moe + gguf 三标签叠加，支持在边缘设备上复现"去抑制"后的多模态幻觉行为，与 Balanced 版形成天然对照实验。可设计探针测试：该模型在数学公式图像推理中是否因"去抑制"而生成更自信但错误的推导？ |
| **⭐ 高** | **[microsoft/FastContext-1.0-4B-SFT](https://huggingface

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*