row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map1 = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
print("""Where do you want to put the treasure? 
column row ex: 31
column 3, row 1""")

position = input()
position = list(position)
cl = int(position[0]) - 1
rw = int(position[1]) - 1
map1[rw][cl] = "🚩"

print(f"{row1}\n{row2}\n{row3}")