from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import pandas as pd
from flask import Flask

load_dotenv()


class MongoDriver:
    def __init__(self):

        user = os.getenv('MONGO_USER')
        password = os.getenv('MONGO_PASSWORD')
        hostname = os.getenv('MONGO_HOSTNAME')

        uri = f"mongodb+srv://{user}:{password}@{hostname}/?retryWrites=true&w=majority"

        # Create a new client and connect to the server
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection

    def test_connection(self):
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

        return

    def import_db(self):
        try:
            mongo_uri = "mongodb+srv://BryanFariasG18:LPVA5dkzHZaaUp9y@cluster0.ksakwuj.mongodb.net/?retryWrites=true&w=majority"
            client = MongoClient(mongo_uri)
            db = client.get_database('prueba')
            collection = db.get_collection('Tp-Link_bestcell')
            # Get a df with full collection:
            df = pd.DataFrame(list(collection.find()))

            ## Exportar a Excel o CSV:
            df.to_csv('file.csv', index=False)
        except Exception as e:
            print(e)
        return


if __name__ == "__main__":
    mi_base_de_datos = MongoDriver()
    mi_base_de_datos.test_connection()
    mi_base_de_datos.import_db()


app = Flask(__name__)
@app.route('/')
def index():
    return(open('file.csv'))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3000, debug=True)

