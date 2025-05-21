from ._anvil_designer import BestMatchesTemplate
from anvil import *
import anvil.server
import time  # Needed for sleep delay


class BestMatches(BestMatchesTemplate):
  def __init__(self, user=None, matches=None, **properties):
    self.init_components(**properties)

    alert("User received:", user)
    alert("Matches received:", matches)

    if not user or not matches:
      alert("Missing user or match data. Please sign in again.")
      open_form("Login")
      return

    # ✅ Continue if data is valid
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
        'special_label': pet.get('Special_Attribute', 'No special attribute'),
        'pet_image': pet['image'],
        'match_label': f"Match: {score}%"
      })

    self.matches_repeating_panel.items = pets_with_scores

  def pet_list_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form()

