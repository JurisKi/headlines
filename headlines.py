import feedparser
from flask import Flask
app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'iol': 'http://www.iol.co.za/cmlink/1.640'}
@app.route("/")
@app.route("/<publication>")
@app.route("/bbc")
def bbc():
    return get_news('bbc')

@app.route("/cnn")
def cnn():
    return get_news('cnn')

def get_news(publication="bbc"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    render_template("home.html", articles=feed['entries'])
        title=first_article.get("title"),
        published=first_article.get("published"),
        summary=first_article.get("summary"))
    return """
    <html>
<head>
<title>Headlines</title>
</head>
<body>
<h1>Headlines</h1>
<b>{{article.title}}</b><br />
<b><a href="{{article.link}}">{{article.title}}</a></b><br />
<p>{{article.summary}}</p>
</body>
</html>
    """.format(first_article.get("title"), first_article.
    get("published"), first_article.get("summary"))
if __name__ == "__main__":
    app.run(port=5000, debug=True)
