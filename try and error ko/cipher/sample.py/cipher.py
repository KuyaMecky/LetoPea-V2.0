# CipherGUI
import tkinter as tk
import tkinter.scrolledtext as tkScroll
from tkinter import filedialog
import os

#Importing all the cipher classes
from DoubleTranspositionCipher import *
from MorseCodeCipher import *
from base64Cipher import *
from VigenereCipher import *
from SkipCipher import *
from CaesarCipher import *

#Creates a global window and names it 'Cipher Buddy'
global root
root = tk.Tk()
root.title('Cipher Buddy')

#Creating a menu bar
def menuBar():
    #Creates main menu bar
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    #Creates submenu 'File'
    fileMenu = tk.Menu(menubar, tearoff=0)

    #Adds options New, Open, Save as..., and Exit to 'File' submenu
    menubar.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="New", command=lambda: os.startfile(r'CipherGUI.py'))
    fileMenu.add_command(label="Open", command=selectFile)
    fileMenu.add_command(label="Save as...", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=root.destroy)

    #Creates submenu 'Edit'
    editMenu = tk.Menu(menubar, tearoff=0)

    #Adds options Undo,Redo, Cut, Copy and Paste to 'Edit' submenu
    menubar.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Undo", command=lambda: executeText.edit_undo())
    editMenu.add_command(label="Redo", command=lambda: executeText.edit_redo())
    editMenu.add_command(label="Cut", command=lambda: root.focus_get().event_generate('<<Cut>>'))
    editMenu.add_command(label="Copy", command=lambda: root.focus_get().event_generate('<<Copy>>'))
    editMenu.add_command(label="Paste", command=lambda: root.focus_get().event_generate('<<Paste>>'))

    #Creates submenu
    helpMenu = tk.Menu(menubar, tearoff=0)

    #Add option About and How does it work?
    menubar.add_cascade(label="Help", menu=helpMenu)
    helpMenu.add_command(label="About...", command=lambda: infoProgram(1))
    helpMenu.add_command(label="How does it work?", command=lambda: infoProgram(2))

    #Creats a submenu inside the submenu 'Help'
    cipherInfoMenu = tk.Menu(menubar, tearoff=0)

    #Adds option to view info of the chosen cipher
    helpMenu.add_cascade(label="Cipher Options Info", menu=cipherInfoMenu)
    cipherInfoMenu.add_command(label="Morse Code", command=lambda: cipherInfo(1))
    cipherInfoMenu.add_command(label="Double Transposition", command=lambda: cipherInfo(2))
    cipherInfoMenu.add_command(label="Base64", command=lambda: cipherInfo(3))
    cipherInfoMenu.add_command(label="Vigenere", command=lambda: cipherInfo(4))
    cipherInfoMenu.add_command(label="Skip", command=lambda: cipherInfo(5))
    cipherInfoMenu.add_command(label="Caesar", command=lambda: cipherInfo(6))


#Opens file explorer to choose a text file to encrypt or decrypt
def selectFile():
    fileName = tk.filedialog.askopenfilename(title="Select a file", filetypes=[("txt Files", "*.txt")])
    fileEntry.delete(0, "end")
    fileEntry.insert(0, fileName)


#Opens file explorer to save resulting text
def saveFile():
    fileSave = tk.filedialog.asksaveasfile(mode='w', defaultextension=("txt File","*.txt"), filetypes=[("txt File", "*.txt")])
    fileSave.write("Original text: \n")
    fileSave.write(executeText.get("1.0", "end") + "\n")
    fileSave.write("Encrypted or Decrypted text: \n")
    fileSave.write(answerText.get("1.0", "end"))


#Adds text in selected file into the text entry block
def insertFile():
    aFile = open(fileEntry.get())
    fileText = aFile.read()
    executeText.delete("1.0", "end")
    executeText.insert("1.0", fileText)

    aFile.close()

#Displays information from the selected option in Help (About, How does it work?)
def infoProgram(choice):
    infoWindow = tk.Tk()

    if choice == 1:
        about = tk.Label(infoWindow, text="""This application was built in order to facilitate a user friendly encryption program.
        It was created as well to show how to create an intermidiate level GUI Applcation using Tkinter. Feel free to update, add to, or
        incorporate this program however you see fit. Hope you enjoy using it as much as me enjoyed making it.\n\n
        CREATORS: Edwin Urbina   Luis Alcaraz   Paola Guadalupe""")
        about.pack()

    else:
        howTo = tk.Label(infoWindow, text="""STEP 1: Load a text file from the 'File Menu' or write the path, and insert it;
        or write a text into the first entry box.\n
        STEP 2: Select a cipher option from the drop down menu and press 'Select'\n
        STEP 3: Press either the 'Encrypt' or 'Decrypt' option button.\n
        STEP 4: Save the resulting text in a text file with the 'Save as...' option from the 'File Menu'""")
        howTo.pack()


