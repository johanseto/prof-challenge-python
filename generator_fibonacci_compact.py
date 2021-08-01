from time import sleep

def fibonacci_gen(max_counter:int):
    a, b = 0, 1
    counter = 0
    while counter < max_counter:
        yield a
        a, b = b, a+b
        counter += 1
if __name__ == "__main__":
 
    for element in fibonacci_gen(5):
        print(element)
        sleep(0.3)
