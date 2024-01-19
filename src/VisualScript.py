# change python syntax and define functions
import tokenize
from io import BytesIO

def process_code(file):
    keys = {

        "size":"range",
        "log":"print",
        "ask": "input",
        "define":"def",
        "convertInt":"int",
        "convertStr":"str",
        "else if":"elif"
    }
    def append(list, value):
        result_list = list.append(value)
        return result_list
    def test(value):
        print(value)
        return
    custom_features = {
        "append":append,
        "test":test
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

if __name__ == "__main__":
    try:
        process_code("/workspaces/VisualScript/src/example.vs")
    except Exception as e:
        print(f"An error occurred: {e}")
    