from flask import Flask, render_template, make_response, redirect
from comicInfo import request_data, comic_credits, date_format, user_offset
import sys

app = Flask(__name__)
app.url_map.strict_slashes = False
 
API_KEY = sys.argv[len(sys.argv) - 1]
CREDITS = ['Characters', 'Teams', 'Locations', 'Concepts', 'Objects']

@app.route('/')
def home():
    """
    redirect to all comics collection endpoint
    """
    response = make_response(redirect('/collection'))
    return response


@app.route('/collection', methods=['GET'])
@app.route('/collection/<index>', methods=['GET'])
def collection(index=0):
    """
    method to get all the comics in an specific api endpoint.
    """
    queryString = "?api_key=" + API_KEY + "&offset=" + str(index) + "&format=json" 
    url = "https://comicvine.gamespot.com/api/issues/" + queryString
    totalOffsets = user_offset(url)
    print("number_of_total_results: ", totalOffsets)
    allComics = request_data(url)
    comicInfo = []
    comics = []
    
    for comic in allComics:
        if comic['name']:
            comicName = comic['volume']['name'] + ' #' + comic['issue_number'] + ' - ' + comic['name']
        else:
            comicName = comic['volume']['name'] + ' #' + comic['issue_number']
        dateTime = date_format(comic['date_added'])
        comicInfo.append(comicName)
        comicInfo.append(dateTime)
        comicInfo.append(comic['image']['original_url'])
        comicId = comic['api_detail_url'].split("/")
        comicInfo.append(comicId[5] + "/" + queryString)
        comics.append(comicInfo)
        comicInfo = []
        sorted(comics, key = lambda x: x[1], reverse=True)
    return render_template("allComics.html", comics=comics)



@app.route('/comic/<issueNumber>', methods=['GET'])
def issue_detail(issueNumber):
    """
    method to get an specific comic information in the given api endpoint
    """
    queryString = "?api_key=" + API_KEY + "&format=json"
    url = "https://comicvine.gamespot.com/api/issue/" + issueNumber + '/' + queryString
    
    print("issue NUMBER: ", issueNumber)
    detailComic = request_data(url)
    if type(detailComic) is not dict:
        print(type(detailComic))
        print("detail comic: ", detailComic)
        print("URL problem", url)
    creditsList = comic_credits(detailComic, queryString)

    return render_template("issueDetail.html", 
                        img=detailComic['image'], 
                        issue=creditsList, 
                        credits=CREDITS)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)