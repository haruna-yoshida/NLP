def 

words = [('ひまわり', 2), ('種', 4), ('植木鉢', 14), ('植木鉢', 23)]
nums = [('50', 6), ('6', 11), ('何', 25)]

for num in nums:
    print(num)
    for word in words:
        print(word[0], ':', abs(word[1] - num[1]))
        
    # print(min(word[1] - num[1]))
    print(min(words, key=))