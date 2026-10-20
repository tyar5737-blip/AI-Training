for i in range(5):
    print(i)
    
scores = [75,65,77,88,44]
for score in scores:
    print(scores)
    
    
    count = 1
    while count  <=5:
        print(count)
        count  +=1
        
        
        
scores = [45, 70, 85, 30, 90, 55]

total = 0
pass_count = 0
fail_count = 0

for score in scores:
    total += score
    if score >= 40:
        pass_count += 1
    else:
        fail_count += 1

average = total / len(scores)

print("Total:", total)
print("Average:", average)
print("Passed:", pass_count)
print("Failed:", fail_count)