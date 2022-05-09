from flask import Flask
from flask import render_template
import urllib.request, json
import datetime
import jyserver.Flask as jsf

app = Flask(__name__)
app.config['TESTING'] = True

@jsf.use(app)
class App:
    def __init__(self):
        self.diff = self.get_time_till_launch()
        self.days = self.diff.day
        self.hours =self.diff.hour
        self.mins = self.diff.minute
        self.secs = self.diff.second


    def refresh(self):
        self.diff = self.get_time_till_launch()
        self.js.document.getElementById('days').innerHTML = self.diff.day
        self.js.document.getElementById('hours').innerHTML = self.diff.hour
        self.js.document.getElementById('mins').innerHTML = self.diff.minute
        self.js.document.getElementById('secs').innerHTML = self.diff.second


    def get_time_till_launch(self):
        with urllib.request.urlopen("https://api.spacexdata.com/v5/launches/next") as url:
            data = json.loads(url.read().decode())
            launch_date_unix = data["date_unix"]
            
            date_now = datetime.datetime.now()
            date_now_unix = datetime.datetime.timestamp(date_now)
            
            diff_unix = launch_date_unix - date_now_unix
            diff = datetime.datetime.fromtimestamp(diff_unix)

        return diff


@app.route("/", methods=["GET","POST"])
def home():
    return App.render(render_template('index.html'))


if __name__ == "__main__":
    app.run(debug=True)