from Simple_deep_coopy_challange import teacher_deepcopy
import copy

original = {
    "Tim": ["Bulchalka", ["Programmer", "Teacher"]],
    "J-P": ["Roberts", ["Programmer", "Teacher"]],
}

copy_1 = copy.deepcopy(original)
copy_2 = teacher_deepcopy(original)

original["Tim"].append("Australia")
original["J-P"].append("UK")
original["Tim"][1].append("Cashier")
jp_list = original["J-P"]
jp_list[1].append("Courier")

print("The original: ", original)
print("Deep........: ", copy_1)
print("Teacher deep: ", copy_2)
