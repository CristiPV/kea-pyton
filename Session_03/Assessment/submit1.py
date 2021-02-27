#1  Model an organisation of employees, management and board of directors in 3 sets.

#Board of directors: Benny, Hans, Tine, Mille, Torben, Troels, Søren
#Management: Tine, Trunte, Rane
#Employees: Niels, Anna, Tine, Ole, Trunte, Bent, Rane, Allan, Stine, Claus, James, Lars



Board = {"Benny", "Hans", "Tine","Mille","Torben","Troels", "Søren"}
Management = {"Tine", "Trunte", "Rane"}
Employees = {"Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"}


#who in the board of directors is not an employee? Benny, Hans, Mille, Torben, Troels og Søren
print(Board.difference(Employees))

#who in the board of directors is also an employee? Tine
print(Board.intersection(Employees))

#how many of the management is also member of the board? Tine
print(Management.intersection(Board))

#REVIEW line:20 - question states "How many", you answer with "Who"
#Could use len(Management.intersection(Board))

#All members of the managent also an employee
print(Management.intersection(Employees))

#All members of the management also in the board? Tine
print(Management.intersection(Board))

#Who is an employee, member of the management, and a member of the board? TIne
print(Employees.intersection(Management.intersection(Board)))

#Who of the employee is neither a memeber or the board or management? Niels, Anna, Ole, Bent, Allan, Stine, Claus, James og Lars
print(Employees.difference(Management,Board))

#2  Using a list comprehension create a list of tuples from the folowing datastructure
#{‘a’: ‘Alpha’, ‘b’ : ‘Beta’, ‘g’: ‘Gamma’}

myset = {'a' : 'Alpha',
            'b' : 'Beta',
            'g' : 'Gamma'}
lst = [x for x in myset.items()]

#REVIEW line:41 - Indentation/formatting is not quite right
#Could do either myset = {'a': 'Alpha', 'b': 'Beta', 'g': 'Gamma'}
#or
#myset = {
#   'a' : 'Alpha',
#   'b' : 'Beta',
#   'g' : 'Gamma'
# }
#Also, the data structure is a dictionary, not a set, therefore it would be more appropriate to name
#the variable something like "mydict" as opposed to "myset"

print(lst)



 
#3  From these 2 sets:
#{'a', 'e', 'i', 'o', 'u', 'y'}
#{'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

#Of the 2 sets create a Union
print(set1.union(set2))

#Of the 2 sets create a Symmetric Difference
print(set1.symmetric_difference(set2))

#Of the 2 sets create a Difference
print(set2.difference(set1))

#Of the 2 sets create a disjoint
print(set1.isdisjoint(set2))

#REVIEW line:78 - The comment is a bit confusing: you don't 'create' a disjoint,
#the method refers to whether the two sets are disjoint or not (have common elements or not)

#4 Date Decoder.
#A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.

#Create a dict suitable for decoding month names to numbers.

date_Decoder = {
    "date": 8,
    "month": "Mar",
    "year": 85
}

#Create a function which uses string operations to split the date into 3 items using the "-" character.
def myfunktion(date_Decoder):
    x1 = date_Decoder.get("date")
    x2 = date_Decoder.get("month")
    x3 = date_Decoder.get("year")
    print(x1,"-",x2,"-",x3) 
myfunktion(date_Decoder)

#Translate the month, correct the year to include all of the digits.

def month_converter(month):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months.index(month) + 1

print(date_Decoder["date"],'-', month_converter(date_Decoder["month"]),'-',date_Decoder["year"])

#The function will accept a date in the "dd-MMM-yy" format and respond with a tuple of ( y , m , d ).

#REVIEW line:89 - "date_decoder" is not decoding month names to numbers, as the preceding comment
#specifies. Your "months" list (line:106) should be turned in a dictionary that would do the decoding.
#Example: months = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8,  'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC':12}
#
#REVIEW line:96 - your function should recieve a string and use string functions on it to split it by the
#"-" separator. One way of doing it would be :
#
#def decode_date( date ):
#   split_date = date.split( "-" )
#
#Your function also does not return (it actually just prints) a tuple in the right format
#(d, -, m, -, y) as opposed to ( y, m, d ) as you mention in comment line:111
#
#REVIEW line:103 - You are not actually correcting the year to include all the digits as you mention
#in the comment. One way of doing this can be:
#
#   #Translating the year
#   #If the given year digits are anything than "00" we add a 19 prefix (example: "85" -> 1985)
#   #If the given digits are "00" we add 20 as a prefix (example: "00" -> 2000)
#   if split_date[2] == "00":
#       year_number = 2000
#   else:
#       year_number = int( "19" + split_date[2] )
#
#REVIEW line:111 - There is no function that takes in a date with that format and returns/prints 
#a tuple in the specified format
