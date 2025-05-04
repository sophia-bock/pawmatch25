from ._anvil_designer import SignUp2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class SignUp2(SignUp2Template):
  def __init__(self, email=None, raw_password=None, **properties):
    self.init_components(**properties)
    self.email = email
    self.raw_password = raw_password

  def button_1_click(self, **event_args):
    pet_name = self.pet_name_box.text
    pet_breed = self.pet_breed_box.text
    location = self.location_box.text

    # Call the server function to create the user
    anvil.server.call('create_user', self.email, self.raw_password, pet_name, pet_breed, location)
    alert("Account created!")
    open_form('Login')

  