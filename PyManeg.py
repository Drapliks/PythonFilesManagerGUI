from tkinter import *
import os
import sys

main = Tk()
main.geometry("330x350")
main.title("Pymaneg")
main.resizable(width=False, height=False)

os.system('mkdir ~/PythonFiles')
os.system('mkdir ~/PythonProjects')

def openfilewin():

    def openfile():
         os.system('exec kitty nvim ~/PythonFiles/' + openfnamespace.get() + ".py")
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
        os.system('touch ~/PythonFiles/' + newfnamespace.get() + '.py')
        
        def yespress():
            os.system('exec kitty nvim ~/PythonFiles/' + newfnamespace.get() + '.py')
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
            os.system('rm -rf ~/PythonFiles/' + delfnamespace.get() + '.py')
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
    delfilewindow.title("Delete file")

    enternfnametxt = Label(delfilewindow, text="Enter file name:")
    enternfnametxt.pack(side="left")

    delfnamespace = Entry(delfilewindow)
    delfnamespace.pack(side="left")

    delbutt = Button(delfilewindow, text="Delete", command=delfile)
    delbutt.pack(side="left")

    delfilewindow.mainloop()

def renamewin():

    def rename():
        os.system('mv ~/PythonFiles/' + oldfilenamespace.get() + '.py' + " ~/PythonFiles/" + newnamefilespace.get() + ".py")
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

def launchfilewin():

    def launchfile():
        os.system('exec kitty python ~/PythonFiles/' + laucnhfnamespace.get() + '.py')
    launchfilewindow = Tk()
    launchfilewindow.geometry("390x130")
    launchfilewindow.resizable(width=False, height=False)
    launchfilewindow.title("Laucnh file")

    enterlfnametxt = Label(launchfilewindow, text="Enter file name:")
    enterlfnametxt.pack(side="left")

    laucnhfnamespace = Entry(launchfilewindow)
    laucnhfnamespace.pack(side="left")

    launchbutt = Button(launchfilewindow, text="Launch", command=launchfile)
    launchbutt.pack(side="left")

    launchfilewindow.mainloop()

def openprojectwin():

    def openprj():

        def openmainpy():
            os.system('exec kitty nvim ~/PythonProjects/' + openpnamespace.get() + '/main.py')
            
        def pipinstallwin():

            def install():
                os.system('pip install ' + installpkgnamespace.get())

            pipinstallwindow = Tk()
            pipinstallwindow.geometry("390x130")
            pipinstallwindow.resizable(width=False, height=False)
            pipinstallwindow.title("pip install")

            enterpippkgametxt = Label(pipinstallwindow, text="Enter package name:")
            enterpippkgametxt.pack(side="left")

            installpkgnamespace = Entry(pipinstallwindow)
            installpkgnamespace.pack(side="left")

            installbutt = Button(pipinstallwindow, text="install", command=install)
            installbutt.pack(side="left")

            pipinstallwindow.mainloop()

        def exitprj():
            openprjwindow.destroy()
            prjwindow.destroy()

        prjwindow = Tk()

        prjwindow.geometry("410x315")
        prjwindow.resizable(width=False, height=False)
        prjwindow.title(openpnamespace.get())
        os.system('source ~/PythonProjects/' + openpnamespace.get() + '/venv/bin/activate')

        openmpyButt = Button(prjwindow, text='Open main.py', command=openmainpy)
        openmpyButt.pack()

        pipiButt = Button(prjwindow, text='pip install', command=pipinstallwin)
        pipiButt.pack()

        newfButt = Button(prjwindow, text='New file')
        newfButt.pack() 

        openfButt = Button(prjwindow, text='Open file')
        openfButt.pack() 

        exitButt = Button(prjwindow, text='Exit', command=exitprj)
        exitButt.pack(side='bottom')

        prjwindow.mainloop()



    openprjwindow = Tk()
    openprjwindow.geometry("390x130")
    openprjwindow.resizable(width=False, height=False)
    openprjwindow.title("Open project")

    enteropnametxt = Label(openprjwindow, text="Enter project name:")
    enteropnametxt.pack(side="left")

    openpnamespace = Entry(openprjwindow)
    openpnamespace.pack(side="left")

    openbutt = Button(openprjwindow, text="Open", command=openprj)
    openbutt.pack(side="left")

    openprjwindow.mainloop()
def newprojectwin():

    def newprj():
        os.system('mkdir ~/PythonProjects/' + newpnamespace.get())
        os.system('touch ~/PythonProjects/' + newpnamespace.get() + '/main.py')
        os.system('mkdir ~/PythonProjects/' + newpnamespace.get() + '/venv/')
        os.system('python -m venv ~/PythonProjects/' + newpnamespace.get() + '/venv/')
        needopenprj = Tk()
        
        def yespress():
            pass
        def nopress():
            newprjwindow.destroy()
            newprjwindow.destroy()

        needopenprj = Tk()
        needopenprj.geometry("230x165")
        needopenprj.resizable(width=False, height=False)
        needopenprj.title("Need open file?")

        quest = Label(needopenprj, text='Do you need open new file?')
        quest.pack()

        yesbutt = Button(needopenprj, text="Yes", command=yespress)
        yesbutt.pack(side='left')

        nobutt = Button(needopenprj, text='No', command=nopress)
        nobutt.pack(side='right')

        needopenprj.mainloop

    newprjwindow = Tk()
    newprjwindow.geometry("390x130")
    newprjwindow.resizable(width=False, height=False)
    newprjwindow.title("Open project")

    enternpnametxt = Label(newprjwindow, text="Enter project name:")
    enternpnametxt.pack(side="left")

    newpnamespace = Entry(newprjwindow)
    newpnamespace.pack(side="left")

    newprjbutt = Button(newprjwindow, text="Create", command=newprj)
    newprjbutt.pack(side="left")

welcometxt = Label(text="Welcome!")
welcometxt.pack()

openfilebutt = Button(main, text="Open file", command=openfilewin)
openfilebutt.pack()

newfilebutt = Button(main, text="New file", command=newfilewin)
newfilebutt.pack()

openprojectbutt = Button(main, text="Open project", command=openprojectwin)
openprojectbutt.pack()

newprojectbutt = Button(main, text="New project", command=newprojectwin)
newprojectbutt.pack()

launchfilebutt = Button(main, text="Launch file", command=launchfilewin)
launchfilebutt.pack()

renamefilebutt = Button(main, text="Rename file", command=renamewin)
renamefilebutt.pack()

delfilebutt = Button(main, text="Delete file", command=delfilewin)
delfilebutt.pack()

exitbutt = Button(main, text="Exit", command=exitfromapp)
exitbutt.pack(side="bottom")

main.mainloop()