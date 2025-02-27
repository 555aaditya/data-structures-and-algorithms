# https://www.youtube.com/watch?v=o4XveLyI6YU&t=144s

# defining a function
def print1():
    print("Hello")
    print(f"__name__ = {__name__}")

# calling the function
if __name__ == "__main__":
    print1()

# this only prints the own method if it is called itself 
# else it will print for the imported function only