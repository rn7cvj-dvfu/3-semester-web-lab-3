from flask import  render_template , request

from src.app import app
from src.auth import auth_required

from src.db.models.post import get_my_posts
from src.config import POSTS_ON_PAGE

BASE_HREF = '/posts/my'

@app.route("/posts/my" ,methods= ['GET'])
@auth_required
def my_posts(telegramId):

    page = request.args.get('page' , default = 1 , type=int)

    page = max(page , 1)

    myPosts = get_my_posts(page  , telegramId)

    havePreviousPage = page > 1

    haveNextPage = myPosts.__len__() == POSTS_ON_PAGE

    return render_template("posts.html" ,  title="My posts" , posts = myPosts , page = page, baseHref = BASE_HREF, havePreviousPage = havePreviousPage , haveNextPage = haveNextPage)