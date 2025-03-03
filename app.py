from flask import Flask, render_template, request, redirect, Response
from movie import *

app = Flask(__name__)

data = {}

@app.route('/')
def home():
    return render_template('index.html', videos=[])

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    results = search_videos(query)["result"]
    for i in results:
        data[i["vid"]]=i
    return render_template('index.html', videos=results)

@app.route("/preview/", defaults={"vid": None}, methods=["GET"])
@app.route("/preview/<vid>", methods=["GET"])
def preview(vid):
    try:
        if not vid:
            return render_template('error.html')
        video = get_serverdownload(vid)
        if video["success"] == False:
            return render_template('notfound.html')
        servers = video["result"]
        json = data[vid]
        return render_template("preview.html", video=json, servers=servers)
    except:
        return render_template('error.html')

@app.route("/watch/", defaults={"vid": None,"server_id": None}, methods=["GET"])
@app.route("/watch/<vid>/", defaults={"server_id": None}, methods=["GET"])
@app.route("/watch/<vid>/<int:server_id>", methods=["GET"])
def watch_video(vid, server_id):
    try:
        if not vid or not server_id:
            return render_template('error.html')
        video = get_serverdownload(vid)
        if video["success"] == False:
            return render_template('notfound.html')
        servers = video["result"]
        if server_id > len(servers) or server_id < 1:
            return render_template('notfound.html')
        server_url = servers[server_id - 1]
        json = data[vid]
        return render_template('watch.html', video=json, server_url=server_url)
    except:
        return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
