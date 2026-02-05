# formatter.py

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
