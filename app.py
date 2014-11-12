from flask import Flask, request, url_for, redirect, render_template
import urllib
import json
import soundcloud

app=Flask(__name__)

@app.route("/")
def index():
    return "this is the index page"

@app.route("/tagged")
def tag(tag="apple"):
    url = "http://api.tumblr.com/v2/tagged?tag=" + tag + "&api_key=dw6tmMQNuJU1I9jM6NPCuyPMwgYWKVlJGXZpQm1fWgMjEa9zxh"
    request = urllib.urlopen(url)
    st = request.read()
    result = json.loads(st)
    retstring = ""
    for s in result["response"]:
        print(s)
        #images
        try: 
            retstring = retstring + "<img src=%s>"%(s['photos'][0]['original_size']['url'])
            ##print(retstring1)
        except:
            pass
    return retstring
                
    #return retstring2
#@app.route("/play")
#def play(tag="apple"):
    #tracklist = ""

    # create a client object with your app credentials
    #client = soundcloud.Client(client_id='5c46cd90fc27e327c5d396d4c2cd2acc')

    #pull tracks using query apple
    #tracks = client.get('/tracks', q=tag)

    # get a tracks oembed data
    #for track in tracks:
        #print track
        #tracklist = tracklist + (client.get('/oembed', url=track))['html']

    #return tracklist

@app.route("/test")
def o(tag="hello"):

    # create a client object with your app credentials
    client = soundcloud.Client(client_id='5c46cd90fc27e327c5d396d4c2cd2acc')

    # get a tracks oembed data
    track_url = 'https://soundcloud.com/odesza/sun-models-feat-madelyn-grant'
    embed_info = client.get('/oembed', url=track_url)
    print embed_info
    # print the html for the player widget
    return render_template('results.html', stuff = embed_info)




if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0")
