import random

debug = False
# база данных о сыщиках
data_igs = {
    "id01": {"Name": "Akachi Onyele", "Set": "Core", "Type": "Gate Closer"},
    "id02": {"Name": "Charlie Kane", "Set": "Core", "Type": "Support"},
    "id03": {"Name": "Diana Stanley", "Set": "Core", "Type": "Magic"},
    "id04": {"Name": "Jacqueline Fine", "Set": "Core", "Type": "Magic"},
    "id05": {"Name": "Jim Culver", "Set": "Core", "Type": "Magic"},
    "id06": {"Name": "Leo Anderson", "Set": "Core", "Type": "All-Rounder"},
    "id07": {"Name": "Lily Chen", "Set": "Core", "Type": "Combat"},
    "id08": {"Name": "Lola Hayes", "Set": "Core", "Type": "All-Rounder"},
    "id09": {"Name": "Mark Harrigan", "Set": "Core", "Type": "Combat"},
    "id10": {"Name": "Norman Withers", "Set": "Core", "Type": "Gate Closer"},
    "id11": {"Name": "Silas Marsh", "Set": "Core", "Type": "All-Rounder"},
    "id12": {"Name": "Charlie Kane", "Set": "Core", "Type": "Support"}
}
if debug:
    print(data_igs)

# база данных о древних
data_ans = {
    "id01": {"Name": "Abhoth", "Set": "Under the Pyramids", "Type": "slow"},
    "id02": {"Name": "Antediluvium", "Set": "Masks of Nyarlathotep", "Type": "fast"},
    "id03": {"Name": "Atlach-Nacha", "Set": "The Dreamlands", "Type": "fast"},
    "id04": {"Name": "Azathoth", "Set": "Core", "Type": "slow"},
    "id05": {"Name": "Cthulhu", "Set": "Core", "Type": "slow"},
    "id06": {"Name": "Elder Things", "Set": "Mountains of Madness", "Type": "board"},
    "id07": {"Name": "Hastur", "Set": "Signs of Carcosa", "Type": "fast"},
    "id08": {"Name": "Hypnos", "Set": "The Dreamlands", "Type": "board"},
    "id09": {"Name": "Ithaqua", "Set": "Mountains of Madness", "Type": "slow"},
    "id10": {"Name": "Nephren-Ka", "Set": "Under the Pyramids", "Type": "board"},
    "id11": {"Name": "Nyarlathotep", "Set": "Masks of Nyarlathotep", "Type": "fast"},
    "id12": {"Name": "Shub-Niggurath", "Set": "Core", "Type": "slow"},
    "id13": {"Name": "Shudde M'ell", "Set": "Cities in Ruin", "Type": "fast"},
    "id14": {"Name": "Syzygy", "Set": "Strange Remnants", "Type": "fast"},
    "id15": {"Name": "Yig", "Set": "Forsaken Lore", "Type": "fast"},
    "id16": {"Name": "Yog-Sothoth", "Set": "Core", "Type": "slow"}
}

if debug:
    print(data_ans)

actual_data_ans = dict()
for ancient in data_ans:
    if data_ans[ancient]["Set"] in ["Core"]:
        actual_data_ans.update({ancient: data_ans[ancient]})

if debug:
    print(actual_data_ans)

random.seed()

print(f"Welcome to Silver Key.\nEternal Danger is coming.\n")
j = actual_data_ans[random.sample(actual_data_ans.keys(),1)[0]]["Name"]
print(f"Great Ancient One {j} wants to defeat mankind\n")

igs_numbers = int(input("How many investigators will stand against the Ancient One?\n"))

igs_team = random.sample(data_igs.keys(), igs_numbers)

for j in range(0,igs_numbers):
    print(f"Investigator № {j+1}", data_igs[igs_team[j]]["Name"])


