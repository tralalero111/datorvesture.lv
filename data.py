
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Datoru vēsture</h1><p>Šī ir mājaslapa par datoru dziļo vēsturi.</p><p>Datori mūsdienās ir attīstījušies līdz mākslīgajam intelektam un kvantu skaitļošanai.</p>'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5500))  # Render prasa izmantot šādi
    app.run(host='0.0.0.0', port=port)        # Ļauj ārēji Render piekļūt
