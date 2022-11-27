from discount_game import discount_dice
bill = 0
sumRotev = 0
total = 0
end = ""
quantity = 0
beer = 20
out = 60
extra = 2
price_discount = 0
dice = ""



def pizza_order():
  global bill
  global sumRotev
  global total
  global quantity
  global extra
  global price_discount
  age = int(input("to get permission for ordering insert your age:  "))
  while age < 18:
    print("you are under age")
    break

  else:
    while end != "yes":
      print("\n\n\twelcome to pizza shemesh")
      print("\n1 small(s)= 4 slice and price 40 $")
      print("2 medium(m)= 6 slice and price 50 $ ")
      print("3 large(l)= 8 slice and price 60 $")
      print("4 extra.l(xl)= 8 large slice and price 75 $")
      size = input("\n what size pizza would you like, S, M, L, xl:     ")
      quantity = int(input("how many you want?, 1-12:    "))
      if size == "s":
        bill += (40 * quantity)
        print(bill)
      elif size == "m":
        bill += (50 * quantity)
        print(bill)
      elif size == "l":
        bill += (60 * quantity)
        print(bill)
      elif size == "xl":
        bill += (75 * quantity)
        print(bill)
      rotev = input("\n would you like rotev, yes,no:    ")
      if rotev == 'yes':
        sumRotev = sumRotev + extra
      view = input("are you in beersheva, yes, no:     ")
      if view == "yes":
        total = bill + sumRotev + beer
        discount_dice(total)
        # total = bill + sumRotev + out
        total = bill + sumRotev
        print(total)
        choice = input("do you want to continue ?, yes,no: ")
      if choice == "no" or choice == "n":
          print("\nthank you for order!! ")
          break
      else:
          print("your price with out game is :", total, "$")


pizza_order()
