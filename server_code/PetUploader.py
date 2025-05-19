import anvil.server
import anvil.media
import csv
from .. import app_tables

@anvil.server.callable
def import_pets_from_csv(file):
  # Convert uploaded media file to a temporary file
  f = anvil.media.TempFile(file)

  @anvil.server.callable
  def upload_pet_data(file):
    csv_content = file.get_bytes().decode()
  reader = csv.DictReader(StringIO(csv_content))

  for row in reader:
    app_tables.pets.add_row(
      name=row["name"],
      age=row["age"],
      type=row["type"],
      location=row["location"],
      gender=row["gender"],
      size=row["size"],
      image=None,  # you can set this later
      trait=row["feather_type(bird)_or_fur_type(dog)_or_temperament(cat)"]
    )