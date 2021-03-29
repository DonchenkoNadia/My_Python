company = {
    "Bob" : ["Dima", "Jack", "Ludwig"],
    "Dima" : ["Igor", "Tatiana", "Nikita"],
    "Nikita" : ["Sasha", "Andrey", "Vova"],
    "Igor" : ["Nadia", "Ruslan"],
    "Nadia" : ["Zheniya", "Andy"],
    "Jack" : [],
    "Ludwig" : [],
    "Tatiana": [],
    "Sasha": [],
    "Andrey": [],
    "Vova": [],
    "Ruslan": [],
    "Zheniya": [],
    "Andy": []
}
#for the beginning I want to count how many people each boss has in team
"""
def how_big_team(company, boss, my_lst):
    for empl in company[boss]:
        my_lst.append(empl)
        my_lst.append(how_big_team(company, empl, my_lst))
    return my_lst
my_lst = []
print(how_big_team(company, "Igor", my_lst))

boss = "Igor"
my_lst = [empl for empl in company[boss]]
print(my_lst)
"""
def reports(company, boss):
  res = 0
  for empl in company[boss]:
    res += 1 + reports(company, empl)
  return res
print(reports(company, "Igor"))
p = {}
if print(p.get("igor")) == None:
    print ("No milk today")
