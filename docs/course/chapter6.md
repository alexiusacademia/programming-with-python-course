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

In the listing above, on line 17, we added the padding for horizontal with `padx` and the `fill='x'` to
make the entry expand horizontally when the window is resized.

Line 3-5 is a function that we will be dealing with later. For now, it just gets the content of the `txt_url` entry and
prints it to the console, but later, we will using this to add the logic for the download of the best quality video
available for the youtube video given.

## The library

In this project, we will be using the `yt-dlp` library. As the other libraries, `pytube` and `youtube-dl` is giving
some issues, we will be using this one for now.

To install the library:

```
pip install yt-dlp
```

This will install the `yt-dlp` alongside with other pre-requisite libraries:

- `Brotli`
- `certifi`
- `mutagen`
- `pycryptodomex`
- `websockets`

Now let's create a new class in a new file. For this let's call it `downloader.py` or name it anything you want.

```py title="downloader.py"
import yt_dlp

class Downloader:
    def __init__(self, url: str):
        self.url = url

    def download(self):
        """
        Download the video.

        Args:
            format_id (str): The format id selected.
        """
        ydl_opts = {
            'format': 'best[ext=mp4]/best'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])
```

This class has a constructor that takes url as a required argument so we must pass it
in the object initialization from our main code like this.

```
downloader = Downloader(url)
```

So now, our download function would be like below:

```
import tkinter as tk
from downloader import Downloader

def download():
    url = txt_url.get()

    downloader = Downloader(url)
    downloader.download()

####
####
```

Our `main.py` now will be

```py title="main.py"
import tkinter as tk
from downloader import Downloader

def download():
    url = txt_url.get()

    downloader = Downloader(url)
    downloader.download()

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

Now you can run the program and paste a youtube url in the entry. Then click on the Download button.
This will download the video with the best format in your current directory.

In summary, we have tackled the following:

- Created a new class `Downloader`
- Using the third party package `yt-dlp`
- Object initialization and usage of the constructor with parameter `downloader = Downloader(url)`
- We created a method called `download` inside our class for downloading

In the next chapter, we will be using a treeview to display the available video formats
in a tabulated form so that the user can select (double-click) an item to download, we will also display
the progress of download in a progress bar with the help of threading for multitasking.

The code for this chapter can be access on this website's repository or you can directly go into this link
[https://github.com/alexiusacademia/programming-with-python-course/tree/main/docs/course/chapter6](https://github.com/alexiusacademia/programming-with-python-course/tree/main/docs/course/chapter6)

I hope you gained something from this. For any queries, jsut ask in the comment below. Thanks!
