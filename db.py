from tinydb import TinyDB, Query
from tinydb.table import Document

class DB:
    def __init__(self, path) -> None:
        self.db = TinyDB(path, indent=4, separators=(',', ': '))
        self.query = Query() 
        self.channels = self.db.table('channels')

    def add_channel(self, channel_id, channel_name):
        self.channels.insert(Document({'id': channel_id, 'name': channel_name}, doc_id=channel_id))
    
    def get_all_channels(self):
        return self.channels.all()
    
    def get_channel(self, channel_id):
        return self.channels.get(self.query.id == channel_id)
    
    def delete_channel(self, channel_id):
        self.channels.remove(self.query.id == channel_id)