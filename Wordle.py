def wordle():
    import random
    def checkguess(answer,guess):
        position=0
        clue=''
        for letter in guess:
            if letter==answer[position]:
                clue+='G'
            elif letter in answer:
                clue+='Y'
            else:
                clue+='-'
            position+=1
        print(clue)
        return clue == 'GGGGG'
        
    wordlist=[]
    f=open('words.txt','r')
    for j in f.readlines():
        wordlist.append(j.strip())
    answer=random.choice(wordlist)
    iscorrect=False
    ct=0
    while ct<6 and not iscorrect:
        guess=input('Input a five-letter word: ')
        if len(guess)!=5:
            print("Please enter a 5 letter word")
            break
        print('GUESS: ',guess)
        ct+=1
        iscorrect=checkguess(answer,guess)

    if iscorrect:
        print('You guessed correctly in',ct)
    else:
        print('You have used up your guesses')
        print('Correct Word :',answer)