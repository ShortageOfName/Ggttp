from pymongo import MongoClient 
import dns.resolver,datetime ,time ,json
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']


MONGODB ="mongodb+srv://shortageofmind:shortageofmind@cluster.rz30rhc.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGODB) 
db = client.database
users_setting = db.users_setting 



def ret_setting(user_id):
    payload = {"user_id":user_id}
    setting = users_setting.find_one(payload)
    if setting != None :
        return True ,setting['approach'] , setting['language'] 
    else :
        return False , False 
    
def usr_set(usr_id , approach='Academic',language='English'):
    if ret_setting(usr_id)[0] ==  False :
        users_setting.insert_one({'user_id':usr_id , 'approach':approach, 'language':language})

def update_language(user_id , language):
    filter = {"user_id":user_id}
    update = {"$set" : {'language':language}}
    users_setting.update_one(filter , update)
        
def update_approach(user_id,approach):
    filter = {"user_id":user_id}
    update = {"$set" : {'approach':approach}}
    users_setting.update_one(filter , update)
    
