# change python syntax and define functions
import tokenize
from io import BytesIO
import tkinter
from tkinter import * 
import turtle
import matplotlib.pyplot as plt
import sys
from statistics import *
from flask import *
import webbrowser

tur = turtle

window = tkinter




def process_code(file):
    keys = {

        "log":"print",
        "ask": "input",
        "convertInt":"int",
        "convertStr":"str",
        "else if":"elif",
        "//":"#",
        "get":"import",
        "size":"len",
        "f":"format",
        "x=":"!=",
        "delete":"del",
        "with_name":"as",
        "function":"def",
        "toLowerCase":"lower",
        "toUpperCase":"upper",
        "firstLetterUpper":"title",
        "skip":"pass"
        
        
        
        

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
        screen = turtle.Screen()
        screen.title("VisualScript Art Window")
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
        tur.turtle.listen()
        return
    def artStatic(feature):
        if feature == "stamp":
            tur.turtle.stamp()
        elif feature == "dot":
            tur.turtle.dot()
    def ForeverRun():
        while True:
            pass
    def chartLine(datasetx, datasety, ytitle, xtitle):
        plt.plot(datasetx, datasety)
        plt.ylabel(ytitle)
        plt.xlabel(xtitle)
        plt.show()
    def chartDot(datasetx, datasety, ytitle, xtitle):
        plt.scatter(datasetx, datasety)
        plt.xlabel(xtitle)
        plt.ylabel(ytitle)
    def chartScatter(datasetx, datasety, xtitle, ytitle):
        timesx = len(datasetx)
        for i in range(timesx):
            plt.scatter(datasetx[i], datasety[i])
        plt.xlabel(xtitle)
        plt.ylabel(ytitle)
        plt.show
    def chartTheme(theme):
        plt.style(theme)
        return
    def windowTitle(title):
        window.title(title)
        return
    def ArtBoardTitle(name):
        screen = turtle.Screen()
        screen.title(name)
        return
    
    def ChartShow():
        plt.show()
        return
    def logf(value, formatedvalue):
        print(value+"{}".format(formatedvalue))
        return
    def returnMedian(list, chart):
        sortedlist = sorted(list) 
        middle_value = len(sortedlist) // 2
        final = (sortedlist[middle_value] + sortedlist[~middle_value]) / 2 
        if chart.lower() == 'y':
            plt.scatter(final, final)
            plt.show()
        else:
            pass
        return final
    def exit():
        sys.exit()
    def returnMode(list):
        sortedlist = sorted(list)
        avg = mode(sortedlist)
        return avg
    def returnMean(list):
        sortedlist = sorted(list)
        meannum = sum(sortedlist) / len(sortedlist)
        return meannum
    def webPageStatic(title="", header="", cssfile=None, filename="index.html", content="", contentt="", contenttr="", contentb="", contenth="", contentcb="", cb="0"):
        filenamecustom = filename
        structure = f"""
        <!DOCTOTYPE html>
        <html>
        <head>
            <title>{title}</title>
            <link rel="stylesheet" type="text/css/scss" href="{cssfile}">
        </head>
        <body>
            <h1>{header}</h1>
            <p>{content}</p>
            <p>{contentt}</p>
            <p>{contenttr}</p>
            <p>{contentb}</p>
            <p>{contenth}</p>
            <p>{contentcb}</p>
        </body>
        </html>
        """

        with open(filename, "w") as html:
            html.write(structure)
        webbrowser.open(filename)
    def webPage(filename):
        structure = f"""
        <!DOCTOTYPE html>
        <html>
        <head>
        """
        with open(filename, "a") as html:
            html.write(structure)
    def webPageTitle(filename, titleCB):
        structure = f"""
        \n<title>{titleCB}</title>\n
        """
        with open(filename, "a") as html:
            html.write(structure)
    def webPageStyles(filename, cssfile=None):
        structure = f"""
        \n<link rel="stylesheet" type="text/css/scss" href="{cssfile}">\n
        """
        with open(filename, "a") as html:
            html.write(structure)
    def webPageBody(filename):
        structure = f"""
        </head>
        <body>
        """
        with open(filename, "a") as html:
            html.write(structure)
    def webPageHeader(filename, headerCB):
        structure = f"""
        \n<h1>{headerCB}</h1>\n
        """
        with open(filename, "a") as html:
            html.write(structure)
    def webPageContent(filename, contentCB):
        structure = f"""
        \n<p>{filename}</p>\n
        """
        with open(filename, "a") as html:
            html.write(structure)
    def webPageContacts(filename, infoCB):
        structure = f"""
        \n<address>{infoCB}</address>\n
        """
        with open(filename, "a") as html:
            html.write(structure)
    def webPageLinks(filename, link, textCB):
        structure = """
        \n <a href={link}>{textCB}</a>\n
        """
        with open(filename, "a") as html:
            html.write(structure)
    def webPageSound(filename, soundfileCB):
        structure = """
          <audio>
             <source src={soundfileCB} type="audio/mpeg">
          </audio>
        """
        with open(filename, "a") as html:
            html.write(structure)
    def webPageBGsound(filename, soundfileCB):
        structure = f"""
        \n<bgsound src={soundfileCB}/>\n
        """
        with open(filename, "a") as html:
            html.write(structure)
    def webPageBodyClosure(filename):
        structure = f"""
        </body>
        """
        with open(filename, "a") as html:
            html.write(structure)
    def webPageclose(filename):
        structure = f"""
        </html>
        """
        with open(filename, "a") as html:
            html.write(structure)
    

    def webPageStart(filename):
        # opens html files only
        webbrowser.open(filename)
    
    



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


print("VisualScipt\nEnter a filename or license for license or help() for help or exit() to exit")
if __name__ == "__main__":
    while True:
        filename = input(">>> ")
        if filename.lower() == 'exit()':
            break
        elif filename.lower() == 'help()':
            print("\nexit() to exit or enter to go back\n")
        elif filename.lower() == 'license':
            print("\nVisualScript is lisensed under a MIT license.\nRead the terms here:\nhttps://github.com/Bruceli-iscool/VisualScript/blob/main/LICENSE\n")
        try:
            process_code(filename)
        except Exception as e:
            if len(filename) < 1 or filename == 'help()' or filename == 'license':
                pass
            else:
                print(f"An error occurred: {e}")
  
