# Print multiplication table from 1 to 10
for i in range(1, 11):
    print(f"Multiplication table for {i}:")
    for j in range(1, 11):
        result = i * j
        print(f"{i} * {j} = {result}")
    print()  
