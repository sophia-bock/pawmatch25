import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import secrets
import hashlib

@anvil.server.callable
def get_top_pet_matches(user, limit=6):
  pets = app_tables.pets.search()
  scores = []

  preferences = {
    "location": user['pet_location_preference'],
    "type": user['pet_type_preference'],
    "gender": user['pet_gender_preference'],
    "size": user['pet_size_preference'],
    "age": user['pet_age_preference']
  }

  weights = {
    "location": user['rank_location'],
    "type": user['rank_type'],
    "gender": user['rank_gender'],
    "size": user['rank_size'],
    "age": user['rank_age']
  }

  for pet in pets:
    score = 0
    if pet['location'] == preferences['location']:
      score += weights.get('location', 0)
    if pet['type'] == preferences['type']:
      score += weights.get('type', 0)
    if pet['gender'] == preferences['gender']:
      score += weights.get('gender', 0)
    if pet['size'] == preferences['size']:
      score += weights.get('size', 0)
    if pet['age'] == preferences['age']:
      score += weights.get('age', 0)

    scores.append({'pet': pet, 'score': score})  # ✅ include score

  # Sort and return top matches
  top = sorted(scores, reverse=True, key=lambda x: x['score'])[:limit]
  return top




@anvil.server.callable
def hash_password(password):
  # Generate a random salt
  salt = secrets.token_hex(16)  # 32 characters of hex = 16 bytes
  salted_password = salt + password
  hashed = hashlib.sha256(salted_password.encode()).hexdigest()
  return f"{salt}${hashed}"  # Store salt and hash together

@anvil.server.callable
def create_user(email, password, username,
                pet_location_preference, pet_type_preference,
                pet_gender_preference, pet_size_preference, pet_age_preference,
                rankings):

  if app_tables.users.get(email=email):
    raise Exception("An account with this email already exists.")

  hashed = hash_password(password)

  user = app_tables.users.add_row(  # ← save this to a variable
    email=email,
    password=hashed,
    username=username,
    pet_location_preference=pet_location_preference,
    pet_type_preference=pet_type_preference,
    pet_gender_preference=pet_gender_preference,
    pet_size_preference=pet_size_preference,
    pet_age_preference=pet_age_preference,
    rank_size=rankings['size'],
    rank_age=rankings['age'],
    rank_type=rankings['type'],
    rank_location=rankings['location'],
    rank_gender=rankings['gender']
  )

  anvil.server.session['user_id'] = user.get_id()  # Store user ID in session


@anvil.server.callable
def login_user(email, password):
  user = app_tables.users.get(email=email)
  if user:
    stored = user['password']
    salt, stored_hash = stored.split('$')
    check_hash = hashlib.sha256((salt + password).encode()).hexdigest()
    if stored_hash == check_hash:
      anvil.server.session['user_id'] = user.get_id()  # Store user ID
      return {'success': True}
  return {'success': False}


@anvil.server.callable
def check_email_exists(email):
  return app_tables.users.get(email=email) is not None

@anvil.server.callable
def get_logged_in_user():
  user_id = anvil.server.session.get('user_id')
  if user_id:
    return app_tables.users.get_by_id(user_id)
  return None
