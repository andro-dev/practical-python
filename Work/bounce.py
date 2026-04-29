# bounce.py
#
# Exercise 1.5


height = 100
bounce = 3 / 5
i = 1
while i <=10:
    print(i, f"{height * bounce:.4}")
    height *= bounce
    i+=1
