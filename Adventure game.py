# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 23:03:41 2020

@author: hamad
"""
import random
import time


screen_width = 100

def gaps():
    print("\n" * 20)
    
def gap():
    print("\n" * 5)

def displayintro():
    print("IT'S 4 O'ClOCK IN THE MORNING AND YOU CAN BARELY OPEN YOUR EYES...")
    
    time.sleep (2)
    
    print("YESTERDAY WAS A PRETTY AWFUL DAY WITH JUST ONE HOUR OF SLEEP...")
    
    time.sleep(2)
    
    print("YOU WERE WORKING CONSTANTLY LIKE A MACHINE, BUT YOU DON'T HAVE ANY OTHER CHOICE.")
    
def stageoneintro():
    print("Your assistant (Dr.David) rushed to the lab...")
    
    time.sleep(2)
    
    print("Dr.David: Hurry up and hide! there is a virtual press conference!")
    
    time.sleep(1.5)
    
    print("YOU ANSWERED: I MUST ATTEND THIS CONFERENCE AND I THINK I WILL LOSE MY JOB IF I DIDN'T.")

def gameover():
    print(''' 
$$$$$$$  $$$$$$$  $$$$$$$  $$$$$$$  $$$$$$$  $       $  $$$$$$$  $$$$$$$  $$  
$        $     $  $  $  $  $        $     $   $     $   $        $     $  $$
$ $$$$$  $$$$$$$  $  $  $  $$$$$$$  $     $    $   $    $$$$$$$  $$$$$$$  $$ 
$     $  $     $  $  $  $  $        $     $     $ $     $        $$       
$$$$$$$  $     $  $  $  $  $$$$$$$  $$$$$$$      $      $$$$$$$  $ $      $$
    ''')

def completestory():
    complete = "w"
    while complete != "":
        complete = input ("Press ENTER to continue ---->")
    return complete

def playagain1():
    gap()
    again = input ("""
         Do you want to play again? (Yes / No)
         >""")
    
    again = again.lower()
    
    accept = ["yes", "y"]
    deny = ["no","n"]
    if again in accept:
       gaps()
       gameplay1()
       gameplay2()
       gameplay3()
    
    elif again in deny:
        gaps()
        gameover()
        time.sleep(5)
    
    elif again not in accept and again not in deny:
        print("INVALID CHARACTER ENTERED, TRY AGAIN...")
        print("="*50)
        playagain1()
  
    else:
       print("SOMETHING WENT WRONG")
            
def playagain2():
    gap()
    again = input ("""
         Do you want to play again? (Yes / No)
         >""")
    
    again = again.lower()
    
    accept = ["yes", "y"]
    deny = ["no","n"]
    if again in accept:
       gaps()
       gameplay2()
       gameplay3()
    
    elif again in deny:
        gaps()
        gameover()
        time.sleep(5)
    
    elif again not in accept and again not in deny:
        print("INVALID CHARACTER ENTERED, TRY AGAIN...")
        print("="*50)
        playagain2()
  
    else:
       print("SOMETHING WENT WRONG")

def playagain3():
    gap()
    again = input ("""
         Do you want to play again? (Yes / No)
         >""")
    
    again = again.lower()
    
    accept = ["yes", "y"]
    deny = ["no","n"]
    if again in accept:
       gaps()
       gameplay3()
    
    elif again in deny:
        gaps()
        gameover()
        time.sleep(5)
    
    elif again not in accept and again not in deny:
        print("INVALID CHARACTER ENTERED, TRY AGAIN...")
        print("="*50)
        playagain3()
  
    else:
       print("SOMETHING WENT WRONG")
        
def question1():
    print("""YOU JOINED THE CONFERENCE.
          ONE OF THE REPORTERS ASKED: THERE ARE MORE THAN 1 MILLION CONFIRMED CASES
         WORLDWIDE WE WANT TO KNOW YOUR PROGRESS, DID YOU ACTUALLY REACH TO ANYTHNIG?""")
       
    time.sleep(3) 
        
    print("""YOU HAVE THREE OPTIONS TO CHOOSE FROM:
             A) LIE AND SAY THAT YOU HAVE SUCCESSFULLY COMPLETED 90% OF THE WORK.
             B) SAY THE TRUTH (THAT YOU DIDN'T REACH TO NEW RESULTS).
             C) BABBLE SOME SCIENTIFIC FACTS AND CHANGE THE TOPIC.
                """)
    
    choice =  input("""
                Which option do you want to choose?
                     >""")
     
    choice = choice.lower()
    
    ans1 = ["a","1","lie and say that you have successfully completed 90% of the work."]
     
    ans2 = ["b","2","say the truth (that you didn't reach to new results)."] 

    ans3 = ["c","2","babble some scientific facts and change the topic."]    
                   
    if choice in ans1:
        print("YOUR ASSISTANT TOLD EVERYONE THAT YOU ARE A LIAR AND YOU GOT FIRED.")
        time.sleep(1.5)
        gameover()
        time.sleep(3)
        playagain1()
        
    elif choice in ans2:
        print("EVERYONE LOST HOPE BECAUSE YOU TOLD THEM THAT YOU DIDN'T REACH TO ANYTHING")
        time.sleep(1.5)
        print("YOU GOT FIRED AND SOMEONE ELSE STARTED TO DO YOUR JOB")
        time.sleep(1.5)
        gameover()
        time.sleep(3)
        playagain1()
        
    elif choice in ans3:
        print("""YOU SAID: WE CONTAMINATED THE VIRUS AS THE FIRST STEP AND WHAT WE OBSERVED 
             IS THAT THIS VIRUS IS A REALLY DANGEROUS VIRUS THAT SPREADS RAPIDLY
             AND IT DOESN'T GET AFFECTED BY (RTS,S), BUT IT SHOWED A MINOR WEAKNESS WHEN WE
             PUT (HYDROXYCHLOROQUINE) ON IT.   
             """)
        
        time.sleep(5)   
        
        print("""THE REPORTERS STARTED TO CLAP FROM THEIR HOME (AS THIS CONFERENCE WAS HELD ONLINE)
             WITHOUT UNDERSTANDING A WORD YOU SAID AND THEY THOUGHT THAT YOU ARE VERY CLOSE FROM DEVELOPING THE VACCINE.
              """)
              
        time.sleep(3)
    
        completestory()
    
        gap()
    
        print("WHOA! THAT WAS A PRETTY CLEVER ANSWER, BUT THIS WAS JUST THE FIRST QUESTION")
        
        completestory()
        
        gap()
        
        print("="*50)
    
    elif choice not in ans1 and choice not in ans2 and choice not in ans3:
        print('INVALID CHARACTER ENTERED. TRY AGAIN....')
        print("="*50)
        question1()
    else:
        print('SOMETHING WENT WRONG! (1)')

def question2():
    print("ANOTHER REPORTER ASKED: HOW MUCH DAMAGE DO YOU EXPECT FROM THE NOVEL CORONAVIRUS?")
        
    time.sleep(3)
        
    print("""YOU HAVE THREE OPTIONS TO CHOOSE FROM:
          A) I DON'T KNOW, I WAS JUST PROCRASTINATING AND DIDN'T STUDY THE VIRUS.
          B) I CAN'T GIVE AN EXACT NUMBER BECAUSE WE ARE STILL TRYING TO STUDY THE VIRUS.
          C) I EXPECT THAT IT WILL AFFECT AT LEAST 1.5 MILLION PEOPLE GLOBALLY.
                """)
                
    choice =  input("""
                    Which option do you want to choose?
                    >""")
     
    choice = choice.lower()
    
    ans1 = ["a","1","i don't know, i was just procrastinating and didn't study the virus."]
     
    ans2 = ["b","2","i can't give an exact number because we are still trying to study the virus."] 

    ans3 = ["c","3","i expect that it will affect at least 1.5 million people globally."]   
       
    if choice in ans1:
        print("I AM SURE YOU KNEW THIS WASN'T THE RIGHT ANSWER AND YOU WERE JUST PLAYING AROUND")
        time.sleep(1.5)
        print("BUT UNFORTUNATELY YOU HAVE TO RESTART THE GAME")
        time.sleep(1.5)
        gameover()
        time.sleep(3)
        playagain1()
    
    elif choice in ans2:
         print("WOW! THAT WAS A VERY LOGICAL ANSWER, BUT THERE'S STILL ONE LAST QUESTION OF THE CONFERENCE.")
            
         completestory()
           
         gaps()    
    
    elif choice in ans3:
         print("THE REPORTER CONTINUED: HOW DID YOU GIVE AN EXACT NUMBER?")
         time.sleep(1.5)
         print("YOU COULDN'T ANSWER AS THE REALITY WAS THAT YOU CAME UP WITH THAT NUMBER.")
         time.sleep(1.5)
         gameover()
         time.sleep(3)
         playagain1()
   
    elif choice not in ans1 and choice not in ans2 and choice not in ans3:
        print("INVALID CHARACTER ENTERED. TRY AGAIN...")
        print("="*50)
        question2()
    
    else:
        print("SOMETHING WENT WRONG! (2)")
        
def question3():
    print("THE THIRD REPORTER ASKED: WHAT ARE YOU ADVISING PEOPLE TO DO?")
            
    time.sleep(3)
            
    print("""YOU HAVE THREE OPTIONS TO CHOOSE FROM:
          A) DON'T PANIC.
          B) WE WILL ALL DIE, SO IT'S BETTER TO SUICIDE.
          C) STAY AT HOME, MAINTAIN SOCIAL DISTANCING, AND WASH YOUR HANDS FREQUENTLY.
                """)
    choice =  input("""
                    Which option do you want to choose?
                    >""")
     
    choice = choice.lower()
    
    ans1 = ["a","1","don't panic."]
     
    ans2 = ["b","2","we will all die, so it's better to suicide."] 

    ans3 = ["c","3","stay at home, maintain social distancing, and wash your hands frequently."]   
        
    if choice in ans1:
        print("IT'S A LOGICAL ANSWER BUT TWO WORDS AREN'T ENOUGH.")
        time.sleep(1.5)
        gameover()
        playagain1()
        
    elif choice in ans2:
        print("MAYBE THIS ANSWER IS RIGHT FOR YOU ONLY.")
        time.sleep(1.5)
        print("SORRY TO SAY THIS BUT YOU GOT FIRED AND THE JUDGE SENTENCED 1000 YEARS OF JAIL FOR YOU!")
        time.sleep(1.5)
        gameover()
        playagain1()
        
    elif choice in ans3:
        gaps()
       
        print("GREAT JOB! YOU HAVE SUCCESSFULLY COMPLETED STAGE 1")
        
        completestory()
                
        gaps()
    elif choice not in ans1 and choice not in ans2 and choice not in ans3:
        print("INVALID CHARACTER ENTERED. TRY AGAIN...")
        print("="*50)
        question3()
    else:
        print("SOMETHING WENT WRONG! (3)")
        
def question4():
    print("YOU BROUGHT A SAMPLE OF THE VIRUS FROM AN INFECTED PERSON'S SLAIVA AND PUT IT IN A TEST TUBE")
    time.sleep(1.5)
    print("WHAT DO YOU WANT TO DO NEXT?")
    print("""YOU HAVE THREE OPTIONS TO CHOOSE FROM:
           A) EXAMINE IT UNDER A MICROSCOPE. 
           B) PUT (HYDROXYCHLOROQUINE) ON IT.
           C) OBSERVE ITS REACTION WITH OXYGEN.
                """)
                
    choice =  input("""
                    Which option do you want to choose?
                    >""")
     
    choice = choice.lower()
    
    ans1 = ["a","1","examine it under a microscope."]
     
    ans2 = ["b","2","put (hydroxychloroquine) on it."] 

    ans3 = ["c","3","observe its reaction with oxygen."]   
    
    if choice in ans1:
        print("YOU GOT THE RIGHT ANSWER AGAIN!")
        time.sleep(1.5)
        completestory()    
    
    elif choice in ans2:
        print("YOU ALREADY PUT (HYDROXYCHLORQUINE) ON IT BEFORE AS YOU SAID IN THE PRESS CONFERENCE...")
        time.sleep(1.5)
        gameover()
        playagain2()
    
    elif choice in ans3:
        print("I THINK OXYGEN ALREADY REACTED WITH CORONAVIRUS IN NORMAL AIR...")
        time.sleep(1.5)
        gameover()
        playagain2()
    
    elif choice not in ans1 and choice not in ans2 and choice not in ans3:
        print("INVALID CHARACTER ENTERED. TRY AGAIN...")
        time.sleep(3)
        print("="*50)
        question4()
    else:
        print("SOMETHING WENT WRONG! (4)")

def question5():
    print("AFTER EXAMINING THE VIRUS UNDER MICROSCOPE...")
    time.sleep(5)
    print("AND BY COMPARING THE AVAILABLE GENOME SEQUENCE DATA FOR KNOWN CORONAVIRUS STRAINS")
    print("YOU FIRMLY DETERMINED THAT THE VIRUS EVOLVED AND ORIGINATED THROUGH NATURAL PROCESSES.")
    completestory()
    gap()
    print("IN ORDER TO PRODUCE A VACCINE, WHAT'S THE FIRST THING YOU WANT TO DO?")
    time.sleep(1.5)
    print("""YOU HAVE THREE OPTIONS TO CHOOSE FROM:
          A) TEST THE VACCINE'S EFFECT ON THE VIRUS. 
          B) GENERATE AN ANTIGEN.
          C) GO HOME AND SIT ALONE TO MAINTAIN SOCIAL DISTANCING.
                """)
    choice =  input("""
                    Which option do you want to choose?
                    >""")
     
    choice = choice.lower()
    
    ans1 = ["a","1","test the vaccine's effect on the virus."]
     
    ans2 = ["b","2","generate an antigen."] 

    ans3 = ["c","3","go home and sit alone to maintain social distancing."]   
    
    if choice in ans1:
       print("HOW CAN YOU TEST THE VACCINE'S EFFECT BEFORE DEVELOPING THE VACCINE?!")
       time.sleep(1)
       print("SORRY!")
       time.sleep(1.5)
       gameover()
       playagain2()
    
    elif choice in ans2:
        print("THAT'S RIGHT!")
        time.sleep(1.5)
        print("YOU ARE NOW NEARER TO THE VACCINE")
            
        completestory()
            
        gaps()
    
    elif choice in ans3:
       print("IF YOU WENT HOME THEN WHO WILL DEVELOP THE VACCINE?")
       time.sleep(1.5)
       print("PLEASE LEARN TO BE RESPONSBILE!!!")
       time.sleep(1.5)
       gameover()
       playagain2()
        
    
    
    elif choice not in ans1 and choice not in ans2 and choice not in ans3:
        print("INVALID CHARACTER ENTERED. TRY AGAIN...")
        question5()
    else:
        print("SOMETHING WENT WRONG! (5)")

def question6():
    print("WHAT SHOULD YOU DO NEXT?")
    print("""YOU HAVE THREE OPTIONS TO CHOOSE FROM:
                A) TEST IT ON YOURSELF.
                B) ANNOUNCE THAT YOU REACHED TO THE VACCINE PUBLICLY.
                C) TEST IT ON AN ANIMAL CELL.
                """) 
                
    choice =  input("""
                    Which option do you want to choose?
                    >""")
     
    choice = choice.lower()
    
    ans1 = ["a","1","test it on yourself."]
     
    ans2 = ["b","2","announce that you reached to the vaccine publicly."] 

    ans3 = ["c","3","test it on an animal cell."]   
    
    if choice in ans1:
        print("AND WHAT IF YOU DIE?")
        time.sleep(1)
        print("WHO WILL DEVELOP THE VACCINE AFTER YOU? (KNOWING THAT YOU ARE THE BEST DOCTOR IN THE WORLD)")
        time.sleep(1.5)
        gameover()
        playagain3()
    
    elif choice in ans2:
        print("ARE YOU SURE THAT THIS VACCINE WILL WORK?")
        time.sleep(1.5)
        gameover()
        playagain3()
    
    elif choice in ans3:
        print("CORRECT ANSWER!")
        print("YOU MUST BE A SCIENTIST.")
        completestory()    
        
    elif choice not in ans1 and choice not in ans2 and choice not in ans3:
        print("INVALID CHARACTER ENTERED. TRY AGAIN...")
        print("="*50)
        question6()
    
    else:
        print("SOMETHING WENT WRONG! (6)")

def question7():
    print("YOU TESTED THE VACCINE AND IT WORKED!")
    time.sleep(5)
    print("\n")
    print("YOU ANNOUNCED PUBLICLY THAT YOU FOUND THE VACCINE AND EVERYONE WAS SUPER HAPPY!")
    time.sleep(5)
    print("\n")
    print("BUT UNFORTUNATELY THE TEST TUBE WASN'T WITH YOU SO YOU WENT TO THE LAB TO BRING IT")
    time.sleep(5)
    print("\n")
    print("YOU HEARD DR.DAVID SCREAMING: NOOOOOOO!")
    time.sleep(5)
    print("\n")
    print("AS SOON AS YOU HEARD THE SCREAM YOU WENT TO THE LAB RUNNING")
    time.sleep(5)
    print("\n")
    print("AND ASKED:WHAT HAPPENED?!")
    time.sleep(5)
    print("\n")
    print("DR.DAVID REPLIED WITH A VERY SAD VOICE:")
    time.sleep(5)
    print("\n")
    print("WE FORGOT TO LABEL THE TEST TUBES AND NOW WE DON'T KNOW WHICH ONE HAS THE VACCINE.")
    time.sleep(5)
    print("\n")
    print("YOU LAUGHED AND REPLIED: HA!HA!HA! NO PROBLEM WE WILL DO THE TESTS AGAIN.")
    completestory()
    gap()
    print("AT THE SAME MOMENT AN EARTHQUAKE OCCURED....")
    completestory()
    print("YOU HAVE SIX TEST TUBES, AND YOU CAN ONLY TAKE ONE OUTSIDE BECAUSE OF THE EARTHQUAKE")
    print("YOU MUST CHOOSE THE RIGHT TUBE OR YOU WILL LOSE EVERYTHING YOU DID!")    
    choice =  input("""
                    PLEASE ENTER A NUMBER:
                    >""")
                    
    correctTube = random.randint(1,6)
    
    if choice == str(correctTube):
            print("YOU GOT THE RIGHT TEST TUBE!")
            print("YOU SAVED THE WORLD!")
            completestory()
            print('''
$$$$$$$  $$$$$$$  $$   $  $$$$$$$  $$$$$$$  $$$$$$$  $$$$$$$  $$$$$$$  $$          
$        $     $  $ $  $  $        $     $  $     $     $     $        $$
$        $     $  $  $ $  $ $$$$$  $$$$$$$  $$$$$$$     $     $$$$$$$  $$
$        $     $  $   $$  $     $  $$       $     $     $           $
$$$$$$$  $$$$$$$  $    $  $$$$$$$  $ $      $     $     $     $$$$$$$  $$
           ''')
            playagain1()
        
    elif choice != str(correctTube):
            print("THAT WAS THE WRONG TEST TUBE!")
            time.sleep(3)
            print("BUT DON'T WORRY YOU GET A LAST CHANCE, BE CAREFUL THIS TIME!")
            print("="*50)
            choice2 =  input("""
                    PLEASE ENTER A NUMBER:
                    >""")
            
            if choice2 == str(correctTube):
                print("YOU GOT THE RIGHT TEST TUBE!")
                print("YOU SAVED THE WORLD!")
                completestory()
                print('''
$$$$$$$  $$$$$$$  $$   $  $$$$$$$  $$$$$$$  $$$$$$$  $$$$$$$  $$$$$$$  $$          
$        $     $  $ $  $  $        $     $  $     $     $     $        $$
$        $     $  $  $ $  $ $$$$$  $$$$$$$  $$$$$$$     $     $$$$$$$  $$
$        $     $  $   $$  $     $  $$       $     $     $           $
$$$$$$$  $$$$$$$  $    $  $$$$$$$  $ $      $     $     $     $$$$$$$  $$
           ''')
           
            elif choice2 != str(correctTube):
                print("THAT WAS THE WRONG TEST TUBE!")
                print("YOU HAVE LOST EVERYTHING!")
                print("AND YOU HAVE TO START FROM THE BEGINNING!")
                completestory()
                gameover()
                playagain1()

    else:
        ("SOMETHING WENT WRONG (7)")             
      
def gameplay1():

#TITLE 
    print('''
$$$$$$$  $     $  $$$$$$$      $$$$$$$  $    $  $$$$$$$  $$$$$$$  $$$$$$$ $$$$$$$  $$$$$$$  $  $
   $     $     $  $            $     $  $    $     $     $     $  $     $ $        $     $  $ $
   $     $$$$$$$  $$$$$$$      $     $  $    $     $     $$$$$$$  $$$$$$$ $$$$$$$  $$$$$$$  $$
   $     $     $  $            $     $  $    $     $     $     $  $$      $        $     $  $ $
   $     $     $  $$$$$$$      $$$$$$$  $$$$$$     $     $$$$$$$  $ $     $$$$$$$  $     $  $  $     
''')
    time.sleep(2)
    
    completestory()

    gap()
#INTRO
    displayintro()

    time.sleep(2)
#NAME
    name = input('Enter your name\n')

    gap()
#GREETING
    print(f'''
          Hello Doctor {name}
          ''')

    time.sleep(2)

    completestory()

    gap()
#COMPLETION OF STORY
    print('YOU ARE A DOCTOR FIGHTING AGAINST THE NEW PANDEMIC')

    time.sleep(2)

    print('(COVID-19)')

    time.sleep(1.5)

    gap()
    
    completestory()

    print("YOU ARE NOT A SIMPLE DOCTOR WHO SITS IN THE EMERGENCY ROOM AND WAITS FOR PATIENTS TO EXAMINE THEM.")

    time.sleep(1)

    print("INFACT YOU ARE AN INFECTIOUS DISEASE SPECIALIST WHO IS TRYING TO DEVELOP A VACCINE FOR (COVID - 19).")
    
    time.sleep(2)

    print("IT WON'T BE AN EASY JOB, SO GOOD LUCK!")

    completestory()

    gaps()
#FIRST STAGE TITLE
    print('''
$$$$$$$  $$$$$$$$  $$$$$$$  $$$$$$$  $$$$$$$        $ 
$           $      $     $  $        $             $$ 
$$$$$$$     $      $$$$$$$  $ $$$$$  $$$$$$$        $
      $     $      $     $  $     $  $              $
$$$$$$$     $      $     $  $$$$$$$  $$$$$$$      $$$$$
''')

    completestory()

    gaps()
#STAGE 1 INTRO
    stageoneintro()

    time.sleep(1.5)

    completestory()

    gap()
#FIRST QUESTION
    question1()
       
    time.sleep(5)   
    
#SECOND QUESTION    
    
    question2()
    
#THIRD QUESTION           
    question3()
                
    print('''
$$$$$$$  $     $  $$$$$$$  $$$$$$$  $  $  $$$$$$$  $$$$$$$  $$$$$$$  $$   $  $$$$$$$  $$         
$        $     $  $        $        $ $   $     $  $     $     $     $ $  $     $     $$
$        $$$$$$$  $$$$$$$  $        $$    $$$$$$$  $     $     $     $  $ $     $     $$
$        $     $  $        $        $ $   $        $     $     $     $   $$     $  
$$$$$$$  $     $  $$$$$$$  $$$$$$$  $  $  $        $$$$$$$  $$$$$$$  $    $     $     $$
                ''')
 
def gameplay2():
   
#SECOND STAGE TITLE 
    print('''
$$$$$$$  $$$$$$$$  $$$$$$$  $$$$$$$  $$$$$$$       $$$$$$$  
$           $      $     $  $        $                   $
$$$$$$$     $      $$$$$$$  $ $$$$$  $$$$$$$       $$$$$$$
      $     $      $     $  $     $  $             $ 
$$$$$$$     $      $     $  $$$$$$$  $$$$$$$       $$$$$$$
''')

    completestory()    
 
    print("THE PRESS CONFERENCE WENT VERY WELL, YOUR ANSWERS WERE OUTSTANDING!")
    time.sleep(1.5)
    print("BUT NOW YOU REALLY HAVE TO START DEVELOPING THE VACCINE.")
    time.sleep(1.5)
    completestory()
    gaps()
#FOURTH QUESTION
    question4()
#FIFTH QUESTION        
    question5()
            
    print('''
$$$$$$$  $     $  $$$$$$$  $$$$$$$  $  $  $$$$$$$  $$$$$$$  $$$$$$$  $$   $  $$$$$$$  $$         
$        $     $  $        $        $ $   $     $  $     $     $     $ $  $     $     $$
$        $$$$$$$  $$$$$$$  $        $$    $$$$$$$  $     $     $     $  $ $     $     $$
$        $     $  $        $        $ $   $        $     $     $     $   $$     $  
$$$$$$$  $     $  $$$$$$$  $$$$$$$  $  $  $        $$$$$$$  $$$$$$$  $    $     $     $$
                ''')
            
def gameplay3():
    print('''
$$$$$$$  $$$$$$$$  $$$$$$$  $$$$$$$  $$$$$$$       $$$$$$$  
$           $      $     $  $        $                   $
$$$$$$$     $      $$$$$$$  $ $$$$$  $$$$$$$       $$$$$$$
      $     $      $     $  $     $  $                   $
$$$$$$$     $      $     $  $$$$$$$  $$$$$$$       $$$$$$$
''')
    
    completestory()
    
    print("YOU HAVE GENERATED AN ANTIGEN, DEVELOPED A VACCINE AND TESTED IT IN THE LAB ON THE VIRUS")
    time.sleep(2)
#SIXTH QUESTION 
    question6()
#SEVENTH QUESTION       
    question7()
    



gameplay1()
gameplay2()
gameplay3()

  
