import requests
from bs4 import BeautifulSoup
from urllib import parse
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class example(Resource):
 def get(self):
    URL = "https://scrapethissite.com/pages/"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
  # If this line causes an error, run 'pip install html5lib' or install html5lib
    results = []
    for hel in soup.find_all('div', {'class': 'page'}):
        tii = hel.h3.text.strip()
        hello = hel.p.text.strip()
        results.append({
        'heading': tii,
        'des': hello
         })

    return results


api.add_resource(example, '/helsearch')

if __name__ == '__main__':
    app.run(debug=True)