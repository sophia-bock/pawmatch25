from ._anvil_designer import BestMatchesTemplate
from anvil import *
import anvil.server
from ..PetCard import PetCard

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

    # ✅ Pass score to PetCard
    for match in matches:
      pet = match['pet']
      score = match['score']

      card = PetCard(pet, score=score)
      self.matches_panel.add_component(card)
