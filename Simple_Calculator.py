#       
#             This GUI was made my Jacob Joseph Bejarano
#                  Contact: JacobJBejarano@gmail.com
#                         GitHub: JakeJayB
#          
#      LinkedIn: https://www.linkedin.com/in/jacob-j-bejarano-74347b230/
#          GitHub: https://github.com/JakeJayB?tab=repositories
#       
#
#                     Updated as of: May 21, 2022 
#               GUI is subject to change in later dates
#
#


##############################################################################################################################

# placeholder for the entire result of the calculation
result = 0

# Result Counter will prevent a calculation from happening when hitting an operand after hitting "="
# A calculation can resume after pushing another number
resultCounter = False

# Math is used to determine what type of calculation to use when hitting "=" and for finishCalculation()
# It is also used to determine whether to perform a calculation immediately when
# an operator function is called or to reset the math value to then resume calculation
math = ""

# Used to determine the end of an calculation. 
endCalculation = False

# after hitting "=", is used to determine which math function to calculate result  
resetCalculation = False

# used to determine which subtraction functionality to use
# (Ex: result - input, or result + input)
isResultNotZero = False

# used in the "else" statement in every operator function
# to stop the program from proceeding after dividing
# a result to 0
hasErrorOccured = False

# used to placehold the very last number in the input
# box after hitting "=". This will allow us to rerun the same
# calculation with a different result after hitting "=" again
latestNumberInBox = 0

# buttonAction is called when a number is hit
def buttonAction(number):
    global resultCounter
    global result
    global math
    global endCalculation
    global resetCalculation

    if hasErrorOccured == False:
        # if input box is 0, delete input box without saving value
        # or, if a number is pushed after 
        if inputBox.get() == "0" or resultCounter == True:
            inputBox.delete(0, END)
            resultCounter = False

        # After hitting a number after hitting "=": reset and end calculation
        if endCalculation == True and resetCalculation == True:
            Clear()

        # after hitting an operator, then a number after pressing "=": set resetCalculation to 
        # false so that finishCalculation() can be called
        elif endCalculation == False and resetCalculation == True:
            print("resetCalculation = false")
            resetCalculation = False

        current = inputBox.get()
        inputBox.delete(0, END)
        inputBox.insert(0, str(current) + str(number))
    

# These conditions are checked before computing a calculation
def checkBeforeCalculate():
    global resetCalculation
    global endCalculation
    global isResultNotZero
    global result

    # When pushing an operator after hitting "=", set endCalculation to False
    # to indicate the calculation processes hasn't ended yet
    if resetCalculation == True and endCalculation == True:
        endCalculation = False
    
    # if result is not zero: set subtractCount to True to ensure the  
    # appropriate subtraction functionality is used if ever called
    if isResultNotZero == False:
        #print("isResultNotZero = True")
        isResultNotZero = True


def buttonAdd():
    global endCalculation
    global resetCalculation
    global result
    global math

    print("Addiction called")
    checkBeforeCalculate()

    if math == "Addition" or math == "":
        if resultCounter == False:
            print("Addition: computation is called")
            number = int(inputBox.get())
            result += number
    elif resetCalculation == True:
        print("Addition: resetCalculation is called")
        pass
    else:
        print("Addition: else is called")
        finishCalculation()

        if hasErrorOccured == True:
            inputBox.delete(0, END)
            inputBox.insert(0, "Result is undefined (clear to restart)")
            Clear()
            return  

    math = "Addition"
    inputBox.delete(0, END)
    inputBox.insert(0, "0")


def buttonSubtract():
    global endCalculation
    global resetCalculation
    global isResultNotZero
    global result
    global math

    print("Subtraction called")
    checkBeforeCalculate()

    if math == "Subtraction" or math == "":         
        if resultCounter == False:
            print("Subtract: computation is called")
            number = int(inputBox.get())

            if isResultNotZero == True:
                result = result - number
            else:
                result += number
                isResultNotZero = True
    elif resetCalculation == True:
        print("Subtract: resertCalculation is called")
        pass
    else:
        print("Subtract: else is called")
        finishCalculation()

        if hasErrorOccured == True:
            inputBox.delete(0, END)
            inputBox.insert(0, "Result is undefined (clear to restart)")
            Clear()
            return  
    
    math = "Subtraction"
    inputBox.delete(0, END)
    inputBox.insert(0, "0")


def buttonMultiply():  
    global endCalculation
    global resetCalculation
    global result
    global math

    print("multiply called")
    checkBeforeCalculate()

    if math == "Multiplication" or math == "":
        if resultCounter == False:
            #print("Mutiply: computation is called")

            number = int(inputBox.get())
            if result != 0:
                result *= number
            else:
                result += number  
    elif resetCalculation == True:
        #print("Mutiply: resetCalculation is called")
        pass
    else:
        #print("Mutiply: else is called")
        finishCalculation()

        if hasErrorOccured == True:
            inputBox.delete(0, END)
            inputBox.insert(0, "Result is undefined (clear to restart)")
            Clear()
            return           

    math = "Multiplication" 
    inputBox.delete(0, END)
    inputBox.insert(0, "0")


