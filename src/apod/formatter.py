# formatter.py
from html import escape

import markdown


def apod_to_markdown(data: dict) -> str:
    return f"""# NASA Astronomy Picture of the Day
**Date:** {data.get('date', '')}

---

## Title
{data.get('title', '')}

---

## Explanation
{data.get('explanation', '')}

---

## Image
![APOD Image]({data.get('url', '')})

---

## Metadata
- **Media type:** {data.get('media_type', '')}
- **HD URL:** {data.get('hdurl', 'N/A')}
"""


def apod_to_html(data: dict) -> str:
    md = apod_to_markdown(data)
    body = markdown.markdown(md, extensions=["fenced_code", "tables"])

    title = data.get("title", "NASA APOD")
    date = data.get("date", "")
    media_type = data.get("media_type", "")
    hdurl = data.get("hdurl")
    url = data.get("url")

    hd_link = (
        f'<a class="btn" href="{escape(hdurl)}" target="_blank" rel="noopener">Open HD</a>'
        if hdurl else ""
    )
    src_link = (
        f'<a class="btn btn-ghost" href="{escape(url)}" target="_blank" rel="noopener">Open Source</a>'
        if url else ""
    )

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{escape(title)}</title>
  <style>
    :root {{
      --bg: #0b1020;
      --card: rgba(255,255,255,.06);
      --card2: rgba(255,255,255,.08);
      --text: rgba(255,255,255,.92);
      --muted: rgba(255,255,255,.68);
      --line: rgba(255,255,255,.12);
      --accent: #7aa2ff;
    }}

    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: var(--text);
      background:
        radial-gradient(1200px 800px at 10% 10%, rgba(122,162,255,.22), transparent 60%),
        radial-gradient(900px 700px at 80% 20%, rgba(255,170,120,.12), transparent 55%),
        linear-gradient(180deg, #060a16, var(--bg));
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
      line-height: 1.65;
    }}

    .wrap {{ max-width: 980px; margin: 0 auto; padding: 36px 18px 64px; }}

    header {{
      display: flex;
      gap: 16px;
      align-items: flex-end;
      justify-content: space-between;
      margin-bottom: 18px;
    }}

    .brand {{ display: grid; gap: 6px; }}

    .kicker {{
      color: var(--muted);
      font-size: 13px;
      letter-spacing: .08em;
      text-transform: uppercase;
    }}

    h1 {{ margin: 0; font-size: 28px; line-height: 1.25; }}

    .meta {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      justify-content: flex-end;
      color: var(--muted);
      font-size: 13px;
    }}

    .pill {{
      border: 1px solid var(--line);
      background: rgba(255,255,255,.04);
      padding: 6px 10px;
      border-radius: 999px;
    }}

    .card {{
      border: 1px solid var(--line);
      background: var(--card);
      border-radius: 18px;
      padding: 18px;
      backdrop-filter: blur(10px);
      box-shadow: 0 20px 60px rgba(0,0,0,.35);
    }}

    .actions {{ display: flex; gap: 10px; flex-wrap: wrap; margin: 14px 0 0; }}

    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 10px 14px;
      border-radius: 12px;
      border: 1px solid rgba(122,162,255,.35);
      background: rgba(122,162,255,.15);
      color: var(--text);
      text-decoration: none;
      font-size: 14px;
    }}

    .btn:hover {{ background: rgba(122,162,255,.22); }}

    .btn-ghost {{
      border-color: var(--line);
      background: rgba(255,255,255,.04);
    }}

    .content {{ margin-top: 18px; }}

    .content h1, .content h2, .content h3 {{ margin: 18px 0 10px; line-height: 1.25; }}

    .content h2 {{ font-size: 18px; }}

    .content p {{ margin: 10px 0; }}

    .content hr {{
      border: 0;
      border-top: 1px solid var(--line);
      margin: 18px 0;
    }}

    .content a {{ color: var(--accent); text-decoration: none; }}
    .content a:hover {{ text-decoration: underline; }}

    .content img {{
      max-width: 100%;
      height: auto;
      border-radius: 14px;
      border: 1px solid var(--line);
      background: var(--card2);
      display: block;
      margin: 14px 0;
    }}

    .content code, .content pre {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
      background: rgba(255,255,255,.06);
      border: 1px solid var(--line);
      border-radius: 12px;
    }}

    .content code {{ padding: 2px 6px; }}
    .content pre {{ padding: 12px; overflow-x: auto; }}

    footer {{ margin-top: 22px; color: var(--muted); font-size: 12px; text-align: center; }}
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="brand">
        <div class="kicker">NASA APOD • local landing</div>
        <h1>{escape(title)}</h1>
      </div>
      <div class="meta">
        {f'<span class="pill">Date: {escape(date)}</span>' if date else ''}
        {f'<span class="pill">Media: {escape(media_type)}</span>' if media_type else ''}
      </div>
    </header>

    <div class="card">
      <div class="actions">
        {hd_link}
        {src_link}
      </div>
      <div class="content">
        {body}
      </div>
    </div>

    <footer>
      Generated by your APOD CLI • Markdown → HTML
    </footer>
  </div>
</body>
</html>"""