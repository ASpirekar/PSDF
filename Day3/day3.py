#Strings and display it on screen
print("Welome to my 1st-Repository")
#Assiging a string to a variable through double ""
str1="I am a string no.1"
print(str1) 
#Assigning a string with three double ""
lngstr= """Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
"Mauris sed semper sem, in egestas diam.Sed molestie ex sed magna interdum,
 sed mollis risus efficitur."""
print(lngstr)

#Assiging a string with single '''
sngstr='''This is signle qouets string assiging to a variable'''
#print(sngstr)
print(sngstr[15:21])
#printing string thorugh for loop
#for a in '''This is signle qouets string assiging to a variable''':
#print(a)
a='''This is signle qouets string assiging to a variable'''
#checking length of a string
print(len(a))
#checking string through in keyword
txt="The best things in life are free!"
#print("free" in txt)
#checking string though if keyword
txt1="The best things in life are free! eat mango"
if "mango" in txt1:
    print("Yes", 'mango',"is available")
print("Mango" not in txt1)
#print with value if it is not in string 
if "mango" not in txt:
    print("No'Mango' is not available")

#modifying string

print(txt1.upper())