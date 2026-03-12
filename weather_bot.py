import requests
import datetime
import random

# 烟雾弹城市
cities = ["Berlin", "Paris", "London", "Rome","Warsaw"]
random.shuffle(cities)

def get_weather(city):
    try:
        # 使用 wttr.in 获取天气，?format=3 是简洁模式
        res = requests.get(f"https://wttr.in/{city}?format=3")
        return res.text.strip()
    except:
        return "N/A"

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
content = f"# 🌍 Watchman Dashboard\n\n"
content += f"**Last Update:** `{now} (UTC)`\n\n"
content += "### Current Weather in Europe\n"

for city in cities:
    weather = get_weather(city)
    content += f"- {weather}\n"

content += "\n\n---\n*Updated by GitHub Actions & Python*"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
