# change python syntax and define functions
import tokenize
from io import BytesIO
import tkinter
from tkinter import * 
import turtle
import matplotlib

tur = turtle

window = tkinter




def process_code(file):
    keys = {

        "log":"print",
        "ask": "input",
        "define":"def",
        "convertInt":"int",
        "convertStr":"str",
        "else if":"elif",
        "//":"#",
        "get":"import",
        "size":"len",
        "f":"format",
        "x=":"!=",
        "delete":"del",
        "with_name":"as"
        
        
        

    }
  
    def __init__():
       pass
    def add(num1, num2):
        x = num1+num2
        return x
    def window(title):
        window.Tk()
        window.title(title)
        window.mainloop()
        return 
        
    def subtract(num1, num2):
        yx = num1-num2
        return yx
    def multiply(num1, num2):
        xy = num1*num2
        return xy
    def divide(num1, num2):
        xyx = num1/num2
        return xyx
    def artboard(color):
        tur.turtle = turtle.Turtle()
        tur.turtle.color(color)
        return
    def artColor(color):
        tur.turtle.color(color)
        return
    def artLeft(amount):
        tur.turtle.left(amount)
        return
    def artRight(amount):
        tur.turtle.right(amount)
        return
    def artForward(amount):
        tur.turtle.forward(amount)
        return
    def artBackward(amount):
        tur.turtle.backward(amount)
        return
    def artClose():
        tur.turtle.exitonclick()
        return
    def artSpeed(speed):
        tur.turtle.speed(speed)
        return
    def artColor(color):
        tur.turtle.color(color)
        return
    def artKey(function, key):
        tur.turtle.onkey(function, key)
        return
    def artStatic(feature):
        if feature == "stamp":
            tur.turtle.stamp()
        elif feature == "dot":
            tur.turtle.dot()
    def ForeverRun():
        while True:
            pass
    def chart(datasetx, datasety):
        pass
    def windowTitle(title):
        window.title(title)
        return
    
    


    custom_features = {
       
    }

    with open(file, "rb") as source:
        tokens = []
        for token in tokenize.tokenize(source.readline):
            if token.string in keys:
                t = (token.type, keys[token.string])
            elif token.string in custom_features:
                t = (token.type, token.string)
            else:
                t = (token.type, token.string)
            tokens.append(t)

    code = tokenize.untokenize(tokens).decode("utf-8")
    exec(code)

    for feature_name, feature_func in custom_features.items():
        if feature_name in globals():
            feature_func()


print("VisualScipt\nEnter a filename or exit to exit")
if __name__ == "__main__":
    while True:
        filename = input(">>> ")
        if filename.lower() == 'exit':
            break
        try:
            process_code(filename)
        except Exception as e:
            if len(filename) < 1:
                pass
            else:
                print(f"An error occurred: {e}")
  