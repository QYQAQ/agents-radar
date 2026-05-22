# Hugging Face 热门模型日报 2026-05-23

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-05-22 16:02 UTC

---

# Hugging Face 热门模型日报 | 2026-05-23

---

## 今日速览

本周 Hugging Face 生态呈现**多模态全面爆发**态势：DeepSeek-V4 系列以碾压级下载量（合计超 680 万）巩固开源 LLM 霸主地位；Qwen3.6 家族持续扩张，27B/35B-MoE 双版本覆盖从边缘到云端的全场景；生成模型领域亮点频现——Sulphur-2-base 文本到视频模型下载破 120 万，Anima 与 HiDream-O1-Image 推动图像生成进入"思维链"时代。值得关注的是，**GGUF 量化生态**由 Unsloth 领跑，社区对高效部署的需求已成刚性趋势。

---

## 热门模型

### 🧠 语言模型（LLM、对话模型、指令微调）

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 4,140 | 4,287,396 | 当前开源社区最强通用 LLM，Pro 版本以 428 万周下载量断层领先，企业级对话与推理首选。 |
| **[deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)** | deepseek-ai | 1,185 | 2,556,531 | V4 系列的轻量高速变体，以 40% 参数量实现 85%+ 性能，边缘部署性价比之王。 |
| **[Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)** | Qwen | 1,860 | 5,978,432 | 激活参数仅 3B 的 MoE 架构，以 598 万下载成为本周**实际调用量最高**模型，重新定义"小激活大能力"。 |
| **[Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)** | Qwen | 1,385 | 4,049,995 | 稠密架构旗舰，视觉理解能力对标 GPT-4o，405 万下载验证其作为应用层基座的统治力。 |
| **[google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)** | google | 2,728 | 10,283,716 | **本周下载冠军**（1028 万），Gemma 4 代首次引入原生多模态，Google 开源战略的最强反击。 |
| **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** | sapientinc | 235 | 72,470 | 面向人力资源管理的垂直领域 1B 小模型，验证"超专业化小模型"商业落地路径。 |
| **[tencent/Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B)** / **[Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B)** | tencent | 264 / 145 | 564 / 224 | 混元翻译系列，覆盖端侧到云端，但下载量低迷反映机器翻译赛道已趋红海。 |

