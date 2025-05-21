from ._anvil_designer import FullPetListTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import time  # Needed for sleep delay

class FullPetList(FullPetListTemplate):
  def __init__(self, matches=None, user=None, **properties):
    self.init_components(**properties)

    # If user wasn't passed in, try to get it from session
    if user is None:
      user = anvil.server.call('get_logged_in_user')
      if not user:
        alert("Please log in first.")
        open_form("Login")
        return

    if matches is None:
      matches = anvil.server.call('get_top_pet_matches', user)

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

  def best_matches_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('BestMatches')
