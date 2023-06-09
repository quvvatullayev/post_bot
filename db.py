from tinydb import TinyDB, Query
from tinydb.database import Document

class DB:
    def __init__(self, path):
        self.db = TinyDB(path, indent=4, separators=(',', ': '))
        self.query = Query()
        self.groups = self.db.table('groups')
        self.summation_groups = self.db.table('summation_groups')

    def add_group(self, group_id):
        self.groups.insert(Document({'group_id':group_id}, doc_id=group_id))
        return True
    
    def get_all_groups(self):
        return self.groups.all()
    
    def get_group(self, group_id):
        return self.groups.get(doc_id=group_id)
    
    def delete_group(self, group_id):
        self.groups.remove(doc_ids=[group_id])
        return True
    
    def add_summation_group(self, chat_id ,group_id=None):
        self.summation_groups.insert(Document({'group_id':group_id}, doc_id=str(chat_id)))
        return True
    
    def updeate_summation_group(self, group_id, chat_id):
        self.summation_groups.update(Document({'group_id':group_id}, doc_id=chat_id))
        return True
    
    def get_summation_group(self, chat_id):
        return self.summation_groups.get(doc_id=chat_id)
    
    def delete_summation_group(self, chat_id):
        self.summation_groups.remove(doc_ids=[chat_id])
        return True
    
class Admin:
    def __init__(self, path):
        self.db = TinyDB(path, indent=4, separators=(',', ': '))
        self.query = Query()
        self.admins = self.db.table('admins')

    """
    admins schema:
        "username":{
            "id": 123456789,
            "username": "username",
            "first_name": "first_name",
        }
    """
    def add_admin(self, username='admin', id='1', first_name='admin'):
        self.admins.insert(Document({'chat_id':id, 'username':username, 'first_name':first_name}, doc_id=id))
        return True

    def updeate_admin(self, username, id, first_name):
        self.admins.update(Document({'chat_id':id, 'username':username, 'first_name':first_name}, doc_id=id))
        return True

    def get_admin(self, id):
        return self.admins.get(doc_id=id)
    
    def get_admin_by_username(self, username):
        admin  = self.admins.search(self.query.username == username)
        return admin
    
    def get_all_admins(self):
        return self.admins.all()
    
    def delete_admin(self):
        self.admins.remove(doc_ids=[1])
        return True
    
    def delete_admin_by_chat_id(self, chat_id):
        self.admins.remove(doc_ids=[chat_id])
        return True
    
class Users:
    def __init__(self, path):
        self.db = TinyDB(path, indent=4, separators=(',', ': '))
        self.query = Query()
        self.users = self.db.table('users')

    """
    users schema:
        "chat_id":{
            "id": 123456789,
            "username": "username",
            "first_name": "first_name",
        }
    """
    def add_user(self, username, id, first_name):
        self.users.insert(Document({'chat_id':id, 'username':username, 'first_name':first_name}, doc_id=id))

    def get_user(self, chat_id):
        return self.users.get(doc_id=chat_id)
    
    def get_user_by_username(self, username):
        user  = self.users.search(self.query.username == username)
        return user
    
    def get_all_users(self):
        return self.users.all()
    
    def delete_user(self, chat_id):
        self.users.remove(doc_ids=[chat_id])
        return True