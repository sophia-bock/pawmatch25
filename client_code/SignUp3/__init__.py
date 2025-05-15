from ._anvil_designer import SignUp3Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


def signup_button_click(self, **event_args):
  anvil.server.call('create_user', self.email, self.raw_password, self.username, pet_location_preference, pet_breed_preference, pet_gender_preference, pet_size_preference, pet_age_preference)
  alert("Account created!")
  open_form("Home")