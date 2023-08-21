import numpy as np
from numpy import random

class Player:
    def __init__(self,pseudo,answer):
        self.pseudo = pseudo
        self.answer = answer
    def get_pseudo(self):
        return self.pseudo
    def get_answer(self):
        return self.answer
    
print("Bienvenue dans le Mystery Number")
print("Les régles du jeu sont simples:")
print("=============================================================")
print("Le nombre mystere est compris entre 1 et 100\nPour commencer,tu dois choisir un nombre,si celui-ci est le nombre mystére alors tu as gagné la partie du premier coup")
print("Sinon,l'indication 'est plus petit'ou'est plus grand's'affiche\nDans ce cas,choisis un autre nombre plus petit ou plus grand jusqu'à trouver le nombre mystere")
print("=============================================================")
print("Veuillez choisir un mode ,Solo(tapez 1) ou 2players(tapez 2)")
answer_mode = int(input())

if answer_mode == 1:
    print("Veuillez choisir le mode de difficultée\nEasy(tapez 1) ou Normal(2) ou Hard(3)")
    answer_diff = int(input())
    if answer_diff == 1:
      print("Veuillez choisir votre pseudo")
      pseudo1 = input()
      answer1 = 0
      player1 = Player(pseudo1,answer1)
    
      x = random.randint(1, 51)
      print(player1.get_pseudo(),",veuillez bien choisir un nombre")
      answer1 = int(input())
    
      fausser = True
      while fausser == True:
        if answer1 < x:
            print("Le nombre mystére est plus grand ;)")
            print(player1.get_pseudo(),"veuillez choisir un autre nombre")
            answer1 = int(input())
        elif answer1 > x:
            print("Le nombre mystére est plus petit ;)")
            print(player1.get_pseudo(),"veuillez choisir un autre nombre")
            answer1 = int(input())
        else:
            fausser = False
            print("Bravo",player1.get_pseudo(),"vous avez trouvé le nombre mystere qui est",x)
          
    if answer_diff == 2:
      print("Veuillez choisir votre pseudo")
      pseudo1 = input()
      answer1 = 0
      player1 = Player(pseudo1,answer1)
    
      x = random.randint(1, 101)
      print(player1.get_pseudo(),",veuillez bien choisir un nombre")
      answer1 = int(input())
    
      fausser = True
      while fausser == True:
        if answer1 < x:
            print("Le nombre mystére est plus grand ;)")
            print(player1.get_pseudo(),"veuillez choisir un autre nombre")
            answer1 = int(input())
        elif answer1 > x:
            print("Le nombre mystére est plus petit ;)")
            print(player1.get_pseudo(),"veuillez choisir un autre nombre")
            answer1 = int(input())
        else:
            fausser = False
            print("Bravo",player1.get_pseudo(),"vous avez trouvé le nombre mystere qui est",x)
    if answer_diff == 3:
      print("Veuillez choisir votre pseudo")
      pseudo1 = input()
      answer1 = 0
      player1 = Player(pseudo1,answer1)
    
      x = random.randint(1, 201)
      print(player1.get_pseudo(),",veuillez bien choisir un nombre")
      answer1 = int(input())
    
      fausser = True
      while fausser == True:
        if answer1 < x:
            print("Le nombre mystére est plus grand ;)")
            print(player1.get_pseudo(),"veuillez choisir un autre nombre")
            answer1 = int(input())
        elif answer1 > x:
            print("Le nombre mystére est plus petit ;)")
            print(player1.get_pseudo(),"veuillez choisir un autre nombre")
            answer1 = int(input())
        else:
            fausser = False
            print("Bravo",player1.get_pseudo(),"vous avez trouvé le nombre mystere qui est",x)      
