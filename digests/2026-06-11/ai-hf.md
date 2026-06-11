# Hugging Face 热门模型日报 2026-06-11

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-11 00:37 UTC

---

# Hugging Face 研究模型日报 | 2026-06-11

## 今日速览

本周 Hugging Face 热门模型中，**Google Gemma-4 系列**以统一的 any-to-any 架构成为多模态研究焦点，其原生视觉-语言融合设计为 OCR 与文档理解提供了新基座。**DeepSeek-V4-Pro** 以 4758 点赞领跑，其 MoE 架构与推理优化值得关注。**NVIDIA LocateAnything-3B** 的开放视觉定位能力与 **Step-3.7-Flash** 的高效 VLM 设计，反映了视觉语言模型向轻量专用化发展的趋势。后训练对齐方面，多个"abliterated/uncensored"变体的出现（如 Huihui-gemma-4、Qwen3.6-Uncensored）提示了安全对齐与能力解锁之间的持续张力。

---

## 热门模型

### 🎭 多模态与视觉语言（VLM、视觉编码器、跨模态模型、图文理解）

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it) | google | 885 | 675,936 | **统一 any-to-any 架构的轻量多模态基座**，原生支持图像-文本交错输入与输出，为文档理解、OCR 后处理提供端到端研究平台；其视觉编码器与语言模型的深度融合设计可探索视觉定位与文本推理的协同机制 |
| [google/gemma-4-12B](https://huggingface.co/google/gemma-4-12B) | google | 502 | 140,221 | Gemma-4 基础权重，**any-to-any 预训练检查点**，适合研究多模态预训练策略、视觉-语言对齐的初始表征结构 |
| [nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B) | nvidia | 1,803 | 131,794 | **开放视觉定位 VLM**，支持任意指代表达理解与自然语言定位输出；与 OCR/HMER 研究高度相关——可将公式检测从分类任务升级为指代表达定位，探索"指出这个积分区域"式的交互式文档理解 |
| [HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive) | HauhauCS | 1,630 | 3,057,541 | **高下载量 MoE VLM 的激进对齐解除版本**，vision 标签确认视觉能力保留；可用于研究视觉语言模型的安全对齐边界、多模态幻觉与真实能力之间的关联，以及后训练干预对视觉推理的影响 |
| [stepfun-ai/Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash) | stepfun-ai | 363 | 50,187 | **高效视觉语言模型**，vision-language 架构优化推理速度；适合研究 VLM 的延迟-精度权衡、长文档流式视觉理解 |
| [google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it) | google | 213 | 0 | **扩散模型与语言模型融合实验**，image-text-to-text 任务支持；可探索基于扩散的文本渲染质量对 OCR 纠错、公式生成的影响 |
| [nex-agi/Nex-N2-Pro](https://huggingface.co/nex-agi/Nex-N2-Pro) / [mini](https://huggingface.co/nex-agi/Nex-N2-mini) | nex-agi | 180/134 | 1,185/1,222 | **Qwen3.5-MoE 架构的视觉语言变体**，image-text-to-text 能力；适合作为 MoE 路由策略在多模态场景下的消融研究基线 |
| [unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF) / [qat-GGUF](https://huggingface.co/unsloth/gemma-4-12B-it-qat-GGUF) / [26B-A4B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-qat-GGUF) | unsloth | 548/187/129 | 711,706/148,252/129,110 | **Gemma-4 的量化推理优化版本**，GGUF/QAT 技术栈；研究多模态模型在低精度下的视觉-语言对齐稳定性、量化对 OCR 细粒度识别的影响 |

### 🧠 长上下文与推理模型（扩展上下文 LLM、推理增强模型、数学模型）

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | deepseek-ai | 4,758 | 4,061,006 | **本周绝对热度冠军**，DeepSeek-V4 MoE 架构，conversational 优化；其超长上下文窗口与推理效率设计为长文档理解、多页 OCR 后联合推理提供强基座，可研究 MoE 专家路由在长序列多模态任务中的模式 |
| [nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16) / [NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4) | nvidia | 189/158 | 59,066/91,117 | **550B 总参数/55B 激活的超大 MoE**，BF16 与 NVFP4 双精度发布；适合研究超大规模模型在长上下文推理中的涌现行为、低精度格式对数学/逻辑推理可靠性的影响 |
| [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B) | LiquidAI | 581 | 142,134 | **液态神经网络架构的 MoE 变体**，非 Transformer 的连续时间动态系统；为长上下文建模提供替代性归纳偏置，可探索其对结构化输入（如表格、公式树）的时序推理优势 |
| [JetBrains/Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking) | JetBrains | 281 | 18,273 | **显式 Thinking 模式的代码推理模型**，conversational 架构；其思维链显化机制可迁移至多模态数学公式推导、几何证明等需要逐步视觉推理的场景 |

### 🔧 Post-Training 与对齐（RLHF/DPO/SFT 模型、偏好微调模型、对齐-focused 发布）

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [huihui-ai/Huihui-gemma-4-12B-it-abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-it-abliterated) | huihui-ai | 135 | 6,400 | **Gemma-4 的对齐解除实验**，保留 any-to-any 多模态能力；直接研究"abliteration"技术对视觉语言模型安全对齐层的影响，评估多模态拒绝行为与真实能力的解耦程度 |
| [OBLITERATUS/Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED) | OBLITERATUS | 212 | 14,838 | **另一 Gemma-4 对齐解除变体**，GGUF 支持本地部署；对比研究不同后训练干预方法对同一多模态基座的差异化影响 |
| [sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B) | sapientinc | 739 | 134,752 | **HRM（Human Resource Model?）专用文本模型**，hrm_text 标签独特；若涉及人力资源文档的敏感信息处理，可研究领域特定对齐与隐私保护机制 |
| [CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) | CohereLabs | 255 | 1,859 | **Cohere2 MoE 代码模型**，conversational 优化；代码生成与文档理解的交叉——研究结构化标记语言（LaTeX、MathML）作为"代码"的对齐策略 |

### 👁️ 幻觉缓解（事实 grounded 模型、校准置信度模型、RAG 增强模型）

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [google/gemma-4-12B-it-qat-q4_0-gguf](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf) | google | 123 | 96,749 | **官方 QAT 量化版**，any-to-any 能力保留；量化本身可作为幻觉缓解的研究变量——低精度是否导致视觉细节（如公式符号）的系统性误识别，及其校准方法 |
| [nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) | nvidia | 342 | 4,965 | **流式 ASR 的缓存感知设计**，cache-aware streaming；语音-文本对齐的实时置信度估计机制，可迁移至视觉语言模型的流式文档理解中的不确定性量化 |

### 🏗️ 研究基础设施（训练框架、评测套件、数据集工具）

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [ByteDance/Bernini-R](https://huggingface.co/ByteDance/Bernini-R) | ByteDance | 210 | 305 | **图像-文本到视频渲染器**，Apache-2.0 开源；文档理解的可视化延伸——将静态公式/图表渲染为动态解释视频，为 OCR/HMER 结果的可解释性提供新维度 |
| [jdopensource/JoyAI-Echo](https://huggingface.co/jdopensource/JoyAI-Echo) | jdopensource | 126 | 5,457 | **LTX-Video 架构的文本到视频**，audio-video-generation 支持；多模态生成的同步控制研究，对需要音视频联合呈现的数学教育内容生成有参考价值 |

---

## 研究生态信号

**Gemma-4 家族**以统一 any-to-any 架构正成为开源多模态研究的新默认基座，其 12B/26B 双尺寸与官方/社区量化生态的迅速形成，标志着 Google 在 VLM 开放权重策略上的激进转向。与之对比，**DeepSeek-V4-Pro** 以纯文本 MoE 守住推理模型高地，两者形成"多模态轻量 vs 文本推理重型"的分工格局。值得警惕的是，**对齐解除社区**（abliterated/uncensored）的活跃——Huihui-ai、OBLITERATUS、HauhauCS 等账号快速跟进主流 VLM 的"去安全化"版本，其高下载量暗示研究社区对"干净"后训练基线的强烈需求，但也模糊了安全研究与能力滥用的边界。NVIDIA 在 **LocateAnything** 的开放视觉定位与 **Nemotron-Ultra** 的超大 MoE 两端同时发力，显示其对"精确空间理解"与"规模涌现"两条路径的押注。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | [nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B) | **OCR/HMER 的范式升级机会**：将传统"检测→识别→结构化"流水线替换为端到端指代表达理解。可直接测试"定位这个偏微分方程的积分区域""指出证明中的逻辑漏洞"等任务，探索公式理解从字符级到语义级的跃迁。3B 规模适合单卡研究，开放权重允许深入分析视觉-语言对齐机制 |
| ⭐⭐⭐ | [google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it) | **多模态统一架构的基准测试平台**。any-to-any 设计允许构造"图像→文本→图像"的循环任务（如手写公式识别→LaTeX 生成→渲染验证），直接量化端到端系统中的误差传播与幻觉累积。配合社区 abliterated 版本，可系统研究安全对齐层对视觉推理能力的抑制/保护效应 |
| ⭐⭐☆ | [deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | **长上下文推理的极限探针**。4M+ 下载量验证的工程稳定性，使其成为测试"整本数学教材→跨章节定理关联""长文档多页表格一致性验证"等极端场景的首选。MoE 路由的可解释性分析可揭示：在面对结构化数学内容时，模型是否自发形成"符号推理专家"与"自然语言专家"的功能分化 |

---

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*