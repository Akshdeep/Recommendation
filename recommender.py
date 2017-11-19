import requests
import json
from flask import Flask, render_template

url = "https://api.themoviedb.org//3/tv/1668/similar?page=1&language=en-US&api_key=50d758ab154c75008d9c80ca5c656f0e"

payload = "{}"
response = requests.request("GET", url, data=payload)

for result in json.loads(response.text)["results"]:
    print(result["name"])

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/', methods=['GET', 'POST'])
def index():
    return json.loads(response.text)["results"]


if __name__ == "__main__":
    app.run()