#Displays info from selected cipher in Chiper Option Info
def cipherInfo(choice):
    infoWindow = tk.Tk()

    if choice == 1:
        morseCodeInfo = tk.Label(infoWindow, text="""A Morse Code is the method of writing
        with dots and dashes to encrypt letters and symbols. This was created in order send
        messages through the telegraph created by Samuel Morse, to which this style of encryption is named after.""")
        morseCodeInfo.pack()

    elif choice == 2:
        dtInfo = tk.Label(infoWindow, text="""A Double Transposition Cipher is the application of a Columnar Transposition twice.
        You start by picking two key words. Your text is converted into a matrix where its number of columns is dipicted by the letters in your key word.
        Then it starts transposing your matrix by column in alphabetical order. Then it does this process again with the next key word. The decryption
        method is just the opposite where your matrix's first column is the key word and you transpose the rows in the order of the key word.\n\n
        For purpose of this cipher GUI, the key word is set to lower case and the redundant letters are removed after the first appearnce.\n\n
        Alert *THE DECRYPTION OPTION ONLY WORKS WITH FILES ENCRYPTED BY THIS TOOL*""")
        dtInfo.pack()

    elif choice == 3:
        Base64Info = tk.Label(infoWindow, text="""Base64, also known as MIME encoding, translates binary into safe text. 
        It is used to send attachments in email and to change small bits of unsafe high-character data into stuff that 
        is a lot nicer for text-based system.""")
        Base64Info.pack()

    elif choice == 4:
        VigenereInfo = tk.Label(infoWindow, text=""" Vigenere Cipher is a method of encrypting alphabetic text. 
        It uses a simple form of polyalphabetic substitution. A polyalphabetic cipher is any cipher based on substitution, 
        using multiple substitution alphabets. To encrypt, a table of alphabets can be used, termed a tabula recta, 
        Vigenère square or Vigenère table. It has the alphabet written out 26 times in different rows, each alphabet 
        shifted cyclically to the left compared to the previous alphabet, corresponding to the 26 possible Caesar 
        ciphers. At different points in the encryption process, the cipher uses a different alphabet from one of the rows. 
        The alphabet used at each point depends on a repeating keyword""")
        VigenereInfo.pack()

    elif choice == 5:
        SkipInfo = tk.Label(infoWindow, text=""" The skip cipher is a transposition cipher that consists of extracting
         the letters of a message every n characters (by jumping n characters). 
         When the end of the message is reached, resume at the beginning (loop). To decrypt the message the cipher 
         reorders the letters of the message by indexing the message characters in order with the jump.
         For encryption or decryption to work, it is necessary to use a jump value that is not prime with 
         the length of the message.""")
        SkipInfo.pack()

    elif choice == 6:
        CaesarInfo = tk.Label(infoWindow, text=""" Caesar cipher (or Caesar code) is a shift cipher, one of the most 
        easy and most famous encryption systems. It uses the substitution of a letter by another one further in the 
        alphabet.""")
        CaesarInfo.pack()

#Creates the main window of the GUI
def mainWindow():
    #Runs the menu bar
    menuBar()
    #Sets dimensions for canvas
    HEIGHT = 500
    WIDTH = 700

    #Sets canvas
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    #Creates label to instruct user of options to enter text
    entryLabel = tk.Label(root, text='Enter text or load a text file:')
    entryLabel.place(x=50, y=60)

    #Creates label to instruct user where he can write his programs path
    fileLabel = tk.Label(root, text='File:')
    fileLabel.place(x=50, y=80)

    #Creates an entry to type file path
    global fileEntry
    fileEntry = tk.Entry(root)
    fileEntry.place(x=80, y=78)

    #Creates button that inserts file in text entry block
    fileButton = tk.Button(root, text="Insert", command=insertFile)
    fileButton.place(x=210, y=70)

    #Creates label that indicates that this is the cipher option drop down menu
    optionLabel = tk.Label(root, text="Cipher Options:")
    optionLabel.place(x=275, y=78)

    #Creates default cipher option
    option = tk.StringVar()
    option.set("Choose")

    #Creates drop down menu with cipher options
    dropMenu = tk.OptionMenu(root, option, "Morse Code", "Double Transposition", "Base64", "Vigenere", "Skip", "Caesar")
    dropMenu.place(x=370, y=70)

    #Creates button to select cipher option and update window depending on the cipher requirements
    optionButton = tk.Button(root, text="Select", command=lambda: cipherWindows(option.get()))
    optionButton.place(x=530, y=72)

    #Creates entry text box to place text to encrypt or decrypt text
    global executeText
    executeText = tkScroll.ScrolledText(root, undo=True)
    executeText.place(x=50, y=100, height=150, width=600)

    #Creates entry text box to place result of encryption or decryption
    global answerText
    answerText = tkScroll.ScrolledText(root, undo=True)
    answerText.place(x=50, y=325, height=150, width=600)

    #Creates encryption button to encrypt text
    encryptButton = tk.Button(root, text="Encrypt", command=lambda: encryptText(option.get()))
    encryptButton.place(x=295, y=260)

    #Creates decryption button to encrypt text
    decryptButton = tk.Button(root, text="Decrypt", command=lambda: decryptText(option.get()))
    decryptButton.place(x=355, y=260)


