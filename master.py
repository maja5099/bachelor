import sqlite3
import pathlib
from dotenv import load_dotenv
from bottle import request, response
import os
import re

##############################
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}


##############################
def db():
  db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/uniduniverse.db") 
  db.row_factory = dict_factory
  return db

##############################
def user():
  try:
    load_dotenv(".env")
    user = request.get_cookie("user", secret=os.getenv('MY_SECRET'))
    print("user cookie", user)
    if user:
      return user
    else:
      return None
  except Exception as ex:
    print(ex)
    raise ex
  
##############################
#Email Validation

EMAIL_MIN = 6
EMAIL_MAX = 100
EMAIL_REGEX = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def validate_email():
  error = f"User email is not valid"
  email = request.forms.get("email", "")
  print(email)
  email = email.strip()
  if len(email) < EMAIL_MIN:
    response.status = 400 
    raise Exception(error)
  if len(email) > EMAIL_MAX: 
    response.status = 400
    raise Exception(400, error)
  if not re.match(EMAIL_REGEX, email): 
    response.status = 400
    raise Exception(error)
  return email

##############################
#Username Validation

USERNAME_MIN = 4
USERNAME_MAX = 15
USERNAME_REGEX = "^[a-zA-Z0-9_]{4,15}$"

def validate_username():
	error = f"Your username has to be at least {USERNAME_MIN} to {USERNAME_MAX} lowercased english letters"
	username = request.forms.get("username", "")
	username = username.strip()
	if not re.match(USERNAME_REGEX, username): raise Exception(400, error)
	return username

##############################
#Password Validation

PASSWORD_MIN = 10
PASSWORD_MAX = 128
PASSWORD_REGEX = "^[a-zA-Z0-9]{10,128}$"

def validate_password():
  error = f"Your password must be between {PASSWORD_MIN} to {PASSWORD_MAX} characters long"
  password = request.forms.get("password", "")
  password = password.strip()
  if len(password) < PASSWORD_MIN:
    response.status = 400
    raise Exception(error)
  if len(password) > PASSWORD_MAX: raise Exception(400, error)
  if not re.match(PASSWORD_REGEX, password): raise Exception(400, error)
  return password

##############################
# Phone Validation
PHONE_REGEX = "^\d{8}$" 

def validate_phone():
    error = "Phone number must be exactly 8 digits"
    phone = request.forms.get("phone", "")
    phone = phone.strip()
    if not re.match(PHONE_REGEX, phone):
        raise ValueError(error)
    return phone