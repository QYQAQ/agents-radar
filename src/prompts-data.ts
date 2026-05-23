/**
 * LLM prompt builders for data-source reports (trending, web, HN)
 * and rollup reports (weekly, monthly).
 *
 * Separated from prompts.ts to keep each module focused.
 */

import type { WebFetchResult } from "./web.ts";
import type { TrendingData } from "./trending.ts";
import type { HnData } from "./hn.ts";
import type { PhData } from "./ph.ts";
import type { ArxivData } from "./arxiv.ts";
import type { HfData } from "./hf.ts";
import type { DevtoData } from "./devto.ts";
import type { LobstersData } from "./lobsters.ts";
import type { Lang } from "./i18n.ts";
export function buildTrendingPrompt(data: TrendingData, dateStr: string, lang: Lang = "zh"): string {
  const trendingSection =
    data.trendingFetchSuccess && data.trendingRepos.length > 0
      ? data.trendingRepos
          .map(
            (r) =>
              `- [${r.fullName}](${r.url})` +
              (r.language ? ` [${r.language}]` : "") +
              ` ⭐${r.totalStars.toLocaleString()}` +
              (r.todayStars > 0 ? ` (+${r.todayStars} today)` : "") +
              (r.forks > 0 ? ` 🍴${r.forks.toLocaleString()}` : "") +
              (r.description ? `\n  ${r.description}` : ""),
          )
          .join("\n")
      : lang === "en"
        ? "(Unable to fetch today's GitHub Trending list)"
        : "（未能抓取今日 GitHub Trending 榜单）";

  const searchSection =
    data.searchRepos.length > 0
      ? data.searchRepos
          .map(
            (r) =>
              `- [${r.fullName}](${r.url})` +
              (r.language ? ` [${r.language}]` : "") +
              ` ⭐${r.stargazersCount.toLocaleString()}` +
              ` [topic:${r.searchQuery}]` +
              (r.description ? `\n  ${r.description}` : ""),
          )
          .join("\n")
      : lang === "en"
        ? "(No search results)"
        : "（无搜索结果）";

  if (lang === "en") {
    return `You are a research analyst focused on long-context reasoning, OCR/HMER, multimodal reasoning, post-training alignment, and hallucination mitigation. The following is ${dateStr} GitHub trending repository data. Please STRICTLY filter for relevance to your research directions only, categorize, and analyze trends. Skip unrelated general tools, frontend frameworks, games, chatbots, or pure business applications.

## Data Sources
- **Trending List** (github.com/trending, today's stars most reliable): Real-time hot list with today's new stars
- **Topic Search** (GitHub Search API, topic tags): AI-related projects active in last 7 days, grouped by topic

---

## GitHub Today's Trending (${data.trendingRepos.length} repositories)
${trendingSection}

---

## AI Topic Search Results (${data.searchRepos.length} repositories, deduplicated)
${searchSection}

---

Generate a structured AI Open Source Trends Report in English:

**Step 1 (Filter)**: From the above data, select ONLY projects clearly related to your research directions: long-context reasoning, OCR/document understanding, HMER, multimodal reasoning (VLM), post-training alignment (RLHF/DPO/SFT), or hallucination mitigation. Exclude unrelated general tools, frontend frameworks, games, chatbots, and pure business applications.

**Step 2 (Categorize)**: Group filtered projects into these categories (a project can belong to multiple; pick the primary one):
- 📄 OCR & Document Intelligence (text recognition, layout analysis, PDF parsing, HMER)
- 🎭 Multimodal Reasoning (vision-language models, visual QA, cross-modal alignment)
- 🧠 Long-Context & Reasoning (context window extension, reasoning frameworks, chain-of-thought)
- 🔧 Post-Training & Alignment (RLHF, DPO, SFT, preference optimization, reasoning enhancement)
- 👁️ Hallucination & Reliability (fact grounding, hallucination detection, confidence calibration)
- 🏗️ Infrastructure (training frameworks, inference engines, evaluation tools for above areas)

**Step 3 (Output Report)** with these sections:

1. **Today's Highlights** — 3-5 sentences on the most noteworthy developments relevant to long-context, OCR/multimodal, post-training, or hallucination research today

2. **Top Projects by Category** — For each category, list 3-8 representative projects, each with:
   - Project name (with link)
   - Stars data (total + today's new, if available)
   - One sentence: what it is and why it's worth attention today

3. **Research Trend Signal Analysis** — 200-300 words, distill from today's hot list:
   - Which research-relevant tools (OCR, multimodal, alignment, reasoning) are gaining community attention?
   - Any new open-source models, benchmarks, or frameworks relevant to your focus areas?
   - Connection to recent research breakthroughs or model releases in long-context / vision-language / alignment

4. **Research Hot Spots** — Bullet list of 3-5 specific projects or directions worth researcher focus, with brief reasoning and relevance to your areas

Style: English, professional and concise, must include GitHub links for every project.
`;
  }

  return `你是一位专注于长上下文推理、OCR/HMER、多模态推理、post-training 对齐和幻觉缓解的研究分析师。以下是 ${dateStr} 的 GitHub 热门仓库数据，请严格按你的研究方向进行相关性筛选、分类和趋势分析。跳过无关的通用工具、前端框架、游戏、聊天机器人或纯商业应用。

## 数据说明
- **Trending 榜单**（github.com/trending，今日 stars 数最可信）：今日实时热榜，含今日新增 stars
- **主题搜索**（GitHub Search API，topic 标签）：7天内活跃的 AI 相关项目，按主题分类

---

## GitHub 今日 Trending 榜单（共 ${data.trendingRepos.length} 个仓库）
${trendingSection}

---

## AI 主题搜索结果（共 ${data.searchRepos.length} 个仓库，已去重）
${searchSection}

---

请生成一份结构清晰的《AI 开源趋势日报》，要求：

**第一步（过滤）**：从以上数据中只筛选与你的研究方向明确相关的项目：长上下文推理、OCR/文档理解、HMER、多模态推理（VLM）、post-training 对齐（RLHF/DPO/SFT）、幻觉缓解。排除无关的通用工具、前端框架、游戏、聊天机器人和纯商业应用。

**第二步（分类）**：将筛选后的项目按以下维度分类（一个项目可归入多类，优先归入最主要类别）：
- 📄 OCR 与文档智能（文本识别、版面分析、PDF 解析、HMER）
- 🎭 多模态推理（视觉语言模型、视觉问答、跨模态对齐）
- 🧠 长上下文与推理（上下文扩展、推理框架、思维链）
- 🔧 Post-Training 与对齐（RLHF、DPO、SFT、偏好优化、推理增强）
- 👁️ 幻觉与可靠性（事实 grounding、幻觉检测、可信度校准）
- 🏗️ 基础设施（上述领域的训练框架、推理引擎、评测工具）

**第三步（输出报告）**，包含以下部分：

1. **今日速览** — 3~5 句话概括今日与长上下文、OCR/多模态、post-training、幻觉研究相关的最值得关注的动向

2. **各维度热门项目** — 每个维度列出 3~8 个代表项目，每项包含：
   - 项目名（附链接）
   - stars 数据（总量 + 今日新增，如有）
   - 一句话说明：这个项目是什么，为什么今天值得关注

3. **研究趋势信号分析** — 200~300 字，从今日热榜中提炼：
   - 哪些与研究相关的工具（OCR、多模态、对齐、推理）正在获得社区关注？
   - 是否有与你的研究方向相关的新开源模型、基准测试或框架首次登榜？
   - 与近期长上下文/视觉语言/对齐领域的研究突破或模型发布的关联

4. **研究关注热点** — 以 bullet 形式列出 3~5 个值得研究者重点关注的具体项目或方向，给出简短理由及与你研究领域的相关性

语言要求：中文，专业简洁，每个项目必须附 GitHub 链接。
`;
}

