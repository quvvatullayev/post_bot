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