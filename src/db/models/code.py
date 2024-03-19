from datetime import datetime
from src.db.db import db
from src.app import app

class CodeDTO: 

    userTelegramId : str
    code : str
    creationDate : datetime

    def __init__(self , userTelegramId: str , code : str , creationDate : datetime) -> None:
        self.userTelegramId = userTelegramId
        self.code = code
        self.creationDate = creationDate
    
    def __repr__(self) -> str:
        strings = []

        strings.append(f"Code for {self.userTelegramId} id")
        strings.append(f"\tCode:{self.code}")
        strings.append(f"\tCreated at: {self.creationDate}")

        return '\n'.join(strings)


class Code(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    userTelegramId = db.Column(db.String, nullable=False)
    code = db.Column(db.String , nullable=False)
    creationDate = db.Column(db.DateTime , nullable=False)
    
    def convertToDTO(self) -> CodeDTO:
        return CodeDTO(self.userTelegramId , self.code , self.creationDate)

    def __repr__(self) -> str:
        strings = []

        strings.append(f"Code id {self.id} for {self.userTelegramId} id")
        strings.append(f"\tCode:{self.code}")
        strings.append(f"\tCreated at: {self.creationDate}")

        return '\n'.join(strings)

def update_login_code(userTelegramId  : str , loginCode : str):
    
    with app.app_context():

        now = datetime.now()

        code =  Code.query.where(Code.userTelegramId == userTelegramId).first()


        if code == None:

            newCode = Code(userTelegramId = userTelegramId , code = loginCode , creationDate = now)
            
            db.session.add(newCode)
            db.session.commit()
            return
        
        code.creationDate = now
        code.code = loginCode

        db.session.commit()


def get_code(loginCode) -> CodeDTO | None:

    code = Code.query.where(Code.code == loginCode).first()

    if code == None:
        return None

    return code.convertToDTO()
