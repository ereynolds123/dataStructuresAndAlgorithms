"""The difference between a list and a dictionary is that a list is an ordered sequence of objects. A dictionary on the other
hand is unordered and uses key pairs to index.  A dictionary would be used to index key pairs of usually strings.
Dictionaries allow you to map to various key pairs. Dictionaries are highly optimized."""

#Create a list of books
bookList =["Harry Potter", "Little Women", "Varney's Midwifery", "Catfight"]

#Search the list for a specific book
if "Harry Potter" in bookList:
    print("Harry Potter found")


#Create a dictionary
def main():
    studentGPA ={"Sweeny Todd": 4, "Tyler Banks": 3, "Stewart Strapp": 2}

    if studentGPA.get("Sweeny Todd"):
        print("Data exists")
        
main()