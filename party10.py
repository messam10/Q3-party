people = []
x = 0
i = input("How many people the you wants to invite to a party?")
if int(i) > 10 :
    print("Too many people...")
    i = input("Chose Number less than 10: ")

while x+1 <= int(i):
    y = input("Enter name : ")
    people.append(y)
    x+=1

for x in range(len(people)):
    print("{:d} ) {:s} has been invited".format(x+1, people[x]))
