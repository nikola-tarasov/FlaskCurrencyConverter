from flask import Flask,render_template
import requests
from config import API_KEY




app = Flask(__name__)


@app.route("/")
def index():

    r = requests.get('https://api.currencylayer.com/live?access_key={API_KEY}')
    print(r.status_code)
  
    # r.headers['content-type']
    # 'application/json; charset=utf8'
    # r.encoding
    # 'utf-8'
    # r.text
    # '{"authenticated": true, ...'
    # r.json()
    # {'authenticated': True, ...}

#     {
#     "success": true,
#     "terms": "https://currencylayer.com/terms",
#     "privacy": "https://currencylayer.com/privacy",
#     "timestamp": 1430401802,
#     "source": "USD",
#     "quotes": {
#         "USDAED": 3.672982,
#         "USDAFN": 57.8936,
#         "USDALL": 126.1652,
#         "USDAMD": 475.306,
#         "USDANG": 1.78952,
#         "USDAOA": 109.216875,
#         "USDARS": 8.901966,
#         "USDAUD": 1.269072,
#         "USDAWG": 1.792375,
#         "USDAZN": 1.04945,
#         "USDBAM": 1.757305,
#     [...]
#     }
#  }


    return render_template('index.html', title = 'Главная')

if __name__ == '__main__':
    app.run(debug=True)