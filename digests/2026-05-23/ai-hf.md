# Hugging Face 热门模型日报 2026-05-23

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-05-23 14:52 UTC

---

# Hugging Face 研究模型日报 | 2026-05-23

## 今日速览

本周 Hugging Face 热门模型中，**多模态推理与长上下文**成为核心趋势：Google 开源 **Gemma-4-31B-it** 以超千万下载量领跑视觉语言模型赛道，Qwen3.6 系列（27B/35B-A3B）持续巩固国产 VLM 生态；**DeepSeek-V4-Pro/Flash** 以 400万+ 下载量展现长上下文推理模型的强劲需求；**MiniCPM-V-4.6** 与 **HiDream-O1-Image** 分别在端侧文档理解和图像生成推理方面取得突破。值得关注的是，OCR/HMER 专用模型仍显稀缺，但 **NuExtract3** 等基于 Qwen3.5 的视觉提取模型暗示了文档理解向通用 VLM 迁移的趋势。后训练对齐领域未见专门模型上榜，反映该方向更多以训练框架而非权重形式存在。

---

## 热门模型

### 📄 OCR 与文档模型

| 模型 | 作者/指标 | 研究相关性 |
|:---|:---|:---|
| **[numind/NuExtract3](https://huggingface.co/numind/NuExtract3)** | numind<br>👍 82 / ⬇ 9,918 | 基于 Qwen3.5 的视觉信息提取模型，将 OCR 后结构化提取任务融入 VLM 范式；对研究**文档理解从专用 OCR 管道向端到端 VLM 迁移**具有参考意义，但纯 HMER/版面分析模型仍缺位 |

### 🎭 多模态与视觉语言

| 模型 | 作者/指标 | 研究相关性 |
|:---|:---|:---|
| **[google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)** | google<br>👍 2,738 / ⬇ 10,289,284 | **本周下载量冠军**，Gemma 4 代视觉语言模型；研究相关在于其大规模采用所揭示的**开源 VLM 标准化趋势**，以及多模态对话中幻觉问题的工程化缓解方案 |
| **[Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**<br>**[Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)** | Qwen<br>👍 1,397 / ⬇ 4,115,906<br>👍 1,873 / ⬇ 6,011,835 | Qwen3.5 架构迭代版，35B-A3B 为 MoE 变体；**国产 VLM 生态核心基座**，其 image-text-to-text 能力为 OCR+多模态推理研究提供可控实验平台，MTP（Multi-Token Prediction）训练目标对视觉序列建模有启发 |
| **[openbmb/MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)** | openbmb<br>👍 911 / ⬇ 247,170 | **端侧高效 VLM 代表**，4.6 版本在保持小参数的同时强化高分辨率图像理解；直接相关于**移动端 OCR/文档理解**的部署研究，以及视觉编码器效率优化 |
| **[HiDream-ai/HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)** | HiDream-ai<br>👍 423 / ⬇ 23,882 | 基于 Qwen3-VL 的图像生成推理模型，将 **O1 式长链推理引入视觉生成**；对研究多模态推理中的"慢思考"机制、以及生成过程中的幻觉自检具有开创性 |
| **[CohereLabs/command-a-plus-05-2026-bf16](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16)**<br>**[CohereLabs/command-a-plus-05-2026-w4a4](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4)** | CohereLabs<br>👍 109 / ⬇ 12,186<br>👍 176 / ⬇ 4,261 | Cohere 2 代视觉语言模型，提供 bf16 与 W4A4 量化双版本；**企业级多模态对齐**的量化-性能权衡研究样本，w4a4 版本对边缘部署的幻觉鲁棒性有待验证 |
| **[bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance)** | bytedance-research<br>👍 680 / ⬇ 1,227 | **Any-to-any 统一多模态架构**，支持图像/视频/文本的任意模态转换；对研究**跨模态表征统一**、以及多模态生成中的幻觉传播机制具有范式价值 |
| **[unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**<br>**[unsloth/Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)** | unsloth<br>👍 429 / ⬇ 597,584<br>👍 339 / ⬇ 507,644 | Unsloth 优化的 GGUF 量化版本，**MTP 训练目标的消费级部署验证**；研究相关在于量化对多模态推理精度的影响，以及长上下文场景下的 KV Cache 效率 |
| **[Jackrong/Qwopus3.5-9B-Coder-GGUF](https://huggingface.co/Jackrong/Qwopus3.5-9B-Coder-GGUF)**<br>**[Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF)**<br>**[Jackrong/Qwopus3.6-27B-v2-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-GGUF)** | Jackrong<br>👍 168 / ⬇ 35,795<br>👍 76 / ⬇ 27,398<br>👍 73 / ⬇ 2,853 | 社区微调 Qwen 代码/多模态变体，反映 **Qwen 生态的垂直分化**；对研究代码-视觉联合推理、以及社区后训练对齐实践具有观察价值 |

### 🧠 长上下文与推理模型

| 模型 | 作者/指标 | 研究相关性 |
|:---|:---|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**<br>**[deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)** | deepseek-ai<br>👍 4,180 / ⬇ 4,510,828<br>👍 1,203 / ⬇ 2,703,252 | **本周点赞与下载双高**，V4 系列延续 DeepSeek 在长上下文与推理上的优势；Pro 版适合**超长文档理解/多轮工具调用**研究，Flash 版针对推理效率优化，两者均为长上下文幻觉评估的基准模型 |
| **[NemoStation/Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)** | NemoStation<br>👍 262 / ⬇ 5,283 | 基于 Qwen3.5 的 **video-text-to-text 模型**，2B 参数聚焦视频理解；研究相关在于长时序视觉序列的上下文压缩、以及视频-文本对齐中的时序幻觉问题 |
| **[Cactus-Compute/needle](https://huggingface.co/Cactus-Compute/needle)** | Cactus-Compute<br>👍 123 / ⬇ 335 | 名称直指 **"Needle-in-Haystack" 长上下文评测**，JAX 实现的编码器-解码器架构；虽下载量小，但可能是长上下文能力评估的基础设施，值得追踪其评测方法论 |

### 🔧 Post-Training 与对齐

| 模型 | 作者/指标 | 研究相关性 |
|:---|:---|:---|
| **[froggeric/Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)** | froggeric<br>👍 377 / ⬇ 0 | 专注 **Qwen3.5 对话模板的修正与标准化**，MLX 格式；研究相关在于揭示社区对官方模板对齐质量的反馈，以及模板工程对多轮对话一致性的影响——**零下载量高点赞**反映其作为"补丁"而非独立模型的工具属性 |
| **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** | sapientinc<br>👍 250 / ⬇ 78,771 | "HRM" 可能指向 **Human Reward Modeling** 或特定领域；高下载量与"text-generation"任务标签提示其可能是对齐后的指令模型，需进一步验证其训练配方是否涉及 RLHF/DPO |

### 👁️ 幻觉缓解

| 模型 | 作者/指标 | 研究相关性 |
|:---|:---|:---|
| *本周期暂无专门标注"幻觉缓解"的模型上榜* | — | 幻觉缓解仍以**训练后属性**而非独立模型存在，如 DeepSeek-V4 的推理链自检、HiDream-O1 的生成过程反思；该方向研究需从模型行为分析切入 |

### 🏗️ 研究基础设施

| 模型 | 作者/指标 | 研究相关性 |
|:---|:---|:---|
| **[nvidia/Nemotron-Labs-Diffusion-14B](https://huggingface.co/nvidia/Nemotron-Labs-Diffusion-14B)** | nvidia<br>👍 72 / ⬇ 3,282 | **"Diffusion" 架构的纯文本生成模型**，非视觉扩散；研究相关在于探索扩散模型在 LLM 训练中的替代潜力，以及该范式对文本生成幻觉的固有影响（扩散的去噪过程 vs 自回归的累积错误） |

---

## 研究生态信号

**Qwen 生态的垂直分化与国际化竞争**构成本周核心信号。Qwen3.5/3.6 架构已成为国产多模态事实标准，衍生出官方版本（Qwen）、社区量化（Unsloth, Jackrong）、垂直领域（HiDream, NuExtract, Marlin）三层生态，与 Google Gemma-4、DeepSeek-V4 形成"开源三极"。值得注意的是，OCR/HMER 专用模型几乎消失，文档理解全面融入通用 VLM，这既是技术进步的体现，也可能导致**细粒度文本识别能力的评估盲区**。后训练对齐领域呈现"隐形化"特征——RLHF/DPO 更多作为训练流程而非独立模型发布，Cohere 的 W4A4 量化与 Unsloth 的 GGUF 优化反映对齐后的**部署压缩**成为新焦点。幻觉缓解方面，"O1 式推理"（HiDream-O1, DeepSeek-V4）正从文本向视觉生成扩散，但缺乏系统性的幻觉评测基础设施。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[HiDream-ai/HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)** | **首个将 O1 长链推理引入图像生成的开源模型**，可直接研究：(1) 视觉生成中的"思维链"如何影响输出一致性；(2) 多模态推理的幻觉自检机制是否可迁移至 OCR/文档理解；(3) Qwen3-VL 架构的生成-理解统一潜力 |
| ⭐⭐⭐ | **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | **长上下文推理的基准级模型**，450万+下载量验证其社区地位；建议用于：(1) 超长文档（>100K）的 OCR 后理解评测；(2) 多模态链式推理中的错误传播分析；(3) 与 Qwen3.6-35B-A3B 的 MoE vs Dense 架构对比实验 |
| ⭐⭐☆ | **[Cactus-Compute/needle](https://huggingface.co/Cactus-Compute/needle)** | **疑似长上下文评测基础设施**，名称与任务 N/A 的异常组合暗示其工具属性；若验证为 Needle-in-Haystack 实现，可填补当前 VLM 长上下文幻觉评测的方法论空白，建议优先复现其评测协议并扩展至多模态场景 |

---

*日报基于 2026-05-23 Hugging Face Hub 周点赞数据生成。模型标签与任务分类以官方标注为准，研究相关性判断存在主观推断，建议结合原始论文与模型卡验证。*

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*