from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("400x300")
root.title("YouTube Video Downloader")

def download():
	try:
		status.set("Downloading...")
		root.update()
		YouTube(link.get()).streams.get_by_resolution(resolution.get()).download()
		status.set("Video Dowloaded Successfully")
	except Exception as e:
		status.set("Please check the link or\n choose another resolution")
		root.update()

Label(root, text="Youtube Downloader", font="Consolas 15 bold").grid(row=0,column=1,padx=10,pady=10)
Label(root, text="Enter video link").grid(row=1,column=0,padx=10,pady=20)
link= StringVar()
link.set("Enter link here")
Entry(root, textvariable=link).grid(row=1,column=1)
options = ["1080p","720p","480p","360p","240p","144p"]
resolution = StringVar()
resolution.set("480p")
Label(root, text="Resolution").grid(row=2,column=0)
drop = OptionMenu(root, resolution, *options).grid(row=2, column=1)
Button(root, text='Download', command=download).grid(row=3, column=1,padx=30,pady=30)
status = StringVar()
status.set("")
status_label = Label(root, textvariable=status).grid(row=4,column=1)
root.update()
root.mainloop()
