
from src.db.models.post import Post

MOCK_POSTS = [    "Exploring the Future of Tech" , "Discover the latest trends in technology, from AI to quantum computing. #TechFuture"

    , "Healthy Living Tips" , "Stay fit and healthy with these simple daily habits. #HealthyLiving"

    , "Sustainable Fashion" , "Embrace eco-friendly fashion with these sustainable tips. #SustainableFashion"

    , "Eco-Friendly Products" , "Find the best eco-friendly products for your home. #EcoFriendly"

    , "Digital Marketing Trends" , "Keep up with the latest digital marketing strategies. #DigitalMarketing"

    , "Remote Work Tips" , "Master the art of remote work with these top tips. #RemoteWork"

    , "Innovative Startups" , "Discover the next big thing in startups. #Innovation"

    , "Mental Health Awareness" , "Support mental health with these practical tips. #MentalHealth"

    , "Sustainable Travel" , "Plan your next trip with a focus on sustainability. #SustainableTravel"

    , "DIY Home Projects" , "Save money and time with these DIY home projects. #DIY"

    , "Financial Literacy" , "Improve your financial health with these tips. #FinancialLiteracy"

    , "Tech Gadgets" , "Check out the latest tech gadgets. #TechGadgets"

    , "Healthy Recipes" , "Try these healthy recipes for a delicious meal. #HealthyRecipes"

    , "Eco-Friendly Living" , "Learn how to live more sustainably. #EcoLiving"

    , "Digital Wellness" , "Take care of your digital well-being. #DigitalWellness"

    , "Sustainable Living" , "Embrace a sustainable lifestyle with these tips. #SustainableLiving"

    , "Tech Innovations" , "Stay ahead with the latest tech innovations. #TechInnovations"

    , "Healthy Eating" , "Discover healthy eating habits. #HealthyEating"

    , "Eco-Friendly Home" , "Transform your home into an eco-friendly haven. #EcoHome"

    , "Digital Marketing Secrets" , "Unlock the secrets of digital marketing success. #DigitalSecrets"

    , "Remote Work Success" , "Tips for thriving in remote work. #RemoteSuccess"

    , "Innovative Ideas" , "Explore innovative ideas for your business. #InnovativeIdeas"

    , "Mental Health Resources" , "Find resources for mental health support. #MentalHealthResources"

    , "Sustainable Travel Tips" , "Plan your next sustainable travel adventure. #SustainableTravelTips"

    , "DIY Home Ideas" , "Get creative with these DIY home ideas. #DIYHome"

    , "Financial Goals" , "Set and achieve your financial goals. #FinancialGoals"

    , "Tech Gadget Reviews" , "Read the latest tech gadget reviews. #TechReviews"

    , "Healthy Snacks" , "Find healthy snack ideas for on-the-go. #HealthySnacks"

    , "Eco-Friendly Product Reviews" , "Check out eco-friendly product reviews. #EcoProductReviews"

    , "Digital Marketing Strategies" , "Learn effective digital marketing strategies. #DigitalStrategies"]

from src.app import app
from src.db.db import db

with app.app_context():
    for i in range(0  ,len(MOCK_POSTS) , 2):
        
        postTitle = MOCK_POSTS[i]
        postText = MOCK_POSTS[i + 1]

        newPost = Post(authorTelegramId = '1453255909' , postTitle = postTitle , postText = postText)

        db.session.add(newPost)

        db.session.commit()
