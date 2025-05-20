from ._anvil_designer import SignUp3Template
import anvil.server
from anvil import alert, open_form, RadioButton

# ✅ Recursive helper function
def get_group_value(component, group_name):
  if isinstance(component, RadioButton) and component.group_name == group_name and component.selected:
    return component.value
  elif hasattr(component, 'get_components'):
    for sub in component.get_components():
      result = get_group_value(sub, group_name)
      if result is not None:
        return result
  return None

class SignUp3(SignUp3Template):
  def __init__(self, email=None, raw_password=None, username=None,
               pet_location_preference=None, pet_type_preference=None,
               pet_gender_preference=None, pet_size_preference=None,
               pet_age_preference=None):
    self.email = email
    self.raw_password = raw_password
    self.username = username
    self.pet_location_preference = pet_location_preference
    self.pet_type_preference = pet_type_preference
    self.pet_gender_preference = pet_gender_preference
    self.pet_size_preference = pet_size_preference
    self.pet_age_preference = pet_age_preference

  def signup_button_click(self, **event_args):
    try:
      rank_size = int(get_group_value(self, "size_rank_group"))
      rank_age = int(get_group_value(self, "age_rank_group"))
      rank_type = int(get_group_value(self, "type_rank_group"))
      rank_location = int(get_group_value(self, "location_rank_group"))
      rank_gender = int(get_group_value(self, "gender_rank_group"))
    except (TypeError, ValueError):
      alert("Please select a ranking for all categories before continuing.")
      return

    rankings = [rank_size, rank_age, rank_type, rank_location, rank_gender]
    if len(set(rankings)) != len(rankings):
      alert("Each ranking must be unique. Please assign a different number (1–5) to each preference.")
      return

    # Call the create_user server function
    anvil.server.call(
      'create_user',
      self.email,
      self.raw_password,
      self.username,
      self.pet_location_preference,
      self.pet_type_preference,
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

    # ✅ Get user and their top matches
    #user = anvil.server.call("get_logged_in_user")
    #top_matches = anvil.server.call("get_top_pet_matches", user)

    # ✅ Open BestMatches form with matches passed in
    top_matches = anvil.server.call('get_top_pet_matches',{
      'pet_location_preference': self.pet_location_preference,
      'pet_type_preference': self.pet_type_preference,
      'pet_gender_preference': self.pet_gender_preference,
      'pet_size_preference': self.pet_size_preference,
      'pet_age_preference': self.pet_age_preference,
      'rank_size': rank_size,
      'rank_age': rank_age,
      'rank_type': rank_type,
      'rank_location': rank_location,
      'rank_gender': rank_gender
    })
    alert(top_matches)
    #top_matches = anvil.server.call('get_top_pet_matches', self.username)
    open_form("BestMatches", matches=top_matches)
  
  def button_1_click(self, **event_args):
    pass
