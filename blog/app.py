from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Article(db.Model) :
    __tablename__ = "articles"
    article_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    created_at = db.Column(db.String, nullable=False)

db.create_all()

@app.route('/')
def index() :
    return redirect('/articles')

@app.route('/articles')
def articles() :
    data = Article.query.all()
    
    return render_template('articles.html', data=data)

@app.route('/articles/new')
def new() :
    
    return render_template('new.html')

@app.route('/articles/create', methods=['POST'])
def create() :
    title = request.form.get('title')
    content = request.form.get('content')
    author = request.form.get('author')
    nowDate = datetime.datetime.now()
    
    art = Article(title=title, content=content, author=author, created_at=nowDate)
    db.session.add(art)
    db.session.commit()
    
    idData = Article.query.all()

    idNum = idData[len(idData)-1].article_id
    
    return render_template("create.html", idNum=idNum)
    
@app.route('/articles/<int:num>')
def articleNum(num) :
    data = Article.query.get(num)
    
    return render_template("articleNum.html", data=data, num=num)
    
@app.route('/articles/<int:num>/edit', methods=['POST'])
def editArticle(num) :
    data = Article.query.get(num)
    
    return render_template("edit.html", data=data, num=num)

@app.route('/articles/<int:num>/update', methods=['POST'])
def update(num) :
    title = request.form.get('title')
    content = request.form.get('content')
    author = request.form.get('author')
    nowDate = datetime.datetime.now()
    
    data = Article.query.get(num)
    data.title = title
    data.content = content
    data.author = author
    data.created_at = nowDate
    db.session.commit()
    
    idData = Article.query.all()
    idNum = idData[len(idData)-1].article_id
    
    return render_template('update.html', idNum=idNum)

@app.route('/articles/<int:num>/delete', methods=['POST'])
def delete(num) :
    data = Article.query.get(num)
    db.session.delete(data)
    db.session.commit()
    
    return render_template("delete.html")

    
    


# def getArticles() :
#     c = sqlite3.connect('blog.db')
#     db = c.cursor()
    
#     sql = "SELECT title, id FROM articles"
#     db.execute(sql)
#     data = db.fetchall()
    
#     return data
    
# def getArticle(num) :
#     c = sqlite3.connect('blog.db')
#     db = c.cursor()
    
#     sql = "SELECT title, content, created_at, author FROM articles WHERE id = {}".format(num)
#     db.execute(sql)
#     data = db.fetchone()
    
#     return data
    
# def createArticle(title, content, author, nowDate) :
#     c = sqlite3.connect('blog.db')
#     db = c.cursor()
    
#     sql = "INSERT INTO articles(title, content, created_at, author) VALUES('{}', '{}', '{}', '{}')".format(title, content, nowDate, author)
#     db.execute(sql)
#     c.commit()
    
# def updateArticle(title, content, author, nowDate, num) :
#     c = sqlite3.connect('blog.db')
#     db = c.cursor()
    
#     sql = "UPDATE articles SET title='{}', content='{}', author='{}', created_at='{}' WHERE id={}".format(title, content, author, nowDate, num)
#     db.execute(sql)
#     c.commit()
    
# def deleteArticle(num) :
#     c = sqlite3.connect('blog.db')
#     db = c.cursor()
    
#     sql = "DELETE FROM articles WHERE id={}".format(num)
#     db.execute(sql)
#     c.commit()