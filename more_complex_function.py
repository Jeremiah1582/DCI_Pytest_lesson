myString = "  PyLint, a  widely uSed tool that checks for .errors. in Python code and encourages good Python coding patterns, Is integrated into Visual Studio for Python projects. Run PyLint. In Visual Studio, right-click a Python project in Solution Explorer and select Python and then "

def remove_double_space(func): #func refers to the function being decorated (format_text)
    def wrapper(*args, **kwargs): #args & kwargs refers to format_text()'s arguments  
        new_text = func(*args, **kwargs).replace("  ", "") #func(*args, **kwargs) === myString
        return new_text
    return wrapper
    
def remove_space_before_fullstop(func):
    def wrapper(*args, **kwargs):    
        new_text = func(*args, **kwargs).replace(" .", ". ")
        return new_text
    return wrapper

def remove_double_fullstop(func):
    def wrapper(*args, **kwargs): 
        new_text = func(*args, **kwargs).replace("..", ".")
        return new_text
    return wrapper

@remove_double_space
@remove_space_before_fullstop
@remove_double_fullstop
def format_text(text):
    return text


new_text = format_text(myString)
print("New text:", new_text)
