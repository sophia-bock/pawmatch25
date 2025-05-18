from ._anvil_designer import SignUp3Template
import anvil.server
from anvil import alert, open_form

class SignUp3(SignUp3Template):
  def __init__(self, email=None, raw_password=None, username=None,
               pet_location_preference=None, pet_breed_preference=None,
               pet_gender_preference=None, pet_size_preference=None,
               pet_age_preference=None):
    self.email = email
    self.raw_password = raw_password
    self.username = username
    self.pet_location_preference = pet_location_preference
    self.pet_breed_preference = pet_breed_preference
    self.pet_gender_preference = pet_gender_preference
    self.pet_size_preference = pet_size_preference
    self.pet_age_preference = pet_age_preference
    self.pet_ear_preference = pet_ear_preference

  def signup_button_click(self, **event_args):
    # Read rankings from radio buttons
    try:
      rank_size = int(self.size_rank_group.selected_value)
      rank_age = int(self.age_rank_group.selected_value)
      rank_type = int(self.type_rank_group.selected_value)
      rank_location = int(self.location_rank_group.selected_value)
      rank_gender = int(self.gender_rank_group.selected_value)
    except (TypeError, ValueError):
      alert("Please select a ranking for all categories before continuing.")
      return  # <-- This return must be indented to stay inside the function

    # Check for unique rankings
    rankings = [rank_size, rank_age, rank_type, rank_location, rank_gender]
    if len(set(rankings)) != len(rankings):
      alert("Each ranking must be unique. Please assign a different number (1-5) to each preference.")
      return

    # Proceed if all rankings are unique
    anvil.server.call(
      'create_user',
      self.email,
      self.raw_password,
      self.username,
      self.pet_location_preference,
      self.pet_breed_preference,
      self.pet_gender_preference,
      self.pet_size_preference,
      self.pet_age_preference,
      {
        'size': rank_size,
        'age': rank_age,
        'type': rank_type,
        'location': rank_location,
        'gender': rank_gender
      }
    )
    alert("Account created!")
    open_form("Home")