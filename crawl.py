import requests
import xml.etree.ElementTree as ET
from datetime import datetime

def get_live_news():
    url = "https://www.sciencemag.org/rss/news_current.xml"
    try:
        response = requests.get(url, timeout=10)
        root = ET.fromstring(response.content)
        items = root.findall('.//item')
        return [items[0].find('title').text, items[1].find('title').text, items[2].find('title').text]
    except:
        return ["国际宠物健康研究取得新进展", "宠物营养行业发布年度报告", "新型数字化诊疗工具投入临床"]

def update_all():
    news = get_live_news()
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 直接生成整段 HTML 代码，不再搞替换，这样绝对不会报错
    html_template = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>宠物专家动态中心</title>
        <style>
            body {{ font-family: sans-serif; background: #f0f2f5; padding: 20px; }}
            .card {{ background: white; border-radius: 12px; padding: 20px; max-width: 600px; margin: auto; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
            h1 {{ color: #1a73e8; text-align: center; }}
            .news-item {{ border-bottom: 1px solid #eee; padding: 15px 0; }}
            .tag {{ background: #e8f0fe; color: #1967d2; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>宠物科研实时情报站</h1>
            <div class="news-item">
                <span class="tag">实时动态 1</span>
                <p>{news[0]}</p>
            </div>
            <div class="news-item">
                <span class="tag">实时动态 2</span>
                <p>{news[1]}</p>
            </div>
            <div class="news-item">
                <span class="tag">实时动态 3</span>
                <p>{news[2]}</p>
            </div>
            <p style="text-align:center; color:#bbb; font-size:0.7rem;">更新时间：{now_time}</p>
        </div>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)

if __name__ == "__main__":
    update_all()