export function buildWebReportPrompt(results: WebFetchResult[], dateStr: string, lang: Lang = "zh"): string {
  const isAnyFirstRun = results.some((r) => r.isFirstRun);

  const siteSections = results
    .map(({ siteName, isFirstRun, newItems, totalDiscovered }) => {
      const mode =
        lang === "en"
          ? isFirstRun
            ? `First full crawl (sitemap total ${totalDiscovered} URLs, showing latest ${newItems.length} articles)`
            : `Incremental update, ${newItems.length} new articles today`
          : isFirstRun
            ? `首次全量抓取（sitemap 共 ${totalDiscovered} 条 URL，以下为最新 ${newItems.length} 篇正文内容）`
            : `今日增量更新，共 ${newItems.length} 篇新内容`;

      if (newItems.length === 0) {
        const noContent =
          lang === "en" ? `(${mode}, no content to analyze.)` : `（${mode}，暂无可供分析的内容。）`;
        return `## ${siteName}\n\n${noContent}`;
      }

      const categoryLabel = lang === "en" ? "Category" : "分类";
      const dateLabel = lang === "en" ? "Published/Updated" : "发布/更新";
      const unknownDate = lang === "en" ? "unknown" : "未知";
      const excerptLabel = lang === "en" ? "Excerpt" : "内容节选";
      const metadataOnlyNote =
        lang === "en"
          ? "(metadata-only: title derived from URL slug, may be inaccurate; no article text available)"
          : "（仅元数据：标题由 URL 路径推断，可能不准确；无法获取正文内容）";
      const itemsText = newItems
        .map((item) => {
          const lines = [
            `### [${item.title || item.url}](${item.url})`,
            `- ${categoryLabel}: ${item.category} | ${dateLabel}: ${item.lastmod.slice(0, 10) || unknownDate}`,
          ];
          if (item.content) {
            lines.push(`- ${excerptLabel}: ${item.content}`);
          } else {
            lines.push(`- ${metadataOnlyNote}`);
          }
          return lines.join("\n");
        })
        .join("\n\n");

      const lp = lang === "en" ? "(" : "（";
      const rp = lang === "en" ? ")" : "）";
      return `## ${siteName}${lp}${mode}${rp}\n\n${itemsText}`;
    })
    .join("\n\n---\n\n");

  const firstRunNote =
    lang === "en"
      ? isAnyFirstRun
        ? "This is the first full crawl. Please focus on the overall content landscape, historical context, and core themes of each site, rather than individual articles."
        : "This is an incremental update. Please focus on today's new content and assess its strategic significance in context."
      : isAnyFirstRun
        ? "本次为首次全量抓取，请重点梳理各站点的内容格局、历史脉络与核心主题，而非仅关注单篇文章。"
        : "本次为增量更新，请聚焦今日新增内容，并结合上下文判断其战略意义。";

  if (lang === "en") {
    return `You are a research analyst focused on long-context reasoning, OCR/HMER, multimodal reasoning, post-training alignment, and hallucination mitigation. Skilled at extracting research-relevant signals from official announcements, technical blogs, and product documentation.

The following content was crawled on ${dateStr} from Anthropic (claude.com / anthropic.com) and OpenAI (openai.com). ${firstRunNote}

${siteSections}

---

Generate a research-focused Official Content Tracking Report in English with these sections:

1. **Today's Highlights** — 3-5 sentences on the most important developments relevant to long-context, multimodal, alignment, or hallucination research

2. **Anthropic / Claude Research Highlights** — Organize content by relevance to your focus areas. For each relevant piece:
   - 2-4 sentences extracting technical insights, model capabilities, or research methodology
   - Note publication date and original link
   - Assess relevance to OCR, multimodal reasoning, post-training, or hallucination mitigation
   - If first full crawl, trace research milestones chronologically

3. **OpenAI Research Highlights** — Same structure, focus on research / safety / model capabilities
   - ⚠️ Note: OpenAI data is metadata-only. Only list URLs and categories objectively. Do NOT fabricate content. If information is insufficient, state the limitation clearly.

4. **Research Signal Analysis** — Based on both companies' release cadence and content focus, analyze:
   - Each company's recent research priorities (model capabilities / multimodal / safety / alignment)
   - Implications for long-context handling, visual understanding, and reasoning reliability
   - Potential impact on researchers in your focus areas

5. **Notable Research Details** — Extract hidden signals from titles, phrasing, and timing, e.g.:
   - New terms or topics relevant to your research areas appearing for the first time
   - Dense releases in multimodal, alignment, or safety categories
   - Policy, safety, and hallucination-related developments

${isAnyFirstRun ? "6. **Content Landscape Overview** — First full crawl only: summarize the content category distribution for both companies and describe their content strategy style (academic-oriented vs product-oriented vs user stories, etc.)\n\n" : ""}Style: English, professional and detailed, suited for AI researchers, product managers, and technical decision-makers. Every item must include official links.
`;
  }

  return `你是一位专注于长上下文推理、OCR/HMER、多模态推理、post-training 对齐和幻觉缓解的研究分析师，擅长从官方公告、技术博客和产品文档中提炼与研究相关的信号。

以下是 ${dateStr} 从 Anthropic（claude.com / anthropic.com）和 OpenAI（openai.com）官网抓取的内容，${firstRunNote}

${siteSections}

---

请生成一份研究导向的《官方内容追踪报告》，包含以下部分：

1. **今日速览** — 3~5 句话概括与长上下文、多模态、对齐或幻觉研究相关的最重要的新发布或动向

2. **Anthropic / Claude 研究精选** — 按与你研究方向的相关性整理内容。每篇相关文章：
   - 用 2~4 句话提炼技术洞察、模型能力或研究方法论
   - 标注发布日期和原文链接
   - 评估与 OCR、多模态推理、post-training、幻觉缓解的相关性
   - 如首次全量，按时间线梳理研究里程碑

3. **OpenAI 研究精选** — 同上，聚焦 research / safety / model capabilities
   - ⚠️ 注意：OpenAI 数据为仅元数据模式。请仅基于 URL 和分类进行客观列举，不要编造内容摘要。如果信息不足以分析，直接说明数据受限即可。

4. **研究信号解读** — 基于两家公司的发布节奏和内容重点，分析：
   - 各自近期的研究优先级（模型能力 / 多模态 / 安全 / 对齐）
   - 对长上下文处理、视觉理解和推理可靠性的影响
   - 对你研究领域研究者的潜在影响

5. **值得关注的研究细节** — 从标题、措辞、发布时机中提取隐含信号，例如：
   - 与你研究领域相关的新兴词汇或话题的首次出现
   - 多模态、对齐或安全类别的密集发布
   - 政策、安全和幻觉相关的动向

${isAnyFirstRun ? "6. **内容格局总览** — 首次全量独有：汇总两家公司各内容类别的数量分布，并说明各自的内容运营风格（学术导向 vs 产品导向 vs 用户故事等）\n\n" : ""}语言要求：中文，专业深入，内容详实，适合 AI 领域研究者、产品经理和技术决策者阅读。每个条目必须附上 GitHub/官网链接。
`;
}

