from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Login(LoginTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # Set password box to hide text by default
    self.password_box.hide_text = True

    # Set default icon to 'eye-slash' (🙈 hidden)
    self.toggle_visibility_button.icon = "fa:eye-slash"
  
  def toggle_visibility_button_click(self, **event_args):
    if self.password_box.hide_text:
      self.password_box.hide_text = False
      self.toggle_visibility_button.icon = "fa:eye"  # 👁 show eye icon
    else:
      self.password_box.hide_text = True
      self.toggle_visibility_button.icon = "fa:eye-slash"  # 🙈 crossed out

  def button_2_click(self, **event_args):
    # This is the "Register" button's action
    open_form('SignUp1')

  def button_login_click(self, **event_args):
    email = self.email_box.text
    password = self.password_box.text

    result = anvil.server.call('login_user', email, password)

    if result['success']:
      import time
    time.sleep(0.2)  # ✅ Allow session time to update before retrieving user

    # ✅ Safely retrieve the logged-in user
    user = anvil.server.call('get_logged_in_user')

    # ✅ ADD THIS CHECK: handle if user is still None
    if not user:
      alert("Login session failed. Please try again.")
      return

    # ✅ Continue only if user was successfully retrieved
    matches = anvil.server.call('get_top_pet_matches', user)
    open_form("BestMatches", user=user, matches=matches)

    else:
    # ✅ Existing handling if login fails
      alert("Invalid email or password.")




    
    
          
