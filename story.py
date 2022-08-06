# -*- coding: utf-8 -*-

import sys
import time
import random
import qi


NAO_IP = "pepper.local"

class Story():
    def __init__(self, session, name=""):
        self.name = name
        self.tts = session.service("ALAnimatedSpeech")
        self.motion_service = session.service("ALMotion")
        self.tabletService = session.service("ALTabletService")
        self.audio_player_service = session.service("ALAudioPlayer")
        self.steps = []
        self.tangram = {"task": None,
                        "clue": None,
                        "solution": None,
                        "backup": None
}
                        
        self.encouragements = ["I like the way you approach the game.",
                                "You both are good as a team",
                                "It may look hard but you can do it!",
                                "Keep going!"]
        self.funfacts = []


    def show_image(self, name, delay=1.0):
        self.tabletService.showImage("http://198.18.0.1/apps/tangram/" + name)
        time.sleep(delay)
#        self.tabletService.hideImage()


    def show_image_with_speech(self, name, speech, delay=3):
        self.tabletService.showImage("http://198.18.0.1/apps/tangram/" + name)
        self.tts.say(speech)
        time.sleep(delay)
#        self.tabletService.hideImage()
        
    def add_steps(self, steps):
        self.steps = steps
        
    def add_funfact(self, funfact):
        self.funfacts.append(funfact)

    def add_game(self, id, img, text=""):
        self.tangram[id] = [img, text]
    
    def run(self, t0, file):
        file.write(str(time.time() - t0) + ",Started story: " + self.name + "\n")
        for step in self.steps:
            if step[0] == 0:
                self.show_image_with_speech(step[1], step[2], step[3])
            elif step[0] == 1:
                self.tts.say(step[1])
                time.sleep(step[2])
            elif step[0] == 2:
                self.show_image(step[1], step[2])
            elif step[0] == 3:
                fileId = self.audio_player_service.loadFile("/home/nao/.local/share/PackageManager/apps/tangram/" + step[1])
                self.audio_player_service.play(fileId)
                time.sleep(step[2])
                
        try:
            self.game(t0, file)
        except TypeError:
            return


    def game(self, t0, file):
        self.show_image_with_speech(self.tangram["task"][0],
                                        "Go ahead and try to solve this puzzle. Remember that you need to use all 7 pieces to form the shape.")
                                        
        clue_count = 0
          
        command = ""
        file.write(str(time.time() - t0) + ",starting tangram puzzle\n")
        while 1:
            command = raw_input("input c for a clue, s for the solution, e for encouragements, f for a funfact, q to skip the game, h to propose help and n to change the tangram game, r to repeat the rules, l to speak louder\n")
            file.write(str(time.time() - t0) + "," + command+"\n")
            if command == "s":
                correct = raw_input("correct? (y/n)\n")
                file.write(str(time.time() - t0) + "," +  correct+"\n")
                if correct == "y":
                    break
                elif correct=="n":
                    self.tts.say("Unfortunately, your solution is not correct. But you are almost there. If you want to continue trying, say \"Pepper continue\".")
                    if self.tangram["backup"]:
                        self.tts.say("If you want to try another puzzle, say \"Pepper change\".")
                    self.tts.say("If you want to skip the puzzle and continue the story, say \"Pepper done\".")
                command = raw_input("continue (z), change (n), skip (q)\n")
                file.write(str(time.time() - t0) + "," + command+"\n")
            if command == "c":
                clue_count += 1
                
                if self.tangram["backup"] and clue_count == 3:
                    self.show_image_with_speech(self.tangram["backup"][0][0], "You can change the puzzle to this one if the current one is too hard or you can continue with the one you are doing? If you wish to change at any time, please say \"Pepper change\"", 5.0)
                    self.show_image(self.tangram["task"][0], 1.0)
                else:
                    self.tts.say("Ok! I will display the solution on my tablet for 4 seconds. Be Ready!")
                    self.show_image(self.tangram["clue"][0], 4.0)
                    self.show_image(self.tangram["task"][0], 1.0)
            elif command == "h":
                if not self.tangram["backup"]:
                    continue
                self.show_image_with_speech(self.tangram["backup"][0][0], "Do you want to change the puzzle to this one, or keep continuing with the one you are doing? If you wish to change please say  \"Pepper change\".", 5.0)
                self.show_image(self.tangram["task"][0], 1.0)
            elif command == "l":
                self.tts.say("Sorry! I could not understand what you said. Can you please speak louder?")
            elif command == "n":
                if not self.tangram["backup"]:
                    continue
                self.tts.say("Let's try this one now!")
                self.tangram["task"][0] = self.tangram["backup"][0][0]
                self.tangram["clue"][0] = self.tangram["backup"][0][1]
                self.show_image(self.tangram["task"][0], 1.0)
            elif command == "q":
                break
            elif command == "f" and self.funfacts:
                if len(self.funfacts) == 0:
                    continue
                index = random.randint(0, len(self.funfacts)-1)
                self.tts.say(self.funfacts[index])
                self.funfacts.pop(index)
            elif command == "e":
                if len(self.encouragements) == 0:
                    continue
                index = random.randint(0, len(self.encouragements)-1)
                self.tts.say(self.encouragements[index])
                self.encouragements.pop(index)
            elif command == "r":
                rule = raw_input("1. all pieces\n2. help\n3. change\n4. all\n")
                file.write(str(time.time() - t0) + "," +  rule+"\n")
                if rule == "1":
                    self.tts.say("Let me remind you that you have to use all 7 pieces.")
                elif rule == "2":
                    self.tts.say("Let me remind you that if you need help you can say Pepper help.")
                elif rule == "3":
                    self.tts.say("If you find the puzzle too hard and want to try another one, say Pepper change.")
                elif rule == "4":
                    self.tts.say("Let me remind you the rules of the game. You have to use all 7 pieces. If you need help you can say Pepper help and when you are done, please say pepper done, or if you need a break anytime during the session, say Pepper break. If you find the puzzle too hard and want to try another one, say Pepper change. The main rule here is, that you both need to agree with each other on your decisions.")
            
        self.tts.say("Alright! Let me check the solution for you.")
        self.show_image(self.tangram["clue"][0], 5.0)
        index = random.randint(0, len(self.encouragements)-1)
        self.tts.say("You did great!" + self.encouragements[index])
        
        command = ""
        while not command == "n":
            file.write(str(time.time() - t0) + ",n\n")
            command = raw_input("input n to move on to the next game\n")
