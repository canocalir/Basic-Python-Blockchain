def lightning_hash(data):
  return data + '*'

class Block:
  def __init__(self, data, hash, last_hash):
      self.data = data
      self.hash = hash
      self.last_hash = last_hash

class Blockchain:
  def __init__(self):
    self.chain = []