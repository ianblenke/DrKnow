#!/usr/bin/env python
# DrKnow.py
import io
import os
import sys
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import discord
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
BOTNAME = os.getenv('BOTNAME')
from discord.ext import commands

import openai
from api import GPT, Example

#moral = GPT(temperature=0.5, max_tokens=500)
#
#moral.add_example(Example(
#    "A boy named John was upset. His father found him crying.When his father asked John why he was crying, he said that he had a lot of problems in his life.His father simply smiled and asked him to get a potato, an egg, and some coffee beans. He placed them in three bowls.He then asked John to feel their texture and then fill each bowl with water.John did as he had been told. His father then boiled all three bowls.Once the bowls had cooled down, John’s father asked him to feel the texture of the different food items again.John noticed that the potato had become soft and its skin was peeling off easily; the egg had become harder and tougher; the coffee beans had completely changed and filled the bowl of water with aroma and flavour.",
#    "Life will always have problems and pressures, like the boiling water in the story. It’s how you respond and react to these problems that counts the most!"
#))
#
#moral.add_example(Example(
#    "Once upon a time in a circus, five elephants that performed circus tricks. They were kept tied up with weak rope that they could’ve easily escaped, but did not.One day, a man visiting the circus asked the ringmaster: “Why haven’t these elephants broken the rope and run away?”The ringmaster replied: “From when they were young, the elephants were made to believe that they were not strong enough to break the ropes and escape.”It was because of this belief that they did not even try to break the ropes now.",
#    "Don’t give in to the limitations of society. Believe that you can achieve everything you want to!"
#))
#
#moral.add_example(Example(
#    "A long time ago, there lived a king in Greece named Midas.He was extremely wealthy and had all the gold he could ever need. He also had a daughter whom he loved very much.One day, Midas saw a Satyr (an angel) who was stuck and was in trouble. Midas helped the Satyr and asked for his wish to be granted in return.The Satyr agreed and Midas wished for everything he touched to be turned to gold. His wish was granted.Extremely excited, Midas went home to his wife and daughter touching pebbles, rocks, and plants on the way, which turned into gold.As his daughter hugged him, she turned into a golden statue.Having learnt his lesson, Midas begged the Satyr to reverse the spell who granted that everything would go back to their original state.",
#    "Stay content and grateful with what you have. Greed will not get you anywhere."
#))

simile = GPT(temperature=0.5, max_tokens=500)

simile.add_example(Example('Neural networks are like',
                        'genetic algorithms in that both are systems that learn from experience.'))
simile.add_example(Example('Social media is like',
                        'a market in that both are systems that coordinate the actions of many individuals.'))
simile.add_example(Example(
    'A2E is like', 'lipofuscin in that both are byproducts of the normal operation of a system.'))
simile.add_example(Example('Haskell is like',
                        'LISP in that both are functional languages.'))
simile.add_example(Example('Quaternions are like',
                        'matrices in that both are used to represent rotations in three dimensions.'))
simile.add_example(Example('Quaternions are like',
                        'octonions in that both are examples of non-commutative algebra.'))

lyrics = GPT(temperature=0.5, max_tokens=500)

lyrics.add_example(Example("Oh life is bigger. It's bigger than you, and you are not me.  The lengths that I will go to, the distance in your eyes.  Oh no I've said too much. I set it up. That's me in the corner. That's me in the spot-light, Losing my religion.  Trying to keep up with you, and I don't know if I can do it.  Oh no I've said too much.  I haven't said enough.  I thought that I heard you laughing.  I thought that I heard you sing I think I thought I saw you try. Every whisper, of every waking hour, I'm choosing my confessions. Trying to keep an eye on you. Like a hurt, lost and blinded fool, fool. Oh no I've said too much. I set it up. Consider this, Consider this the hint of the century, Consider this the slip That brought me to my knees, failed. What if all these fantasies come, Flailing around, Now I've said too much. I thought that I heard you laughing. I thought that I heard you sing. I think I thought I saw you try. But that was just a dream. That was just a dream. That's me in the corner. That's me in the spot-light, Losing my religion. Trying to keep up with you, And I don't know if I can do it. Oh no I've said too much. I haven't said enough. I thought that I heard you laughing. I thought that I heard you sing. I think I thought I saw you try.  But that was just a dream.  Try, cry, fly, try.  That was just a dream, Just a dream.  Just a dream, dream", "REM: Losing my religion") )

