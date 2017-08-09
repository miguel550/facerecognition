from flask import Flask, request, jsonify, render_template
from kairosapi import KairosApi


app = Flask(__name__)
api = KairosApi()


@app.route('/')
def home():
    context = {"hi": "hoi"}
    return render_template('index.html', **context)


@app.route('/enroll', methods=["POST"])
def enroll():
    if request.method == "POST":
        print(request.get_json(force=True))
        image = request.json["image"].split(",")[1]
        subject_id = request.json["subject_id"]
        return jsonify(api.enroll(subject_id, image))


@app.route('/recognize', methods=["POST"])
def recognize():
    if request.method == "POST":
        print(request.get_json(force=True))
        image = request.json["image"].split(",")[1]
        return jsonify(api.recognize(image=image))

if __name__ == '__main__':
    app.run()
