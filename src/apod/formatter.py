# formatter.py
import markdown


def apod_to_markdown(data: dict) -> str:
    return f"""# 🌌 NASA Astronomy Picture of the Day
**Date:** {data['date']}

---

## 🪐 Title
{data['title']}

---

## 📖 Explanation
{data['explanation']}

---

## 🖼 Image
![APOD Image]({data['url']})

---

## ℹ️ Metadata
- **Media type:** {data['media_type']}
- **HD URL:** {data.get('hdurl', 'N/A')}
"""


def apod_to_html(data: dict) -> str:
    md = apod_to_markdown(data)

    body = markdown.markdown(
        md,
        extensions=["fenced_code", "tables"]
    )

    title = data.get("title", "NASA APOD")

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Arial; margin: 40px; line-height: 1.6; max-width: 900px; }}
    img {{ max-width: 100%; height: auto; display: block; margin: 16px 0; }}
    code, pre {{ background: #f6f8fa; padding: 2px 4px; border-radius: 4px; }}
    pre {{ padding: 12px; overflow-x: auto; }}
    hr {{ margin: 24px 0; }}
  </style>
</head>
<body>
{body}
</body>
</html>"""