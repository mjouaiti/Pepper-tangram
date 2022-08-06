#~/.local/share/PackageManager/apps/tangram/html

import qi
from story import Story
import argparse
import time
import sys


def main(session):
    recorder = session.service("ALAudioRecorder")
    print("Recording sound now!!!")
    recorder.startMicrophonesRecording("/home/nao/tangram/pilot_audio.wav", "wav", 48000, [1,1,1,1])
        
    tts = session.service("ALTextToSpeech")
    tts.setParameter("speed", 70)
    
    welcome = Story(session, "welcome")
    welcome.add_steps([
                    (0, "story/story_welcome_new.png", "Hi! I am happy to see you today! My name is Pepper. Today, we are going to play a game, and I hope that you both will enjoy this game!", 2.0),
                        (0, "story/story_tangram_1.png", "Let's play the popular game: tangram. Both of you should work together and solve the tangram puzzle", 1.0),
                        (0, "story/story_hifi.png", "Before we start the game, I want you both to give each other a High Five.", 4.0),
                        (1, "It is good to see you interacting with each other", 2.0)])

    demo = Story(session, "demo")
    demo.add_steps([
                    (0, "story/story_tangram_2.png", "I think you know how to play Tangram. To get more comfortable how about doing a small warm-up activity? ", 1.0),
                    (1, "As you can see, there are 7 pieces on the table. I am going to show you a shape, on my tablet, like this", 3.0),
                    (0, "story/story_commands.png", "If you need help you can say Pepper help and when you are done, please say pepper done, or if you need a break anytime during the session, say Pepper break.", 1.0),
                    (0, "puzzles/puzzle_warm_up.png", "The main rule here is, that you both need to agree with each other on your decisions.", 1.0)])

    demo.add_game("task", "puzzles/puzzle_warm_up.png", "Go ahead, and try to solve this puzzle. Remember, that you need to use all 7 pieces to form the shape.")
    demo.add_game("clue", "puzzles/sol_warm_up.png")


    tangram_rabbit = Story(session, "rabbit")
    tangram_rabbit.add_steps([
                                (0, "story/story_Tangram_creatures.png", "You both have done a great job! Let us get started with the real game. Now, we are going to do something a little different. I will tell you a story called Tangram Creatures.", 2.0),
                                (0, "story/story_two_rabbits.png", "This is a story of two Rabbits, called Lucas and Ema! ", 1.0),
                                (0, "story/story_two_rabbits_forest.png", "Although, Lucas and Ema were best friends they always try to fool with each other in playful competitions. One day, this rivalry almost brought their friendship to a tragic end.", 1.0),
                                (0, "", "They were sitting under their favorite tree, beside a river, talking about their magic powers. ", 2.0),
                                (3, "html/sounds/River.wav", 1.0),
                                (0, "story/story_commands.png", "If you need help you can say Pepper help and when you are done, please say pepper done, or if you need a break anytime during the session, say Pepper break. If you find the puzzle too hard and want to try another one, say Pepper change.", 1.0),
                                (0, "puzzles/puzzle_rabbit.png", "The main rule here is, that you both need to agree with each other on your decisions.", 1.0)])

    tangram_rabbit.add_game("task", "puzzles/puzzle_rabbit.png")
    tangram_rabbit.add_game("clue", "puzzles/sol_rabbit.png")
    tangram_rabbit.add_game("backup", ["puzzles/backup_rabbit.png", "puzzles/backup_sol_rabbit.png"])
    
    tangram_rabbit.add_funfact("Rabbits can hop and BOY can they also jump! In fact, rabbits can jump to impressive heights and distances.. a little over 3 feet high and a whopping 10 feet long!")
    tangram_rabbit.add_funfact("To express happiness, bunnies will sometimes jump around and flick their heads and feet. That adorable behavior is known within the rabbit community as a \"binky\".")
    tangram_rabbit.add_funfact("Like deer, a female rabbit is called a \"doe\" and a male rabbit is called a \"buck\".")
    tangram_rabbit.add_funfact("Bunny's ears aren't just for listening! They also help regulate body temperatures and they can also be rotated almost a full circle to 270 degrees.")

    tangram_fox = Story(session, "fox")
    tangram_fox.add_steps([
                            (0, "story/story_two_rabbits.png", "Let's continue the story. As you remember, the two Rabbits, Lucas and Ema, had magical powers and these powers allowed them to transform, from one creature to another instantaneously! Lucas said: I can change myself into a Fox as quick as a wink. I bet you can not do that! ", 1.0),
                            (0, "story/story_lucas_fox.png", " As a Fox, I can chase you, since I will have strong legs and I will be fast and smart! ", 1.0),
                            (0, "story/story_lucas_transformation", "Anyways, actions speak louder than words! And Lucas changed himself into a Fox!", 0.0),
                            (3, "html/sounds/Transformation.wav", 1.0),
                            (0, "story/story_challenge_fox.png", "Now, there is another challenge for you", 1.0),
#                            (0, "story/story_commands.png", "If you need help you can say Pepper help and when you are done, please say pepper done, or if you need a break anytime during the session, say Pepper break. If you find the puzzle too hard and want to try another one, say Pepper change.", 1.0),
                            (2, "fox_puzzle.png", 1.0)])
    tangram_fox.add_game("task", "puzzles/puzzle_fox.png")
    tangram_fox.add_game("clue", "puzzles/sol_fox.png")
    tangram_fox.add_game("backup", ["puzzles/backup_fox.png", "puzzles/backup_sol_fox.png"])
    
    tangram_fox.add_funfact("Foxes, have long, bushy tails, and narrow faces. Have you seen a fox before?")
    tangram_fox.add_funfact("You know what, foxes have a lot in common with cats")
    tangram_fox.add_funfact("A thing about Foxes is that, they are active at night.")
    tangram_fox.add_funfact("Do you know that, foxes can run thirty miles per hour?")
    
    tangram_goose = Story(session, "goose")
    tangram_goose.add_steps([   (1, "Fantastic! Now we continue our story. ", 1.0),
                                (0, "story/story_lucas_chasing_ema.png", "Remember, Lucas has already changed himself into a Fox and started chasing Emma. Lucas not only looked like a Fox, but also felt and acted like a Fox! baring his teeth and lashed his tail saying... I love rabbits! I am going to get you, and gobble you up! And then Lucas, the Fox, started chasing Ema who was a Rabbit! As Lucas got closer and closer! Ema's eyes grew bigger and bigger! She was too frightened to move at first but then, she started running fast, towards a lake!", 1.0),
                                (0, "story/story_ema_goose.png", "While running, Ema thought it would be better if she could change herself into a goose, in order to escape through the water, because foxes are very scared of going into the water! Then, Ema transformed herself into a goose.", 0.0),
                                (2, "story/story_ema_to_goose.png", 0.0),
                                (3, "html/sounds/Transformation.wav", 1.0),
                                (1, "She splashed through water and smoothly swam into the lake! ", 2.0),
                                (0, "story/story_challenge_goose.png", "Let us move on to the next challenge in this story.", 2.0),
                                (0, "story/story_commands.png", "If you need help you can say Pepper help and when you are done, please say pepper done, or if you need a break anytime during the session, say Pepper break. If you find the puzzle too hard and want to try another one, say Pepper change.", 1.0),
                                (0, "puzzles/puzzle_goose.png", "The main rule here is, that you both need to agree with each other on your decisions.", 1.0)])
    tangram_goose.add_game("task", "puzzles/puzzle_goose.png")
    tangram_goose.add_game("clue", "puzzles/sol_goose.png")
    tangram_goose.add_game("backup", ["puzzles/backup_goose.png", "puzzles/backup_sol_goose.png"])
    
    tangram_goose.add_funfact("You know what, Geese are a social bird that likes to be part of a group.")
    tangram_goose.add_funfact("Do you know that there are around 30 species of geese, around the world")
    tangram_goose.add_funfact("An interesting thing about geese is that, they like to swim and spend a lot of time in the water.")
    tangram_goose.add_funfact("You know what, Geese are active during the day.")
    
    tangram_hunter = Story(session, "hunter")
    tangram_hunter.add_steps([
                            (1, "Marvelous. You have completed the third puzzle. Now, let's move on with the story.", 1.0),
                            (0, "story/story_goose_flying.png", "As you remember, Ema had escaped from Lucas and transformed herself into a goose. Suddenly, she heard other geese, spread her wings and took to the air to reach them!", 0.0),
                            (3, "html/sounds/goose.wav", 1.0),
                            (0, "story/story_flying_after", "While seeing Ema flying, Lucas felt sad and thought: why did we play this game? as he might not see Ema again! Soon after, Lucas turned himself into a goose, to reach Ema as soon as possible. Moments later, Lucas was flying after Ema saying: I am tired of our game, come back with me to our tree.", 2.0),
                            (0, "story/story_hunter.png", "But, before Ema could answer, she suddenly felt something passing near her right wing. It was a hunter, trying to shoot them. She was scared and started flying down to the forest, to hide from the hunter. Lucas, immediately followed her.", 2.0),
#                            (0, "story/story_commands.png", "If you need help you can say Pepper help and when you are done, please say pepper done, or if you need a break anytime during the session, say Pepper break. If you find the puzzle too hard and want to try another one, say Pepper change.", 1.0),
                            (2, "puzzles/puzzle_hunter.png", 0.0)])
    tangram_hunter.add_game("task", "puzzles/puzzle_hunter.png")
    tangram_hunter.add_game("clue", "puzzles/sol_hunter.png")
    tangram_hunter.add_game("backup", ["puzzles/backup_hunter.png", "puzzles/backup_sol_hunter.png"])
         
    tangram_hunter.add_funfact("Humans began hunting around 3 million years ago, and it has remained a part of our civilization since then")
    tangram_hunter.add_funfact("When agriculture was introduced about 11,000 years ago, hunting became less important as people dedicated more time to cultivating crops")
    tangram_hunter.add_funfact("Hunting is still important for people who live in areas where farming is impossible or very difficult, such as rainforests in South America or jungles in Southeastern Asia")
    tangram_hunter.add_funfact("Hunting with firearms began in the 16th century")
    
