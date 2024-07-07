# # row_list = ['1','2','.','4','5']
# # row_set = set(row_list)

# # print(row_set)

# # second_row_list = list(row_set)
# # print(second_row_list)

# pattern = "abba"
# s = "dog cat cat dog"

# pat = {}
# for i in range(len(pattern)):
#     pat[pattern[i]] = str(i) if pattern[i] not in pat else pat[pattern[i]] + str(i)


# string = {}
# s_list = s.split(" ")
# print(s_list)
# for i in range(len(s_list)):  # Corrected loop to iterate over indices
#     string[s_list[i]] = str(i) if s_list[i] not in string else string[s_list[i]] + str(i)
# # for val in pat.values():
# #     print(val)

# # for val in string.values():
# #     print(val)

# for val1,val2 in zip(string.values(),pat.values()):
#     if val1!=val2:
#         print("False")
#         break
#     else:
#         print("True")


# pattern = "abba"
# s = "dog cat cat dog"

# s = s.split(" ")
# print(s)
# if len(s) != len(pattern):
#     print("False")

# map = {}
# seen = set()
# i = 0
# for word in pattern:
#     if i > len(s):
#         break
#     if word not in map:
#         map[word] = s[i]
#         seen.add(s[i])
    
#     if word in map and map[word] != s[i]:
#         print(False)
    
#     i+=1
        

# for key, val in map.items():
#     print(f'{key} :: {val}')
    

# print(True)

# s = "a good   example"
# s = s.strip()
# print(s)

# words = s.split(" ")
# print(words)

# words = words[::-1]
# print(words)

# s = " ".join(words)
# print(s)

# s = " ".join(s.split())
# print(s)

# reached = []

# reached.append(10)

# print(reached)



# z = 6%10 + 6%10 + 0
# print(z)
# if z>9:
#     carry = z - 10
# print(z//10)
# print(carry)
# string = "praful"
# sorted = ''.join(sorted(string))
# print(sorted)

nums = [1,2,3,4,5]

num = nums - nums[0]

print(num)