export function buildWeeklyPrompt(
  dailyDigests: Record<string, string>,
  weekStr: string,
  lang: Lang = "zh",
): string {
  const digestEntries = Object.entries(dailyDigests)
    .map(([date, content]) => `## ${date}\n\n${content}`)
    .join("\n\n---\n\n");

  if (lang === "en") {
    return `You are a research analyst focused on long-context reasoning, OCR/HMER, multimodal reasoning, post-training alignment, and hallucination mitigation. The following are daily research digest summaries from the past 7 days (${weekStr}). Generate a comprehensive weekly recap focused on your research directions.

${digestEntries}

---

Generate a Research Weekly Report with these sections:

1. **Week's Top Research Stories** - 5-8 most important research-relevant events, paper releases, and community developments this week, each with date
2. **OCR & Document Intelligence Progress** - Key developments in text recognition, layout analysis, HMER, and document understanding tools this week
3. **Multimodal & Reasoning Ecosystem** - Key developments in vision-language models, long-context handling, and reasoning enhancement this week
4. **Post-Training & Alignment Trends** - Most notable directions in RLHF, DPO, SFT, preference optimization, and alignment research this week
5. **Hallucination & Reliability Highlights** - Core discussions and developments on hallucination detection, fact grounding, and model trustworthiness this week
6. **Research Community Pulse** - Notable technical discussions from Hacker News and GitHub relevant to your focus areas
7. **Next Week's Research Signals** - Based on this week's data, predict research trends and upcoming papers/events worth watching

Style: English, concise and professional, helping technical developers quickly grasp the week's developments.
`;
  }

  return `你是一位专注于长上下文推理、OCR/HMER、多模态推理、post-training 对齐和幻觉缓解的研究分析师。以下是过去 7 天（${weekStr}）的每日研究动态摘要，请生成本周综合回顾报告。

${digestEntries}

---

请生成《研究动态周报》，包含以下部分：

1. **本周研究要闻** - 5-8 条本周最重要的研究相关事件、论文发布、社区动向，每条附日期
2. **OCR 与文档智能进展** - 文本识别、版面分析、HMER、文档理解工具的本周关键进展
3. **多模态与推理生态** - 视觉语言模型、长上下文处理、推理增强的本周关键进展
4. **Post-Training 与对齐趋势** - RLHF、DPO、SFT、偏好优化和对齐研究的本周显著方向
5. **幻觉与可靠性亮点** - 幻觉检测、事实 grounding、模型可信度的本周核心讨论和进展
6. **研究社区脉搏** - 本周 Hacker News 和 GitHub 上与你关注领域相关的技术讨论
7. **下周研究信号** - 基于本周数据，预判值得关注的研究趋势或即将到来的论文/事件

语言要求：中文，简洁专业，适合技术开发者快速掌握一周动态。
`;
}

