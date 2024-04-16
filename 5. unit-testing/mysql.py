
def findUser(email, hash):
  if (email == 'ivan.auda@hva.nl' and hash == '1a9a729d8ba48d8c08a03fbddec6a2b42473390907aa32514b91ce255ee95ebf'):
    return {
      'id': 1,
      'email': 'ivan.auda@hva.nl',
      'role': 'admin',
    }
  return None

def query(sqlString):
  """Runs a MySQL Query across the database."""
  # TODO: Define & Implement the query function
  raise UserWarning("Not Implemented Yet!")