#    tangram_lion = Story(session, "lion")
#    tangram_lion.add_steps([(0, "story/story_hunter_running", "Great job! We are now at the end of the story. By the time, they were on the ground, they saw the hunter running towards them! Ema shouted: Fly away Lucas! Save yourself! The hunter will kill us! I am too scared to fly! Lucas said: I won't leave you alone, with a mighty ROAR,", 0.0),
#                            (3, "html/sounds/roar.wav", 2.0),
#                            (0, "story/story_goose_transformation.png", "Lucas had changed himself into a big, and fierce Lion. ", 0.0),
#                            (3, "html/sounds/Transformation.wav", 1.0),
#                            (0, "puzzles/puzzle_lion.png", "Here is an optional challenge for you. Arrange the pieces to form a lion. If you wish to skip the puzzle, and continue listening to the story, please say \"Pepper story\"", 1.0)])
#    tangram_lion.add_game("task", "puzzles/puzzle_lion.png")
#    tangram_lion.add_game("clue", "puzzles/sol_lion.png")
#    tangram_lion.add_game("backup", ["puzzles/backup_lion.png", "puzzles/backup_sol_lion.png"])
    
#    tangram_lion.add_funfact("You know what, Lions run at a speed of, eighty one, kilometers per hour.")
#    tangram_lion.add_funfact("Lion is often known as the \"King of the jungle\".")
#    tangram_lion.add_funfact("Do you know that, male lion's roar can be heard up to eight kilometeres. ")
#    tangram_lion.add_funfact("Lions, are the second largest, big cat species, in the world. Have you seen a lion?")
    
    story_end = Story(session, "end")
    story_end.add_steps([
                        (0, "story/story_hunter_running.png", "Let me finish the story. By the time, they were on the ground, they saw the hunter running towards them! Ema shouted: Fly away Lucas! Save yourself! The hunter will kill us! I am too scared to fly! Lucas said: I won't leave you alone, with a mighty ROAR,", 1.0),
                        (3, "html/sounds/roar.wav", 2.0),
                        (0, "story/story_goose_transformation.png", "Lucas had changed himself into a big, and fierce Lion. ", 0.0),
                        (3, "html/sounds/Transformation.wav", 1.0),
                         (0, "story/story_lion_ROAR.png", "Before the hunter raised his weapon, Lucas jumped and knocked it from his hand. After that, the hunter fled, leaving the weapon behind.", 3.0),
                         (0, "story/story_end.jpg", " Lucas, and Ema returned to their natural rabbit shapes. And Lucas helped Ema to recover from the tragic experience.", 3.0),
                         (1, "Hope you enjoyed today's session. Thank you for coming!", 0.0)])
    
    stories = [welcome, demo, tangram_rabbit, tangram_fox, tangram_goose, tangram_hunter, story_end]
#    stories = []

    t0 = time.time()
    
    file = open("game_events_" + str(time.time()) + ".csv", "w")
    file.write("timestamp,event\n")

    for story in stories:
        file.write(str(time.time()-t0) + ",Starting Story: " + story.name + "\n")
        story.run(t0, file)
        
    file.close()
        
    raw_input()
    recorder.stopMicrophonesRecording()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                                            help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
            "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
