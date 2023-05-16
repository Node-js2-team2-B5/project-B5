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


@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    all_comment = list(db.guestbook.find({},{'_id':False}))
    return jsonify({'result': all_comment})

@app.route("/members", methods=["GET"])
def members_get():
    all_members = list(db.member.find({},{'_id':False}))
    return jsonify({'result': all_members})

@app.route("/members/:id", methods=["GET"])
def members_get():
    all_membersid = list(db.memberid.find({},{'_id':request.args.get('id')[id:1]}))  #S.A에 request부분  id = request.args.get(’id’){id:1}
    return jsonify({'result': all_membersid})

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
    app.run()








