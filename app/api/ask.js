/**
 * Serverless function: POST with { topicTitle, topicContent, question }
 * Calls OpenAI with topic as context and returns the model's answer.
 * Set OPENAI_API_KEY in Vercel project settings.
 */
const MAX_CONTENT_LENGTH = 8000;

function cap(str, max) {
  if (typeof str !== 'string') return '';
  return str.length <= max ? str : str.slice(0, max) + '\n\n[... content truncated for context ...]';
}

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const apiKey = process.env.OPENAI_API_KEY;
  if (!apiKey) {
    return res.status(503).json({
      error: 'Q&A is not configured',
      detail: 'Set OPENAI_API_KEY in the project environment to enable Ask about this topic.',
    });
  }

  let body;
  try {
    body = typeof req.body === 'string' ? JSON.parse(req.body) : req.body || {};
  } catch {
    return res.status(400).json({ error: 'Invalid JSON body' });
  }

  const { topicTitle, topicContent, question } = body;
  if (!question || typeof question !== 'string' || !question.trim()) {
    return res.status(400).json({ error: 'Missing or empty question' });
  }

  const title = typeof topicTitle === 'string' ? topicTitle : 'This topic';
  const context = cap(typeof topicContent === 'string' ? topicContent : '', MAX_CONTENT_LENGTH);

  const systemContent =
    `You are a helpful assistant. Answer the user's question using only the following glossary topic content as context. If the answer is not in the context, say so and keep the answer brief. Do not make up details that are not in the context.\n\n## Topic: ${title}\n\n${context}`.trim();

  try {
    const response = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${apiKey}`,
      },
      body: JSON.stringify({
        model: 'gpt-4o-mini',
        messages: [
          { role: 'system', content: systemContent },
          { role: 'user', content: question.trim() },
        ],
        max_tokens: 1024,
      }),
    });

    if (!response.ok) {
      const err = await response.text();
      console.error('OpenAI API error', response.status, err);
      return res.status(502).json({
        error: 'LLM request failed',
        detail: response.status === 401 ? 'Invalid API key' : 'Try again later.',
      });
    }

    const data = await response.json();
    const answer = data.choices?.[0]?.message?.content?.trim() || 'No response generated.';
    return res.status(200).json({ answer });
  } catch (e) {
    console.error('Ask API error', e);
    return res.status(500).json({ error: 'Server error', detail: 'Try again later.' });
  }
}