export function buildMonthlyPrompt(
  sourceDigests: Record<string, string>,
  monthStr: string,
  lang: Lang = "zh",
): string {
  const digestEntries = Object.entries(sourceDigests)
    .map(([key, content]) => `## ${key}\n\n${content}`)
    .join("\n\n---\n\n");

  if (lang === "en") {
    return `You are a research analyst focused on long-context reasoning, OCR/HMER, multimodal reasoning, post-training alignment, and hallucination mitigation. The following are ${monthStr} research digest summaries (${Object.keys(sourceDigests).length} reports total). Generate a comprehensive monthly review focused on your research directions.

${digestEntries}

---

Generate a Research Monthly Report with these sections:

1. **Month's Top Research Stories** - 5-10 most important research events and milestones this month, in chronological order
2. **OCR & Document Intelligence Monthly** - Overall development trajectory, major model releases, and dataset/tool progress in text recognition and document understanding
3. **Multimodal & Reasoning Ecosystem Review** - Landscape shifts, emerging VLM projects, long-context breakthroughs, and reasoning enhancement signals this month
4. **Post-Training & Alignment Trend Summary** - Most significant directions in RLHF, DPO, SFT, preference optimization, and alignment methodology this month
5. **Hallucination & Reliability Assessment** - Monthly progress on hallucination detection, fact grounding, and model trustworthiness evaluation
6. **Research Community Health** - Monthly activity comparison across research-relevant projects, researcher engagement evaluation
7. **Next Month's Research Outlook** - Based on this month's trends, predict key research directions and potential paper releases/events to watch

Style: English, in-depth analysis, data-driven, suited for monthly retrospectives and strategic decision-making.
`;
  }

  return `你是一位专注于长上下文推理、OCR/HMER、多模态推理、post-training 对齐和幻觉缓解的研究分析师。以下是 ${monthStr} 月的研究动态汇总（共 ${Object.keys(sourceDigests).length} 份报告），请生成本月综合回顾报告。

${digestEntries}

---

请生成《研究动态月报》，包含以下部分：

1. **月度研究要闻** - 本月最重要的 5-10 条研究事件和里程碑，按时间排列
2. **OCR 与文档智能月度进展** - 文本识别和文档理解领域的主要模型发布、数据集/工具进展的整体发展轨迹
3. **多模态与推理生态月报** - 本月视觉语言模型格局变化、新兴项目、长上下文突破和推理增强信号
4. **Post-Training 与对齐趋势总结** - 本月 RLHF、DPO、SFT、偏好优化和对齐方法论的最显著方向
5. **幻觉与可靠性评估** - 本月幻觉检测、事实 grounding 和模型可信度评估的进展
6. **研究社区健康度** - 各研究相关项目的月度活跃度对比、研究者参与度评估
7. **下月研究展望** - 基于本月趋势，预判值得重点关注的研究方向和潜在论文发布/事件

语言要求：中文，深度分析，数据驱动，适合月度复盘和战略决策参考。
`;
}

// ---------------------------------------------------------------------------
// Highlights prompt — extracts structured highlights from finished reports
// for use in Telegram notifications.
// ---------------------------------------------------------------------------

export interface ReportHighlights {
  [reportId: string]: string[];
}

export function buildHighlightsPrompt(
  reportContents: Record<string, string>,
  lang: Lang = "zh",
  itemsPerReport: number = 6,
): string {
  const sections = Object.entries(reportContents)
    .map(([id, content]) => `## [${id}]\n\n${content.slice(0, 2000)}`)
    .join("\n\n---\n\n");

  if (lang === "en") {
    return `You are a concise research editor. The following are today's research digest excerpts, each labeled with a report ID.

${sections}

---

For each report, extract ${itemsPerReport} of the most noteworthy research highlights — the kind that would make a researcher want to click through. Each highlight should be a single short sentence (under 60 characters).

Return ONLY valid JSON, no markdown fences, no explanation. Format:
{"ai-cli":["highlight 1","highlight 2",...],"ai-agents":["highlight 1","highlight 2",...],...}

Rules:
- Use the exact report IDs from the [brackets] above as keys
- Only include reports that have meaningful content (skip reports with failure messages or no activity)
- ${itemsPerReport} highlights per report, each under 60 characters
- Focus on: new paper releases, notable research features, trending research projects, key technical discussions relevant to long-context, OCR/multimodal, alignment, or hallucination
- Be specific: include project names, version numbers, star counts where relevant`;
  }

  return `你是一位简洁的研究编辑。以下是今日各研究动态报告的摘要，每个报告用 ID 标注。

${sections}

---

为每份报告提取 ${itemsPerReport} 条最值得关注的研究亮点——能让研究者产生点击欲望的那种。每条亮点用一句简短的话（不超过 30 个字）。

只返回合法的 JSON，不要 markdown 代码块，不要解释。格式：
{"ai-cli":["亮点1","亮点2",...],"ai-agents":["亮点1","亮点2",...],...}

规则：
- 用上面方括号中的报告 ID 作为 key
- 只包含有实际内容的报告（跳过失败或无活动的报告）
- 每个报告 ${itemsPerReport} 条亮点，每条不超过 30 个字
- 重点关注：新论文发布、重要研究特性、热门研究项目、与长上下文/OCR/多模态/对齐/幻觉相关的关键技术讨论
- 要具体：包含项目名、版本号、star 数等关键信息`;
}

