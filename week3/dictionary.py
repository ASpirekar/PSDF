thisdict={
    "myname":"Tayyab",
    "programming":"python",
    "subjects":["Database","Networking","Algorithm"],
    "tupitems":("Laptop","mobile"),
    "myname":"Usama",
    "subject":{
        "computer":56,
        "Math":34,
        "English":64,
        "Physics":45
    }

}
"""thisdict["myname"]="Hamza"
thisdict["newkey"]="keypair"
print(thisdict["tupitems"])
print(thisdict["programming"])
print(thisdict["subjects"])
print(thisdict["myname"])
print(thisdict["newkey"])

 print(thisdict["subject"]["computer"])"""
# print(len(thisdict.keys()))
# print(len(list(thisdict.keys())))
# print(list(thisdict.values()))


# pairs=thisdict.items()
#print(pairs[0])
# print(thisdict.items())
print(thisdict.get("subject1"))
print(thisdict["programming"])
thisdict.update({"City":"Faisalabad"})
print(thisdict)
newdict={"city1":"Lahore"}
thisdict.update(newdict)
print(thisdict)
mydict=dict(city="Faisalabad", country="Pakistan")
print(mydict)
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
print(marks)"""