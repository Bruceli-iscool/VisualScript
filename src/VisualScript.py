# change python syntax and define functions
import tokenize
from io import BytesIO

def process_code(project):
    keys = {

        "size":"range",
        "log":"print",
        "ask": "input",
        "define":"def",
        "convertInt":"int",
        "convertStr":"str",
        "else if":"elif"
        

    }