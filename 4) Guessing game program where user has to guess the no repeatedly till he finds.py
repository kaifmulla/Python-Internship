#Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether there no was too large or too small. At the end the no of tries needed should be printed. It counts only as one try if they input the same no multiple times consecutively.
secrete_num = 67
count = 0
guess = int(input("Guess the secrete number :- "))
dummy = secrete_num
print(dummy)
while True:
    if guess == dummy:
        print("you have guess right secrete")
        count = count + 1
        print(f"No of attempts :- {count}")
        break
    else:
        while guess!=secrete_num:
            if guess > secrete_num:
                print("Your no is large")
                count = count + 1
                guess = int(input("Again guess the secrete no :- "))
            else:
                print("your no is smaller")
                count = count + 1
                guess = int(input("Again guess the secrete no :- "))



            

