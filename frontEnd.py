from pathlib import Path
from re import MULTILINE
import tkinter as tk
from tkinter import Canvas, Image, filedialog, Text
from tkinter import scrolledtext
global feedbackTextLabel, feedbackText
feedbackText=""

def DebugAddLog(log): 
    feedbackTextLabel=feedbackTextL = tk.Label(pathFrame, text=feedbackText, fg="white", bg="#181818", border=5)
    feedbackTextL.pack()


def writeFile(templatePath, outputePath, textBox):
    text=textBox.get('1.0', tk.END)
    if(templatePath!="" and  outputePath!="" and text!=""):
        # generate in file
        filename = "data.in"
        p=Path(__file__).with_name(filename)
        f = open(p,"w")
        a ={"a", "a"}
        len(a)
        if(templatePath.__contains__("=")):
            aux = templatePath.split("=")
            templatePath = aux[len(aux)-1]
        if(templatePath.__contains__(".")):
            templatePath=templatePath.split(".")[0]
        f.write("template="+templatePath+".docx\n")

        if(outputePath.__contains__("=")):
            aux = outputePath.split("=")
            outputePath = aux[len(aux)-1]
        if(outputePath.__contains__(".")):
            outputePath=outputePath.split(".")[0]
        f.write("outfile="+outputePath+".docx\n")

        f.write(text)
        #print(text)
        f.close()
        print("check data.in")

        # run backend script
        backendFile = "templateGenerator.py"
        p=Path(__file__).with_name(backendFile)
        exec(open(p).read())

        # read debug file
        p=Path(__file__).with_name("data.out")
        f = open(p,"a")
        if(f.readable()):
            try:
                rawLines = f.readlines()
                DebugAddLog(rawLines)
            finally:
                DebugAddLog("File successfully created!")
        f.close()
    else:
        DebugAddLog("None of the values must be empty!")
        print("error")




# INITIALIZE SECTION
root = tk.Tk()
canvas = tk.Canvas(root, height=700, width=1000, bg="gray")
canvas.pack()
frame = tk.Frame(root, bg="black")
frame.place(relwidth=1, relheight=1, relx=0, rely=0)
# TITLE SECTION
titleLabel = tk.Label(frame, text="Youtube Research", fg="white", bg="black", height=1, )
titleLabel.pack()

# PATH SECTION
pathFrame = tk.Frame(root, bg="#181818")
pathFrame.place(relwidth=1, relheight=0.2, rely=0.1, relx=0)

# template path
pathTemplate = tk.StringVar()

pathTemplateTitle = tk.Label(pathFrame, text="Template Path", fg="white", bg="#181818", border=5)
pathTemplateTitle.pack()
pathTemplateTextBox = tk.Entry(pathFrame, width=50, textvariable = pathTemplate, bg="white", border=5)
pathTemplateTextBox.pack()

# output path
pathOutput = tk.StringVar()

pathOutputLabel = tk.Label(pathFrame, text="Output Path", fg="white", bg="#181818", border=5)
pathOutputLabel.pack()
pathOutputTextBox = tk.Entry(pathFrame, width=50, textvariable = pathOutput, bg="white", border=5)
pathOutputTextBox.pack()



 # TEXT SECTION
textFrame = tk.Frame(root, bg="#181818")
textFrame.place(relwidth=1, relheight=0.4, rely=0.31, relx=0)


textTitle = tk.Label(textFrame, text="Output Path", fg="white", bg="#181818", border=5)
textTitle.pack()
textTextBox = scrolledtext.ScrolledText(textFrame, bg="white", border=5, width=50, height=10)
textTextBox.pack()
#print(textTextBox.get('1.0', tk.END))

#print(textTextBox.get('1.0', tk.END))
# GENERATION BUTTON

generationButton = tk.Button(textFrame, text="Generate!", fg="white", bg="#181818", border=5, command=lambda: writeFile(pathTemplate.get(), pathOutput.get(), textTextBox))
generationButton.pack()

# FEEDBACK SECTION
feedbackFrame = tk.Frame(root, bg="#181818")
feedbackFrame.place(relwidth=1, relheight=0.2, rely=0.72, relx=0)

feedbackText=""
feedbackTitle = tk.Label(feedbackFrame, text="Debug Log:", fg="white", bg="#181818", border=5)
feedbackTitle.pack()
feedbackTextLabel = tk.Label(feedbackFrame, text=feedbackText, fg="white", bg="#181818", border=5)
feedbackTextLabel.pack()





root.mainloop()