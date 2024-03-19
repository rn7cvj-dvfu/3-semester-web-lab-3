from flask import  render_template , request

from src.app import app
from src.auth import auth_required

from src.db.models.post import get_subscriptions_post

from src.config import POSTS_ON_PAGE

BASE_HREF = '/posts/subscriptions'

@app.route("/posts/subscriptions" ,methods= ['GET'])
@auth_required
def subscriptions_posts(telegramId):

    page = request.args.get('page' , default = 1 , type=int)

    page = max(page , 1)
    
    subscriptionsPosts = get_subscriptions_post(page  , telegramId)


    havePreviousPage = page > 1

    haveNextPage = subscriptionsPosts.__len__() == POSTS_ON_PAGE

    return render_template("posts.html" ,  title="Subscriptions posts" , posts = subscriptionsPosts , page = page, baseHref = BASE_HREF, havePreviousPage = havePreviousPage , haveNextPage = haveNextPage)