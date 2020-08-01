def median(X, Y, n): 
      
    if n == 1:
        return (X[0] + Y[0])/2
    if X[n/2] < Y[n/2]:
        return median(X[(n/2 + 1):n], Y[0:n/2], n/2) 
    return median(X[0:n/2], Y[(n/2 + 1):n], n/2)

if __name__ == '__main__': 
    n = 3
    X = [10, 12, 2000]  
    Y = [34, 80, 500]
    print("median of both of the arrays is", median(X, Y, n))
