def classify_number(n):
    factors_sum = sum([i for i in range(1, n) if n % i == 0])
    
    if factors_sum == n:
        return "Perfect"
    elif factors_sum > n:
        return "Abundant"
    else:
        return "Deficient"
    
print(classify_number(6))  
print(classify_number(12)) 
print(classify_number(8))  