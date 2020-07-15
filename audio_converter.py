
from tkinter import * 
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename 
from pydub import AudioSegment
import tkinter as tk
import tkinter.messagebox as messagebox

file_path = file_name = file_ext=""

def listToString(array):  
	string = ""  
	for character in array:  
		string += character   
	return string  

def get_filename(filename_label,convert_butt): 
	global file_path, file_name, file_ext
	file_path = askopenfilename(filetypes=(('M4A','*.m4a'),('MP3','*.mp3')))
	file_name=file_path.split("/")[-1]
	file_ext = file_name.split(".")[-1]
	file_name=file_name.split(".")
	file_name.pop()
	file_name = listToString(file_name)
	messagebox.showinfo("Info","Audio File Selected : "+file_path)
	filename_label.config(text = 'Filename : '+file_path)
	convert_butt["state"]=tk.NORMAL

def convert(spinner,convert_butt):
	convert_butt["state"]=tk.DISABLED
	global file_path, file_name, file_ext
	try :
		volume = int(spinner.get())
	except:
		messagebox.showerror("Error","Select Valid Decibel Value")
		convert_butt["state"]=tk.NORMAL
		return
	messagebox.showinfo("Info","Audio File is being processed, Please Wait!")
	if file_ext=="m4a":
		wav_audio = AudioSegment.from_file(file_path, format="m4a")
		file_path_list=file_path.split("/")
		file_path_list.pop()
		new_file_path = ""
		for directory in file_path_list:
			new_file_path  = new_file_path + directory + "/"
		new_file_path = new_file_path+file_name+".mp3"
		wav_audio.export(new_file_path, format="mp3")
		file_path = new_file_path
	song = AudioSegment.from_mp3(file_path)
	louder_song = song + volume
	louder_song.export(file_path, format='mp3')
	messagebox.showinfo("Info","Audio File Exported to "+file_path)
	convert_butt["state"]=tk.NORMAL

root = Tk() 
root.title('Audio Converter')
root.geometry('300x250') 
filename_label = tk.Label(root, text="Filename : ")
spinner_label = tk.Label(root, text="Select Decibel Value Below : ")
spinner = Spinbox(root, from_=5, to=150)
convert_butt = Button(root, text ='Convert', command = lambda:convert(spinner,convert_butt),state=tk.DISABLED) 
file_dialog = Button(root, text ='Select File', command = lambda:get_filename(filename_label,convert_butt)) 
filename_label.pack(side = TOP, pady = 10) 
file_dialog.pack(side = TOP, pady = 10) 
spinner_label.pack(side = TOP, pady = 10)
spinner.pack()
convert_butt.pack(side = TOP, pady = 10) 
mainloop() 