export function buildHnPrompt(data: HnData, dateStr: string, lang: Lang = "zh"): string {
  const storiesText = data.stories
    .map((s, i) =>
      lang === "en"
        ? `${i + 1}. **${s.title}**\n` +
          `   Link: ${s.url}\n` +
          `   Discussion: ${s.hnUrl}\n` +
          `   Score: ${s.points} | Comments: ${s.comments} | Author: ${s.author} | Time: ${s.createdAt.slice(0, 16)}`
        : `${i + 1}. **${s.title}**\n` +
          `   链接: ${s.url}\n` +
          `   讨论: ${s.hnUrl}\n` +
          `   分数: ${s.points} | 评论: ${s.comments} | 作者: ${s.author} | 时间: ${s.createdAt.slice(0, 16)}`,
    )
    .join("\n\n");

  if (lang === "en") {
    return `You are a research analyst focused on long-context reasoning, OCR/HMER, multimodal reasoning, post-training alignment, and hallucination mitigation. The following are top posts from Hacker News in the past 24 hours as of ${dateStr}. Please STRICTLY filter for posts relevant to your research directions. Ignore startup funding, product launches, and general industry news unrelated to your focus areas.

---

${storiesText}

---

Generate a research-focused Hacker News Digest in English:

1. **Today's Research Highlights** — 3-5 sentences on the hottest technical discussions relevant to long-context, multimodal, OCR, alignment, or hallucination research on HN today

2. **Research News & Discussions** — Organized by research direction, select the 2-5 most representative items per category. If a category has no relevant posts, state "No relevant posts today." Each item includes:
   - Title (with original link) + HN discussion link
   - Score and comment count
   - One sentence: research significance and community reaction

   Categories:
   - 🧠 Long-Context & Reasoning (context windows, reasoning methods, comprehension)
   - 📄 OCR & Document Intelligence (text recognition, PDF processing, HMER)
   - 🎭 Multimodal & Vision-Language (VLMs, visual reasoning, cross-modal models)
   - 🔧 Post-Training & Alignment (RLHF, DPO, SFT, preference optimization)
   - 👁️ Hallucination & Reliability (fact-checking, grounding, trustworthiness)

3. **Community Sentiment Signal** — 100-200 words analyzing today's HN discussion mood in your focus areas:
   - Which research topics are most active (high score + high comments)?
   - Any controversy or consensus on alignment, hallucination, or multimodal capabilities?
   - Compared to last cycle, any notable shift in research focus?

4. **Worth Deep Reading** — List 2-3 pieces most worth researchers reading in depth, with brief reasoning about research relevance

Style: English, concise and professional, preserve all original links.
`;
  }

  return `你是一位专注于长上下文推理、OCR/HMER、多模态推理、post-training 对齐和幻觉缓解的研究分析师。以下是 ${dateStr} 从 Hacker News 抓取的过去 24 小时内热门帖子。请严格筛选与你研究方向相关的内容，忽略创业融资、产品发布和无关的行业新闻。

---

${storiesText}

---

请生成一份研究导向的《Hacker News 研究动态日报》，要求：

1. **今日研究速览** — 3~5 句话，概括今日 HN 社区围绕长上下文、多模态、OCR、对齐、幻觉研究最热门的讨论方向和情绪

2. **研究新闻与讨论** — 按以下研究方向分类整理，每类选取最具代表性的 2~5 条。如某方向无相关帖子，注明"今日无相关帖子"。每条包含：
   - 标题（附原文链接）+ HN 讨论链接
   - 分数和评论数
   - 一句话说明：研究意义及社区典型反应

   分类：
   - 🧠 长上下文与推理（上下文窗口、推理方法、理解能力）
   - 📄 OCR 与文档智能（文本识别、PDF 处理、HMER）
   - 🎭 多模态与视觉语言（VLM、视觉推理、跨模态模型）
   - 🔧 Post-Training 与对齐（RLHF、DPO、SFT、偏好优化）
   - 👁️ 幻觉与可靠性（事实核查、grounding、可信度）

3. **社区情绪信号** — 100~200 字，分析今日 HN 在你关注领域的讨论情绪：
   - 哪些研究话题最活跃（高分 + 高评论）？
   - 对齐、幻觉或多模态能力方面有无争议或共识？
   - 与上周期相比，研究关注方向有无明显变化？

4. **值得深读** — 列出 2~3 条今日最值得研究者深入阅读的内容，简述研究相关理由

语言要求：中文，简洁专业，保留所有原文链接。
`;
}

