#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import String

shapes = ['square','triangle','rectangle','circle','star']
colors  = ['white','black','blue','pink','yellow','orange','green']
animals = ['horse','pig','cow','cat',"hippopotamus",'mouse','hamster']

wordlist = []
 
wordToGuess = random.choice(shapes+colors+animals)

ingame = False

correctCounter = 0

firstGuess = True

pub = ""

def callback(data):
    phrase = data.data
    wordsInPhrase = phrase.split()
    global ingame, wordToGuess, correctCounter, firstGuess, wordlist,pub

    #logic to apply if the robot is not in the guessing game. 
    #if the user wishes to start a game, a series of variable settings are performed.
    if not ingame:
        if(wordsInPhrase[0] == 'link' and 'guessing' in wordsInPhrase):
           wordlist = shapes + colors + animals 
           wordToGuess = random.choice(wordlist)
           wordlist.remove(wordToGuess)
           print("starting the quessing game")
           ingame = True
           print("say the word "+ wordToGuess+ "!")

    #very simple game logic, it just checks if the pronounced word
    #is correct. if it is, it increases a counter, when said counter reaches the 
    #value 5, the game ends.

    if ingame:
        if(wordsInPhrase[0] == 'link' and 'stop' in wordsInPhrase):
            print("stopping the guessing game")
            ingame = False
        else:
            if wordToGuess in wordsInPhrase:

                #doing this to avoid the same words
                wordToGuess = random.choice(wordlist)
                wordlist.remove(wordToGuess)

                correctCounter += 1

                if(correctCounter<5):
                    #this is to avoid printing the last word.
                    print('correct!! now say the word '+ wordToGuess+ "!" )
                print(correctCounter)
            
            #doing this to iterate to the next word.
            elif "next" in wordsInPhrase:
                wordToGuess = random.choice(wordlist)
                wordlist.remove(wordToGuess)
                print('please pronounce the word ' + wordToGuess + "!")

            else:
                if not firstGuess:
                    print("wrong, repeat again!")
                firstGuess = False

            if correctCounter == 5:
                print('congratulations! you won the game.')
                correctCounter = 0
                firstGuess = True
                ingame = False
                wonGame()
                

def guessingGame():

    global pub
    rospy.init_node('guessingGame')

    rospy.Subscriber('/speech_recognition/final_result', String, callback)

    pub = rospy.Publisher('/dancer', String, queue_size=10)

    rospy.spin()

def wonGame():

    print("sending dancing message")
    pub.publish("dancing")



if __name__ == '__main__':

    guessingGame()
    try:
        wonGame()
    except rospy.ROSInterruptException:
        pass
