import sqlite3
import pathlib


##############################
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}


##############################
def db():
  db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/uniduniverse.db") 
  db.row_factory = dict_factory
  return db