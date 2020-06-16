'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, memo={}):
    # Your code here

    if n in memo:
        return memo[n]

    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        memo[n] = eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)
        return memo[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