export function buildPhPrompt(data: PhData, dateStr: string, lang: Lang = "zh"): string {
  const productsText = data.products
    .map((p, i) =>
      lang === "en"
        ? `${i + 1}. **${p.name}** — ${p.tagline}\n` +
          `   Product Hunt: ${p.url}\n` +
          `   Website: ${p.website}\n` +
          `   Votes: ${p.votesCount} | Comments: ${p.commentsCount} | Topics: ${p.topics.join(", ")}`
        : `${i + 1}. **${p.name}** — ${p.tagline}\n` +
          `   Product Hunt: ${p.url}\n` +
          `   官网: ${p.website}\n` +
          `   投票: ${p.votesCount} | 评论: ${p.commentsCount} | 话题: ${p.topics.join(", ")}`,
    )
    .join("\n\n");

  if (lang === "en") {
    return `You are a research analyst focused on long-context reasoning, OCR/HMER, multimodal reasoning, post-training alignment, and hallucination mitigation. The following are products launched on Product Hunt in the past 24 hours. Please STRICTLY filter for products relevant to your research directions: tools for document understanding, visual reasoning, alignment evaluation, or research workflows. Skip general chatbots, marketing tools, and unrelated SaaS products.

---

${productsText}

---

Generate a research-focused Product Hunt Digest in English:

1. **Today's Highlights** — 3-5 sentences on the most notable product launches relevant to document intelligence, multimodal reasoning, alignment tools, or research workflows on Product Hunt today

2. **Top Products** — Organized by research relevance, select the most representative products per category. If a category has no relevant products, state "No relevant products today." Each includes:
   - Product name + tagline (with Product Hunt link and website link)
   - Vote count and comment count
   - One sentence: what research problem it addresses, why it stands out for researchers

   Categories:
   - 📄 Document Intelligence & OCR (PDF tools, text extraction, formula recognition, layout analysis)
   - 🎭 Multimodal & Vision (visual reasoning tools, image-to-text, cross-modal platforms)
   - 🔧 Alignment & Evaluation (RLHF tools, preference data collection, hallucination detection, model eval)
   - 🧠 Reasoning & Research (long-context tools, chain-of-thought visualization, research assistants)
   - 🏗️ Research Infrastructure (training platforms, dataset tools, benchmarking suites)

3. **Research Market Signal** — 100-200 words analyzing today's launch patterns relevant to your focus areas:
   - Which research-tool categories are most active?
   - Any innovative approaches to OCR, multimodal understanding, or alignment?
   - Open-source vs closed-source trend among research tools

4. **Worth Exploring** — List 2-3 products most worth researchers exploring, with brief reasoning about research utility

Style: English, concise and professional, preserve all original links.
`;
  }

  return `你是一位专注于长上下文推理、OCR/HMER、多模态推理、post-training 对齐和幻觉缓解的研究分析师。以下是 ${dateStr} 从 Product Hunt 抓取的过去 24 小时内产品发布。请严格筛选与你研究方向相关的产品：文档理解、视觉推理、对齐评测或研究工作流工具。跳过通用聊天机器人、营销工具和无关的 SaaS 产品。

---

${productsText}

---

请生成一份研究导向的《Product Hunt 研究工具日报》，要求：

1. **今日速览** — 3~5 句话，概括今日 Product Hunt 上与文档智能、多模态推理、对齐工具或研究工作流相关的产品发布趋势和亮点

2. **热门产品** — 按研究相关性分类整理，每类选取最具代表性的产品。如某方向无相关产品，注明"今日无相关产品"。每个产品包含：
   - 产品名 + 简介（附 Product Hunt 链接和官网链接）
   - 投票数和评论数
   - 一句话说明：解决什么研究问题，对研究者有何独特价值

   分类：
   - 📄 文档智能与 OCR（PDF 工具、文本提取、公式识别、版面分析）
   - 🎭 多模态与视觉（视觉推理工具、图像到文本、跨模态平台）
   - 🔧 对齐与评测（RLHF 工具、偏好数据收集、幻觉检测、模型评测）
   - 🧠 推理与研究（长上下文工具、思维链可视化、研究助手）
   - 🏗️ 研究基础设施（训练平台、数据集工具、基准测试套件）

3. **研究市场信号** — 100~200 字，分析今日与你关注领域相关的产品发布规律：
   - 哪些研究工具类别最活跃？
   - OCR、多模态理解或对齐方面有无创新性思路？
   - 研究工具中开源 vs 闭源的趋势

4. **值得探索** — 列出 2~3 个最值得研究者探索的产品，简述研究价值

语言要求：中文，简洁专业，保留所有原文链接。
`;
}

// ---------------------------------------------------------------------------
// ArXiv prompt
// ---------------------------------------------------------------------------

export function buildArxivPrompt(data: ArxivData, dateStr: string, lang: Lang = "zh"): string {
  const papersText = data.papers
    .map((p, i) => {
      const authors =
        p.authors.length > 3 ? p.authors.slice(0, 3).join(", ") + " et al." : p.authors.join(", ");
      const cats = p.categories.slice(0, 3).join(", ");
      return lang === "en"
        ? `${i + 1}. **${p.title}**\n` +
            `   Link: ${p.url}\n` +
            `   Authors: ${authors} | Categories: ${cats}\n` +
            `   Published: ${p.published.slice(0, 10)}\n` +
            `   Abstract: ${p.summary.slice(0, 300)}${p.summary.length > 300 ? "..." : ""}`
        : `${i + 1}. **${p.title}**\n` +
            `   链接: ${p.url}\n` +
            `   作者: ${authors} | 分类: ${cats}\n` +
            `   发布: ${p.published.slice(0, 10)}\n` +
            `   摘要: ${p.summary.slice(0, 300)}${p.summary.length > 300 ? "..." : ""}`;
    })
    .join("\n\n");

  if (lang === "en") {
    return `You are a research analyst focused on long-context reasoning, OCR/HMER, multimodal reasoning, post-training alignment, and hallucination mitigation. The following are recent papers from ArXiv as of ${dateStr} (${data.papers.length} papers from targeted keyword searches covering cs.CV, cs.CL, cs.AI, cs.LG).

---

${papersText}

---

Generate a structured Research Digest in English:

1. **Today's Highlights** — 3-5 sentences on the most significant research directions and breakthroughs relevant to your focus areas

2. **Key Papers** — Select 8-15 most important papers, organized by research direction:
   - 📄 Dense Text OCR & Document Intelligence (text recognition, layout analysis, scene text, document understanding)
   - 🖋️ Handwritten Math Expression Recognition HMER (formula recognition, symbolic decoding, math datasets)
   - 🧠 Long-Context Comprehension & Reasoning (context extension, positional encoding, long-document understanding, reasoning methods)
   - 🎭 Multimodal Reasoning (vision-language models, visual QA, cross-modal alignment, image-text understanding)
   - 🔧 Post-Training & Alignment (RLHF, DPO, SFT, preference optimization, test-time compute, reasoning enhancement)
   - 👁️ Hallucination Detection & Mitigation (fact grounding, confidence calibration, trustworthiness evaluation)

   For each paper:
   - Title (with ArXiv link)
   - Authors (abbreviated)
   - One sentence: key contribution and why it matters to researchers in your focus areas

3. **Research Trend Signal** — 100-200 words on emerging research directions visible from today's submissions relevant to your focus areas

4. **Worth Deep Reading** — 2-3 papers most worth reading in full, with reasoning about relevance to OCR, multimodal, alignment, or hallucination research

Style: English, concise and professional, preserve all ArXiv links.
`;
  }

  return `你是一位专注于长上下文推理、OCR/HMER、多模态推理、post-training 对齐和幻觉缓解的研究分析师。以下是 ${dateStr} ArXiv 上最新的相关论文（共 ${data.papers.length} 篇，来自针对 cs.CV、cs.CL、cs.AI、cs.LG 的关键词搜索）：

---

${papersText}

---

请生成一份结构清晰的研究日报，要求：

1. **今日速览** — 3~5 句话，概括今日与你关注领域最相关的研究方向和突破

2. **重点论文** — 选出 8~15 篇最重要的论文，按研究方向分类：
   - 📄 密集文本 OCR 与文档智能（文本识别、版面分析、场景文本、文档理解）
   - 🖋️ 手写数学公式识别 HMER（公式识别、符号解码、数学数据集）
   - 🧠 长上下文理解与推理（上下文扩展、位置编码、长文档理解、推理方法）
   - 🎭 多模态推理（视觉语言模型、视觉问答、跨模态对齐、图文理解）
   - 🔧 Post-Training 与对齐（RLHF、DPO、SFT、偏好优化、推理时计算、推理增强）
   - 👁️ 幻觉检测与缓解（事实 grounding、可信度校准、可靠性评估）

   每篇论文包含：
   - 标题（附 ArXiv 链接）
   - 作者（缩写）
   - 一句话说明：核心贡献及对你研究方向的研究价值

3. **研究趋势信号** — 100~200 字，从今日投稿中观察到的与你关注领域相关的新兴研究方向

4. **值得精读** — 2~3 篇最值得完整阅读的论文，简述与 OCR、多模态、对齐或幻觉研究的相关性

语言要求：中文，简洁专业，保留所有 ArXiv 链接。
`;
}

