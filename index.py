# import the python datetime module to help us create a timestamp

from walking import Cow, Donkey, Goat, Llama, Sheep
from swimming import Duck, Frog, Goldfish, Goose, Trout
from slithering import Cobra, Copperhead, LeglessLizard, Python, Worm


# bertha = Cow("Bertha", "cow", "midday")
# print(
#     f"{bertha.name} the {bertha.species} is available to pet during the {bertha.shift} shift"
# )

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow")

miss_fuzz.feed()

daisy = Donkey("Daisy", "donkey", "evening", "hay")

print(daisy)

fang = Cobra("Fang", "snake", "rats")

print(fang)
