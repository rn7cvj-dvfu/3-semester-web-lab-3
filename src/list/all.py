from flask import  render_template , redirect , request

from src.app import app
from src.auth import auth_required

from src.db.models.post import get_all_posts

from src.config import POSTS_ON_PAGE

BASE_HREF = '/posts/all'


@app.route('/posts')
@auth_required
def posts(telegramId : str):
    return redirect("/posts/all")


@app.route("/posts/all" ,methods= ['GET'])
@auth_required
def all_posts(telegramId : str):


    page = request.args.get('page' , default = 1  , type=int)

    page = max(page , 1)

    posts = get_all_posts(page , telegramId)

    havePreviousPage = page > 1

    haveNextPage = posts.__len__() == POSTS_ON_PAGE

    return render_template("posts.html" , title="All posts", posts = posts , page = page, baseHref = BASE_HREF, havePreviousPage = havePreviousPage , haveNextPage = haveNextPage )