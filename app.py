from flask import Flask, render_template, request, jsonify
application = app = Flask(__name__) 

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.jy74xj7.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guestbook')
def guestbook():
    return render_template('guestbook.html')

@app.route("/members", methods=["POST"])
def member_post():
    name_receive = request.form['name_give']
    mbti_receive = request.form['mbti_give']
    hobby_receive = request.form['hobby_give']
    comment_receive = request.form['comment_give']
    
    doc = {
        'name' : name_receive,
        'mbti' : mbti_receive,
        'hobby' : hobby_receive,
        'comment' : comment_receive
    }
    db.member.insert_one(doc)
    return jsonify({'msg':'등록 완료!'})

@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name' : name_receive,
        'comment' : comment_receive
    }
    db.guestbook.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)