#Function that updates the main window depending on the cipher chosen
def cipherWindows(option):
    global tempFrame
    tempFrame = tk.Frame(root, height=70, width=250)
    tempFrame.place(x=49, y=255)

    key1Label = tk.Label(tempFrame, text='Key 1:')
    global key1Entry
    key1Entry = tk.Entry(tempFrame)

    key2Label = tk.Label(tempFrame, text='Key 2:')
    global key2Entry
    key2Entry = tk.Entry(tempFrame)

    global errorMessage
    errorMessage = tk.StringVar()
    global errorLabel
    errorLabel = tk.Label(tempFrame, textvariable=errorMessage)

    if option == "Double Transposition":
        key1Label.place(x=0, y=0)
        key1Entry.place(x=40, y=0)

        key2Label.place(x=0, y=20)
        key2Entry.place(x=40, y=20)

    elif option == "Vigenere":
        key1Label.place(x=0, y=0)
        key1Entry.place(x=40, y=0)

    elif option == "Skip":
        key1Label.place(x=0, y=0)
        key1Entry.place(x=40, y=0)

    elif option == "Caesar":
        key1Label.place(x=0, y=0)
        key1Entry.place(x=40, y=0)

    else:
        tempFrame.destroy


#Function to encrypt text
def encryptText(choice):
    #Pass text in entry text box to 'aText' variable
    aText = executeText.get("1.0", "end")
    aText = aText[:-1]

    #Flag to detect errors in input of keys
    flag = False

    #If statement to make encrypted text into the type of cipher selected
    if choice == "Double Transposition" and aText != "":
        encryptedText = DoubleTranspositionCipher(aText, key1Entry.get(), key2Entry.get())

    elif choice == "Morse Code" and aText != "":
        encryptedText = MorseCodeCipher(aText)

    elif choice == "Base64" and aText !="":
        encryptedText = base64cipher(aText)

    elif choice == "Vigenere" and aText !="":
        encryptedText = VigenereCipher(aText, key1Entry.get())

    elif choice == "Skip" and aText !="":
        encryptedText = SkipCipher(aText, key1Entry.get())

        #Detects if key entered is a number
        if key1Entry.get().isdigit() == True:

            #If key is not coprime it shows error
            if encryptedText.coprime(len(aText), int(key1Entry.get())) == False:
                flag = True
                errorMessage.set("Error. Key must be a coprime\n number to the length of text.")
                errorLabel.place(x=0, y=20)
            else:
                errorLabel.place_forget()

        else:
            #If key is not a number shows error
            flag = True
            errorMessage.set("Error. Key must a digit.")
            errorLabel.place(x=0, y=20)

    elif choice == "Caesar" and aText !="":
        encryptedText = CaesarCipher(aText, key1Entry.get())

        #If key is not a number it shows error
        if key1Entry.get().isdigit() == False:
            flag = True
            errorMessage.set("Error. Key must a digit.")
            errorLabel.place(x=0, y=20)
        else:
            errorLabel.place_forget()


    #If there is no flag in there is a text than the text is encrypted
    if(aText != "" and flag == False):
        answerText.delete("1.0", "end")
        answerText.insert("1.0", encryptedText.encrypt())


#Function to decrypt text
def decryptText(choice):
    aText = executeText.get("1.0", "end")
    aText = aText[:-1]

    # Flag to detect errors in input of keys
    flag = False

    if choice == "Double Transposition" and aText != "":
        decryptedText = DoubleTranspositionCipher(aText, key1Entry.get(), key2Entry.get())

    elif choice == "Morse Code" and aText != "":
        decryptedText = MorseCodeCipher(aText)

    elif choice == "Base64" and aText != "":
        decryptedText = base64cipher(aText)

    elif choice == "Vigenere" and aText != "":
        decryptedText = VigenereCipher(aText, key1Entry.get())

    elif choice == "Skip" and aText != "":
        decryptedText = SkipCipher(aText, key1Entry.get())

        # Detects if key entered is a number
        if key1Entry.get().isdigit() == True:

            # If key is not coprime it shows error
            if decryptedText.coprime(len(aText), int(key1Entry.get())) == False:
                flag = True
                errorMessage.set("Error. Key must be a coprime\n number to the length of text.")
                errorLabel.place(x=0, y=20)
            else:
                errorLabel.place_forget()

        else:
            # If key is not a number shows error
            flag = True
            errorMessage.set("Error. Key must a digit.")
            errorLabel.place(x=0, y=20)

    elif choice == "Caesar" and aText != "":
        decryptedText = CaesarCipher(aText, key1Entry.get())

        # If key is not a number it shows error
        if key1Entry.get().isdigit() == False:
            flag = True
            errorMessage.set("Error. Key must a digit.")
            errorLabel.place(x=0, y=20)
        else:
            errorLabel.place_forget()

    #If there is no flag in there is a text than the text is encrypted
    if (aText != "" and flag == False):
        answerText.delete("1.0", "end")
        answerText.insert("1.0", decryptedText.decrypt())

#Main program to run
def main():
    mainWindow()
    root.mainloop()

#Runs program
main()