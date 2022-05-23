from flask import Flask, redirect, request, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from datetime import datetime


# TODO---------- I DID THIS FIRST--------------
# App init.Giving the route of the diffrent sub pages
# In order for the render_template() to work all
# of the html files should be in the same folder named 'templates'
# In order for CSS to work The path should be corrected{IN HTML}
# The path of the pictures should be linked NOT with HTML or CSS{IN PYTHON}(see.code)
# The diffrent routes where conected + the quick links at the footer{IN HTML}(GITHUB,FACEBOOK,ETC)
def create_app():
    @app.route('/')
    @app.route('/')
    def index():
        posts = BlogPost.query.all()
        return render_template('index.html',posts=posts)

    @app.route('/about')
    def about(name=None):
        return render_template('about.html', name=name)

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    # configuring the post
    @app.route('/post/<int:post_id>')
    def post(post_id):
        post = BlogPost.query.filter_by(id=post_id).one()
        date_posted = post.date_posted.strftime('%d %B %Y')
        return render_template('post.html',post=post, date_posted = date_posted)



    # TODO--------------4- I DID THIS -----------,--
    # CONFIGURE ADD A BLOG COPY AND RECONFIGURE ID ,
    #  PLACEHOLDERS , TYPE, NAME IN THE HTML FILE
    @app.route('/add')
    def add():
        return render_template('add.html')

    # TODO------------5- I DID THIS -------------
    # CONFIGURE THE request and the comunication with the database.
    # The POST method is to read write and update information.
    @app.route('/addpost', methods=['POST'])
    def addpost():
        title = request.form['title']
        subtitle = request.form['subtitle']
        author = request.form['author']
        content = request.form['content']

        # Saving the way blog-post will be saved on  db
        # #datetime 'from datetime'
        post = BlogPost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())
        # test if the post a blog works
        # return f"<h1>Title: {title} Subtitle: {subtitle} Author: {author} Content: {content}</h1>"

        # Saving to the db
        db.session.add(post)
        db.session.commit()

        # check if its commited
        # redirecting the user to the home page
        return redirect(url_for('index'))

    return app


app = Flask(__name__)
'''------------2-I DID THIS SECOND-------------
There is a diffrence when giving the path of the database 
sqlite:///(absolute $PATH) or sqlite://(relative $PATH)
After the proper init follow the steps in order for the table to be created:
1.Navigate to the DIR
2.Open Python 
3.CMD from $NameOfTheFile import db
4.db.create_all()
After this the tables is created in the database'''

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///G:/Blog/website/blog.db'
db = SQLAlchemy(app)


# ------------3-- I DID THIS -------------
# CREATING A MODEL (FORM) FOR OUR DATABASE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(40))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8080)
