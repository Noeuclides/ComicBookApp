from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import requests, json, urllib.request
 
app = Flask(__name__)
Bootstrap(app)
 
@app.route('/', methods=['GET'])
def home():
    url = "https://comicvine.gamespot.com/api/issues/?api_key=17f5af21b9359b8cbbf8f5153c87c6feb0183aa9&format=json"
    req = urllib.request.urlopen(url)
    data = req.read().decode()
    try:
        allComics = json.loads(data)
    except:
        allComics = None
    return render_template("allComics.html", comics=allComics['results'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)