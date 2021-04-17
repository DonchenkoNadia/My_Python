company = { "Bob" : ["Dima", "Magda", "Yeti"],
            "Dima": ["Igor", "Nikita"],
            "Igor": ["Nadia", "Ruslan"]
}

def how_big_team(company, boss):
    res = 0
    for empl in company.get(boss, []):
        res += 1 + how_big_team(company, empl)
    return res

#print(how_big_team(company, "Dima"))

#let us try now to print structure level by level

def bfs(company, node, level_num):

    if len(levels) == level_num:
        levels.append([])

    levels[level_num].append(node)

    for new_node in company.get(node, []):
        bfs(company, new_node, level_num + 1)

    return levels

levels = []
levels = bfs(company, "Bob", 0)
print(levels)

"""
levels = []
print(len(levels))
levels.append([])
print(len(levels))
levels[0] = "Bob"
print(levels)
"""
