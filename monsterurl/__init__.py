import os.path
import random
from string import capwords

ROOT = os.path.abspath(os.path.dirname(__file__))
ASSETS = os.path.join(ROOT, 'assets')
ADJECTIVES = os.path.join(ASSETS, 'adjectives')
MONSTERS = os.path.join(ASSETS, 'monsters')
ANIMALS = os.path.join(ASSETS, 'animals')

def get_monster(monster = False):
    with open(ADJECTIVES) as f:
        adjectives = f.read().splitlines()
    with open(MONSTERS) as f:
        monsters = f.read().splitlines()
    with open(ANIMALS) as f:
        animals = f.read().splitlines()
    adjective_1 = capwords(random.choice(adjectives))
    adjective_2 = capwords(random.choice(adjectives))
    if monster:
        creature = random.choice(monsters)
    else:
        creature = random.choice(animals)
    return "%s%s%s" % (adjective_1, adjective_2, creature)

