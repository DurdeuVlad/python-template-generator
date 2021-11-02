from pathlib import Path
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
from datetime import date



filename = "data.in"
p=Path(__file__).with_name(filename)

global lines, i, context, errors
errors = {""}

try:
    f = open(p,"r")
finally:
    f = open(p,"a")
    f.close()
    f = open(p,"r")
    #errors.update({"Input file not found. Created a new one at:"+f.name})
    #print(f.name)

rawLines = f.readlines()


lines=[]

for line in rawLines:
    if(line.__contains__("=")):
        line = line.split("=")
        if (line[1].__contains__("\n")):
            line[1] = line[1].split("\n")[0]
            lines.append(line[0])
            lines.append(line[1])
    print(line, end="\n")

print(lines[1], end="\n")
print(lines[3], end="\n")

if(lines[0]=="template"):
    p=Path(__file__).with_name(lines[1])
    doc = DocxTemplate(p)
    context = {"" : ""}

    for x in range(len(lines)-1):
        aux = x
        a = aux.__divmod__(2)
        print(x, a, a[1]==0)
        if(a[1]==0):
            context.update({lines[x] : lines[x+1]})
        print(context)

    doc.render(context)
    if(lines[2]=="outfile"):
        p=Path(__file__).with_name(lines[3])
        doc.save(p)
    else:
        errors.update({"The input file\'s second line must be \"outfile=*filepath*\""})
else:
    errors.update({"The input file must start with \"template=*filepath*\""})


f.close()

filedebug = "data.out"
p=Path(__file__).with_name(filedebug)
f = open(p,"w")
if (errors != {""}):
    for str in errors:
        f.write(str)
else:
    f.write("Template created successfully!")
