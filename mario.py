from cs50 import get_int


user = get_int("How tall would you like your staircase: ")


while(user <= 0 or user > 8):
    user = get_int("Sorry can't do that Try again:")


for i in range(user+1):
        print()
        for j in range(i):
            print("#", end="")

print()







