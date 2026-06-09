#1st list creation with string values
li=["mango","cherry","apple","orange"]
print(li)

#list with integer values
integ=[12,11,23,22,20]
print(integ)

#list with mixed type values
mixed=["Ahmad",19,2.4,True]
print(mixed)


#Accessing Items from list
print(mixed[1:4])
print(mixed[-3:-5])

#Modifying Items in lists 
#change by index
animals=[1,"cat","Horse","Tiger","dog","bird"]
animals[1]=10

animals[4]="sparrow"

print(animals)


#Adding ItemsUse these essential methods to expand your list:
colors=[]
colors.append("yellow")
colors.append(10)
print(colors)
print(colors.append(4))


#insert method
colors.insert(0,"seegreen")
print(colors)

#extend method
colors.extend(animals)
print(colors)

#length of list checking
print(len(colors))

#Remove method in list by value
colors.remove(10)
print(colors)
print(colors.pop(4))