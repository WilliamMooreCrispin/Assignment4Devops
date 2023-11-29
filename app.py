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
        ("File could not be read, Please try agian later")

# Function to print formatted book information
def printFormate(printData):
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
       
# Main menu loop
dataBase = inputDatabase("booklist.txt")  # Load data from file
printFormate(dataBase)