def query_filter(query, n):
    q = ""
    query_parts = query.split("AND")
    
    for i in range(min(n, len(query_parts))):  # Ensure n does not exceed the number of parts
        q += query_parts[i].strip() + " OR " if i < n - 1 else query_parts[i].strip()
    
    return q.strip()  # Remove trailing spaces

from datetime import datetime, timedelta
# https://docs.python.org/3/library/json.html
# This library will be used to parse the JSON data returned by the API.
import json
# https://docs.python.org/3/library/urllib.request.html#module-urllib.request
# This library will be used to fetch the API.
import urllib.request
import urllib.parse
import os

def gnews_search(query):

    api_key = os.getenv("GNEWS_API_KEY")

    # Get yesterday's date at midnight
    yesterday_midnight = (datetime.now() - timedelta(days=5)).replace(hour=0, minute=0, second=0, microsecond=0)

    # Format the date into the desired string format
    yesterday_date = f"{yesterday_midnight.strftime('%Y-%m-%dT%H:%M:%SZ')}"

    encoded_query = urllib.parse.quote(query)

    url = f"https://gnews.io/api/v4/search?q={encoded_query}&lang=en&from={yesterday_date}&max=100&apikey={api_key}"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))
        articles = data["articles"]
        
    return articles
