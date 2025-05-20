from ._anvil_designer import BestMatchesTemplate
from anvil import *
import anvil.server

class BestMatches(BestMatchesTemplate):
  def __init__(self, matches=None, **properties):
    self.init_components(**properties)

    if matches is None:
      user = anvil.server.call('get_logged_in_user')
      if not user:
        alert("Please log in first.")
        open_form("Login")
        return
      matches = anvil.server.call('get_top_pet_matches', user)

    # ✅ Prepare cleaned data for the RepeatingPanel
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
        'match_label': f"Match: {score}%",
        'pet_image': pet['image']
      })

    # ✅ Set items ONCE, after preparing them
    self.matches_repeating_panel.items = pets_with_scores
