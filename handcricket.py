import random
k=0
w=int(input("Enter number of wickets for the game."))
if w<1:
      print("Invalid, try again.")
lt=["t","h"]
t=random.choice(lt)
if t=="t":
    print("Computer chooses tails.")
    ht="h"
else:
    print("Computer chooses heads.")
    ht="t"
lt2=[1,2,3,4,5,6]
t2=random.choice(lt2)
ht2=int(input("Throw a number to determine batting or balling."))
if ht2>=1 or ht2<=6:
    if (ht2+t2)%2==0:
        print("Computer throws",t2,". It's tails.")
        if ht=="t":
            k=1
    else:
        print("Computer throws",t2,". It's heads.")
        if ht=="h":
            k=1
#toss winner is determined
if k==0:
    lt3=["bt","bl"]
    t3=random.choice(lt3)
    if t3=="bt":
        print("Computer wins and chooses to bat first.")
        i=0
        runs=0
        while i!=w:
            cbt=random.choice(lt2)
            hbl=int(input("Throw a number"))
            if hbl<1 or hbl>6:
                print("Invalid")
            else:
                if cbt==hbl:
                    print("Computer throws ",cbt,".Out!")
                    i+=1
                    print("wickets remaining = ", (w-i))
                else:
                    runs+=cbt
                    print("Computer throws ",cbt)
                    print("runs made is = ", runs)
        else:
            print("Total runs by computer= ",runs)
        print("B-R-E-A-K")
        print("press Enter")
        input()
        print("Your turn to bat.")
        ih=0
        runsh=0
        while ih!=w:
            cbl=random.choice(lt2)
            hbt=int(input("Throw a number."))
            if hbt<1 or hbt>6:
                print("Invalid")
            else:
                if cbl==hbt:
                    print("Computer throws ",cbl,".Out!")
                    ih+=1
                    print("wickets remaining = ", (w-ih))
                else:
                    runsh+=hbt
                    print("Computer throws ",cbl)
                    print("runs made is = ",runsh)
            if runsh>runs:
                print("You win by ",(i),"wickets! Congratulations!")
                break
        else:
            print("Your total runs is = ",runsh,". You lost! Try again")
            
        

            
    else:
        print("Computer wins and chooses to bowl first.")
        ih=0
        runsh=0
        while ih!=w:
            cbl=random.choice(lt2)
            hbt=int(input("Throw a number."))
            if hbt<1 or hbt>6:
                print("Invalid")
            else:
                if cbl==hbt:
                    print("Computer throws ",cbl,".Out!")
                    ih+=1
                    print("wickets remaining = ", (w-ih))
                else:
                    runsh+=hbt
                    print("Computer throws ",cbl)
                    print("runs made is = ",runsh)
        else:
            print("Your total runs is = ",runsh,".")
        print("B-R-E-A-K")
        print("press Enter")
        input()
        print("Computer's turn to bat")
        i=0
        runs=0
        while i!=w:
            cbt=random.choice(lt2)
            hbl=int(input("Throw a number"))
            if hbl<1 or hbl>6:
                print("Invalid")
            else:
                if cbt==hbl:
                    print("Computer throws ",cbt,".Out!")
                    i+=1
                    print("wickets remaining = ", (w-i))
                else:
                    runs+=cbt
                    print("Computer throws ",cbt)
                    print("runs made is = ", runs)
            if runs>runsh:
                print("Computer wins by ",(i),"wickets. You Lose!")
                break
        else:
            print("Computer's total runs is = ",runs,". You win by ",(runsh-runs)," runs!")
#If Human wins the toss
else:
      lt3=["bt","bl"]
      t3=random.choice(lt3)
      print("You won the toss.")
      ht3=input("Enter bt for batting and bl for balling")
      if ht3 not in lt3:
        print("Invalid input.")
      else:
        if ht3=="bt":
            print("You choose to bat first.")
            ih=0
            runsh=0
            while ih!=w:
                cbl=random.choice(lt2)
                hbt=int(input("Throw a number."))
                if hbt<1 or hbt>6:
                    print("Invalid")
                else:
                    if cbl==hbt:
                        print("Computer throws ",cbl,".Out!")
                        ih+=1
                        print("wickets remaining = ", (w-ih))
                    else:
                        runsh+=hbt
                        print("Computer throws",cbl)
                        print("runs made is = ",runsh)
            else:
                print("Your total runs is = ",runsh,".")
                print("B-R-E-A-K")
                print("press Enter")
                input()
                print("Computer's turn to bat")
                i=0
                runs=0
                while i!=w:
                    cbt=random.choice(lt2)
                    hbl=int(input("Throw a number"))
                    if hbl<1 or hbl>6:
                        print("Invalid")
                    else:
                        if cbt==hbl:
                            print("Computer throws ",cbt,".Out!")
                            i+=1
                            print("wickets remaining = ", (w-i))
                        else:
                            runs+=cbt
                            print("Computer throws",cbt)
                            print("runs made is = ", runs)
                    if runs>runsh:
                        print("Computer wins by ",(i),"wickets. You Lose!")
                        break
                else:
                    print("Computer's total runs is = ",runs,". You win by ",(runsh-runs)," runs!")
        else:
            print("You choose to ball first.")
            i=0
            runs=0
            while i!=w:
                cbt=random.choice(lt2)
                hbl=int(input("Throw a number"))
                if hbl<1 or hbl>6:
                    print("Invalid")
                else:
                    if cbt==hbl:
                        print("Computer throws ",cbt,".Out!")
                        i+=1
                        print("wickets remaining = ", (w-i))
                    else:
                        runs+=cbt
                        print("Computer throws",cbt)
                        print("runs made is = ", runs)
            else:
                print("Total runs by computer= ",runs)
                print("B-R-E-A-K")
                print("press Enter")
                input()
                print("Your turn to bat.")
                ih=0
                runsh=0
                while ih!=w:
                    cbl=random.choice(lt2)
                    hbt=int(input("Throw a number."))
                    if hbt<1 or hbt>6:
                        print("Invalid")
                    else:
                        if cbl==hbt:
                            print("Computer throws ",cbl,".Out!")
                            ih+=1
                            print("wickets remaining = ", (w-ih))
                        else:
                            runsh+=hbt
                            print("Computer throws",cbl)
                            print("runs made is = ",runsh)
                    if runsh>runs:
                        print("You win by ",(i),"wickets! Congratulations!")
                        break
                else:
                    print("Your total runs is = ",runsh,". You lost! Try again")
            
