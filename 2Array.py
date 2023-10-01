#Create a 2x3 array
fruits = [["Banana", "Apple", "Orange"],["Cherry", "Kiwi", "Peach"]]


#Example of 1 dimensional array

for row in fruits:
    for fruits in row:
        print(f"|{fruits}", end="")
    print("|")    

#Create a 3x4 array of your favorite hobbies of sports.
#Use a for loop to display the values or items you have.
#Screen shot the code and output and paste it in our teams chatbox.

print("+++++++++++++++++++++++++++++++++++++++")
hobbies = ["Soccer", "Volleyball", "Darts", "Games"], ["Basketball", "Singing", "Running", "Sleeping"], ["Video Games","Playing Instruments","Napping", "Eating"]

for row2 in hobbies:
    for hobbies in row2:
        print (f"|{hobbies}", end="")
    
    print("|")
    
#Store new
fruits[1][2] = str("guava")
print(fruits)