---
comments: true
---

This will be our first official coding activity for this course.

In this activity, you may be using the following programming concepts:

- Classes and Objects
- Graphical User Interface with tkinter
- Usage of external libraries
- Usage of of standard library

## Activity

Create a GUI application with the following specifications.

- There will be a main window, you can create a custom class for the main frame if you want
- The window shall have two main panes, left and right pane. (You can use either pack or grid geometry management)
- The left pane will display a list of all images in a directory, to be selected by the user.
- The right pane will display a canvas

For the tutorials of canvas and treeview, please see the following:

- [https://tkdocs.com/tutorial/canvas.html](https://tkdocs.com/tutorial/canvas.html)
- [https://tkdocs.com/tutorial/tree.html](https://tkdocs.com/tutorial/tree.html)

For getting the list of all images, use the `os` module from the python standard library, specifically at
[https://docs.python.org/3/library/os.html#os.listdir](https://docs.python.org/3/library/os.html#os.listdir)

To filter the files so that only images are displayed, check for each filename that must have '.jpg' extensions with the
built-in string method `endswidth()`.

For example, to check if a given string ends with `.xyz`, we do

```py
fp = 'sample.xyz'

fp.endswith('xyz') # Returns True
```

For the user to select a folder, you will add a menu for the application. Please see the documentation for adding menu at

[https://tkdocs.com/tutorial/menus.html](https://tkdocs.com/tutorial/menus.html) and for a tutorial blog if you get confused

[https://pythonbasics.org/tkinter-menu/](https://pythonbasics.org/tkinter-menu/)

Inside the menu is a menu called 'Select Folder' maybe under 'File' menu. This should open a filde dialog for selecting a folder.
Look at `tk.filedialog` module. There should be a `filedialog.askdirectory()` method.

Please take note that this exercise will practice you to find and read documentations about the language and tools
that we will be suing. This is how programming in the real world is done.

For any queries about this activity, post it in the comment below.
