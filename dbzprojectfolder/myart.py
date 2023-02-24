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
    print("Goku: (grinning) Looks like we're evenly matched, Vegeta. We'll have to settle this in a fight someday.")

# Print the closing conversation
print("Vegeta: (smiling) You're on, Kakarot. Let's see who really is the strongest Saiyan!")
print("Goku: (laughing) alright, show me what you got Vegeta.") 

import random

# Set initial health points for both Goku and Vegeta
goku_health = 100
vegeta_health = 100

print( "the fight begins" ) 
print( """ 

Goku and Vegeta face each other, fists clenched, ready for battle.

Goku: "Vegeta, I never thought I'd have to fight you again."

Vegeta: "The feeling is mutual, Kakarot. But our destinies have always been intertwined."

Goku: "Let's settle this once and for all. Are you ready?"

Vegeta: "I was born ready, Kakarot."

They charge at each other, their fists colliding with a loud clash. They exchange blows, moving so fast that their movements are almost a blur. Goku lands a powerful punch to Vegeta's stomach, but Vegeta retaliates with a kick to Goku's face.

Goku: "Not bad, Vegeta. But you'll have to do better than that."

Vegeta: "You underestimate me, Kakarot."

Vegeta charges up a powerful energy blast and fires it at Goku, who narrowly dodges it.

Goku: "You've gotten stronger, Vegeta."

Vegeta: "Don't patronize me, Kakarot. I am the Prince of all Saiyans."

""" )

# Define list of attack names and corresponding damage values
attacks = [
    {"goku": "Kamehameha", "damage": 20},
    {"vegeta": "Galick Gun", "damage": 18},
    {"goku": "Spirit Bomb", "damage": 25},
    {"vegeta": "Final Flash", "damage": 22}
]

# Define a function for choosing a random attack from the list
def choose_attack():
    return random.choice(attacks)

# Define a loop for the fight
while goku_health > 0 and vegeta_health > 0:
    # Print current health points for both fighters
    print("Goku's health: ", goku_health)
    print("Vegeta's health: ", vegeta_health)
    
    # Goku attacks Vegeta
    attack = choose_attack()
    print("Goku uses","kamehameha", "and deals","20", "damage!")
    print(" vegeta health =-20") 
    # Check if Vegeta is still alive
    if vegeta_health <= 0:
        print("Vegeta is defeated!")
        break
    
    # Vegeta attacks Goku
    attack = choose_attack()
    print("Vegeta uses","Galick Gun", "and deals","18", "damage!")
    goku_health -= attack["82"]
    
    # Check if Goku is still alive
    if goku_health <= 0:
        print("Goku is defeated!")
        break
       
import random

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
def combat_round(attacker, defender):
    # Choose a random move for the attacker
    move, damage = random.choice(list(attacker.items()))

    # Apply the damage to the defender
    defender_power = max(0, defender_power - damage)

    # Print the result of the round
    print(f"{attacker} used {move}! {defender} took {damage} damage.")

    # Check if the defender has been defeated
    if defender_power == 0:
        print(f"{defender} has been defeated!")
        return True
    else:
        return False

# Main combat loop
while True:
    # Determine the order of attack
    if random.random() < 0.5:
        attacker = "Goku"
        defender = "Vegeta"
        moves = goku_moves
    else:
        attacker = "Vegeta"
        defender = "Goku"
        moves = vegeta_moves

    # Simulate a round of combat
    if combat_round(attacker, defender):
        # Defender has been defeated, end the combat
        print(f"{attacker} is victorious!")
        break

    # Swap the roles of the fighters for the next round
    attacker, defender = defender, attacker

# Print final health points for both fighters
print("Final health points:")
print("Goku's health: ", goku_health)
print("Vegeta's health: ", vegeta_health)