def buttonDivide(): 
    global endCalculation
    global resetCalculation
    global result
    global math
    global hasErrorOccured

    #print("Division called")
    checkBeforeCalculate()

    if math == "Division" or math == "":
        if resultCounter == False:
            #print("Division: computation is called")
            try:
                number = int(inputBox.get())
                if result != 0:
                    result /= number
                else:
                    result += number
            except:
                hasErrorOccured = True
                inputBox.delete(0, END)
                inputBox.insert(0, "Result is undefined (Clear to restart)")
                Clear()
                return

    elif resetCalculation == True:
        #print("Division: resetCalculation is called")
        pass  
    else:
        #print("Division: else is called")
        finishCalculation()
        

    math = "Division"
    inputBox.delete(0, END)
    inputBox.insert(0, "0")


def finishCalculation():
    global result 
    global math
    global hasErrorOccured

    endNumber = float(inputBox.get())
    #print("Inside finishCalculation")
    
    if math == "Addition":
        result += endNumber
    elif math == "Subtraction":
        result -= endNumber
    elif math == "Multiplication":
        result *= endNumber
    elif math == "Division":
        try:
            result /= endNumber
        except:
            hasErrorOccured = True
            return
    else:
        return


def buttonEqual():
    global result
    global resultCounter
    global math
    global endCalculation
    global resetCalculation
    global latestNumberInBox
    global hasErrorOccured

    if endCalculation == False:
        latestNumberInBox = float(inputBox.get())
        checkBeforeCalculate()
    
    if math == "Addition":
        result += latestNumberInBox
    elif math == "Subtraction":
        result = result - latestNumberInBox
    elif math == "Multiplication":
        result *= latestNumberInBox
    elif math == "Division":
        try:
            result /= latestNumberInBox
        except:
            inputBox.delete(0, END)
            inputBox.insert(0, "Result is undefined (clear to restart)")
            hasErrorOccured = True
            Clear()
            return
    else:
        result = int(inputBox.get())
        

    inputBox.delete(0, END)
    inputBox.insert(0, result)
    endCalculation = True
    resetCalculation = True
    resultCounter = True


def Clear():
    #print("Program Reset")
    global result
    global math
    global endCalculation
    global resetCalculation
    global isResultNotZero
    global resultCounter
    global hasErrorOccured
    global latestNumberInBox

    endCalculation = False
    resetCalculation = False
    isResultNotZero = False
    hasErrorOccured = False
    resultCounter = False
    latestNumberInBox = 0
    result = 0
    math = ""


def buttonClear():
    inputBox.delete(0, END)
    inputBox.insert(0, "0")
    Clear()


#                                          End of calculator functionality...
##############################################################################################################################
#
#
#                           (Note:)
#       Everything down below is related to creating the GUI
#
#
#
from tkinter import *

root = Tk()
root.title("Simple Calculator")

inputBox = Entry(root, width=35, borderwidth=7)
inputBox.grid(row=0, column=0, columnspan=5, padx=10, pady=25)
inputBox.insert(0, "0")

button1 = Button(root, text="1", padx=32, pady=15, command=lambda: buttonAction(1))
button2 = Button(root, text="2", padx=32, pady=15, command=lambda: buttonAction(2))
button3 = Button(root, text="3", padx=32, pady=15, command=lambda: buttonAction(3))
button4 = Button(root, text="4", padx=32, pady=15, command=lambda: buttonAction(4))
button5 = Button(root, text="5", padx=32, pady=15, command=lambda: buttonAction(5))
button6 = Button(root, text="6", padx=32, pady=15, command=lambda: buttonAction(6))
button7 = Button(root, text="7", padx=32, pady=15, command=lambda: buttonAction(7))
button8 = Button(root, text="8", padx=32, pady=15, command=lambda: buttonAction(8))
button9 = Button(root, text="9", padx=32, pady=15, command=lambda: buttonAction(9))
button0 = Button(root, text="0", padx=71, pady=15, command=lambda: buttonAction(0))

buttonAddition = Button(root, text="+", padx=30, pady=15, command=buttonAdd)
buttonMulitplication = Button(root, text="X", padx=30, pady=15, command=buttonMultiply)
buttonDivision = Button(root, text="/", padx=31, pady=15, command=buttonDivide)
buttonSubtraction = Button(root, text="-", padx=31, pady=15, command=buttonSubtract)

clearButton = Button(root, text="C", padx=31, pady=15, command=buttonClear)
equalButton = Button(root, text="=", padx=22, pady=3, command=buttonEqual)

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button0.grid(row=4, column=0, columnspan=2)

buttonAddition.grid(row=4, column=3)
buttonSubtraction.grid(row=3, column=3)
buttonMulitplication.grid(row=2, column=3)
buttonDivision.grid(row=1, column=3)

equalButton.grid(row=0, column=3, rowspan=1, columnspan=2)
clearButton.grid(row=4, column=2)

root.mainloop()

