# Double Summation: Compute a double summation

def dsum(n):
    somme = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            somme += 3 * i
    print("The sum is", somme)

if __name__ == "__main__":
    dsum(2)