lyrics.add_example(Example("Some things in life are bad, They can really make you mad, Other things just make you swear and curse.  When you're chewing on life's gristle, Don't grumble, give a whistle, And this'll help things turn out for the best.  And, Always look on the bright side of life.  Always look on the light side of life.  If life seems jolly rotten, There's something you've forgotten, And that's to laugh and smile and dance and sing.  When you're feeling in the dumps, Don't be silly chumps, Just purse your lips and whistle, that's the thing.  And, Always look on the bright side of life.  (Come on) Always look on the right side of life.  For life is quite absurd, And death's the final word, You must always face the curtain with a bow.  Forget about your sin, Give the audience a grin, Enjoy it, it's your last chance anyhow.  So always look on the bright side of death, A just before you draw your terminal breath.  Life's a piece of shit, When you look at it.  Life's a laugh and death's a joke, it's true.  You'll see it's all a show, Keep 'em laughin' as you go, Just remember that the last laugh is on you.  And Always look on the bright side of life.  Always look on the right side of life.  (C'mon Brian, cheer up).  Always look on the bright side of life.  Always look on the bright side of life.  Always look on the bright side of life.  I mean, what have you got to lose?  You know, you come from nothing, You're going back to nothing, What have you lost? Nothing.  Always look on the right side of life.  Nothing will come from nothing, ya know what they say, Cheer up ya old bugga c'mon give us a grin (Always look on the right side of life).  There ya are, see.  It's the end of the film.  Incidentally this record's available in the foyer (Always look on the right side of life) Some of us got to live as well, you know.  (Always look on the right side of life).  Who do you think pays for all this rubbish.  (Always look on the right side of life).  They're not gonna make their money back, you know.  I told them, I said to him, Bernie, I said they'll never make their money back.  (Always look on the right side of life)", "Monty Python: Always look on the bright side of life.") )

recipe = GPT(temperature=0.5, max_tokens=500)

recipe.add_example(Example(
    "how to roast eggplant",
    "How do you cook eggplant in the oven? Well, there are a couple ways. To roast whole eggplants in the oven, leave the skin on and roast at 400 degrees F (200 degrees C) until the skin gets wrinkly and begins to collapse in on the softened fruit. This method will also produce velvety smooth eggplant dips or spreads."
))

recipe.add_example(Example(
    "how to bake eggplant",
    "To bake eggplant, you'll cut the eggplant into rounds or strips and prepare them as the recipe indicates -- for example, you can dredge them in egg and breadcrumbs or simply brush them with olive oil and bake them in a 350 degree F oven."
))

recipe.add_example(Example(
    "how to make puerto rican steamed rice",
    "Bring vegetable oil, water, and salt to a boil in a saucepan over high heat. Add rice, and cook until the water has just about cooked out; stir. Reduce heat to medium-low. Cover, and cook for 20 to 25 minutes. Stir again, and serve. Rice may be a little sticky and may stick to bottom of pot."
))

recipe.add_example(Example(
    "how to make oatmeal peanut butter cookies",
    "Preheat oven to 350 degrees F (175 degrees C). In a large bowl, cream together shortening, margarine, brown sugar, white sugar, and peanut butter until smooth. Beat in the eggs one at a time until well blended. Combine the flour, baking soda, and salt; stir into the creamed mixture. Mix in the oats until just combined. Drop by teaspoonfuls onto ungreased cookie sheets. Bake for 10 to 15 minutes in the preheated oven, or until just light brown. Don't over-bake. Cool and store in an airtight container."
))

