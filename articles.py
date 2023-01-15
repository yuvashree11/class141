from flask import Flask,jsonify,request
import csv

all_articles = []

with open('articles.csv')as f:
    reader=csv.reader(f)
    data=list(reader)
    all_articles = data[1:]

liked_articles =[]
not_liked_articles=[]
did_not_watch = []

app=Flask(__name__)
@app.route("/get-article")
def get_articles():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    })

@app.route("/liked_article",methods = ["POST"])
def like_articles():
    article=all_articles[0]
    all_articles=all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status":"success"
    }),201


@app.route("/unliked_article",methods = ["POST"])
def unlike_articles():
    article=all_articles[0]
    all_articles=all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status":"success"
    }),201

@app.route("/did_not_watch_article",methods = ["POST"])
def didnotwatch_articles():
    article=all_articles[0]
    all_articles=all_articles[1:]
    did_not_watch.append(article)
    return jsonify({
        "status":"success"
    }),201

if __name__ =="__main__":
    app.run()