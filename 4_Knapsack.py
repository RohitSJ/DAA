import time

def knapsack_dp(weights, values, capacity):
    n = len(values)
    
    dp = [[0 for x in range(capacity + 1)] for y in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    print("\nDP Table:")
    for row in dp:
        print(row)
    
    return dp[n][capacity]

n = int(input("Enter the number of items: "))

weights = []
values = []

for i in range(n):
    weight = int(input(f"Enter weight of item {i+1}: "))
    value = int(input(f"Enter profit of item {i+1}: "))
    weights.append(weight)
    values.append(value)

capacity = int(input("Enter the capacity of the knapsack: "))

start_time = time.time()

max_value = knapsack_dp(weights, values, capacity)

end_time = time.time()

print(f"\nThe maximum value that can be carried is {max_value}")
print(f"Execution time: {end_time - start_time} seconds")
