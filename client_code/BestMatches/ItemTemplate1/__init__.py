from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

  if self.item:
    self.pet_name.text = self.item['pet_name']
    self.pet_age.text = self.item['pet_age']
    self.pet_location.text = self.item['pet_location']
    self.pet_size.text = self.item['pet_size']
    self.pet_type.text = self.item['pet_type']
    self.pet_gender.text = self.item['pet_gender']
    self.special_label.text = self.item['special_label']
    self.match_label.text = self.item['match_label']
    self.pet_image.source = self.item['pet_image']