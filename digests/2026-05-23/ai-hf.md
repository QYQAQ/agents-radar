# Hugging Face 热门模型日报 2026-05-23

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-05-23 00:30 UTC

---

# Hugging Face 热门模型日报 | 2026-05-23

---

## 今日速览

本周 Hugging Face 生态呈现**多模态爆发**态势，Google Gemma-4 以千万级下载量领跑，DeepSeek-V4 系列延续强劲势头。Qwen3.6 家族全面铺开，覆盖 27B 稠密到 35B MoE 架构，社区量化版本同步跟进。生成式 AI 向**any-to-any**演进，字节跳动 Lance 与 Sulphur-2 分别探索统一多模态与视频生成边界。值得注意的是，3D 生成（Pixal3D）和双向视频控制（SANA-WM）等前沿方向开始涌现，显示开源社区正快速追赶闭源产品的能力边界。

---

## 热门模型

### 🧠 语言模型（LLM、对话模型、指令微调）

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 4,151 | 4,287,396 | 本周绝对顶流，DeepSeek V4 专业版以最高点赞数和近 430 万下载量证明其作为开源推理旗舰的地位 |
| **[deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)** | deepseek-ai | 1,189 | 2,556,531 | V4 轻量版本，平衡性能与速度，企业部署首选 |
| **[Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)** | Qwen | 1,868 | 5,978,432 | Qwen3.6 MoE 架构旗舰，近 600 万下载量显示其已成为开源社区事实标准之一 |
| **[Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)** | Qwen | 1,390 | 4,049,995 | 稠密架构高性价比之选，视觉语言能力全面 |
| **[google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)** | google | 2,730 | 10,283,716 | **本周下载之王**，Gemma 4 代突破千万下载，Google 开源战略持续施压闭源生态 |
| **[tencent/Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B)** | tencent | 277 | 564 | 腾讯混元翻译专用小模型，1.8B 参数瞄准端侧部署 |
| **[tencent/Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B)** | tencent | 214 | 224 | 混元翻译大模型，30B MoE 架构对标专业翻译场景 |
| **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** | sapientinc | 243 | 72,470 | 人力资源领域专用文本模型，垂直场景微调代表 |
| **[nvidia/Nemotron-Labs-Diffusion-14B](https://huggingface.co/nvidia/Nemotron-Labs-Diffusion-14B)** | nvidia | 62 | 1,992 | NVIDIA 实验室扩散语言模型，探索生成式预训练新范式 |

### 🎨 多模态与生成（图像、视频、音频、文本到X）

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance)** | bytedance-research | 645 | 1,001 | 字节跳动 **any-to-any** 统一多模态模型，单一架构打通图像/视频/文本任意转换，代表下一代多模态方向 |
| **[openbmb/MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)** | openbmb | 904 | 221,612 | 面壁智能端侧视觉语言模型，4.6 代持续领跑高效多模态 |
| **[SulphurAI/Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)** | SulphurAI | 1,267 | 1,249,582 | **视频生成黑马**，125 万下载验证其作为开源 Sora 挑战者的潜力 |
| **[circlestone-labs/Anima](https://huggingface.co/circlestone-labs/Anima)** | circlestone-labs | 1,498 | 602,483 | ComfyUI 生态热门，60 万下载的图像/视频生成工作流核心模型 |
| **[HiDream-ai/HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)** | HiDream-ai | 421 | 22,783 | 图像生成+理解双模态，"O1" 暗示类推理时扩展的生成策略 |
| **[TencentARC/Pixal3D](https://huggingface.co/TencentARC/Pixal3D)** | TencentARC | 191 | 0 | 腾讯 ARC 单图生 3D，学术前沿但尚未开放权重下载 |
| **[Efficient-Large-Model/SANA-WM_bidirectional](https://huggingface.co/Efficient-Large-Model/SANA-WM_bidirectional)** | Efficient-Large-Model | 84 | 0 | 双向视频生成控制，支持正向/反向时间轴编辑，视频可控性新突破 |
| **[Supertone/supertonic-3](https://huggingface.co/Supertone/supertonic-3)** | Supertone | 580 | 37,545 | 韩国 Supertone 第三代 TTS，3.7 万下载显示音频生成商业化加速 |
| **[ResembleAI/Dramabox](https://huggingface.co/ResembleAI/Dramabox)** | ResembleAI | 229 | 1,354 | 戏剧化语音克隆，情感表达丰富的专业级 TTS |
| **[ScenemaAI/scenema-audio](https://huggingface.co/ScenemaAI/scenema-audio)** | ScenemaAI | 123 | 441 | 场景化音频生成，从文本直接产出环境音与配乐 |

### 🔧 专用模型（代码、数学、医疗、嵌入）

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[NemoStation/Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)** | NemoStation | 249 | 4,002 | 视频理解+文本生成，2B 小模型探索高效视频语言建模 |
| **[numind/NuExtract3](https://huggingface.co/numind/NuExtract3)** | numind | 77 | 7,576 | 文档信息抽取专用，基于 Qwen3.5 视觉能力的结构化数据提取 |
| **[Cactus-Compute/needle](https://huggingface.co/Cactus-Compute/needle)** | Cactus-Compute | 120 | 328 | JAX 函数调用专用模型，工具使用与编码器-解码器架构实验性项目 |
| **[facebook/VGGT-Omega](https://huggingface.co/facebook/VGGT-Omega)** | facebook | 91 | 0 | Meta 视觉几何基础模型，3D 视觉理解但未开放下载 |

### 📦 微调与量化（社区微调、GGUF、AWQ）

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)** | unsloth | 412 | 532,255 | Unsloth 官方量化，MTP 多 token 预测加速，53 万下载验证消费级部署需求 |
| **[unsloth/Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)** | unsloth | 333 | 466,060 | MoE 架构 GGUF 量化，以 3B 激活参数跑 35B 模型，效率与质量兼得 |
| **[Jackrong/Qwopus3.5-9B-Coder-GGUF](https://huggingface.co/Jackrong/Qwopus3.5-9B-Coder-GGUF)** | Jackrong | 163 | 28,599 | 社区代码模型量化，Qwopus 系列填补 Qwen 代码专用生态 |
| **[Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF)** | Jackrong | 67 | 21,448 | MTP 加速版本，社区开发者持续迭代代码模型推理效率 |
| **[froggeric/Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)** | froggeric | 368 | 0 | MLX 苹果芯片专用，修复 Qwen3.5 对话模板，零下载但高点赞反映 Mac 开发者痛点 |
| **[CohereLabs/command-a-plus-05-2026-w4a4](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4)** | CohereLabs | 172 | 2,127 | Cohere 官方 W4A4 量化，4-bit 权重+4-bit 激活的企业级压缩方案 |
| **[CohereLabs/command-a-plus-05-2026-bf16](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16)** | CohereLabs | 108 | 11,950 | BF16 完整精度版本，Cohere 视觉语言模型开源跟进 |

---

## 生态信号

**Qwen 家族已成开源基础设施**。从 1.8B 到 35B MoE，官方+社区量化覆盖 GGUF、MLX、AWQ 全栈，Unsloth、Jackrong 等社区力量快速跟进，形成"发布即量化"的成熟管线。**DeepSeek 与 Google 双头并进**：前者以技术深度（V4-Pro 4K+ 点赞）征服开发者，后者以 Gemma-4 千万下载量证明开源分发渠道的统治力。值得警惕的是，**真正创新的 any-to-any（Lance）、3D 生成（Pixal3D）下载量极低**，反映开源社区仍偏好"安全"的 LLM 微调，前沿多模态落地存在鸿沟。量化领域出现分化：GGUF 主导消费端（百万级下载），但 W4A4、MTP 等算法创新尚未形成社区共识。

---

## 值得探索

| 模型 | 理由 |
|:---|:---|
| **[bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance)** | **架构级创新**。any-to-any 是 2026 年多模态的圣杯——单一模型统一理解/生成、跨模态任意转换，可能替代当前割裂的"LLM+扩散模型"拼接方案。字节跳动首次将这一概念产品化，值得深度拆解其注意力机制与训练策略。 |
| **[SulphurAI/Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)** | **开源视频生成的临界点**。125 万下载量意味着社区已验证其可用性，diffusers+GGUF 双格式支持降低门槛。若配合 Anima 的 ComfyUI 工作流，可能形成开源视频生产的完整工具链，对标 Runway/可灵。 |
| **[google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)** | **开源战略的风向标**。千万级下载不仅是数字，更是 Google 对开源生态的"定价权"——Gemma-4 性能对标 GPT-4o 级闭源模型，却以 Apache 许可释放，直接压缩商业 API 溢价空间。研究其训练数据与对齐方法，可预判 Google I/O 后的技术路线。 |

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*