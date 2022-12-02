STATICKY_TEXT="This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "

def writeTextToFile(text):
    final_text=STATICKY_TEXT+str(text)
    with open("linewriter.txt", "w") as output:
        output.write(final_text)
    return("linewriter.txt")

writeTextToFile("xdd")


