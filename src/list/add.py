from flask import  render_template , request , redirect

from src.app import app
from src.auth import auth_required

from src.db.models.post import add_new_post

@app.route("/posts/add" ,methods= ['GET' , 'POST'])
@auth_required
def add_post(telegrmaId):

    if request.method == "POST":
        handel_add_post(telegrmaId)
        return redirect("/posts/add")

    return render_template("add.html" , title="New post")

def handel_add_post(authorId):
    postTitle = request.form.get("postTitle")
    postText = request.form.get("postText")

    add_new_post(postTitle , postText , authorId)

    print("-" * 10)

    print("New post")
    print(f"\tPost title: {postTitle}")
    print(f"\tPost text: {postText}")

    print("-" * 10)