from flask import Flask, redirect, url_for, session, request
from flask_oauth import OAuth
from pprint import pprint

import requests
import json
from flask import Flask, render_template

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/recommend', methods=['GET', 'POST'])
def index():
    url = "https://api.themoviedb.org//3/tv/1668/similar?page=1&language=en-US&api_key=50d758ab154c75008d9c80ca5c656f0e"

    payload = "{}"
    response = requests.request("GET", url, data=payload)

    for result in json.loads(response.text)["results"]:
        print(result["name"])
    return render_template("index.html", data=json.dumps(json.loads(response.text)["results"]))


@app.route('/getdata', methods=['GET', 'POST'])
def data():
    url = "https://api.themoviedb.org//3/tv/1668/similar?page=1&language=en-US&api_key=50d758ab154c75008d9c80ca5c656f0e"

    payload = "{}"
    response = requests.request("GET", url, data=payload)

    for result in json.loads(response.text)["results"]:
        print(result["name"])

    return json.dumps(json.loads(response.text)["results"])

if __name__ == "__main__":
    app.run(debug=True)

import recommender

SECRET_KEY = 'development key'
DEBUG = True
FACEBOOK_APP_ID = '296763407509160'
FACEBOOK_APP_SECRET = '6799f7f9623bab0918ce7531bc774506'

app = Flask(__name__)

app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'user_likes',  'auth_type': 'rerequest'},

)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True ))


@app.route('/login/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['oauth_token'] = (resp['access_token'], '')
    me = facebook.get('/me/television')
    # Flask.jsonify(me.data)
    #pprint(me.data['data'], depth=100)
    #pprint(me.data, depth=100)

    result =[]
    for strx in me.data['data']:
        result.append(str(strx['name']))

    pprint(result, depth= 100)
    recommender.main()
    #return redirect(recommender.(url_for('recommend')))

    #return 'Logged in as id=%s television=%s redirect=%s' % \
         #(str1, str1, request.args.get('next'))


@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')


if __name__ == '__main__':
    app.run(debug=True)
