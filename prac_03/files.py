name = input("What is your name? ")
file = open('name.txt', 'w')
file.write(name)
file.close()

file = open('name.txt', 'r')
name = file.read()
print(f"Your name is {name}")
file.close()

file = open('numbers.txt', 'r')
first_number = int(file.readline())
second_number = int(file.readline())
result = first_number + second_number
print(f"The sum of the first two numbers is {result}")
file.close()


file_name = "numbers.txt"  # Insert desired file name in quotes
file = open(file_name, 'r')
total = 0
for line in file:
    all_numbers = int(line.strip())
    total += all_numbers
print(f"The sum of all numbers is {total}")
file.close()
