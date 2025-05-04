from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Login(LoginTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def button_2_click(self, **event_args):
    # This is the "Register" button's action
    open_form('SignUp1')

  def button_login_click(self, **event_args):
    email = self.email_box.text
    password = self.password_box.text

    result = anvil.server.call('login_user', email, password)

    if result['success']:
      alert("Login successful!")
      open_form('Home')
    else:
      alert("Invalid email or password.")



    
    
