from email.policy import default


def main() -> None:
    print("Simple Calculator")

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = float(num1) + float(num2)

print (result)