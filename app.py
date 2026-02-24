import re

from flask import Flask, abort, render_template, Response

app = Flask(__name__)

# UCM greeting names: alphanumeric, underscore, hyphen only
GREETING_NAME_RE = re.compile(r"^[a-zA-Z0-9_-]+$")


@app.route("/", methods=["HEAD"])
def head():
    return ("", 204)


@app.route("/<greetingName>", methods=["HEAD", "POST", "GET"])
def renderCURRI(greetingName):
    if not GREETING_NAME_RE.match(greetingName):
        abort(400)
    body = render_template("announcement.xml", name=greetingName)
    return Response(body, mimetype="application/xml")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
