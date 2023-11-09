import tkinter as tk
import tkinter.filedialog as fd
import rarfile
import os

def extract_rar(archive_file, extract_path):
    with rarfile.RarFile(archive_file, 'r') as rf:
        rf.extractall(extract_path)

def browse_files():
    filetypes = (("RAR files", "*.rar"), ("All files", "*.*"))
    archive_file = fd.askopenfilename(filetypes=filetypes)
    if archive_file:
        desktop_path = os.path.expanduser("~/Desktop")
        extract_rar(archive_file, desktop_path)

# Создание графического интерфейса
window = tk.Tk()
window.title("RAR Extractor")

browse_button = tk.Button(window, text="Выбрать архив", command=browse_files)
browse_button.pack(pady=20)

window.mainloop()