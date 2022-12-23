import requests
from textblob import TextBlob

# News API key
api_key = "0868520dfa904823828c47672a2a34d6"

# requesting to the News API for a specific topic
topic = "technology"
url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"
response = requests.get(url)

# Converting the response to a JSON object
data = response.json()

# Loop through each article in the response
for article in data['articles']:
 
  content = article['content']
  print(article)

  polarity = TextBlob(content).sentiment.polarity
 
  print(f"Polarity: {polarity}")

  if polarity<0:
    print("negative")
  elif (polarity >= 0.1) or(polarity<=0.01):
    print("neutral")
  else:
    print("positive")
  
