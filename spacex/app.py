from flask import Flask, request
import urllib.request, json 

app = Flask(__name__)


@app.route("/")
def hello_world():
    with urllib.request.urlopen("https://api.spacexdata.com/v3/dragons/dragon1") as url:
        data = json.loads(url.read().decode())
    return data


if __name__ == "__main__":
    app.run()