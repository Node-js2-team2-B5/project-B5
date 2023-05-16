from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient 
import certifi 

ca = certifi.where() 
client = MongoClient('mongodb+srv://sparta:test@cluster0.ytw3j7c.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca) 
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

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

if __name__ == '__main__':
   app.run()