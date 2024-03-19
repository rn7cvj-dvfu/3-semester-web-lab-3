
from functools import wraps
import jwt
from flask import request , redirect  , session
from flask import current_app


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        token = session.get('Authorization', None)


        if not token:
            return redirect("/")
        try:
            data=jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            
            userTelegramId = data["telegramId"]

            
        except Exception as e:
            return redirect("/")

        return f(str(userTelegramId), *args, **kwargs)

    return decorated