# functions

def greet():
    return"Artheeson"
print(greet()) 

def greet(name):
    return f"hello {name}"
print(greet("world"))

def get_cutoff(mark):
    total_mark=500
    return (mark / total_mark)*100
print(get_cutoff(423))

# decorator

def my_decorator(function):
    def wrapper():
        print("numbers start")
        function()
        print("numbers end")
    return wrapper
@my_decorator
def count():
    for i in range(10):
        print(i)
        continue
    print(type(i))
count()


def require_staff(function):
    def wrapper(user):
        if user != "staff":
            print("Access denied")
            return
        return function(user)
    return wrapper

@require_staff
def view_dashboard(user):
    print(f"access granted, {user}!")

view_dashboard("student")   
view_dashboard("staff")     



