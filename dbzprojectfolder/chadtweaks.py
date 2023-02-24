# Define Goku and Vegeta's power levels
goku_power_level = 9000
vegeta_power_level = 8000

# Print the starting conversation
print("Goku: Hey Vegeta, have you ever wondered who's stronger?")

print("Vegeta: (smirks) Don't tell me you're finally ready to admit that I'm the strongest Saiyan.")
     
# Compare power levels and determine who is stronger
if goku_power_level > vegeta_power_level:
    print("Goku: Actually, I think I might be stronger. My power level is", goku_power_level, "compared to your", vegeta_power_level)
elif vegeta_power_level > goku_power_level:
    print("Vegeta: (laughing) Don't make me laugh, Kakarot. My power level is", vegeta_power_level, "compared to your measly", goku_power_level)
else:
    print("Goku: (grinning) Looks like we're evenly matched, Vegeta. We'll have to settle this in a fight, last one standing wins.")

# Print the closing conversation
print("Vegeta: (smiling) You're on, Kakarot. Let's see who really is the strongest Saiyan!")
print("Goku: (laughing) alright, show me what you got Vegeta.") 

print( "the fight begins" ) 
print( """ 

Goku and Vegeta face each other, fists clenched, ready for battle.

Goku: "Vegeta, I never thought I'd have to fight you again."

Vegeta: "The feeling is mutual, Kakarot. But our destinies have always been intertwined."

Goku: "Let's settle this once and for all. Are you ready?"

Vegeta: "I was born ready, Kakarot."

They charge at each other, their fists colliding with a loud clash. They exchange blows, moving so fast that their movements are almost a blur. 
Goku lands a powerful punch to Vegeta's stomach, but Vegeta retaliates with a kick to Goku's face.

Goku: "Not bad, Vegeta. But you'll have to do better than that."

Vegeta: "You underestimate me, Kakarot."

Vegeta charges up a powerful energy blast and fires it at Goku, who narrowly dodges it.

Goku: "You've gotten stronger, Vegeta."

Vegeta: "Don't patronize me, Kakarot. I am the Prince of all Saiyans."
""" )

round = 0
import random
# Set initial power levels
goku_health = 100
vegeta_health = 100

# Define the moves available to each fighter
goku_moves = {
    "Punch": 20,
    "Kick": 30,
    "Kamehameha": 50
             }

vegeta_moves = {
    "Punch": 20,
    "Kick": 30,
    "Galick Gun": 50
               }

# Define a function to simulate a round of combat
def combat_round(attacker= "goku", defender= "vegita"):
    # Choose a random move for the attacker
    punch=20
    kick=30
    kamehameha=50

while True:
    print("You determine the winner of the match, what should goku do next?")
    answer = input (">")
    if answer=="punch".lower():
        print("vegeta takes 20 point damage")
        vegeta_health -= 20
    if answer=="kick".lower():
        print("vegeta takes 30 point damage")
        vegeta_health -= 30
    if answer=="kamehameha".lower():
        print("vegeta takes 50 point damage")
    # Print the result of the round
        print("goku" used {kamehameha}! {vegeta} took {50} damage.")

    # Check if the defender has been defeated
    if vegeta_health <= 0:
        print("Vegeta has been defeated!")


# Main combat loop
while True:
    # Determine the order of attack
    if random.random() < 0.9:
        attacker = "Goku"
        defender = "Vegeta"
        moves = goku_moves
    else:
        attacker = "Vegeta"
        defender = "Goku"
        moves = vegeta_moves
        break

    # Simulate a round of combat
while True:
    if ("goku"==attacker):
        print:(goku,kicks,vegita,sends,a,kameahameha,attack)
 
        # Defender has been defeated, end the combat
        print(f"{attacker} is victorious!")
        break

    # Swap the roles of the fighters for the next round
    attacker, defender = defender, attacker
while True:
    if (vegeta==attacker):
        print:(vegeta,kicks,goku,sends,a,galick,gun,attack)
        # Defender has been defeated, end of combat
        print(f"{vegeta} is victorious!")
        break

