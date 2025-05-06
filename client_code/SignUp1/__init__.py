from ._anvil_designer import SignUp1Template
from anvil import *
import anvil.server

class SignUp1(SignUp1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

  def next_button_click(self, **event_args):
      email = self.email_box.text
      password = self.password_box.text
      confirm_password = self.confirm_password_box.text

      # Check if passwords match
      if password != confirm_password:
        alert("Passwords do not match.")
        return

        # Check password length
        if len(password) < 8:
          alert("Password must be at least 8 characters.")
          return

      # Check if email already exists using the server function
      email_exists = anvil.server.call('check_email_exists', email)
      if email_exists:
        alert("An account with this email already exists.")
        return 
      else:
        # If everything is valid, pass data to SignUp2
        open_form('SignUp2', email=email, raw_password=password)

        