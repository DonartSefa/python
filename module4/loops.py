# names = ["Erina","Blina","Uvejs","Milot","Donart"]
#
# for name in names:
#     print(name)
#
# sentence = "Hello Everyone"
#
# for char in sentence:
#     if char .isalpha():
#         print(char)
#
# for number in range(1,10):
#     print(number)
#
# numbers = [12,20,33,58,59,80,19,43]
# maximum = numbers[0]
#
# for number in numbers:
#     if number > maximum:
#         maximum = number
#
# print('The maximum value in this array was: ',maximum)

#While Loop

# count = 1
#
# while count <=5:
#     print("The number is", count)
#     count+=1
#
# #break
#
# numbers = [1,2,3,4,5,6,7,8]
#
# target = 4
#
# for number in numbers:
#     if number == target:
#         print("Target found")
#         break
#
# #continue
#
# scores = [32,52,75,89,34,23,85,99]
#
# total = 0
# count = 0
#
# mesatarja = 0
#
# for score in scores:
#     if score>50:
#
#         total += score
#         count +=1
#         continue
# mesatarja = total/count if count>0 else 0
#
# print("The averaage score for schores above 50 is : ",mesatarja)

#Do while

# while True:
#     user_input = input("Ente a positive nummber: ")
#
#     if user_input.isnumeric():
#         number = int(user_input)
#
#         if number > 0:
#             break
#
#     print("Input invalid try again.")
#
# print("You entered a positive number: ",number)

total = 0

for number in range(1,11):
    if number%2 == 0:
        total += number
print(total)