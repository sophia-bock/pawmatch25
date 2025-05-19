from ._anvil_designer import PetCardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class PetCard(PetCardTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # Ensure the item is set
    if self.item:
      self.pet_image.source = self.item['image']  # Must be a Media object or a valid URL
      self.pet_name.text = self.item['name']
      self.pet_age.text = f"{self.item['age']} years old"
      self.pet_size.text = self.item['size']
      self.pet_gender.text = self.item['gender']
      self.pet_location.text = self.item['location']

      # Set the special attribute
      self.special_label.text = self.item.get(
        'feather_type(bird)_or_fur_type(dog)_or_temperament(cat)', "No special attribute"
      )

      # Optional: Show match %, if available
      match = self.item.get('match_score')
      if match is not None:
        self.match_label.text = f"Match: {match}%"
      else:
        self.match_label.visible = False
    # Any code you write here will run before the form opens.