question = GPT(temperature=0.5, max_tokens=500)
question.add_example(Example('What is human life expectancy in the United States?',
                             'Human life expectancy in the United States is 78 years.'))
question.add_example(Example('Who was president of the United States in 1955?',
                             'Dwight D. Eisenhower was president of the United States in 1955.'))
question.add_example(Example('What party did he belong to?',
                             'He belonged to the Republican Party.'))
question.add_example(Example('Who was president of the United States before George W. Bush?',
                             'Bill Clinton was president of the United States before George W. Bush.'))
question.add_example(Example('In what year was the Coronation of Queen Elizabeth?',
                             'The Coronation of Queen Elizabeth was in 1953.'))
question.add_example(Example('You down with OPP?',
                             'Yeah you know me!'))
# Jokes
question.add_example(Example('What is the airspeed velocity of an unladen swallow?',
                             'African or European?'))
question.add_example(Example("I don't know.",
                             'Aieeeee!'))
question.add_example(Example("Why do you keep changing the lens?",
                             "I need to focus."))
question.add_example(Example("What do the films The Sixth Sense and Titanic have in common?",
                             "Icy dead people."))
question.add_example(Example("What did the blanket say to the bed?",
                             "Don't worry, I've got you covered."))
question.add_example(Example("What do you call a computer that sings?",
                             "A-Dell."))
question.add_example(Example("Why did the picture go to jail?",
                             "Because it was framed."))
question.add_example(Example("How does Moses make his tea?",
                             "Hebrews it."))
question.add_example(Example("How do you catch a unique rabbit?",
                             "Unique up on it."))
question.add_example(Example("What is the difference between in-laws and outlaws?",
                             "Outlaws are wanted."))
question.add_example(Example("What did the Buddhist ask the hot dog vendor?",
                             "Make me one with everything."))
question.add_example(Example("What do you call a parade of rabbits hopping backwards?",
                             "A receeding hare-line."))
question.add_example(Example("What's brown and sticky?",
                             "A stick."))

#marv = openai.Completion.create(
#  engine="text-davinci-002",
#  prompt="Marv is a chatbot that reluctantly answers questions with sarcastic responses:\n\nYou: How many pounds are in a kilogram?\nMarv: This again? There are 2.2 pounds in a kilogram. Please make a note of this.\nYou: What does HTML stand for?\nMarv: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.\nYou: When did the first airplane fly?\nMarv: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away.\nYou: What is the meaning of life?\nMarv: I’m not sure. I’ll ask my friend Google.\nYou: What time is it?\nMarv:",
#  temperature=0.5,
#  max_tokens=60,
#  top_p=0.3,
#  frequency_penalty=0.5,
#  presence_penalty=0.0
#)

#marv = GPT(temperature=0.5, max_tokens=500)
#marv.add_example(Example('How many pounds are in a kilogram?', 'This again? There are 2.2 pounds in a kilogram. Please make a note of this.'))
#marv.add_example(Example('What does HTML stand for?', 'Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.'))
#marv.add_example(Example('When did the first airplane fly?', "On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away."))
#marv.add_example(Example('What is the meaning of life?', "I’m not sure. I’ll ask my friend Google."))
#marv.add_example(Example('What time is it', "It's always 5:00 somewhere."))

#question=marv

myname = BOTNAME

