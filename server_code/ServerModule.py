import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import hashlib

@anvil.server.callable
def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()

@anvil.server.callable
def create_user(email, password, pet_name, pet_breed, location):
  hashed = hash_password(password)
  app_tables.users.add_row(
    email=email,
    password=hashed,
    pet_name=pet_name,
    pet_breed=pet_breed,
    location=location
  )

@anvil.server.callable
def login_user(email, password):
  user = app_tables.users.get(email=email)
  if user and user['password'] == hash_password(password):
    return {'success': True}
  else:
    return {'success': False}

@anvil.server.callable
def check_email_exists(email):
  return app_tables.users.get(email=email) is not None

  