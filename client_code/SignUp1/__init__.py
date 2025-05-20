from ._anvil_designer import SignUp1Template
from anvil import *
import anvil.server

class SignUp1(SignUp1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

    # Set initial icons and password boxes to hide text
    self.password_box.hide_text = True
    self.confirm_password_box.hide_text = True
    self.toggle_visibility_button_1.icon = "fa:eye-slash"
    self.toggle_visibility_button_2.icon = "fa:eye-slash"

  def toggle_visibility_button_1_click(self, **event_args):
    if self.password_box.hide_text:
      self.password_box.hide_text = False
      self.toggle_visibility_button_1.icon = "fa:eye"
    else:
      self.password_box.hide_text = True
      self.toggle_visibility_button_1.icon = "fa:eye-slash"

  def toggle_visibility_button_2_click(self, **event_args):
    if self.confirm_password_box.hide_text:
      self.confirm_password_box.hide_text = False
      self.toggle_visibility_button_2.icon = "fa:eye"
    else:
      self.confirm_password_box.hide_text = True
      self.toggle_visibility_button_2.icon = "fa:eye-slash"

  def next_button_click(self, **event_args):
    email = self.email_box.text
    password = self.password_box.text
    username = self.username_box.text
    confirm_password = self.confirm_password_box.text

    # Check if passwords match
    if password != confirm_password:
      alert("Passwords do not match.")
      return

    # Check password length
    if len(password) < 8:
      alert("Password must be at least 8 characters.")
      return

    # Check if email already exists
    email_exists = anvil.server.call('check_email_exists', email)
    if email_exists:
      alert("An account with this email already exists.")
      return

    # Proceed to next step
    open_form('SignUp2', email=email, raw_password=password, username=username)
