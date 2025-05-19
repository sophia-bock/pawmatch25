from ._anvil_designer import UploadPetsFormTemplate
from anvil import *
import anvil.server

class UploadPetsForm(UploadPetsFormTemplate):
  def file_loader_1_change(self, file, **event_args):
    if file is not None:
      anvil.server.call('upload_pet_data', file)
      alert("Pet data uploaded successfully!")