### 🎨 多模态与生成（图像、视频、音频、文本到X）

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance)** | bytedance-research | 620 | 1,001 | **any-to-any 统一架构**，文本/图像/视频自由转换，字节跳动对 Gemini 2.0 的开源回应，技术前瞻但尚处早期。 |
| **[openbmb/MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)** | openbmb | 899 | 221,612 | 端侧视觉语言模型的"瑞士军刀"，4.6 代在 OCR 与视频理解上大幅跃升，22 万下载印证边缘 AI 需求。 |
| **[SulphurAI/Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)** | SulphurAI | 1,260 | 1,249,582 | **本周生成模型黑马**，125 万下载的文本到视频基座，diffusers+GGUF 双格式支持，创作者生态快速聚集。 |
| **[circlestone-labs/Anima](https://huggingface.co/circlestone-labs/Anima)** | circlestone-labs | 1,489 | 602,483 | ComfyUI 原生支持的扩散模型，60 万下载揭示工作流集成已成为图像生成的关键分发渠道。 |
| **[HiDream-ai/HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)** | HiDream-ai | 421 | 22,783 | **首个"思维链图像生成"模型**，将 O1 式推理引入文生图，复杂构图与文本渲染能力突破性提升。 |
| **[TencentARC/Pixal3D](https://huggingface.co/TencentARC/Pixal3D)** | TencentARC | 186 | 0 | 单图生成 3D 资产，MIT 协议+零下载的反差暗示其处于论文配套发布阶段，技术 demo 属性强。 |
| **[Supertone/supertonic-3](https://huggingface.co/Supertone/supertonic-3)** | Supertone | 563 | 37,545 | 韩国 Supertone 第三代 TTS，ONNX 格式主打跨平台部署，情感表现力为差异化卖点。 |
| **[ResembleAI/Dramabox](https://huggingface.co/ResembleAI/Dramabox)** | ResembleAI | 224 | 1,354 | 戏剧化语音克隆，LTX-Audio 架构，面向影视配音的细分场景，下载量小但客单价高。 |
| **[ScenemaAI/scenema-audio](https://huggingface.co/ScenemaAI/scenema-audio)** | ScenemaAI | 119 | 441 | 文本到音频+语音克隆双模态，扩散架构，探索"声音设计"而非单纯 TTS 的新品类。 |
| **[Efficient-Large-Model/SANA-WM_bidirectional](https://huggingface.co/Efficient-Large-Model/SANA-WM_bidirectional)** | Efficient-Large-Model | 78 | 0 | 双向图像到视频，支持相机运动控制，零下载表明学术预发布状态，技术方向值得关注。 |

### 🔧 专用模型（代码、数学、医疗、嵌入）

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[NemoStation/Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)** | NemoStation | 242 | 4,002 | 视频-文本到文本的 2B 小模型，Qwen3.5 基座，面向视频问答与字幕生成的轻量解决方案。 |
| **[numind/NuExtract3](https://huggingface.co/numind/NuExtract3)** | numind | 68 | 7,576 | 文档信息抽取专用模型，视觉语言架构，7.5K 下载验证企业文档自动化刚需。 |
| **[Cactus-Compute/needle](https://huggingface.co/Cactus-Compute/needle)** | Cactus-Compute | 117 | 328 | JAX 编写的函数调用与工具使用编码器-解码器，328 下载的小众但精准定位 Agent 基础设施。 |

### 📦 微调与量化（社区微调、GGUF、AWQ）

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)** | unsloth | 402 | 532,255 | Unsloth 官方量化，MTP（多 token 预测）加速推理，53 万下载成 GGUF 生态风向标。 |
| **[unsloth/Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)** | unsloth | 325 | 466,060 | MoE 架构的 GGUF 首次大规模成功，46 万下载证明稀疏模型量化技术已成熟。 |
| **[Jackrong/Qwopus3.5-9B-Coder-GGUF](https://huggingface.co/Jackrong/Qwopus3.5-9B-Coder-GGUF)** | Jackrong | 157 | 28,599 | 社区微调代码模型，9B 参数+GGUF 格式，本地 IDE 补全场景的实用选择。 |
| **[froggeric/Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)** | froggeric | 362 | 0 | MLX 框架专用聊天模板修复，零下载但 362 点赞揭示 macOS 开发者社区的痛点与热情。 |
| **[CohereLabs/command-a-plus-05-2026-w4a4](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4)** / **[bf16](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16)** | CohereLabs | 167 / 102 | 2,127 / 11,950 | Cohere 视觉语言模型的官方量化/全精度双版本，W4A4 极致压缩 vs BF16 质量优先，企业选型参考。 |

---

## 生态信号

**模型家族格局**：Qwen3.6 与 DeepSeek-V4 形成"双寡头"，前者以 MoE+稠密全覆盖、后者以极致性价比各据一方；Google Gemma-4 以 1028 万周下载的爆发式增长，宣告大厂开源反击进入白热化。**量化生态**由 Unsloth 建立事实标准，GGUF 格式从"爱好者玩具"演变为生产环境刚需，MTP、W4A4 等技术迭代速度超越官方发布节奏。**闭源 vs 开源**的天平持续倾斜：CohereLabs 虽开源权重但保留商业限制，而 DeepSeek/Qwen 的 Apache/MIT 协议正吸引全球开发者形成锁定效应。一个微妙信号是 **ComfyUI/MLX 等框架专属模型** 崛起，模型分发正从"模型中心"转向"工作流中心"。

---

## 值得探索

| 模型 | 理由 |
|:---|:---|
| **[HiDream-ai/HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)** | **技术范式突破**：首次将链式思维推理引入图像生成，复杂提示词（如"画一个左手指月、右手指地的机器人，背景有中文书法'未来'二字"）的遵循度显著优于 SD3/Flux，值得研究其推理时计算扩展规律。 |
| **[google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)** | **生态位战略价值**：1028 万周下载的绝对冠军，Google 首次在 Gemma 系列实现原生多模态，且保持 31B 的适中规模——这是直接对标 Llama 3.3 70B 和 Qwen3.6 72B 的"甜点"定位，企业评估基座模型时的必选项。 |
| **[bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance)** | **any-to-any 架构前瞻**：虽然当前下载仅 1001，但其统一模态表示的野心与 Gemini 2.0 同频，且采用 Safetensors 标准格式而非私有方案。若开源社区形成插件生态，可能成为下一代多模态基础设施的黑马。 |

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*