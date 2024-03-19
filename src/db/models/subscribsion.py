from src.db.db import db


class Subcribsion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    authorTelegramId = db.Column(db.String, nullable=False)
    subscriberTelegramId = db.Column(db.String, nullable=False)


def subcribe(authorId , telegramId):

    subcribsion = Subcribsion.query.where(Subcribsion.authorTelegramId == authorId and Subcribsion.subscriberTelegramId == telegramId).first()

    if subcribsion != None:
        return

    newSubscribsion = Subcribsion(authorTelegramId = authorId ,subscriberTelegramId = telegramId )

    db.session.add(newSubscribsion)

    db.session.commit()

def unsubscribe(authorId , telegramId):

    subcribsion = Subcribsion.query.where(Subcribsion.authorTelegramId == authorId and Subcribsion.subscriberTelegramId == telegramId).first()

    if subcribsion == None:
        return
    
    db.session.delete(subcribsion)
    db.session.commit()
