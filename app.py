from flask import Flask, request, url_for, redirect, render_template
import urllib
import json
import soundcloud

app=Flask(__name__)

@app.route("/")
def index():
    #home page
    query = request.args.get("query")
    name = request.args.get("name")
    start = request.args.get("start")
    if(query != "" and start == "Let's do this!"):
        return redirect("/generate/" + query + "_" + name)
    return render_template("home.html")

@app.route("/about")
def about():
    #about page
    return render_template("about.html")
                
@app.route("/generate")
@app.route("/generate/<query>_<name>")
def generate(query, name):
    #IMAGE -----------------------------------------------------------------
    url = "http://api.tumblr.com/v2/tagged?tag=" + query + "&api_key=dw6tmMQNuJU1I9jM6NPCuyPMwgYWKVlJGXZpQm1fWgMjEa9zxh"
    request = urllib.urlopen(url)
    st = request.read()
    result = json.loads(st)
    retstring = ""
    def image():
        for s in result["response"]:
            try: 
                return "<img src=%s width=500 height=500 border=3>"%(s['photos'][0]['original_size']['url'])
            except:
                pass
    retstring = image()
    #AUDIO -----------------------------------------------------------------
    client = soundcloud.Client(client_id='5c46cd90fc27e327c5d396d4c2cd2acc')

    #pulls tracks depending on the tag
    tracks = client.get('/tracks', q=query)

    #renders result.html and passes first track passed on query
    return render_template('results.html', query = query, name = name, image = retstring, stuff = tracks[0])




if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0")
