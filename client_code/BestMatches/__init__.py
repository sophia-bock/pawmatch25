from ._anvil_designer import BestMatchesTemplate
from anvil import *
import anvil.server
import time  # Needed for sleep delay

class BestMatches(BestMatchesTemplate):
  def __init__(self, matches=None, user_data=None, **properties):
    self.init_components(**properties)

    # ✅ No need to fetch user from session if we already passed preferences
    if matches is None or user_data is None:
      alert("Missing user or match data. Please sign in again.")
      open_form("Login")
      return

    # You can now use self.user_data['preferences']['type'], etc.
    self.user_data = user_data

    pets_with_scores = []
    for match in matches:
      pet = match['pet']
      score = match['score']

      pets_with_scores.append({
        'pet_name': pet['name'],
        'pet_age': f"{pet['age']} years old",
        'pet_location': pet['location'],
        'pet_size': pet['size'],
        'pet_type': pet['type'],
        'pet_gender': pet['gender'],
        'special_label': pet.get('feather_type(bird)_or_fur_type(dog)_or_temperament(cat)', 'No special attribute'),
        'pet_image': pet['image'],
        'match_label': f"Match: {score}%"
      })

    self.matches_repeating_panel.items = pets_with_scores

  def pet_list_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form()

