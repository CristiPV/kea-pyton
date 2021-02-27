# Assignment 1
print( "\nAssignment 1\n" )

board_of_directors = { "Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren" }
management = { "Tine", "Trunte", "Rane" }
employees = { "Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars" }

# Who in the board of directors is not an employee?

answer = board_of_directors - employees
print( f"Who in the board of directors is not an employee?\n{answer}" )

# Who in the board of directors is also an employee?

answer = board_of_directors & employees
print( f"Who in the board of directors is also an employee?\n{answer}" )

# How many of the management is also member of the board?

answer = len( management & board_of_directors )
print( f"How many of the management is also member of the board?\n{answer}" )

# All members of the managent also an employee

answer = management & employees
print( f"All members of the managent also an employee\n{answer}" )

# All members of the management also in the board?

answer = management & board_of_directors
print( f"All members of the management also in the board?\n{answer}" )

# Who is an employee, member of the management, and a member of the board?

answer = employees & management & board_of_directors
print( f"Who is an employee, member of the management, and a member of the board?\n{answer}" )

# Who of the employee is neither a memeber or the board or management?

answer = employees - management - board_of_directors
print( f"Who of the employee is neither a memeber or the board or management?\n{answer}" )

# Assignment 2
print( "\nAssignment 2\n" )

dictionary = {
    "a": "Alpha",
    "b": "Beta",
    "g": "Gamma"
}
print( f"Dictionary: {dictionary}" )

list_of_tuples = list(dictionary.items())
print( f"List of tuples: {list_of_tuples}" )

# Assignment 3
print( "\nAssignment 3\n" )

set1 = { "a", "e", "i", "o", "u", "y" }
set2 = { "a", "e", "i", "o", "u", "y", "æ", "ø", "å" }
print( f"Sets we will be working with: \nSet1: {set1}\nSet2: {set2}" )

union = set1 | set2
print( f"Union of set1 and set2: {union}" )

symetric_difference = set1 ^ set2
print( f"Symetric Difference of set1 and set2: {symetric_difference}" )

difference = set1 - set2
print( f"Difference of set1 and set2: {difference}" )

is_disjoint = set1.isdisjoint(set2)
print( f"Are the sets disjoint: {is_disjoint}" )

intersection = set1 & set2
print( f"The common elements in between the sets: {intersection}" )

# Assignment 4
print( "\nAssignment 4\n" )

date_dict = {}
#I am using more dates, just for testing purposes
date1 = "8-MAR-85"
date2 = "29-DEC-00"
date3 = "10-WAT-23"

#Decodes a date in the format dd-MMM-yy to a tuple in the format ( y, m, d )
def decode_date( date ):
    month_dict = {
        "JAN": 1, 
        "FEB": 2, 
        "MAR": 3, 
        "APR": 4, 
        "MAY": 5, 
        "JUN": 6, 
        "JUL": 7, 
        "AUG": 8, 
        "SEP": 9, 
        "OCT": 10, 
        "NOV": 11, 
        "DEC": 12
    }
    #Split the date
    split_date = date.split( "-" )

    #Translating the months
    month_number = month_dict.get(split_date[1], "Month not found")
    
    #Translating the year
    #If the given year digits are anything than "00" we add a 19 prefix (example: "85" -> 1985)
    #If the given digits are "00" we add 20 as a prefix (example: "00" -> 2000)
    if split_date[2] == "00":
        year_number = 2000
    else:
        year_number = int( "19" + split_date[2] )

    translated_date = (year_number, month_number, int(split_date[0]))
    return translated_date

date_dict[date1] = decode_date(date1)
date_dict[date2] = decode_date(date2)
date_dict[date3] = decode_date(date3)

print( f"Decoded dates in dictionary: {date_dict}" )
