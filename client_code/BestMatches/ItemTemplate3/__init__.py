from ._anvil_designer import ItemTemplate3Template
from anvil import *

class ItemTemplate3(ItemTemplate3Template):
  def __init__(self, **properties):
    self.init_components(**properties)

    # Ensure the item dictionary is provided
    if self.item:
      pet = self.item['pet']
      score = self.item['score']

      if pet:
        self.pet_name.text = pet['name']
        self.pet_age.text = f"{pet['age']} years old"
        self.pet_location.text = pet['location']
        self.pet_size.text = pet['size']
        self.pet_type.text = pet['type']
        self.pet_gender.text = pet['gender']
        self.special_label.text = pet['Special_Attribute']
        self.pet_image.source = pet['Image']

      if score is not None:
        self.match_label.text = f"Match: {score}%"
      else:
        self.match_label.visible = False
