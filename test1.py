
power = [3,2,1]
result = 0
for i in range(1, len(power)):
    if power[i] < power[i-1]:
        base = power[i-1] - power[i]
        result += base
        for i in range(i, len(power)):
            power[i] = power[i] + base

print(result)
# result = 0
# carry = 0
# for i in range(1, len(power)):
#     if power[i] + carry < power[i-1]:
#         base = (power[i-1] + carry) - power[i]
#         print("Base is ",base, power[i])
#         carry = base
#         result += base
#         power[i] = power[i] + base
#         print("1carry is ",carry)
#         print(power)
#     else:
#         power[i] += carry
#         print("2carry is ",carry)
#         print(power)

# print(result)





