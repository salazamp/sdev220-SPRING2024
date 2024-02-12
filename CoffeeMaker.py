
def main():

  #Instance
  coffee_maker1= CoffeeMaker("Keurig","K-Elite", 12)
  coffee_maker2= CoffeeMaker("Ninja","Cofee Bar", 12)

  # cofee_maker1
  coffee_maker1.add_water(10)
  coffee_maker1.brew_coffee()

  #cofee_maker2
  coffee_maker2.brew_coffee()

  # printing the coffee makers
  print("Coffee Maker 1:", coffee_maker1 )
  print("Coffee Maker 2:", coffee_maker2 )

  # testing equality
  print( "Are Coffee Maker 1 and coffee_maker2 the same?",  coffee_maker1 ==  coffee_maker2 ) 





class CoffeeMaker:
  def __init__(self, brand, model, capacity):
      self.__brand = brand
      self.__model = model
      self.__capacity = capacity
      self.__water_level = 0

  def get_brand(self):
      return self.__brand

  def set_brand(self, brand):
      self.__brand = brand

  def get_model(self):
      return self.__model

  def set_model(self, model):
      self.__model = model

  def get_capacity(self):
      return self.__capacity

  def set_capacity(self, capacity):
      self.__capacity = capacity

  def get_water_level(self):
      return self.__water_level

  def set_water_level(self, water_level):
      self.__water_level = water_level

  def brew_coffee(self):
      if self.__water_level >= 1:
          self.__water_level -= 1
          print("Coffee brewing...")
      else:
          print("Cannot brew coffee. Add water to the coffee maker.")

  def add_water(self, amount):
      self.__water_level += amount
      print(f"Added {amount} units of water to the coffee maker.")

  def __str__(self):
      return f"{self.__brand} {self.__model} - Capacity: {self.__capacity} cups, Water Level: {self.__water_level} units"

  def __eq__(self, other):
      if isinstance(other, CoffeeMaker):
          return (self.__brand == other.__brand and
                  self.__model == other.__model and
                  self.__capacity == other.__capacity and
                  self.__water_level == other.__water_level)
      return False



if __name__ == "__main__":
  main()



