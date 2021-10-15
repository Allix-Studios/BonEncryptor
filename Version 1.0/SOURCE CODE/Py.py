import os
import tkinter.filedialog
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from tkinter import *

finish1 = True
finish2 = True
def encrypt(key, filename, out_file_name):
    try:
        chunks = 32 * 1024
        file_size = str(os.path.getsize(filename)).zfill(16)
        IV = Random.new().read(16)
        encryptor = AES.new(key, AES.MODE_CFB, IV)
        with open(filename, 'rb') as f_input:
            with open(out_file_name, 'wb') as f_output:
                f_output.write(file_size.encode('utf-8'))
                f_output.write(IV)
                while True:
                    chunk = f_input.read(chunks)
                    if len(chunk) == 0:
                        messagebox.showinfo("100%", "ITS ENCRYPTED")
                        break
                    if len(chunk) % 16 != 0:
                        chunk += b' ' * (16 - (len(chunk) % 16))
                    f_output.write(encryptor.encrypt(chunk))
    except:
        messagebox.showerror("ERROR", "ERROR BY ENCRYPTION")
    

def decrypt(key, filename, out_file_name):
    try:
        chunks = 32 * 1024
        with open(filename, 'rb') as f_input:
            filesize = int(f_input.read(16))
            IV = f_input.read(16)
            decryptor = AES.new(key, AES.MODE_CFB, IV)
            with open(out_file_name, 'wb') as f_output:
                while True:
                    chunk = f_input.read(chunks)
                    if len(chunk) == 0:
                        messagebox.showinfo("100%", "ITS DENCRYPTED")
                        break
                    f_output.write(decryptor.decrypt(chunk))
                    f_output.truncate(filesize)
    except:
        messagebox.showerror("ERROR", "ERROR BY DENCRYPTION")

def get_key(password):
    hashing = SHA256.new(password.encode('utf-8'))
    return hashing.digest()
def grafick():
    def startenc():
        password = entry3.get()
        filename = entry1.get()
        outputfilename = entry2.get()
        encrypt(get_key(password), filename, outputfilename)
    def startdec():
        password = entry3.get()
        filename = entry1.get()
        outputfilename = entry2.get()
        decrypt(get_key(password), filename, outputfilename)
    def openone():
        entry1.delete(0,END)
        file = askopenfilename()
        entry1.insert(10,file)
    def opentwo():
        entry2.delete(0,END)
        file = tkinter.filedialog.asksaveasfilename()
        entry2.insert(10,file)
    app = Tk()
    app.title("BON ENCRYPT")
    app.config(width=350 ,height=250)
    Anzeige = Label(app, text = "Willkommen bei BON ENCRYPT")
    Anzeige.place(x = 80, y = 20 )
    Button1 = Button(app, text="Dursuchen" ,command=openone)
    Button1.place(x = 20, y= 60)
    entry1 = Entry(app, width = 25)
    entry1.place(x = 125, y= 65)
    Button2 = Button(app, text="Speichern", command=opentwo)
    Button2.place(x = 20 , y = 110)
    entry2 = Entry(app, width = 25)
    entry2.place(x =125, y = 115)
    Anzeige2 = Label(app, text = "Passwort")
    Anzeige2.place(x = 130, y = 150)
    entry3 = Entry(app, width = 40)
    entry3.place(x = 10 ,y = 170)
    Button3 = Button(app, text="ENCRYPT", command=startenc)
    Button3.place(x = 50 , y = 200)
    Button4 = Button(app, text="DECRYPT", command=startdec)
    Button4.place(x = 180 , y = 200)
    app.mainloop()
grafick()