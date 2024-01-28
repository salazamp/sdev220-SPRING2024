small = True
green = False
  #statements to print which of these matches those choices: cherry, pea, watermelon, pumpkin.
print("enter the choices")
if small and green:
      print("pea")
elif small and not green:
      print("cherry")
elif not small and green:
      print("watermelon")
elif not small and not green:
      print("pumpkin")