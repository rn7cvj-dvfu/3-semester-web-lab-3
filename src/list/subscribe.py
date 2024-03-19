from flask import request, redirect

from src.app import app
from src.auth import auth_required

from src.db.models.subscribsion import subcribe , unsubscribe

@app.route('/author/subscribe' , methods = ['POST'])
@auth_required
def author_subscribe(telegramId):

    authorId = request.args.get("authorId" , default=None)

    if (authorId == None):
        return redirect("/posts/all")
    
    subcribe(authorId , telegramId)

    return redirect("/posts/all")

@app.route('/author/unsubscribe' , methods = ['POST'])
@auth_required
def author_unsubscribe(telegramId):

    authorId = request.args.get("authorId" , default=None)

    if (authorId == None):
        return redirect("/posts/all")
    
    unsubscribe(authorId , telegramId)

    return redirect("/posts/all")