if answer_mode == 2:
  print("Veuillez choisir le mode de difficultée\nEasy(tapez 1) ou Normal(2) ou Hard(3)")
  answer_diff = int(input())
  if answer_diff == 1:
    print("Joueur 1 ,veuillez choisir votre pseudo")
    pseudo1 = input()
    answer1 = 0
    player1 = Player(pseudo1,answer1)
    print("Joueur 2 ,veuillez choisir votre pseudo")
    pseudo2 = input()
    answer2 = 0
    player2 = Player(pseudo2,answer2)

    x = random.randint(1, 51)
    print(player1.get_pseudo(),",veuillez bien choisir un nombre")
    answer1 = int(input())

    fausser = True
    while fausser == True:
      if answer1 < x:
          print("Le nombre mystére est plus grand ;)")
          print(player2.get_pseudo(),"veuillez choisir un autre nombre")
          answer2 = int(input())
      elif answer1 > x:
          print("Le nombre mystére est plus petit ;)")
          print(player2.get_pseudo(),"veuillez choisir un autre nombre")
          answer2 = int(input())
      elif answer1 == x:
          fausser = False
          print("Bravo",player1.get_pseudo(),"vous avez trouvé le nombre mystere qui est",x)
      if answer2 < x:
          print("Le nombre mystére est plus grand ;)")
          print(player1.get_pseudo(),"veuillez choisir un autre nombre")
          answer1 = int(input())
      elif answer2 > x:
          print("Le nombre mystére est plus petit ;)")
          print(player1.get_pseudo(),"veuillez choisir un autre nombre")
          answer1 = int(input())
      elif answer2 == x:
          fausser = False
          print("Bravo",player2.get_pseudo(),"vous avez trouvé le nombre mystere qui est",x)
  if answer_diff == 2:
    print("Joueur 1 ,veuillez choisir votre pseudo")
    pseudo1 = input()
    answer1 = 0
    player1 = Player(pseudo1,answer1)
    print("Joueur 2 ,veuillez choisir votre pseudo")
    pseudo2 = input()
    answer2 = 0
    player2 = Player(pseudo2,answer2)

    x = random.randint(1, 101)
    print(player1.get_pseudo(),",veuillez bien choisir un nombre")
    answer1 = int(input())

    fausser = True
    while fausser == True:
      if answer1 < x:
          print("Le nombre mystére est plus grand ;)")
          print(player2.get_pseudo(),"veuillez choisir un autre nombre")
          answer2 = int(input())
      elif answer1 > x:
          print("Le nombre mystére est plus petit ;)")
          print(player2.get_pseudo(),"veuillez choisir un autre nombre")
          answer2 = int(input())
      elif answer1 == x:
          fausser = False
          print("Bravo",player1.get_pseudo(),"vous avez trouvé le nombre mystere qui est",x)
      if answer2 < x:
          print("Le nombre mystére est plus grand ;)")
          print(player1.get_pseudo(),"veuillez choisir un autre nombre")
          answer1 = int(input())
      elif answer2 > x:
          print("Le nombre mystére est plus petit ;)")
          print(player1.get_pseudo(),"veuillez choisir un autre nombre")
          answer1 = int(input())
      elif answer2 == x:
          fausser = False
          print("Bravo",player2.get_pseudo(),"vous avez trouvé le nombre mystere qui est",x) 
  if answer_diff == 3:
    print("Joueur 1 ,veuillez choisir votre pseudo")
    pseudo1 = input()
    answer1 = 0
    player1 = Player(pseudo1,answer1)
    print("Joueur 2 ,veuillez choisir votre pseudo")
    pseudo2 = input()
    answer2 = 0
    player2 = Player(pseudo2,answer2)

    x = random.randint(1, 201)
    print(player1.get_pseudo(),",veuillez bien choisir un nombre")
    answer1 = int(input())

    fausser = True
    while fausser == True:
      if answer1 < x:
          print("Le nombre mystére est plus grand ;)")
          print(player2.get_pseudo(),"veuillez choisir un autre nombre")
          answer2 = int(input())
      elif answer1 > x:
          print("Le nombre mystére est plus petit ;)")
          print(player2.get_pseudo(),"veuillez choisir un autre nombre")
          answer2 = int(input())
      elif answer1 == x:
          fausser = False
          print("Bravo",player1.get_pseudo(),"vous avez trouvé le nombre mystere qui est",x)
      if answer2 < x:
          print("Le nombre mystére est plus grand ;)")
          print(player1.get_pseudo(),"veuillez choisir un autre nombre")
          answer1 = int(input())
      elif answer2 > x:
          print("Le nombre mystére est plus petit ;)")
          print(player1.get_pseudo(),"veuillez choisir un autre nombre")
          answer1 = int(input())
      elif answer2 == x:
          fausser = False
          print("Bravo",player2.get_pseudo(),"vous avez trouvé le nombre mystere qui est",x)