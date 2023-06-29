stats = {
    "days": 0,
    "money": 5,
    "tools": ["teeth"]
}

shop = {
    "scissors": 5,
    "oldLM": 25,
    "fancyLM": 250,
    "students": 500
}

while stats["money"] < 1000 and "students" not in stats["tools"]:
    print("*********************")
    choice = input("What do you want to use to cut the grass? " + str(stats["tools"]) + " ")
    if choice == "teeth":
        stats["days"] = stats["days"] + 1
        stats["money"] = stats["money"] + 1
    if choice == "scissors":
        stats["days"] = stats["days"] + 1
        stats["money"] = stats["money"] + 5
    
    print("Day " + str(stats["days"]) + ": You have $" + str(stats["money"]))
    choice = input("Visit the shop or continue cutting? (shop/cutting) ")

    while choice == "shop":
        purchase = input("What do you want to buy? " + str(shop))
        if purchase == "quit":
            break
        if stats["money"] >= shop[purchase]:
            stats["tools"].append(purchase)
            break
        elif stats["money"] < shop[purchase]:
            print("Not enough funds :(")