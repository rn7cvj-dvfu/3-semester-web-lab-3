from src.db.db import db
from src.db.models.subscribsion import Subcribsion
from src.config import POSTS_ON_PAGE

class PostDTO():

    author : str
    title :str 
    text : str 
    isSubscribe : bool

    def __init__(self , author :str , title : str , text : str , isSubscribe : bool) -> None:
        self.author = author
        self.title = title
        self.text = text 
        self.isSubscribe = isSubscribe


class Post(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    authorTelegramId = db.Column(db.String, nullable=False)
    postTitle = db.Column(db.String , nullable=False)
    postText = db.Column(db.String , nullable=False)

    def convertToDTO(self , authorsId) -> PostDTO:
         return PostDTO(self.authorTelegramId , self.postTitle , self.postText , self.authorTelegramId in authorsId)

    def __repr__(self) -> str:
        strings = []

        strings.append(f"Post id {self.id} from {self.authorTelegramId}")
        strings.append(f"\tPost title: {self.postTitle}")
        strings.append(f"\tPost text: {self.postText}")

        return '\n'.join(strings)


def add_new_post(postTitle : str , postText : str):

    newPost = Post(authorTelegramId = '#' , postTitle = postTitle , postText = postText)

    db.session.add(newPost)

    db.session.commit()

def get_all_posts(page , telegramId) -> list[PostDTO]: 

    authorsId = list(map( lambda sub: sub.authorTelegramId,  Subcribsion.query.where(Subcribsion.subscriberTelegramId == telegramId)))

    allPosts = Post.query.paginate(page=page ,per_page=POSTS_ON_PAGE )

    allPosts = list(map( lambda post: post.convertToDTO(authorsId), allPosts))

    return allPosts

def get_my_posts(page , telegramId) -> list[PostDTO]:


    authorsId = list(map( lambda sub: sub.authorTelegramId,  Subcribsion.query.where(Subcribsion.subscriberTelegramId == telegramId)))

    myPosts = Post.query.where(Post.authorTelegramId == telegramId).paginate(page=page ,per_page=POSTS_ON_PAGE)

    myPosts = list(map(lambda post : post.convertToDTO(authorsId) , myPosts))

    return myPosts

def get_subscriptions_post(page , telegramId) -> list[PostDTO]:


    authorsId = list(map( lambda sub: sub.authorTelegramId,  Subcribsion.query.where(Subcribsion.subscriberTelegramId == telegramId)))

    subscriptionsPost = Post.query.where(Post.authorTelegramId.in_(authorsId)).paginate(page=page ,per_page=POSTS_ON_PAGE)


    subscriptionsPost = list(map(lambda post : post.convertToDTO(authorsId) , subscriptionsPost))


    return subscriptionsPost
