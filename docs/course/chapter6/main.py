import tkinter as tk

def download():
    url = txt_url.get()
    print(url)

root = tk.Tk()
root.title('Youtube Downloader')

# Define widgets
lbl_url = tk.Label(root, text='Youtube URL')
txt_url = tk.Entry(root, width=30)
btn_download = tk.Button(root, text='Download', command=download)

# Arrange widgets using geometry manager 'pack'
lbl_url.pack()
txt_url.pack(padx=10, fill='x')
btn_download.pack(pady=5)

root.mainloop()