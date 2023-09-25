# Lambda to check every element is an integer or string
list1 = [1, "Welcome", 482, "world", 1203]

check = lambda x: "Integer" if isinstance(x, int) else "String"
result = list(map(check, list1))

print(result)
