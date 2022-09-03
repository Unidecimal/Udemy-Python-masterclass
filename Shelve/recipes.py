import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open('recipes', writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans_on_toast"] = beans_on_toast
    # recipes["scrambled_eggs"] = scrambled_eggs
    # recipes["soup"] = soup
    # recipes["pasta"] = pasta

    # this ovious was dosen't work to update the shelve.
    # this is beackus preventing to much file access.
    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomata")

    # THE FIRST WAY TO APPEND
    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

    # THE SECOND WAY TO APPEND - with: Writeback=True
    # writeback is happening when the with statement closes.
    # If you have a lot of data the closing proces can take a while.
    # recipes["soup"].append("croutons")

    # the sync() is emptying the cach. that can be tricky
    # recipes["soup"] = soup
    # recipes.sync()
    # soup.append("cream")

    for snack in recipes:
        print(snack, recipes[snack])

""" shelve is not stable for all all things is pickled. and data from 
untrusted sources. or if the system is moved. Data Bases is often a better so"""