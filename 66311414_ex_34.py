word1 = input().lower().replace("," , " ").replace("." , " ").split()
missword = input().lower()

print("Spoiler detected!" if missword in word1 else "No spoiler.")




#testcase1
# word1 = input().split()
# missword = input()

# if word1.count(missword):
#     print("Spoiler detected!")
# else :
#     print("No spoiler.")

#testcase2
# if word1 not in missword : 
#     print("No spoiler.")
# else :
#     print("Spoiler detected!")