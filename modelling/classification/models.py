class Message(object):
  """
  Class to return text message
  """
  def __init__(self, msg=""):
    self.msg = msg
  
  @classmethod
  async def get_result(cls, request):
    self = cls(**request.query)
    message = self.msg
    result = {'message': message}
    return result