import requests
from send_email import send_email

topic = "fitness"
api_key = "901c8d05a95b4d8aaeebb17e1a4cf62d"

# url got it from newsapi.org
# q, from, sortBy, apikey, language are parameters and & is the separator
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-04-08&" \
      "sortBy=publishedAt&" \
      "apiKey=901c8d05a95b4d8aaeebb17e1a4cf62d&" \
      "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description, using debugging option
body = ""
for article in content["articles"][:10]:
    if article["title"] is not None:
        body = "Subject: Today's news" \
               + "\n" + body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2*"\n"

# Covert to utf format
body = body.encode("utf-8")
send_email(message=body)