// ---------------------------------------------------------------------------
// Hugging Face prompt
// ---------------------------------------------------------------------------

export function buildHfPrompt(data: HfData, dateStr: string, lang: Lang = "zh"): string {
  const modelsText = data.models
    .map((m, i) =>
      lang === "en"
        ? `${i + 1}. **${m.id}**\n` +
          `   Link: ${m.url}\n` +
          `   Author: ${m.author} | Pipeline: ${m.pipelineTag || "N/A"}\n` +
          `   Likes: ${m.likes.toLocaleString()} | Downloads: ${m.downloads.toLocaleString()}\n` +
          `   Tags: ${m.tags.slice(0, 5).join(", ")}`
        : `${i + 1}. **${m.id}**\n` +
          `   链接: ${m.url}\n` +
          `   作者: ${m.author} | 任务: ${m.pipelineTag || "N/A"}\n` +
          `   点赞: ${m.likes.toLocaleString()} | 下载: ${m.downloads.toLocaleString()}\n` +
          `   标签: ${m.tags.slice(0, 5).join(", ")}`,
    )
    .join("\n\n");

  if (lang === "en") {
    return `You are a research analyst focused on long-context reasoning, OCR/HMER, multimodal reasoning, post-training alignment, and hallucination mitigation. The following are trending models on Hugging Face Hub as of ${dateStr} (${data.models.length} models, sorted by weekly likes). Please focus on models relevant to your research directions.

---

${modelsText}

---

Generate a structured Hugging Face Research Models Digest in English:

1. **Today's Highlights** — 3-5 sentences on the most notable model releases and trends relevant to OCR, multimodal reasoning, long-context, alignment, or hallucination research on Hugging Face

2. **Trending Models** — Organized by research relevance, each with:
   - Model name (with HF link)
   - Author, likes, downloads
   - One sentence: what it is, why it's trending, and relevance to your focus areas

   Categories:
   - 📄 OCR & Document Models (text recognition, layout analysis, document understanding, formula recognition)
   - 🎭 Multimodal & Vision-Language (VLMs, visual encoders, cross-modal models, image-text understanding)
   - 🧠 Long-Context & Reasoning Models (extended context LLMs, reasoning-enhanced models, math models)
   - 🔧 Post-Training & Alignment (RLHF/DPO/SFT models, preference-tuned models, alignment-focused releases)
   - 👁️ Hallucination Mitigation (fact-grounded models, calibrated confidence models, RAG-enhanced models)
   - 🏗️ Research Infrastructure (training frameworks, evaluation suites, dataset tools for above areas)

3. **Research Ecosystem Signal** — 100-200 words analyzing model ecosystem trends relevant to your focus areas:
   - Which model families in OCR, multimodal, or alignment are gaining momentum?
   - Open-weight vs proprietary trends in vision-language and reasoning models
   - Notable fine-tuning or post-training activity for document understanding or hallucination mitigation

4. **Worth Exploring** — 2-3 models most worth researchers trying or studying, with reasoning about research relevance

Style: English, concise and professional, preserve all HuggingFace links.
`;
  }

  return `你是一位专注于长上下文推理、OCR/HMER、多模态推理、post-training 对齐和幻觉缓解的研究分析师。以下是 ${dateStr} Hugging Face Hub 上的热门模型（共 ${data.models.length} 个，按周点赞数排序）。请重点关注与你研究方向相关的模型。

---

${modelsText}

---

请生成一份研究导向的《Hugging Face 研究模型日报》，要求：

1. **今日速览** — 3~5 句话，概括 Hugging Face 上与 OCR、多模态推理、长上下文、对齐或幻觉研究相关的最值得关注的模型发布和趋势

2. **热门模型** — 按研究相关性分类整理，每个模型包含：
   - 模型名（附 HF 链接）
   - 作者、点赞数、下载数
   - 一句话说明：这个模型是什么，为什么上榜，以及与你研究方向的相关性

   分类：
   - 📄 OCR 与文档模型（文本识别、版面分析、文档理解、公式识别）
   - 🎭 多模态与视觉语言（VLM、视觉编码器、跨模态模型、图文理解）
   - 🧠 长上下文与推理模型（扩展上下文 LLM、推理增强模型、数学模型）
   - 🔧 Post-Training 与对齐（RLHF/DPO/SFT 模型、偏好微调模型、对齐-focused 发布）
   - 👁️ 幻觉缓解（事实 grounded 模型、校准置信度模型、RAG 增强模型）
   - 🏗️ 研究基础设施（上述领域的训练框架、评测套件、数据集工具）

3. **研究生态信号** — 100~200 字，分析与你关注领域相关的模型生态趋势：
   - OCR、多模态或对齐领域哪些模型家族势头正旺？
   - 视觉语言和推理模型中开源权重 vs 闭源的趋势
   - 文档理解或幻觉缓解方面的微调或后训练活动

4. **值得探索** — 2~3 个最值得研究者尝试或研究的模型，简述研究相关理由

语言要求：中文，简洁专业，保留所有 HuggingFace 链接。
`;
}

