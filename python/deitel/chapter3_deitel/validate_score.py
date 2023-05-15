passes = 0
failures = 0

for student in range(10):
    result = 0
    while result != 1 and result != 2:
        result = int(input("Enter result (1 = pass, 2 = fail): "))
        if result == 1:
               passes += 1
        elif(result == 2):
            failures += 1

print("Passed: ", passes)
print("Failed: ", failures)