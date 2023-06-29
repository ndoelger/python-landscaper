stats = {
    "days": 0,
    "money": 0,
    "tools": ["teeth"]
}

shop = {
    "scissors": 5,
    "oldLM": 25,
    "fancyLM": 250,
    "students": 500
}


while stats["money"] < 1000 or "students" not in stats["tools"]:
    print("*********************")
    choice = input("Cut the grass with your " + stats["tools"][len(stats["tools"]) - 1] + "? (y/n) ")
    
    if stats["tools"][len(stats["tools"]) - 1] == "teeth":
        stats["days"] = stats["days"] + 1
        stats["money"] = stats["money"] + 1
        print("Day " + str(stats["days"]) + ": You have $" + str(stats["money"]))
        if stats["money"] >= shop["scissors"]:
            buy = input("You have enough money to buy the scissors. Buy? (y/n) ")
            if buy == "y":
                stats["tools"].append("scissors")
  
    if stats["tools"][len(stats["tools"]) - 1] == "scissors":
        stats["days"] = stats["days"] + 1
        stats["money"] = stats["money"] + 5
        print("Day " + str(stats["days"]) + ": You have $" + str(stats["money"]))
        if stats["money"] >= shop["oldLM"]:
            buy = input("You have enough money to buy the old lawnmower. Buy? (y/n) ")
            if buy == "y":
                stats["tools"].append("oldLM")
  
    if stats["tools"][len(stats["tools"]) - 1] == "oldLM":
        stats["days"] = stats["days"] + 1
        stats["money"] = stats["money"] + 50
        print("Day " + str(stats["days"]) + ": You have $" + str(stats["money"]))
        if stats["money"] >= shop["fancyLM"]:
            buy = input("You have enough money to buy the fancy lawnmower. Buy? (y/n) ")
            if buy == "y":
                stats["tools"].append("fancyLM")
   
    if stats["tools"][len(stats["tools"]) - 1] == "fancyLM":
        stats["days"] = stats["days"] + 1
        stats["money"] = stats["money"] + 100
        print("Day " + str(stats["days"]) + ": You have $" + str(stats["money"]))
        if stats["money"] >= shop["students"]:
            buy = input("You have enough money to buy the students. Buy? (y/n) ")
            if buy == "y":
                stats["tools"].append("students")
    
    if stats["tools"][len(stats["tools"]) - 1] == "students":
        stats["days"] = stats["days"] + 1
        stats["money"] = stats["money"] + 250
        print("Day " + str(stats["days"]) + ": You have $" + str(stats["money"]))

print("You win!")


# def shop(item):
#     buy = input("You have enough money to buy the " + item + " . Buy? (y/n) ")
#     if buy == "y":
#         stats["tools"].append("scissors")
#         shop.pop(shop[0])

    # elif stats["tools"][len(stats["tools"]) - 1] == "scissors":
    #     stats["days"] = stats["days"] + 1
    #     stats["money"] = stats["money"] + 5
    # elif stats["tools"][len(stats["tools"]) - 1] == "oldLM":
    #     stats["days"] = stats["days"] + 1
    #     stats["money"] = stats["money"] + 50
    # elif stats["tools"][len(stats["tools"]) - 1] == "fancyLM":
    #     stats["days"] = stats["days"] + 1
    #     stats["money"] = stats["money"] + 100
    # elif stats["tools"][len(stats["tools"]) - 1] == "students":
    #     stats["days"] = stats["days"] + 1
    #     stats["money"] = stats["money"] + 250

    # choice = input("Visit the shop or continue cutting? (shop/cutting) ")

    # while choice == "shop":
    #     purchase = input("What do you want to buy? " + str(shop))
    #     if purchase == "quit":
    #         break
    #     if stats["money"] >= shop[purchase]:
    #         stats["tools"].append(purchase)
    #         break
    #     elif stats["money"] < shop[purchase]:
    #         print("Not enough funds :(")
