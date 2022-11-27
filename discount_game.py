
import random


def discount_dice(total):
  global price_discount
  dice = input("do yo wanna play game? for yes y and for no n  ")
  while dice == "y":
    first = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    second = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    team1 = random.choice(first)
    team2 = random.choice(second)
    kaful = team1 * team2
    print("the final game result is ", kaful, "%")
    price_discount = total * (1-(kaful/100))
    price_discount2 = round(price_discount,2)
    print("your price with out game is :", total, "$")
    print("this is the discount value", price_discount2, "$")
    break





