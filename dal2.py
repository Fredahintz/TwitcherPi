import os

from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()

# Database connection
#yikes - postgres uses a lot of memory on the pi. I'm going to use sqlite or Tinydb instead for now
postgres_password = os.getenv('POSTGRES_PASSWORD')

DATABASE_URL = f'postgresql://postgres:{postgres_password}@192.168.0.171/birdwatcherdb'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Image(Base):
    __tablename__ = 'images'
    __table_args__ = {'schema': 'postgres'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    date_created = Column(TIMESTAMP, nullable=False)
    image = Column(LargeBinary, nullable=False)
    label = Column(String(250), nullable=False)

# Create the table
Base.metadata.create_all(engine)

# from pymongo import MongoClient
# from io import BytesIO
# from datetime import datetime

# client = MongoClient('mongodb://192.168.1.226')
# db = client.twicherpi

# class ImageDocument():
#     __image = BytesIO
#     __captured_date = ""
#     __author = ""

#     def __init__(self):
#         now = datetime.now()
#         self.__captured_date = now

#     def seed_database(self):
#         labels = ['sparrow', 'blackbird','robin']

#         for label in labels:
#             db.labels2.insert_one({'label':label})

#     def get_labels(self):
#         """ Returns a list of labels """
#         data = list(db.labels2.find({},{"_id":False}))
#         print(data)
#         return data

#     def get_ids(self):
#         id_list = [str(id) for id in db.labels2.find().distinct('_id')]
#         return id_list

#     def save_image(self, image:BytesIO):
#         self.__image = image.getvalue
#         myimage = image.getvalue()
#         image_id = db.images2.insert_one({"date":self.__captured_date, "image":myimage, "author":self.__author})

# # temporary routine
# im = ImageDocument()
# im.get_labels()