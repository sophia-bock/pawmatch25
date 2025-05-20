class ItemTemplate3(ItemTemplate3Template):
  def __init__(self, **properties):
    self.init_components(**properties)

    # Ensure the item dictionary is provided
    if self.item:
      self.pet_name.text = self.item['pet_name']
      self.pet_age.text = self.item['pet_age']
      self.pet_location.text = self.item['pet_location']
      self.pet_size.text = self.item['pet_size']
      self.pet_type.text = self.item['pet_type']
      self.pet_gender.text = self.item['pet_gender']
      self.special_label.text = self.item['special_label']
      self.pet_image.source = self.item['pet_image']
      self.match_label.text = self.item['match_label']