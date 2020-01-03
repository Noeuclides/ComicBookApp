from urllib.error import HTTPError
import json, urllib.request, datetime


def request_data(url):
    """
    method to make the requests to the api. Return results list
    """
    try:
        with urllib.request.urlopen(url) as resp:
            resultsList = json.loads(resp.read().decode('utf-8'))
            return resultsList.get('results')
    except HTTPError as e:
        print(("{} at {}").format(e, url))
        return (str(e))

def user_offset(url):
    """
    method to get the total number of results by making a request too the api
    """
    try:
        with urllib.request.urlopen(url) as resp:
            resultsList = json.loads(resp.read().decode('utf-8'))
            totalOffset = resultsList.get('number_of_total_results')
            return(totalOffset)
    except HTTPError as e:
        print("Error: {}".format(e.code))


def comic_credits(detailComic, queryString):
    """
    method a list  with the tuple name-image in theirs respective credits
    """
    issueList = ['character_credits', 
            'team_credits', 
            'location_credits', 
            'concept_credits', 
            'object_credits']
    imgList = []
    nameList = []
    creditsList = []  

    for item in issueList:
        for char in detailComic[item]:
            nameList.append(char['name'])
            urlChar = char['api_detail_url'] + queryString
            character = request_data(urlChar)
            if type(character) == dict:
                iconImg = character['image']['icon_url']
            else:
                iconImg = character        
            imgList.append(iconImg)

        issueDict = list(zip(nameList, imgList))
        creditsList.append(issueDict)
        print(creditsList)
        nameList = []
        imgList = []
    return(creditsList)

def date_format(date):
    """
    method that return the date in the specified format (month day, year)
    """
    dateTime = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    return(dateTime.strftime('%B %d, %Y'))