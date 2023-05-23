import json

class Database:
    def create_data(self,username,email,password):

        with open('db.json','r') as rf:
            database = json.load(rf)

        if email in database :
            return 0

        else:
            database[email] = [username, password]

            with open('db.json','w') as wf:
                database[email] = [username,password]
                json.dump(database,wf, indent=4)
            return 1

    def search_data(self,email,password):

        with open('db.json',"r") as rf:
            database = json.load(rf)

        if email in database and password == database[email][1]:
            return 1
        else:
            return 0

    def get_user_name(self,email,password):

        with open('db.json','r') as rf:
            database = json.load(rf)


        user = database[email][0]
        return user
#
# dbo=Database()
#
# print(dbo.get_user_name("we@lkj.com",""))