# Creater: a_furbyz
# Data create: 26/02/2021
#tk
#import tkinter as tk
#from tkinter import messagebox as msgbx

# make a new window
#window = tk.Tk()

# show popup
#msgbx.showinfo("title", "This is a text")

from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox as msgbx


#from googletrans import Translator
from sys import platform
import re
import os
import time
if platform == 'linux' or platform == 'linux2':
    clearcmd = 'clear'
elif platform == 'win32':
    clearcmd = 'cls'
clear = lambda:os.system(clearcmd)


window = Tk()
window.title('File Explorer by a_furbyz')
window.geometry("800x600")


labelProg = LabelFrame(window, text = "Information", padx=20, pady=20)
labelProg.place(anchor="center")
labelProg.pack(fill="both", padx=10, pady=10)

labelfile = LabelFrame(window, text = "Information fichier", padx=20, pady=20)
labelfile.place(anchor="center")
labelfile.pack(fill="both", padx=10, pady=10)


_label_file = StringVar()
_panel_file = Label(textvariable=_label_file, background='white', anchor=CENTER)
p = PanedWindow(labelfile, orient=HORIZONTAL)
p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
p.add(Label(text='Ouvert', anchor=CENTER))
p.add(_panel_file)

_label_texte = StringVar()
_panel_texte = Label(textvariable=_label_texte, background='white', anchor=CENTER) 
p = PanedWindow(labelfile, orient=HORIZONTAL)
p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
p.add(Label(text='Texte', anchor=CENTER))
p.add(_panel_texte)

_label_sauv = StringVar()
_panel_sauv = Label(textvariable=_label_sauv, background='white', anchor=CENTER)
p = PanedWindow(labelfile, orient=HORIZONTAL)
p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
p.add(Label(text='Sauvegarde', anchor=CENTER))
p.add(_panel_sauv)

labelDir = LabelFrame(window, text = "Dossier", padx=20, pady=20)
labelDir.pack(side=TOP, fill=BOTH, padx=10, pady=10)

# labelOpen = LabelFrame(window, text = "Parcourir", padx=20, pady=20)
# labelOpen.place(anchor="center")
# labelOpen.pack(fill="both", padx=10, pady=10)

# labelQuit = LabelFrame(window, text = "Button", padx=20, pady=20)
# labelQuit.pack(fill="both", padx=10, pady=10)


_explorer = Label(labelDir, 
							text = "Ouvrir un dossier:", 
							fg = "blue",
                            anchor="w")
_explorer.grid(column = 1, row = 1, sticky=W)


_myListBox = Listbox(labelDir)

def alert():
    msgbx.showinfo("A propos", "Crée par a_furbyz")

def browseFiles():    
    filename = filedialog.askdirectory()
    #filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.rpy"),("all files","*.*")))
    # Change label contents
    myList = os.listdir(filename)
    
    #clear listbox
    _myListBox.delete(0,END)
    
    for file in myList:
        if file.endswith(".rpy"):
            _myListBox.insert(END,  os.path.join(filename, file))
            
    _myListBox.grid(column = 1, row = 2, sticky="news")
    _myListBox.bind("<<ListboxSelect>>", showcontent)
    
    _text.insert(END, "Dossier ouvert")
    _explorer.configure(text="Dossier ouvert: "+filename)


def showcontent(event):
    global file_name, file_fr, file_temp, file_old
    
    x = _myListBox.curselection()[0]
    file = _myListBox.get(x)
    
    file_name = file
    file_fr = file+'_fr'
    file_temp = file+'_temp'
    file_old = file+'_old'
    
    _text.delete('1.0', END)
    _text.insert(END, 'OUVERT: '+file)
    _label_file.set(short(file))
    _text.insert(END, '\n')
    if os.path.exists(file_fr):
        #_text.insert(END, 'TEXTE: '+file_fr, 'ok')
        _label_texte.set(short(file_fr))
        _panel_texte.config(bg='green')
    else:
        #_text.insert(END, 'TEXTE: '+file_fr, 'nok')
        _label_texte.set(short(file_fr))
        _panel_texte.config(bg='red')
    
    #_text.insert(END, '\n')
        
    if os.path.exists(file_old):
        #_text.insert(END, 'SAUV: '+file_old, 'ok')
        _label_sauv.set(short(file_old))
        _panel_sauv.config(bg='green')
    else:
        #_text.insert(END, 'SAUV: '+file_old, 'nok')
        _label_sauv.set(short(file_old))
        _panel_sauv.config(bg='red')
         
    #_text.insert(END, '\n')
    
    

#translator = Translator()
clear()
print('[TESPY] Creator: a_furbyz\n')
#nametextfile = input('Nom de fichier (avec extension): ')
def short(string):
    return '/'.join(string.rsplit('/')[-5:])


