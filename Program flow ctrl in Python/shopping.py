shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#    if item != "spam":
#        print("Buy " + item)

# continue skipp the rest of the code in the for loop and start on the next iteration.
for item in shopping_list:
    if item == "spam":
        continue

    print("Buy " + item)
# break stopp the loop and finish. 
for item in shopping_list:
    if item == "spam":
        break

    print("Buy " + item)

