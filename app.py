from flask import Flask, request, url_for, redirect, render_template
import urllib
import json

app=Flask(__name__)

@app.route("/")
def index():
    return "this is the index page"

@app.route("/tagged")
def tag(tag="apple"):
    url = "http://api.tumblr.com/v2/tagged?tag=%s&api_key=dw6tmMQNuJU1I9jM6NPCuyPMwgYWKVlJGXZpQm1fWgMjEa9zxh"
    url = url%(tag)
    request = urllib.urlopen(url)
    st = request.read()
    result = json.loads(st)
    retstring = ""
    retstring1 = ""
    retstring2 = ""
    for s in result["response"]:
        print(s)
        #images
        try: 
            retstring1 = retstring1 + "<img src=%s>"%(s['photos'][0]['original_size']['url'])
            ##print(retstring1)
        except:
            pass
        #text
        try:
            retstring2 = retstring2 + s['text'][0]
            print s['text'][0]
        except:
            pass
        retstring = retstring + retstring1 + retstring2
        return retstring2
                
    #return retstring2


if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0")
