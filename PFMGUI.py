from tkinter import *
import os
import sys

main = Tk()
main.geometry("330x290")
main.title("Python Files Manager")
main.resizable(width=False, height=False)

def openfilewin():

    def openfile():
         os.system('exec kitty nvim ' + openfnamespace.get() + ".py")
         openfilewindow.destroy()
    

    openfilewindow = Tk()

    openfilewindow.geometry("390x130")
    openfilewindow.resizable(width=False, height=False)
    openfilewindow.title("Open file")

    enterofnametxt = Label(openfilewindow, text="Enter file name:")
    enterofnametxt.pack(side="left")

    openfnamespace = Entry(openfilewindow)
    openfnamespace.pack(side="left")

    openbutt = Button(openfilewindow, text="Open", command=openfile)
    openbutt.pack(side="left")

    openfilewindow.mainloop()
def newfilewin():
    def newfile():
        os.system('touch ' + newfnamespace.get() + '.py')
        
        def yespress():
            os.system('exec kitty nvim ' + newfnamespace.get() + '.py')
            newfilewindow.destroy()
            yornOpenNewFile.destroy()
        def nopress():
            newfilewindow.destroy()
            yornOpenNewFile.destroy()

        yornOpenNewFile = Tk()
        yornOpenNewFile.geometry("230x165")
        yornOpenNewFile.resizable(width=False, height=False)
        yornOpenNewFile.title("Need open file?")

        quest = Label(yornOpenNewFile, text='Do you need open new file?')
        quest.pack()

        yesbutt = Button(yornOpenNewFile, text="Yes", command=yespress)
        yesbutt.pack(side='left')

        nobutt = Button(yornOpenNewFile, text='No', command=nopress)
        nobutt.pack(side='right')


        yornOpenNewFile.mainloop()
    
    newfilewindow = Tk()
    newfilewindow.geometry("390x130")
    newfilewindow.resizable(width=False, height=False)
    newfilewindow.title("New file")

    enternfnametxt = Label(newfilewindow, text="Enter file name:")
    enternfnametxt.pack(side="left")

    newfnamespace = Entry(newfilewindow)
    newfnamespace.pack(side="left")

    createbutt = Button(newfilewindow, text="Create", command=newfile)
    createbutt.pack(side="left")

    newfilewindow.mainloop()

def delfilewin():

    def delfile():
        
        def yespress():
            os.system('rm -rf ' + delfnamespace.get() + '.py')
            delfilewindow.destroy()
            areusurewin.destroy()

        def nopress():
            delfilewindow.destroy()
            areusurewin.destroy()

        areusurewin = Tk()
        areusurewin.geometry("230x165")
        areusurewin.resizable(width=False, height=False)
        areusurewin.title("Sure?")

        quest = Label(areusurewin, text='Are you sure?')
        quest.pack()

        yesbutt = Button(areusurewin, text="Yes", command=yespress)
        yesbutt.pack(side='left')

        nobutt = Button(areusurewin, text='No', command=nopress)
        nobutt.pack(side='right')
        
    delfilewindow = Tk()
    delfilewindow.geometry("390x130")
    delfilewindow.resizable(width=False, height=False)
    delfilewindow.title("New file")

    enternfnametxt = Label(delfilewindow, text="Enter file name:")
    enternfnametxt.pack(side="left")

    delfnamespace = Entry(delfilewindow)
    delfnamespace.pack(side="left")

    delbutt = Button(delfilewindow, text="Delete", command=delfile)
    delbutt.pack(side="left")

    delfilewindow.mainloop()

def renamewin():

    def rename():
        os.system('mv ' + oldfilenamespace.get() + '.py' + " " + newnamefilespace.get() + ".py")
        renamewindow.destroy()

    renamewindow = Tk()
    renamewindow.geometry('285x290')
    renamewindow.resizable(width=False, height=False)
    renamewindow.title('Rename file')

    oldfilenametxt = Label(renamewindow, text='Old name file:')
    oldfilenametxt.pack()

    oldfilenamespace = Entry(renamewindow)
    oldfilenamespace.pack()

    newfilenametxt = Label(renamewindow, text="New name file:")
    newfilenametxt.pack()

    newnamefilespace = Entry(renamewindow)
    newnamefilespace.pack()

    renamefilebutt = Button(renamewindow, text='Rename', command=rename)
    renamefilebutt.pack(side='bottom')

    renamewindow.mainloop()

def exitfromapp():
    sys.exit()

welcometxt = Label(text="Welcome!")
welcometxt.pack()

openfilebutt = Button(main, text="Open file", command=openfilewin)
openfilebutt.pack()

newfilebutt = Button(main, text="New file", command=newfilewin)
newfilebutt.pack()

renamefilebutt = Button(main, text="Rename file", command=renamewin)
renamefilebutt.pack()

delfilebutt = Button(main, text="Delete file", command=delfilewin)
delfilebutt.pack()

exitbutt = Button(main, text="Exit", command=exitfromapp)
exitbutt.pack(side="bottom")

main.mainloop()