from flask import Flask, render_template, make_response, redirect
import requests, json, urllib.request, datetime
import sys

app = Flask(__name__)
app.url_map.strict_slashes = False
 
API_KEY = sys.argv[2]

@app.route('/')
def home():
    """
    redirect to all comics collection endpoint
    """
    response = make_response(redirect('/collection'))
    return response


@app.route('/collection', methods=['GET'])
def collection():
    """
    method to get all the comics in an specific api endpoint
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
    queryString = "?api_key=" + API_KEY + "&offset=680000&format=json" 
    url = "https://comicvine.gamespot.com/api/issues/" + queryString
    try:
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        data = resp.read().decode()
        allComics = json.loads(data)
    except BaseException as e:
        print(e)
        pass
    comicInfo = []
    comics = []
    for comic in allComics['results']:
        if comic['name'] is not None:
            comicName = comic['volume']['name'] + ' #' + comic['issue_number'] + ' - ' + comic['name']
        else:
            comicName = comic['volume']['name'] + ' #' + comic['issue_number']
        dateTime = datetime.datetime.strptime(comic['date_added'], '%Y-%m-%d %H:%M:%S')
        comicInfo.append(comicName)
        comicInfo.append(dateTime.strftime('%B %d, %Y'))
        comicInfo.append(comic['image']['original_url'])
        comicId = comic['api_detail_url'].split("/")
        comicInfo.append(comicId[5] + "/" + queryString)
        comics.append(comicInfo)
        comicInfo = []
        sorted(comics, key = lambda x: x[1], reverse=True)
    return render_template("allComics.html", comics=comics)


@app.route('/comic/<string:issueNumber>', methods=['GET'])
def issue_detail(issueNumber):
    """
    method to get an specific comic information in the given api endpoint
    """
    queryString = "?api_key=" + API_KEY + "&format=json"
    url = "https://comicvine.gamespot.com/api/issue/" + issueNumber + '/' + queryString
    try:
        req = urllib.request.urlopen(url)
        data = req.read().decode()
        detailComic = json.loads(data)
    except:
        detailComic = {'results':[]}
    print("URL", url)
    imgList = []
    nameList = []
    creditsList = []
    issueList = ['character_credits', 'team_credits', 'location_credits', 'concept_credits', 'object_credits']
    credits = ['Characters', 'Teams', 'Locations', 'Concepts', 'Objects']
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
        issueDict = list(zip(nameList, imgList))
        creditsList.append(issueDict)
        nameList = []
        imgList = []
    print(creditsList)
    return render_template("issueDetail.html", 
                        img=detailComic['results']['image'], 
                        issue=creditsList, 
                        credits=credits)
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)