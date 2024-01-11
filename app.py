# to explain
from flask import Flask, render_template, request
# to explain
app = Flask(__name__)
# to explain
@app.route("/")
@app.route("/home")

# Index.html has to be in a "templates" folder!!!
def home():
    return render_template("index.html")
# to explain
@app.route("/result",methods = ['POST', 'GET'] )
# to explain
def result():
    output = request.form.to_dict()
    number = output["number"]
    return render_template("index.html", number = parse_to_roman(number))



# the FUNCTION
def parse_to_roman(number):
    # out of range cases, number has to be an integer
    is_letter_present = number.isdigit()
    if(is_letter_present == False): return "Please enter digits only."
    
    if(int(number) == 0): return ("Zero has not been discovered yet")
    if (int(number) > 3999): return ("out of Roman range...")

    # used symbols as lists for units, tenths, hundreds and thousands
    lists_of_symbols = [['I','V','X'],['X','L','C'],['C','D','M'],['M','M','M']]

    # applied number has to be reversed to start with units in all cases
    reversed_number_str = number[::-1]
    
    # applied number has to be set as a list of integers
    reversed_number_str_list = [*reversed_number_str]
    reversed_number_list = list(map(int, reversed_number_str_list))
    
    # list to fill with roman symbols
    list_to_join_and_reverse = []

    # when a single symbol has to be repeated like II or XXX
    def several_identical_symbols(symbol, repeats):
        several_list = []
        while (repeats > 0):
            several_list.append(symbol)
            repeats -= 1
        return (''.join(several_list))
    
    # loop through applied number
    # index must be set to loop through both number and symbols lists
    i = 0
    while i < len(reversed_number_list):
        # symbols applied for this loop
        symbols = lists_of_symbols[i]
        repeatable, fifth, sup = symbols[0], symbols[1], symbols[2]
        # the digit used fot this loop
        digit = reversed_number_list[i]

        if (digit == 9): list_to_join_and_reverse.append(repeatable + sup)
        if (digit == 4): list_to_join_and_reverse.append(repeatable + fifth)
        if (digit == 5): list_to_join_and_reverse.append(fifth)
        if (digit == 0): pass
        if (digit >= 1 and digit < 4): list_to_join_and_reverse.append(several_identical_symbols(repeatable, digit))
        if (digit >= 6 and digit < 9): list_to_join_and_reverse.append(fifth + several_identical_symbols(repeatable, digit - 5))

        # iteration of index
        i += 1
        
    list_to_join = list_to_join_and_reverse[::-1]
    list_to_display = ''.join(list_to_join)
    print (list_to_display)
    return list_to_display

#let's see the code
# with open(__file__) as sourcefile:
#     print(sourcefile.read())
#end of the html generation?
if __name__ == '__main__':
    app.run(host= "0.0.0.0", port=5000)