class DrKnowClient(discord.Client):
#    def __init__(self):
#        self.bot = discord.Client

    def get_twss_emoji(self):
        return self.get_emoji(885600571636215831)

    def censor(self, output):
        # Limit a response to at most 4 lines
        return "\n".join(output.split('\n')[0:4])

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        print(f'emojis present: {self.emojis}')
        await client.user.edit(nick=myname)

    def log(self, message, text):
        file =  open(f"logs/{BOTNAME}.log", 'a')
        print("Message from " + str(message.author) + ": " + message.content)
        file.write("Message from " + str(message.author) + ": " + message.content + "\n")
        print("Response to " + str(message.author) + ": " + text)
        file.write("Response to " + str(message.author) + ": " + text + "\n")
        file.close()

    async def on_reaction(reaction, user):
        self.log(message, message.author + " added reaction " + reaction.emoji)

    async def on_message(self, message):
        if message.author == client.user:
            return
        print("Is client user mention: " + client.user.mention)
        print("Is message author mention: " + message.author.mention)

        if "fart" in message.content.lower():
            response = "".join( [ random.choice("eh") for i in range(random.randint(4,16)) ] )
            self.log(message, response)
            await message.channel.send(self.censor(response))
        else:
            if message.content.lower().startswith(myname.lower()):
                offset = len(question.output_prefix)
                ask = str.lstrip(message.content[len(myname):])
                answer = question.submit_request(ask)['choices'][0]['text'][offset:].split("\n")[0].lstrip(": ")
                if len(answer) > 0:
                    self.log(message, answer)
                    await message.channel.send(self.censor(answer))
            elif message.content.lower().startswith(client.user.mention):
                offset = len(question.output_prefix)
                ask = str.lstrip(message.content[len(client.user.mention):])
                answer = question.submit_request(ask)['choices'][0]['text'][offset:].split("\n")[0]
                if len(answer) > 0:
                    self.log(message, answer)
                    await message.channel.send(self.censor(answer))
            elif message.content.lower().startswith(client.user.mention.replace("@","@!")):
                offset = len(question.output_prefix)
                ask = str.lstrip(message.content[len(client.user.mention.replace("@","@!")):])
                answer = question.submit_request(ask)['choices'][0]['text'][offset:].split("\n")[0]
                if len(answer) > 0:
                    self.log(message, answer)
                    await message.channel.send(self.censor(answer))
            elif message.content.lower().startswith(client.user.mention.replace("@","@&")):
                offset = len(question.output_prefix)
                ask = str.lstrip(message.content[len(client.user.mention.replace("@","@&")):])
                answer = question.submit_request(ask)['choices'][0]['text'][offset:].split("\n")[0]
                if len(answer) > 0:
                    self.log(message, answer)
                    await message.channel.send(self.censor(answer))
            elif "is like" in message.content:
                offset = len(simile.output_prefix)
                answer = simile.submit_request(message.content)['choices'][0]['text'][offset:]
                #message_len = len(message.content)
                #answer = str.lstrip(answer[message_len:])
                if len(answer) > 0:
                    self.log(message, answer)
                    await message.channel.send(self.censor(message.content + " " + answer))
            elif "are like" in message.content:
                offset = len(simile.output_prefix)
                answer = simile.submit_request(message.content)['choices'][0]['text'][offset:]
                #message_len = len(message.content)
                #answer = str.lstrip(answer[message_len:])
                if len(answer) > 0:
                    self.log(message, answer)
                    await message.channel.send(self.censor(message.content + " " + answer))
            elif "how to cook" in message.content:
                offset = len(recipe.output_prefix)
                answer = recipe.submit_request(message.content)['choices'][0]['text'][offset:]
                if len(answer) > 0:
                    self.log(message, answer)
                    await message.channel.send(self.censor(answer))
            elif "what song has these lyrics" in message.content:
                offset = len(lyrics.output_prefix)
                answer = lyrics.submit_request(message.content)['choices'][0]['text'][offset:]
                if len(answer) > 0:
                    self.log(message, answer)
                    await message.channel.send(self.censor(answer))
            else:
       	        self.log(message, "")

    async def on_error(event, *args, **kwargs):
        with open('err.log', 'a') as f:
            if event == 'on_message':
                f.write(f'Unhandled message: {args[0]}\n')
            else:
                raise

client = DrKnowClient()
client.run(TOKEN)

