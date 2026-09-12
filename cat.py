def main():
    number = get_number()
    meow(number)

def meow(n):
    for _ in range(n):
        print("meow")

def get_number():
    while True:
        x = int(input("Type a number greater than zero: "))
        if x > 0:
            return x

main()