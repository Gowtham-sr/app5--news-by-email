import requests

api_key = "901c8d05a95b4d8aaeebb17e1a4cf62d"
url = "https://newsapi.org/v2/everything?q=tesla&from=" \
      "2023-04-08&sortBy=publishedAt&apiKey=" \
      "901c8d05a95b4d8aaeebb17e1a4cf62d"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description, using debugging option
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
