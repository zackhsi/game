'''
Write a function "solution" that guesses the number!

The "guess" function will either return "too high" or "too low"
'''
from game import guess


# Brute force: try all numbers starting at 0
def solution():
    for i in range(100):
        guess(i)

# Start at 50, go up or down
# def solution():
#     my_guess = 50
#     result = guess(my_guess)
#     if result == 'too high':
#         while True:
#             my_guess = my_guess - 1
#             guess(my_guess)
#     elif result == 'too low':
#         while True:
#             my_guess = my_guess + 1
#             guess(my_guess)


if __name__ == '__main__':
    solution()
