# Function to read data from a file and return a list of tuples containing book information
def inputDatabase(filePath):
    try: 
        data = open(filePath, "r", encoding='utf-8')  # Open the file in read mode with utf-8 encoding <-- https://stackoverflow.com/questions/59422448/with-file-openr-encoding-utf-8-as-f-attributeerror-str-object-has-no-a
        dataBase = []  # Initialize an empty list to store book data

        # Iterate through each line in the file
        for entry in data:
            tempList = entry[:-1].split(',')  # Split the comma-separated values into a list
            title = tempList[0]
            author = tempList[1]
            userRating = float(tempList[2])
            review = int(tempList[3])
            price = float(tempList[4])
            publication_year = int(tempList[5])
            genre = tempList[6].lower()

            # Create a tuple with book information and append it to dataBase list
            tempTuple = (title, author, userRating, review, price, publication_year, genre)
            dataBase.append(tempTuple)

        data.close()  # Close the file
        return dataBase  # Return the list of book data
    except:
        print("ERROR: could not open file please try agian later")

# Function to print formatted book information
def printFormate(printData,count):
    if len(printData) == 0:
         print ("No entries found.")
    else: 
        title_width = max(len(entry[0]) for entry in printData)  # Find maximum title length
        author_width = max(len(entry[1]) for entry in printData)  # Find maximum author length

        # Print the header with dynamic width adjustment
        print(f"{'Title':<{title_width}} | {'Author':<{author_width}} | Publication Date | Rating")
        print("-" * (title_width + author_width + 6 + 18 + 8))  # Adjusted for dynamic widths

        # Print each book's information
        for entry in printData:
            print(f"{entry[0]:<{title_width}} | {entry[1]:<{author_width}} | {entry[5]}             | {entry[2]}")
            
        print(f"\n Number of books: {count}")


       
# Function to search for books by author
def searchByAuthor(dataBase, author):
    count = 0
    printData = []

    # Iterate through each book entry in the database
    for entry in dataBase:
        if author in entry[1].lower().split():  # Check if author name matches the input
            printData.append(entry)  # Add matching entry to printData list
            count += 1
    # Sort printData by titles alphabetically and print the results
    printData = sorted(printData, key=lambda x: x[0], reverse=False)
    printFormate(printData,count)
# Function to search for books by title
def searchByTitle(dataBase, title):
    count = 0
    printData = []

    # Iterate through each book entry in the database
    for entry in dataBase:
        if title in entry[0].lower().split():  # Check if title matches the input
            printData.append(entry)  # Add matching entry to printData list
            count += 1
    # Sort printData by titles alphabetically and print the results
    printData = sorted(printData, key=lambda x: x[0], reverse=False)
    printFormate(printData,count)

# Function to search for books within a specified year range
def searchByYearRange(dataBase, ageRange):
    count = 0
    printData = []

    # Iterate through each book entry in the database
    for entry in dataBase:
        if (ageRange[0] <= entry[5] <= ageRange[1]):  # Check if publication year is within the specified range
            printData.append(entry)  # Add matching entry to printData list
            count += 1
    # Sort printData by publication year and print the results
    printData = sorted(printData, key=lambda x: x[5], reverse=False)
    printFormate(printData,count)

# Function to search for books with a minimum rating
def searchByRating(dataBase, minRating):
    count = 0
    printData = []

    # Iterate through each book entry in the database
    for entry in dataBase:
        if (entry[2] >= minRating):  # Check if userRating is greater than or equal to the specified minimum rating
            printData.append(entry)  # Add matching entry to printData list
            count += 1
    # Sort printData by userRating and print the results
    printData = sorted(printData, key=lambda x: x[2], reverse=False)
    printFormate(printData,count)

# Main menu loop
quit = False
dataBase = inputDatabase("booklist.txt")  # Load data from file
while not quit:
    answersAccepted = ['1', '2', '3', '4', '5', 'Q']

    print("""
    
    
                *****MENU*****
        1 Enter year range
        2 Enter minimum rating
        3 Search for author
        4 Search for title
        Q Quit
        
        
        """)

    userinput = input()
    userinput = userinput.upper()

    if userinput in answersAccepted:
        if userinput == '1':
            ageRange = int(input("Please enter Min Year: ")), int(input("Please enter Max Year: "))
            searchByYearRange(dataBase, ageRange)
        elif userinput == '2':
            flag = False
            while not flag:
                minRating = float(input("Please enter Min Rating (0.0-5.0): "))
                if (0.0 <= minRating <= 5.0):
                    flag = True
                    searchByRating(dataBase, minRating)
        elif userinput == '3':
            author = input("Search by author: ")
            searchByAuthor(dataBase, author.lower())
        elif userinput == '4':
            title = input("Search by title: ")
            searchByTitle(dataBase, title.lower())
        elif userinput == 'Q':
            quit = True  # Set quit flag to exit the loop
