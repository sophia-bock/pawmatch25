from ._anvil_designer import BestMatchesTemplate
from anvil import *
import anvil.server
from ..PetCard import PetCard

class BestMatches(BestMatchesTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # Get current user
    user = anvil.server.call('get_logged_in_user')
    if not user:
      alert("Please log in first.")
      open_form("Login")
      return

    # Call server function to get best matching pets
    top_matches = anvil.server.call('get_top_pet_matches', user)

    for pet in top_matches:
      card = PetCard(pet)
      self.matches_panel.add_component(card)
