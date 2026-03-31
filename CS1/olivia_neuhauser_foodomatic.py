import random                                                                                                                                                                    

mains = ["cauliflower","tilapia fillet","pork loin","salmon","potatoes","three color squash","eggplant","steak","baguette"]                                                      
prices = [20, 25, 28, 30, 18, 20, 22, 30, 20]                                                                                                                   
flairs = ["with balsamico","with garlic and olive oil","with minted yogurt","with chutney","with salad","with salsa","over sticky rice","au jus","with basmati rice"]
pflairs = [1, 1, 3, 3, 5, 2, 5, 0, 5]

meals = []

for m_index, main in enumerate(mains):
    for f_index, flair in enumerate(flairs):
        meals.append([main, flair, m_index, f_index])

while True:  
    try:
        items = int(input("How many menu items do you need? "))
    except ValueError:
        print('Enter an integer')
        continue
    if items > 81:
        print("There are not that many menu selections. Please enter a number equal to or less than eighty-one.")
        continue
    break

for item in range(items):
    meal = random.choice(meals)
    print(f"Item #{item+1}: {meal[0]} {meal[1]}, ${prices[meal[2]]} + ${pflairs[meal[3]]} = ${prices[meal[2]] + pflairs[meal[3]]}")
    meals.remove(meal)
    
