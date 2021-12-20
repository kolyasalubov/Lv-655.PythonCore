class Humen:
  """Human class:
    Attribute: name. 
    3 metod hi_metod, clas_metod, tatic_method"""
    
  species = "Homosapiens"
  
  def __init__ (self,name):
    self.name = name
    
  def hi_metod (self):
    return f"Hello, {self.name}"
  
  @classmethod
  def clas_metod (cls):
    return cls.species

  @staticmethod
  def static_method():
    return "I am humen"
