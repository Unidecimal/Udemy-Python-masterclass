lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "gray", "wise"]
teddy_list = ["cuddly", "stuffed", "googly eys"]

# this is more how the actual dict works in the background.
# that is why the shallow copy gets updated when the referenced list
# gets updated.
animals = {"lion": lion_list,
           "elephant": elephant_list,
           "teddy": teddy_list,
           }

# things = animals.copy()
things = {"lion": lion_list,
          "elephant": elephant_list,
          "teddy": teddy_list,
          }

print(things["teddy"])
print(animals["teddy"])

print("-" * 10)
# things["teddy"].append("toy")
teddy_list.append("toy")  # and this is actually what's happened.
animals["teddy"].append("added via `animals`")
things["teddy"].append("added via `things`")
print(things["teddy"])
print(animals["teddy"])
print(teddy_list)