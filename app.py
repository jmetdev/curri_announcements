from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['HEAD'])
def head():
    return ('', 204)

@app.route('/<greetingName>', methods=['HEAD', 'POST', 'GET'])
def renderCURRI(greetingName):
    return render_template('announcement.xml', name=greetingName)


app.run()