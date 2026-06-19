# Assignmemnt for dictionary
"""details={
    "table":("A furniture item","List of facts and figures"),
    "cat":"A type of animal"
}"""

# print(details["table"])


# WAP that enter marks of three subjects from the student and add into dictionary 
"""
marks={}
x=int(input("Enter physics marks:"))
marks.update({"Phy":x})
x=int(input("Enter Computer marks:"))
marks.update({"Comp":x})
x=int(input("Enter Math marks:"))
marks.update({"Math":x})
print(marks)
set1={1,2,3,"Urdu","english","english"}
set2=set()

print(set1)
print(type(set2))"""
#set methods 1. add method
"""set2.add("cook")
set2.add(1.5)
set2.add(28)
set2.add((1,4.5,6))
# 1. remove method
set2.remove((1,4.5,6))"""
# 1. clear method
# set2.clear()
# print(len(set2))
# 1. pop method
# print(set2.pop())
# print(set2.pop())


# union and intersection methods
"""set_1={1,2,4}
set_2={1,3,2,4,}
print(set_1.union(set_2))
print(set_1.intersection(set_2))"""

# set assignment subjects wise room allocation 
# classroms={"python","java","c++","python",
# "javascript","java","python","java","c++","c"
# }
# print(len(classroms))

#assginment of stroing values 9 , 9.0 in the set as seperate values. 
# values={9,"9.0"} method 1
# values={"9",9.0} method 2
values={
    ("float",9),
    ("int",9.0)
}
print(values)