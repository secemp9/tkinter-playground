# tkinter-playground
Just me playing around with tkinter

I like playing around with tkinter, and for some reasons, I find it more fun to do testing with it where I can quickly see what's happening (aka interactive testing), so I made this repository.

I'll try to detail everything here, although this is more of a log of what files does what.

This is my attempt at many things, so I'll try to explain for each file:

# tk_wmattrs.py

1. Automatically assign methods from a class/function to a button
2. Get the list of possible argument for non-documented features (by making an error on purpose, and parsing said error)
3. Double instances of tkinter (so I don't "pollute" the one where all my tools are)
4. Generation of buttons using their number fo argument and type (eg: bool, etc)

# tk_tools_ext.py

This is where all the methods for each features from tkinter I want to test are. I'll try to reuse this in other things, but for now it's just for that.
The methods names are pretty self-explanatory except for the underlying Magic class, which I'm not entirely sure how it works (some [class magician](https://github.com/Aran-Fey) is probably the cause) but I got a vague idea, so I'll detail this entry later when I find out.

The Magic class is mostly helping me in not having to put `self` everywhere (here it's for variables), which, I'm well aware is recommended and the usual thing to do with classes, but in this specific cases, where I want to test things *and* have fun, I don't want to think all the time about the semantics of classes, OOP and whatnot. I plan on adding support for other menials stuff later.
