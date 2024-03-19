from flask import  render_template , request , redirect , make_response , Response , session
from datetime import datetime , timedelta
import jwt
import humanize

from src.app import app
from src.db.models.code import CodeDTO , get_code 
from src.config import CODE_LIFE_TIME



@app.route('/' , methods = ['GET', 'POST'])
def login():

    if request.method == "GET":


        loginCode = request.args.get('code' , default = ""  , type=str)

        res = handel_telegram_code(loginCode , render_template("auth.html"))
        
        return res

    if request.method == "POST":

        loginCode = request.form.get("telegramCode")

        res = handel_telegram_code(loginCode , redirect("/"))

        return res


def handel_telegram_code(loginCode : str , defaultFallBack : Response) -> Response:

    now = datetime.now()
    lifeTime = timedelta(seconds=CODE_LIFE_TIME)

    code = get_code(loginCode)

    if code == None:
        return defaultFallBack
    
    print(code)
    
    codeTimeDelata = now - code.creationDate

    print(humanize.naturaldelta(codeTimeDelata))

    if codeTimeDelata > lifeTime:
        return defaultFallBack
    

    token = jwt.encode(
                    {"telegramId": code.userTelegramId},
                    app.config["SECRET_KEY"],
                    algorithm="HS256"
                )


    print(f"Set token {token}")

    res = make_response(redirect("/posts/all"))
    
    session["Authorization"] = token

    return res