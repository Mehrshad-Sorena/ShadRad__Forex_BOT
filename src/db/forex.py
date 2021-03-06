#from src.config import mongoConfig
from pymongo import MongoClient
from datetime import datetime
# from src.utils import logs
from uuid import uuid4


class ForexMongo:
    # params = mongoConfig()
    # host = params.get('hostname')
    # port = int(params.get('port'))
    dbname = 'forex'
    collection_name = 'forex'
    # username = params.get('username')
    # password = params.get('password')
    host = '127.0.0.1'
    port = 27017
    username = 'root'
    password = 'rootpwd'

    def __init__(self):
        try:
            self.client = MongoClient(
                    host=self.host,
                    port=self.port,
                    username=self.username,
                    password=self.password)
            self.db = self.client[self.dbname]
            self.forex = self.db[self.collection_name]
        except Exception as ex:
            # logs('warning', ex)
            print(ex)

    def setData(self, simbol, data):
        created_time = datetime.now()
        values = {
                'simbol': simbol,
                'created_time': created_time,
                'data': data.to_json()
        }
        self.forex.insert_one(values)

    def getData(self, simbol):
        key = {'simbol': simbol}
        filters = {'_id': 0, 'data': 1}

        res = list(self.forex.find(key, filters))
        if res:
            return res
