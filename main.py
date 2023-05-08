import requests
from send_email import send_email

api_key = "901c8d05a95b4d8aaeebb17e1a4cf62d"
url = "https://newsapi.org/v2/everything?q=tesla&from=" \
      "2023-04-08&sortBy=publishedAt&apiKey=" \
      "901c8d05a95b4d8aaeebb17e1a4cf62d"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description, using debugging option
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2 * "\n"

# Covert to utf format
body = body.encode("utf-8")
send_email(message=body)

