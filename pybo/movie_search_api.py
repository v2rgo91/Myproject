import os
import sys
import urllib.request
import json

def moviesearch(moviename):
    # moviename =  input("키워드를 입력하세요")
    client_id = "OKQPTGKiQf0V3yitzK6o"
    client_secret = "uIGSvzveCB"

    encText = urllib.parse.quote(moviename)
    url = "https://openapi.naver.com/v1/search/movie?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        jsontemp = json.loads(response_body.decode('utf-8'))

    else:
        print("Error Code:" + rescode)

    # print(jsontemp)



    return jsontemp




# print(moviesearch("스파이럴"))






