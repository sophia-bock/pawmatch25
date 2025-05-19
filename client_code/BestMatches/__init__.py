from ._anvil_designer import BestMatchesTemplate
from anvil import *
import anvil.server
from ..PetCard import PetCard

class BestMatches(BestMatchesTemplate):
  def __init__(self, matches=None, **properties):
    self.init_components(**properties)

    # Use provided matches if available
    if matches is None:
      # Get current user
      user = anvil.server.call('get_logged_in_user')
      if not user:
        alert("Please log in first.")
        open_form("Login")
        return

      # Call server function to get best matching pets
      matches = anvil.server.call('get_top_pet_matches', user)
    alert(matches)
    
    # Display matches using PetCard
    for pet in matches:
      card = PetCard(pet)
      self.matches_panel.add_component(card)
