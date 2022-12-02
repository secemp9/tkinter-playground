import inspect, types

# magic from Aran-Fey, so I don't need to type self on each variable...no, I'm not lazy!
class Magic(dict):
    def __init__(self, globals_, builtins):
        self.globals_ = globals_
        self.builtins = builtins

    def __getitem__(self, key):
        try:
            return self.globals_[key]
        except KeyError:
            pass

        try:
            return self.builtins[key]
        except KeyError:
            pass

        frame = inspect.currentframe().f_back
        try:
            return getattr(frame.f_locals['self'], key)
        finally:
            frame = None


def magic(cls):
    for name, obj in vars(cls).items():
        if not hasattr(obj, '__globals__'):
            continue
        # try:
        if hasattr(obj, "__builtins__"):
            obj = types.FunctionType(
                obj.__code__,
                Magic(obj.__globals__, obj.__builtins__),
                obj.__name__,
                obj.__defaults__,
                obj.__closure__,
            )
        elif hasattr(obj.__globals__['__builtins__'], "__dict__") and not hasattr(obj, "__builtins__"):
            obj = types.FunctionType(
                    obj.__code__,
                    Magic(obj.__globals__, vars(obj.__globals__['__builtins__'])),
                    obj.__name__,
                    obj.__defaults__,
                    obj.__closure__,
                )
        elif not hasattr(obj.__globals__['__builtins__'], "__dict__") and not hasattr(obj, "__builtins__"):
            obj = types.FunctionType(
                    obj.__code__,
                    Magic(obj.__globals__, dict(obj.__globals__['__builtins__'])),
                    obj.__name__,
                    obj.__defaults__,
                    obj.__closure__,
                )

        setattr(cls, name, obj)

    return cls


@magic
class Testme:
    def __init__(self):
        self.important_var = ""
        self.container = ""

    def topmost(self):
        todo = "topmost"
        if important_var.get(todo) == "": # activate it here
            container.get(2).wm_attributes("-" + todo, True)
            important_var.update({todo: True})
        elif important_var.get(todo) == True:
            container.get(2).wm_attributes("-" + todo, False)
            important_var.update({todo: False})
        elif important_var.get(todo) == False:
            container.get(2).wm_attributes("-" + todo, True)
            important_var.update({todo: True})
        print(important_var)

    def fullscreen(self):
        todo = "fullscreen"
        if important_var.get(todo) == "": # activate it here
            container.get(2).wm_attributes("-" + todo, True)
            important_var.update({todo: True})
        elif important_var.get(todo) == True:
            container.get(2).wm_attributes("-" + todo, False)
            important_var.update({todo: False})
        elif important_var.get(todo) == False:
            container.get(2).wm_attributes("-" + todo, True)
            important_var.update({todo: True})
        print(important_var)

    def toolwindow(self):
        todo = "toolwindow"
        if important_var.get(todo) == "": # activate it here
            container.get(2).wm_attributes("-" + todo, True)
            important_var.update({todo: True})
        elif important_var.get(todo) == True:
            container.get(2).wm_attributes("-" + todo, False)
            important_var.update({todo: False})
        elif important_var.get(todo) == False:
            container.get(2).wm_attributes("-" + todo, True)
            important_var.update({todo: True})
        print(important_var)

    def disabled(self):
        todo = "disabled"
        if important_var.get(todo) == "": # activate it here
            container.get(2).wm_attributes("-" + todo, True)
            important_var.update({todo: True})
        elif important_var.get(todo) == True:
            container.get(2).wm_attributes("-" + todo, False)
            important_var.update({todo: False})
        elif important_var.get(todo) == False:
            container.get(2).wm_attributes("-" + todo, True)
            important_var.update({todo: True})
        print(important_var)

    def alpha(self): # this one is not done yet
        # print(container)
        todo = "alpha"
        if important_var.get(todo) == "": # activate it here
            container.get(2).wm_attributes("-" + todo, "1.0")
        else:
            container.get(2).wm_attributes("-" + todo, important_var.get(todo))
