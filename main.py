import feedparser, datetime, ssl

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context
blog_rss_uri = "https://coconutstd.github.io/feed.xml"
feed = feedparser.parse(blog_rss_uri)


markdown_text = """
### ✍ Recent blog posts 
"""

j = 0
for i in feed['entries']:
    j += 1
    if j > 5:
        break
    else:
        dt = i['published']
        markdown_text += f"[{i['title']}]({i['link']}) <br>\n"
        print(i['link'], i['title'])

f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()