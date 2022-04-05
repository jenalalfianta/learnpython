import random

kertas = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

gunting = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

batu = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

print("Apa pilihanmu?\nKetik 1 untuk kertas.\nKetik 2 untuk gunting.\nKetik 3 untuk batu.")
humanInput = int(input("")) - 1
computerInput = round(random.random() * 2)
kgb = [kertas, gunting, batu]
gambarPilihanComputer = kgb[computerInput]
gambarPilihanHuman = kgb[humanInput]

if humanInput == 0 and computerInput == 1:
    hasil = "KAMU KALAH !.."
elif humanInput == 1 and computerInput == 2:
    hasil = "KAMU KALAH !.."
elif humanInput == 2 and computerInput == 0:
    hasil = "KAMU KALAH !.."
elif humanInput == computerInput:
    hasil = "HASIL SERI !.."
else:
    hasil = "KAMU MENANG !.."

print(f"Kamu memilih:\n{gambarPilihanHuman}\nKomputer memilih:\n{gambarPilihanComputer}\n{hasil}")