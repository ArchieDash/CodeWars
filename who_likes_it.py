def like(func):
    def wrapper(*args):
        if len(*args) <  2:
            return func(*args) + " likes this"
        else:
            return func(*args) + " like this"
    return wrapper


@like
def likes(names: list) -> str:
    if names:
        if len(names) == 1:
            return names[0]
        elif len(names) == 2:
            return " and ".join(names) 
        elif len(names) == 3:
            return f"{names[0]}, {names[1]} and {names[2]}"
        elif len(names) > 3:
            return f"{names[0]}, {names[1]} and {len(names)-2} others"
    else:
        return "no one" 


#print(likes([]))
#print(likes(["Peter"]))
#print(likes(['Jacob', 'Alex']))
#print(likes(['Max', 'John', 'Mark']))
#print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
