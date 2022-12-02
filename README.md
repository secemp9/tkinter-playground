# tkinter-playground
Just me playing around with tkinter

I like playing around with tkinter, and for some reasons, I find it more fun to do testing with it where I can quickly see what's happening (aka interactive testing), so I made this repository.

I'll try to detail everything here, although this is more of a log of what files does what.

This is my attempt at many things, so I'll try to explain for each file:

# tk_wmattrs.py

1. Automatically assign methods from a class/function to a button
2. Get the list of possible argument for non-documented features (by making an error on purpose, and parsing said error)
3. Automating creation of classes, or at least, it's underling components (eg: adding self to class's variable, etc)
4. Double instances of tkinter (so I don't "pollute" the one where all my tools are)
5. Generation of buttons using their number fo argument and type (eg: bool, etc)

# tk_tools_ext.py

This is where all the methods for each features from tkinter I want to test are. I'll try to reuse this in other things, but for now it's just for that.
The methods names are pretty self-explanatory except for the underlying Magic class, which I'm not entirely sure how it works (some [class magician](https://github.com/Aran-Fey) is probably the cause) but I got a vague idea, so I'll detail this entry later when I find out.
