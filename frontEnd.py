from pathlib import Path
from re import MULTILINE
import tkinter as tk
from tkinter import Canvas, Image, filedialog, Text
from tkinter import scrolledtext
from tkinter.constants import E, LEFT, RIGHT, W
global saveFileTextLabel, saveFileText
saveFileText=""

#def DebugAddLog(log): 
#    saveFileTextLabel=saveFileTextL = tk.Label(pathFrame, text=saveFileText, fg="white", bg="#181818", border=5)
#    saveFileTextL.pack()

def writeSaveFile(templatePath, outputePath, textBox, outFile):
    text=textBox.get('1.0', tk.END)
    print("EXPORTING FILE \n", templatePath, outputePath)
    if(templatePath!="" and  outputePath!="" and text!=""):
        # generate in file
        filename = outFile+".in"
        p=Path(__file__).with_name(filename)
        f = open(p,"w")
        if(templatePath.__contains__("=")):
            aux = templatePath.split("=")
            templatePath = aux[1]
        #templatePath.replace("\n", "")
        a=""
        if(templatePath.__contains__(".")):
            templatePath=templatePath.split(".")[0]
        templatePath = "template="+templatePath.replace("\n","")+".docx\n"
        print("templatePath", templatePath)
        f.write(templatePath)

        if(outputePath.__contains__("=")):
            aux = outputePath.split("=")
            outputePath = aux[1]
        
        outputePath.replace("\n", "")
        #outputePathP.replace("\n", "")
        if(outputePath.__contains__(".")):
            outputePath=outputePath.split(".")[0]
        outputePath = "outfile="+outputePath.replace("\n","")+".docx\n"
        f.write(outputePath)
        f.write(text)
        f.close()
        print("check "+outFile+".in")


def writeFile(templatePath, outputePath, textBox):
    text=textBox.get('1.0', tk.END)
    print("EXPORTING FILE \n", templatePath, outputePath)
    if(templatePath!="" and  outputePath!="" and text!=""):
        # generate in file
        filename = "data.in"
        p=Path(__file__).with_name(filename)
        f = open(p,"w")
        if(templatePath.__contains__("=")):
            aux = templatePath.split("=")
            templatePath = aux[1]
        #templatePath.replace("\n", "")
        a=""
        if(templatePath.__contains__(".")):
            templatePath=templatePath.split(".")[0]
        templatePath = "template="+templatePath.replace("\n","")+".docx\n"
        print("templatePath", templatePath)
        f.write(templatePath)

        if(outputePath.__contains__("=")):
            aux = outputePath.split("=")
            outputePath = aux[1]
        
        outputePath.replace("\n", "")
        #outputePathP.replace("\n", "")
        if(outputePath.__contains__(".")):
            outputePath=outputePath.split(".")[0]
        outputePath = "outfile="+outputePath.replace("\n","")+".docx\n"

        f.write(outputePath)

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
                #DebugAddLog(rawLines)
            finally:
                print("error")
                #DebugAddLog("File successfully created!")
        f.close()
    else:
        print("error")
        #DebugAddLog("None of the values must be empty!")
        

def loadFile(outFile, pathTemplate):
    filename = outFile+".in"
    p=Path(__file__).with_name(filename)
    f = open(p,"a")
    f.close()
    f = open(p,"r")
    rawlines = f.readlines()
    templatePathOld = ""
    outputPathOld = ""
    data = ""
    try:
        if(len(rawlines)>=1):
            templatePathOld=rawlines[0].split("=")[1]
            if(len(rawlines)>=2):
                outputPathOld=rawlines[1].split("=")[1]
                if(len(rawlines)>=3):
                    data=rawlines
                    data.remove(rawlines[0])
                    data.remove(rawlines[0])
                    print("Loaded data from\""+filename+"\"")
                    print("Data imported: ", templatePathOld, outputPathOld, data)
                    pathTemplate = tk.StringVar(root, value=templatePathOld)

    except:
        print("Error loading file \""+filename+"\"")


# LOAD OLD DATA
filename = "data.in"
p=Path(__file__).with_name(filename)
f = open(p,"a")
f.close()
f = open(p,"r")
rawlines = f.readlines()
templatePathOld = ""
outputPathOld = ""
data = ""
try:
    if(len(rawlines)>=1):
        templatePathOld=rawlines[0].split("=")[1]
        if(len(rawlines)>=2):
            outputPathOld=rawlines[1].split("=")[1]
            if(len(rawlines)>=3):
                data=rawlines
                data.remove(rawlines[0])
                data.remove(rawlines[0])
except:
    print("NO PREVIOUS DATA FOUND")

print("IMPORTING DATA", templatePathOld, outputPathOld, data)

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
pathTemplate = tk.StringVar(root, value=templatePathOld)

pathTemplateTitle = tk.Label(pathFrame, text="Template Path", fg="white", bg="#181818", border=5)
pathTemplateTitle.pack()
pathTemplateTextBox = tk.Entry(pathFrame, width=50, textvariable = pathTemplate, bg="white", border=5)
pathTemplateTextBox.pack()

# output path
pathOutput = tk.StringVar(root, value=outputPathOld)

pathOutputLabel = tk.Label(pathFrame, text="Output Path", fg="white", bg="#181818", border=5)
pathOutputLabel.pack()
pathOutputTextBox = tk.Entry(pathFrame, width=50, textvariable = pathOutput, bg="white", border=5)
pathOutputTextBox.pack()



 # TEXT SECTION
textFrame = tk.Frame(root, bg="#181818")
textFrame.place(relwidth=1, relheight=0.4, rely=0.31, relx=0)


textTitle = tk.Label(textFrame, text="Output Path", fg="white", bg="#181818", border=5)
textTitle.pack()
textTextBox = scrolledtext.ScrolledText(textFrame, bg="white", border=5, width=root.winfo_screenwidth(), height=10)
textTextBox.pack()


data.reverse()
for dat in data:  
    textTextBox.insert('1.0', dat)

#print(textTextBox.get('1.0', tk.END))

#print(textTextBox.get('1.0', tk.END))
# GENERATION BUTTON

generationButton = tk.Button(textFrame, text="Generate!", fg="white", bg="#181818", border=5, command=lambda: writeFile(pathTemplate.get(), pathOutput.get(), textTextBox))
generationButton.pack()



# SAVE DATA SECTION
#writeSaveFile
slFileFrame = tk.Frame(root, bg="#181818")
slFileFrame.place(relwidth=1, relheight=0.2, rely=0.72, relx=0)

slFileName = "default"

slFileTitle = tk.Label(slFileFrame, text="SAVE/LOAD", fg="white", bg="#181818", border=5)
slFileTitle.pack()

slTextBox = tk.Entry(slFileFrame, textvariable=slFileName,
fg="white", bg="#181818", border=5)
slTextBox.pack()

slSaveButton= tk.Button(slFileFrame, text="Save", fg="white", bg="#181818", border=5,
command=lambda: writeSaveFile(pathTemplate.get(), pathOutput.get(), textTextBox, slTextBox.get()))
slSaveButton.pack()

slLoadButton= tk.Button(slFileFrame, text="Load", fg="white", bg="#181818", border=5,
command=lambda: loadFile(slTextBox.get(), pathTemplate))
slLoadButton.pack()



root.mainloop()