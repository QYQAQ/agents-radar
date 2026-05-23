/**
 * ArXiv papers fetched via the ArXiv API (Atom feed).
 *
 * Strategy: keyword-based queries targeting research interests:
 * - Dense text OCR, HMER, document understanding
 * - Multimodal reasoning, vision-language models
 * - Long-context comprehension and reasoning
 * - Post-training alignment (RLHF, DPO, SFT)
 * - Hallucination detection and mitigation
 * Sorted by submission date, filtered to last 48h.
 */

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

export interface ArxivPaper {
  id: string;
  title: string;
  summary: string;
  authors: string[];
  published: string;
  updated: string;
  categories: string[];
  url: string;
  pdfUrl: string;
}

export interface ArxivData {
  papers: ArxivPaper[];
  fetchSuccess: boolean;
}

// ---------------------------------------------------------------------------
// Constants
// ---------------------------------------------------------------------------

const ARXIV_MAX_RESULTS = 50;
const API_URL = "https://export.arxiv.org/api/query";

/** Keyword-based search queries aligned with research interests. */
const SEARCH_QUERIES = [
  // OCR + HMER + document understanding
  "cat:cs.CV+AND+(all:OCR+OR+all:HMER+OR+all:%22handwritten+math%22+OR+all:%22document+understanding%22+OR+all:%22scene+text%22+OR+all:%22dense+text%22)",
  // Multimodal reasoning + vision-language + hallucination
  "(cat:cs.CV+OR+cat:cs.CL+OR+cat:cs.AI)+AND+(all:%22multimodal+reasoning%22+OR+all:%22vision+language%22+OR+all:VLM+OR+all:hallucination+OR+all:%22fact+grounding%22+OR+all:%22visual+reasoning%22)",
  // Long-context + comprehension
  "(cat:cs.CL+OR+cat:cs.AI+OR+cat:cs.LG)+AND+(all:%22long+context%22+OR+all:%22context+window%22+OR+all:%22long+document%22+OR+all:comprehension+OR+all:%22extended+context%22)",
  // Post-training + alignment + reasoning enhancement
  "(cat:cs.LG+OR+cat:cs.AI+OR+cat:cs.CL)+AND+(all:%22post-training%22+OR+all:RLHF+OR+all:DPO+OR+all:SFT+OR+all:%22preference+optimization%22+OR+all:%22reasoning+enhancement%22+OR+all:%22test-time+compute%22)",
];

/** Delay between requests (ArXiv asks for 3s). */
const REQUEST_DELAY_MS = 3000;

// ---------------------------------------------------------------------------
// XML helpers (lightweight, no dependency)
// ---------------------------------------------------------------------------

function extractTag(xml: string, tag: string): string {
  const re = new RegExp(`<${tag}[^>]*>([\\s\\S]*?)</${tag}>`);
  const m = xml.match(re);
  return m ? m[1]!.trim() : "";
}

function extractAllTags(xml: string, tag: string): string[] {
  const re = new RegExp(`<${tag}[^>]*>([\\s\\S]*?)</${tag}>`, "g");
  const results: string[] = [];
  let m: RegExpExecArray | null;
  while ((m = re.exec(xml)) !== null) {
    results.push(m[1]!.trim());
  }
  return results;
}

function extractAttr(xml: string, tag: string, attr: string): string[] {
  const re = new RegExp(`<${tag}[^>]*${attr}="([^"]*)"[^>]*/?>`, "g");
  const results: string[] = [];
  let m: RegExpExecArray | null;
  while ((m = re.exec(xml)) !== null) {
    results.push(m[1]!);
  }
  return results;
}

function extractLinkHref(xml: string, rel: string): string {
  const re = new RegExp(`<link[^>]*rel="${rel}"[^>]*href="([^"]*)"[^>]*/?>`, "g");
  const m = re.exec(xml);
  return m ? m[1]! : "";
}

// ---------------------------------------------------------------------------
// Parse
// ---------------------------------------------------------------------------

function parseEntry(entryXml: string): ArxivPaper | null {
  const id = extractTag(entryXml, "id");
  if (!id) return null;

  const title = extractTag(entryXml, "title").replace(/\s+/g, " ");
  const summary = extractTag(entryXml, "summary").replace(/\s+/g, " ");
  const authors = extractAllTags(entryXml, "name");
  const published = extractTag(entryXml, "published");
  const updated = extractTag(entryXml, "updated");
  const categories = extractAttr(entryXml, "category", "term");

  const url = id; // ArXiv id IS the URL (e.g. http://arxiv.org/abs/...)
  const pdfUrl = extractLinkHref(entryXml, "related") || id.replace("/abs/", "/pdf/");

  return { id, title, summary, authors, published, updated, categories, url, pdfUrl };
}

// ---------------------------------------------------------------------------
// Fetch
// ---------------------------------------------------------------------------

async function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export async function fetchArxivData(): Promise<ArxivData> {
  const seen = new Map<string, ArxivPaper>();

  for (let i = 0; i < SEARCH_QUERIES.length; i++) {
    const query = SEARCH_QUERIES[i]!;
    if (i > 0) await sleep(REQUEST_DELAY_MS);

    try {
      const params = new URLSearchParams({
        search_query: query,
        sortBy: "submittedDate",
        sortOrder: "descending",
        max_results: String(ARXIV_MAX_RESULTS),
      });

      const resp = await fetch(`${API_URL}?${params}`, {
        headers: { "User-Agent": "agents-radar/1.0" },
      });

      if (!resp.ok) {
        console.error(`  [arxiv] query-${i + 1}: HTTP ${resp.status}`);
        continue;
      }

      const xml = await resp.text();

      // Split into entries
      const entryBlocks = xml.split("<entry>").slice(1);
      for (const block of entryBlocks) {
        const paper = parseEntry("<entry>" + block);
        if (paper && !seen.has(paper.id)) {
          seen.set(paper.id, paper);
        }
      }

      console.log(`  [arxiv] query-${i + 1}: ${entryBlocks.length} papers`);
    } catch (err) {
      console.error(`  [arxiv] query-${i + 1}: ${err}`);
    }
  }

  // Filter to last 48h (ArXiv has a ~1-day publishing delay, so 24h would miss today's batch)
  const cutoff = Date.now() - 48 * 60 * 60 * 1000;
  const papers = [...seen.values()]
    .filter((p) => new Date(p.published).getTime() > cutoff)
    .sort((a, b) => new Date(b.published).getTime() - new Date(a.published).getTime())
    .slice(0, ARXIV_MAX_RESULTS);

  console.log(`  [arxiv] ${papers.length} papers (from ${seen.size} unique)`);
  return { papers, fetchSuccess: papers.length > 0 };
}