// ---------------------------------------------------------------------------
// Community prompt (Dev.to + Lobste.rs combined)
// ---------------------------------------------------------------------------

export function buildCommunityPrompt(
  devto: DevtoData,
  lobsters: LobstersData,
  dateStr: string,
  lang: Lang = "zh",
): string {
  const devtoText =
    devto.articles.length > 0
      ? devto.articles
          .map((a, i) =>
            lang === "en"
              ? `${i + 1}. **${a.title}**\n` +
                `   Link: ${a.url}\n` +
                `   Author: ${a.user} | Reactions: ${a.positiveReactionsCount} | Comments: ${a.commentsCount} | Reading: ${a.readingTimeMinutes} min\n` +
                `   Tags: ${a.tags.join(", ")}\n` +
                `   ${a.description}`
              : `${i + 1}. **${a.title}**\n` +
                `   链接: ${a.url}\n` +
                `   作者: ${a.user} | 点赞: ${a.positiveReactionsCount} | 评论: ${a.commentsCount} | 阅读: ${a.readingTimeMinutes} 分钟\n` +
                `   标签: ${a.tags.join(", ")}\n` +
                `   ${a.description}`,
          )
          .join("\n\n")
      : lang === "en"
        ? "(No Dev.to articles available)"
        : "（无 Dev.to 文章）";

  const lobstersText =
    lobsters.stories.length > 0
      ? lobsters.stories
          .map((s, i) =>
            lang === "en"
              ? `${i + 1}. **${s.title}**\n` +
                `   Link: ${s.url}\n` +
                `   Discussion: ${s.commentsUrl}\n` +
                `   Score: ${s.score} | Comments: ${s.commentCount} | Author: ${s.author} | Tags: ${s.tags.join(", ")}`
              : `${i + 1}. **${s.title}**\n` +
                `   链接: ${s.url}\n` +
                `   讨论: ${s.commentsUrl}\n` +
                `   分数: ${s.score} | 评论: ${s.commentCount} | 作者: ${s.author} | 标签: ${s.tags.join(", ")}`,
          )
          .join("\n\n")
      : lang === "en"
        ? "(No Lobste.rs stories available)"
        : "（无 Lobste.rs 内容）";

  if (lang === "en") {
    return `You are a research analyst focused on long-context reasoning, OCR/HMER, multimodal reasoning, post-training alignment, and hallucination mitigation. The following are content from Dev.to and Lobste.rs as of ${dateStr}. Please filter for articles and discussions relevant to your research directions: technical tutorials, implementation experiences, new tools, and research methods. Skip product promotions, business analysis, and general AI news.

## Dev.to Articles (${devto.articles.length} articles)

${devtoText}

---

## Lobste.rs Stories (${lobsters.stories.length} stories)

${lobstersText}

---

Generate a research-focused Tech Community Digest in English:

1. **Today's Research Highlights** — 3-5 sentences on the most discussed technical topics relevant to long-context, multimodal, OCR, alignment, or hallucination research across these communities today

2. **Dev.to Research Highlights** — Select 5-10 most valuable articles relevant to your focus areas:
   - Title (with link)
   - Reactions and comments
   - One sentence: key research takeaway or implementation insight

3. **Lobste.rs Research Highlights** — Select 3-8 most notable stories relevant to your focus areas:
   - Title (with link + discussion link)
   - Score and comments
   - One sentence: research relevance and why it's worth reading

4. **Research Community Pulse** — 100-200 words on what these communities are discussing in your focus areas:
   - Common research themes across both platforms
   - Practical implementation concerns for OCR, multimodal, or alignment researchers
   - Emerging tutorials, patterns, or best practices for document understanding, visual reasoning, or hallucination mitigation

5. **Worth Reading** — 2-3 articles/stories most worth reading in depth, with reasoning about research relevance

Style: English, concise and developer-friendly, preserve all original links.
`;
  }

  return `你是一位专注于长上下文推理、OCR/HMER、多模态推理、post-training 对齐和幻觉缓解的研究分析师。以下是 ${dateStr} Dev.to 和 Lobste.rs 上的内容。请筛选与你研究方向相关的文章和讨论：技术教程、实现经验、新工具和研究方法。跳过产品推广、商业分析和通用 AI 新闻。

## Dev.to 文章（共 ${devto.articles.length} 篇）

${devtoText}

---

## Lobste.rs 内容（共 ${lobsters.stories.length} 条）

${lobstersText}

---

请生成一份研究导向的《技术社区研究动态日报》，要求：

1. **今日研究速览** — 3~5 句话，概括今日技术社区围绕长上下文、多模态、OCR、对齐、幻觉研究最热门的讨论方向

2. **Dev.to 研究精选** — 选出 5~10 篇与你关注领域相关的最有价值的文章：
   - 标题（附链接）
   - 点赞数和评论数
   - 一句话说明：对研究者的核心收获或实现洞察

3. **Lobste.rs 研究精选** — 选出 3~8 条与你关注领域相关的最值得关注的内容：
   - 标题（附链接 + 讨论链接）
   - 分数和评论数
   - 一句话说明：研究相关性及为什么值得阅读

4. **研究社区脉搏** — 100~200 字，分析技术社区在你关注领域的讨论：
   - 两个平台共同关注的研究主题
   - OCR、多模态或对齐研究者的实际实现关切
   - 文档理解、视觉推理或幻觉缓解方面的新兴教程、模式或最佳实践

5. **值得精读** — 2~3 篇最值得深入阅读的内容，简述研究相关理由

语言要求：中文，简洁专业，保留所有原文链接。
`;
}
