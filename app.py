from flask import Flask, render_template, url_for
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    #file1.txt is the default file to read in case no fileName is provided by the user.
    readFile = "./static/files/file1.txt"
    fileName = request.args.get('fileName')
    startLine = request.args.get('startLineNo')
    endLine = request.args.get('endLineNo')

    startLineNo= 0
    endLineNo= -1
    errorMsg = ""

# To check StartLine
    if(startLine):
        try:
            startLineNo=int(startLine)
            if(startLineNo < 0):
                errorMsg="Please provid valid startLineNo. The number must be 0 or positive\n"
        except ValueError:
            errorMsg="ValueError: startLineNo %s is not a whole number. Please provid valid number\n" %(startLine)

# To check EndLine
    if(endLine):
        try:
            endLineNo=int(endLine)
            if(endLineNo < 0):
                errorMsg += "Please provid valid endLineNo. The number must be 0 or positive\n"
        except ValueError:
            errorMsg += "ValueError: endLineNo %s is not a whole number. Please provid valid number\n" %(endLine)

    if((startLine !=None and endLine !=None) and (startLineNo > endLineNo)):
        errorMsg += "startLineNo must be less than or equal to endLineNo"

    if(errorMsg != ""):
        return render_template('index.html', data=errorMsg)

# To check FileName
    if(fileName):
        readFile = "./static/files/" + fileName
    try:
        with open(readFile, 'r') as file:
            fileLines = file.readlines()
    except FileNotFoundError:
        return render_template('index.html', data="FileNotFoundError: Input file %s not found. Please provid valid file name\n" %(fileName))

    fileTxt = ""
    lineReadCounter = 0

# To Read File
    for line in fileLines:
        if((lineReadCounter >= startLineNo) and (endLineNo == -1 or lineReadCounter <= endLineNo)):
            fileTxt += line
        lineReadCounter +=1
    return render_template('index.html', data=fileTxt)

if __name__ == "__main__":
    app.run(debug=True)
