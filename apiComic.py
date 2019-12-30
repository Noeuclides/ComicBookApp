from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import requests, json, urllib.request
 
app = Flask(__name__)
Bootstrap(app)
 
@app.route('/', methods=['GET'])
def home():
    queryString = "?api_key=17f5af21b9359b8cbbf8f5153c87c6feb0183aa9&format=json"
    url = "https://comicvine.gamespot.com/api/issues/" + queryString
    try:
        req = urllib.request.urlopen(url)
        data = req.read().decode()
        allComics = json.loads(data)
    except:
        allComics = {'results':[]}
    return render_template("allComics.html", comics=allComics['results'])

@app.route('/<string:issueNumber>', methods=['GET'])
def issue_detail(issueNumber):
    queryString = "?api_key=17f5af21b9359b8cbbf8f5153c87c6feb0183aa9&format=json"
    url = "https://comicvine.gamespot.com/api/issue/" + issueNumber + '/' + queryString
    try:
        req = urllib.request.urlopen(url)
        data = req.read().decode()
        detailComic = json.loads(data)
    except:
        detailComic = {'results':[]}
    print(url)
    imgList = []
    nameList = []
    creditsList = []
    issueList = ['character_credits', 'team_credits', 'location_credits', 'concept_credits', 'object_credits']
    for item in issueList:
        for char in detailComic['results'][item]:
            nameList.append(char['name'])
            urlChar = char['api_detail_url'] + queryString
            try:
                req = urllib.request.urlopen(urlChar)
                dataChar = req.read().decode()
                character = json.loads(dataChar)
                iconImg = character['results']['image']['icon_url']
            except:
                character = None
                iconImg = ""
            imgList.append(iconImg)
        issueDict = dict(zip(nameList, imgList))
        creditsList.append(issueDict)
        nameList = []
        imgList = []
    return render_template("issueDetail.html", img=detailComic['results']['image'], issue=creditsList)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)