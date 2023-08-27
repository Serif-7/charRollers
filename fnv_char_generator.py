#!/usr/bin/env python3
import random

# total points available to allocate
TOTAL_POINTS = 33

SPECIAL = {
    'Strength': 1,
    'Perception': 1,
    'Endurance': 1,
    'Charisma': 1,
    'Intelligence': 1,
    'Agility': 1,
    'Luck': 1
}

TAG_SKILLS = [
    'Barter',
    'Energy Weapons',
    'Explosives',
    'Guns',
    'Lockpick',
    'Medicine',
    'Melee Weapons',
    'Repair',
    'Science',
    'Sneak',
    'Speech',
    'Survival',
    'Unarmed'
]

TRAITS = [
    'Built to Destroy',
    'Fast Shot',
    'Four Eyes',
    'Good Natured',
    'Heavy Handed',
    'Kamikaze',
    'Loose Cannon',
    'Small Frame',
    'Trigger Discipline',
    'Wild Wasteland',
    'Claustrophobia',
    'Early Bird',
    'Hoarder',
    'Hot Blooded',
    'Logan\'s loophole',
    'Skilled',
    'None'
]

random.seed()

traits = [random.choice(TRAITS)]
while True:
    t2 = random.choice(TRAITS)
    if t2 != traits[0]:
        traits.append(t2)
        break

special = SPECIAL.copy()

i = TOTAL_POINTS
while i > 0:
    stat = random.choice(list(SPECIAL.keys()))
    special[stat] += 1
    i -= 1

tags = [random.choice(TAG_SKILLS)]
while True:
    tag2 = random.choice(TAG_SKILLS)
    if tag2 != tags[0]:
        tags.append(tag2)
        break
while True:
    tag3 = random.choice(TAG_SKILLS)
    if tag3 != tags[0] and tag3 != tags[1]:
        tags.append(tag3)
        break

print('SPECIAL:')
print(special)
print('TAG SKILLS;')
print(tags)
print('TRAITS:')
print(traits)
