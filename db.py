from tinydb import TinyDB, Query
from tinydb.table import Document

class DB:
    def __init__(self, path) -> None:
        self.db = TinyDB(path, indent=4, separators=(',', ': '))
        self.query = Query() 
        self.channels = self.db.table('channels')
        self.channel_add = self.db.table('channel_add')

    def add_channel(self, channel_id, channel_name):
        self.channels.insert(Document({'id': channel_id, 'name': channel_name}, doc_id=channel_id))
    
    def get_all_channels(self):
        return self.channels.all()
    
    def get_channel(self, channel_id):
        return self.channels.get(self.query.id == channel_id)
    
    def delete_channel(self, channel_id):
        self.channels.remove(self.query.id == channel_id)

    def add_channel_add(self, chat_id, channel_name):
        self.channel_add.insert(Document({'id': chat_id, 'name': channel_name}, doc_id=chat_id))

    def get_add_channel(self, chat_id):
        return self.channel_add.get(self.query.id == chat_id)
    
    def delete_add_channel(self, chat_id):
        self.channel_add.remove(self.query.id == chat_id)

    def update_channel(self, channel_id, channel_name):
        self.channels.update({'name': channel_name}, self.query.id == channel_id)        