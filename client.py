import ftplib
import os
import time
from tkinter import Tk, filedialog
from pathlib import Path

HOSTNAME = "your_ftp_hostname"
USERNAME = "your_ftp_username"
PASSWORD = "your_ftp_password"

def browseFiles():
    global textarea, filepathLabel
    Tk().withdraw()
    filename = filedialog.askopenfilename()
    filepathLabel.config(text="Selected File: " + filename)
    
    with open(filename, "rb") as file:
        ftp = ftplib.FTP(HOSTNAME)
        ftp.login(USERNAME, PASSWORD)
        ftp.cwd("sharing_files")
        ftp.storbinary("STOR " + os.path.basename(filename), file)
        ftp.dir()
        ftp.quit()

if __name__ == "__main__":
    textarea = None  # Set the appropriate textarea widget
    filepathLabel = None  # Set the appropriate filepathLabel widget
    browseFiles()
