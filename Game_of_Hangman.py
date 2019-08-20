import random
import string

def random_word(x):
    a=string.ascii_lowercase+string.ascii_uppercase  #Generating a string of lower and upper alphabets to genearte the random word for user
    word=(''.join(random.sample(a,int(x))))   #Generating a random word based of the lenghth given by user
    #word1 = ('*'*int(x))
    #print ('word : ',word1)
    print (word)
    attempt_remaning = attempt
    previous_guess = 0
    choose_list=[]
    while (attempt_remaning !=0):
        word1 = ('*'*int(x))
        print ('word : ',word1)
        print ('Attemp remaning : ',attempt_remaning)
        print ('Previous Guess : ',previous_guess)
        choose= input ('Choose the next letter')
        choose_list.append(choose)
        if choose.isupper() or choose.islower():
            for ch in word:
                if ch == choose:
                    print (choose,'is in the word!')
                    break
            else:
                print (choose,'is not in the word')
        else:
            print (choose,'is not an letter')
        attempt_remaning= int(attempt_remaning)-1
        previous_guess = previous_guess+1
        print ('')
    print ('Random word generated is',word)
    print ('Word which you gussed is',''.join(choose_list) )


def wordlen_check():
    wordlen= input('What minimum word lenght you want?[1-10] : ')
    if(wordlen.isdigit()):
        if(int(wordlen) < 11):
            print ('Selecting word ...')
            random_word(wordlen)  #calling other function and passing the value of world lenth entered by user
        else:
            print (wordlen,'not in range of 1 to 10 ')
            wordlen_check()  #if input in not correct calling the same function
    else:
        print (wordlen,'not in range of 1 to 10 ')
        wordlen_check() ##if input in not correct calling the same function


def attempt_check():
    global attempt
    attempt = input ('How many incorrect attempt you want ?[1-10] : ')
    #attempt=int(attempt)
    if (attempt.isdigit()):
        if (int(attempt) < 11):
            wordlen_check()  #caling another function
        else:
            print (attempt,'is not in between of 1 to 10')
            attempt_check()  #if not correct input calling fuction again until the correct input
    else:
        print (attempt,'is not in between of 1 to 10')
        attempt_check()   ##if not correct input calling fuction again until the correct input
            
         
print ('Starting the game of Hangman')
attempt_check()
