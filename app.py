from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/<greetingName>', methods=['HEAD', 'POST', 'GET'])
def hello_world(greetingName):
    #return f'<p>Hello, {greetingName}! </p>'
    return render_template('announcement.xml', name=greetingName)


app.run()