def create_txt():
    
    clear()
    # Read file
    file = open(file_name,'r+', encoding="utf8")
    output = open(file_fr,'w', encoding='utf-8')
    #file = open(nametextfile,'r+')
    #data = file.read()
    line = file.readline()
    total = len(line)


    cnt = 1
    

    while line:
        if '#' in line or ' old ' in line or line.startswith("translate"):
            cnt += 1
            line = file.readline()
            continue

        #print("Line{}: {}".format(cnt, line.strip()))
        
        match2=re.findall(r'\"(.+?)\"',line.strip())
        try:
            text = match2[0]   
            if text:
                #print("Line {}: {}".format(cnt, text))
                time.sleep(0.1) 

                output.write(text+ '\n')
                line = file.readline()
                cnt += 1
        except:
            line = file.readline()
            pass
        
        #print('{:.0f}'.format(cnt * total / 100))
        #progressbar['value'] = '{:.0f}'.format(cnt * total / 100)
        # Force an update of the GUI
        print("Line {}: {}".format(cnt, total))
        _text.delete('1.0', END)
        _text.insert(END, "Line {}".format(cnt))
        labelProg.update_idletasks()
        
    
            
    file.close()
    output.close()


    print('Le programme est terminé. Résultat enregistré dans '+file_name+'_fr')
    _text.delete('1.0', END)
    _text.insert(END, 'Résultat enregistré dans '+file_fr)

def seach(out, num):
    count = 0
    for line in out:
        #print(line.strip(), num)
        if count == num :
            return line.strip()
        count += 1

def recompile_txt():
    
    # Read file
    file = open(file_name,'r+', encoding="utf8")
    output = open(file_fr,'r+', encoding='utf-8')
    temp = open(file_temp,'w', encoding='utf-8')
    #file = open(nametextfile,'r+')
    #data = file.read()
    line = file.readline()
    out = output.readlines()
    total = len(line)


    cnt = 1
    count = 0
    

    while line:
        if '#' in line or ' old ' in line or line.startswith("translate"):
            cnt += 1
            temp.write(line+ '\n')            
            line = file.readline()
            continue

        #print("Line{}: {}".format(cnt, line.strip()))
        
        match2=re.findall(r'\"(.+?)\"',line.strip())
        try:
            text = match2[0]   
            if text:
                #print("Lineaiii {}: {}".format(cnt, text))
                text_out = seach(out, count)
                    
                #print('dataaaaaaaaa', out.strip())
                time.sleep(0.1) 
                #print("testtt", line.replace(text, text_out))
              
                temp.write(line.replace(text, text_out) + '\n')
        
                #line_read = line.strip().replace(text, text_out)
                #print('dataaaaaaaaa', out.strip())
                #file.write(line)
                #out = out.readline()
                line = file.readline()
                cnt += 1
                count += 1
        except:
            line = file.readline()
            pass
        
        #print('{:.0f}'.format(cnt * total / 100))
        #progressbar['value'] = '{:.0f}'.format(cnt * total / 100)
        #progressbar.update() # Force an update of the GUI
        print("Line {}: {}".format(cnt, total))
        _text.delete('1.0', END)
        _text.insert(END, "Line {}".format(cnt))
        labelProg.update_idletasks()
        
        
    
    file.close()
    output.close()
    temp.close()
    #rename
    os.rename(file_name, file_old)
    os.rename(file_temp, file_name)
    

    print('Recompile terminé. Résultat enregistré dans '+file_name+'_fr')
    _text.delete('1.0', END)
    _text.insert(END, 'Résultat enregistré et sauvegarde créé '+file_name)
    
    
 

#####
_text = Text(labelProg, bg='cyan', width = 90, height = 4 )
_text.grid(column = 1, row = 1)
_text.tag_config('nok', foreground="red")
_text.tag_config('ok', foreground="green")

# Create a File Explorer label
# _explorer = Label(labelOpen, 
# 							text = "File Opened:",
# 							width = 100, height = 4, 
# 							fg = "blue")
# _explorer.grid(column = 1, row = 1)


# _browse = Button(labelQuit, 
# 						text = "Browse Files",
# 						command = browseFiles, height = 2, width = 20) 
# _browse.grid(column = 1, row = 1)

# _txt = Button(labelQuit, 
# 					text = "Extraire texte",
# 					command = create_txt, height = 2, width = 20) 
# _txt.grid(column = 2, row = 1)

# _comp = Button(labelQuit, 
# 					text = "Recompile texte",
# 					command = recompile_txt, height = 2, width = 20) 
# _comp.grid(column = 3, row = 1)

# _exit = Button(labelQuit, 
# 					text = "Exit",
# 					command = exit, height = 2, width = 20) 
# _exit.grid(column = 4, row = 1)

# Grid method is chosen for placing
# the widgets at respective positions 
# in a table like structure by
# specifying rows and columns

#menu
menubar = Menu(window)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Ouvrir un dossier", command=browseFiles)
menu1.add_separator()
menu1.add_command(label="Quitter", command=window.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Extraire le texte", command=create_txt)
menu2.add_command(label="Recompiler le texte", command=recompile_txt)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

window.config(menu=menubar)


# Let the window wait for any events
window.mainloop()