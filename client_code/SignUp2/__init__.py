from ._anvil_designer import SignUp2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class SignUp2(SignUp2Template):
  def __init__(self, email=None, raw_password=None, username=None):
    #self.init_components(**properties)
    self.email = email
    self.raw_password = raw_password
    self.username = username

  def button_1_click(self, **event_args):
    pet_breed_preference = self.pet_breed_box.selected_value
    pet_location_preference = self.location_box.selected_value
    pet_gender_preference = self.gender_box.selected_value
    pet_size_preference = self.size_box.selected_value
    pet_age_preference = self.age_box.selected_value
    
    

    # Call the server function to create the user
    anvil.server.call('create_user', self.email, self.raw_password, self.username, pet_location_preference, pet_breed_preference, pet_gender_preference, pet_size_preference, pet_age_preference)
    alert("Account created!")
    open_form('Home')



  