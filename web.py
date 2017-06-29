import os
import json
from flask import Flask
from flask import request
import passAPI
app = Flask(__name__)

searchForm = open('web_views/form.html')
searchForm = searchForm.read()

@app.route("/")
def main():
    return searchForm

@app.route("/secure", methods=['POST'])
def parse_request():
    key = request.form['pass']
    search = request.form['search']
    return searchForm + '<br />' + passAPI.search(key, search)

@app.route("/api/v1/retrieve", methods=['GET'])
def retrieve_pass():
    key = request.args.get('pass')
    search = request.args.get('search')
    return json.dumps({'success': True, 'data': passAPI.search(key, search)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port, debug=True)
