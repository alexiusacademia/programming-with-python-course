---
comments: true
---

# Chapter 6: Building a Simple Desktop Youtube Downloader

In this chapter, we will be building from the user interface we've shown on chapter 5. We will be building a simple youtube video downloader using a third-party library. In this chapter, we will
exercise more on the concept of classes and objects and usage of a third-party library.

## The Interface

We will be using the user interface from the previous chapter:

![](../course/chapter5/tkinter2/tkinter2.png)

And so we will also be using the code to build it:

```py
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
```

In the listing above, on line
