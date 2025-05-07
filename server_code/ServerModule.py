import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import hashlib

@anvil.server.callable
def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()

@anvil.server.callable
def create_user(email, password, username, pet_location_preference, pet_breed_preference, pet_gender_preference, pet_size_preference, pet_age_preference):
  # Prevent duplicate email registration
  if app_tables.users.get(email=email):
    raise Exception("An account with this email already exists.")

  hashed = hash_password(password)
  app_tables.users.add_row(
    email=email,
    password=hashed,
    self.username, pet_location_preference, pet_breed_preference, pet_gender_preference, pet_size_preference, pet_age_preference
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


  