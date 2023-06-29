stats = {
    "days": 0,
    "money": 0,
    "tools": ["teeth"]
}

while stats["money"] < 1000 and "students" not in stats["tools"]:
    print("*********************")
    choice = input("What do you want to use to cut the grass? " + str(stats["tools"]) + " ")
    if choice == "teeth":
        stats["days"] = stats["days"] + 1
        stats["money"] = stats["money"] + 1
    
    print("Day " + str(stats["days"]) + ": You have $" + str(stats["money"]))
    choice = input("Visit the shop or continue cutting? (shop/cutting) ")
