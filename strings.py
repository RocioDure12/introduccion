"""
PSEUDOCODIGO
Para <variable> <-valor inicial Hasta <valor final> Hacer
<bloque de intrucciones>
FinPara


"""
#Strings are arrays, we can loop through the characters in a string, with a for loop.
x = "banana"
for x in "banana":
    print (x)


#Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string
y="manzana"
print("parte cortada ",y[1])

#To get the lenght of  a string, use len() function

t="123456"
print(len(t))

#To check if a certain phrase or character is present in a string, we can use the Keyword in
texto="The best things in life are free"
print("free" in texto)

#return true o false
#Use it in am if statement
texto2="The life is beautiful is a blessing"
if "blessing" in texto2:
    print("yes, blessing is present")
else : print("Its not")

#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in
text3="The life is beautiful"
print("tree" not in text3)
