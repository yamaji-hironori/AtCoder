Members, NumRelation = map(int, input().split())
Relations = [[int(_) - 1 for _ in input().split()] for i in range(NumRelation)]

max_faction = 1

for factions_assumed in range(2**Members):
    faction = set()

    for i_legislator in range(Members):
        if not factions_assumed & (1 << i_legislator):
            continue
        
        for i_faction in faction:
            if [i_faction, i_legislator] in Relations:
                continue
            else:
                break
        else:
            faction.add(i_legislator)
    
    max_faction = max(max_faction, len(faction))

print(max_faction)