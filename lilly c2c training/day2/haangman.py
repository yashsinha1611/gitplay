import random
test=['python','java','javascript','node','react','vikrant']
word=random.choice(test)
 
word_to_set=set(word)
 
attempts=len(word_to_set)
print("No. of attempts : " ,attempts)
 
for a in range(0,attempts):
    move=input("Enter your move : ")
    if move in word_to_set:
        word_to_set.remove(move)
        attempts=attempts+1
 
if len(word_to_set)==0:
    print(" You won!The Word was :"+word)
else:
    print("You lost")