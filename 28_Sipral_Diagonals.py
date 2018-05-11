if __name__ == "__main__":
    s = 1001 #size of the matrix
    rings = int((s-1)/2) #number of rings
    i = 1
    d = list()
    d.append(i)
    for r in range(rings):
        for k in range(4):
            i += 2*r + 2
            d.append(i)
    print(sum(d))
