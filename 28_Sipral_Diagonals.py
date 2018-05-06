import numpy as np

#arr = np.ndarray(shape=(s,s), dtype, buffer, offset, strides, order)

class Spiral:
    def __init__(self, size):
        self.arr = np.zeros(shape=(s,s), dtype = np.int64) 
        self.__size = size
        self.__pos = [0,0] #initial position filling
        self.__d = [(self.__size-1)/2,(self.__size-1)/2]
        self.__value = 0

        self.nomove = [0,0]
        self.left = [-1,0]
        self.right = [1,0]
        self.up = [0,1]
        self.down = [0,-1]

    def to_coords(self):
        return [int(sum(x)) for x in zip(self.__pos, self.__d)]
        #return (self.__pos[0] + self.__d[0], self.__pos[1] + self.__d[1])

    def __move(self,movement):
        self.__value+=1 #increment 1 the value
        self.__pos = [int(sum(x)) for x in zip(self.__pos, movement)]

        c = self.to_coords()
        #print(self.__pos)
        self.arr[c[0],c[1]] = self.__value


    def fill_values(self):
        max_ring = int((self.__size-1)/2)

        #start by the origin
        self.__move(self.nomove)

        #for every ring do the following
        for ring in range(0,max_ring):
            #print("ring {}".format(ring))
            self.__move(self.right)

            n_down = 2*ring +1 #number of steps down
            for i in range(0,n_down):
                self.__move(self.down)

            n = 2*ring +2 #for left up right same number of moves
            for i in range(0,n):
                self.__move(self.left)
            for i in range(0,n):
                self.__move(self.up)
            for i in range(0,n):
                self.__move(self.right)

    def sum_diagonals(self):

        diag_sum = 0
        #we use matrix indexes in this case

        #sum part (0,0),(1,1),(2,2)... (size-1,size-1)
        i = 0
        while i < self.__size:
            diag_sum += self.arr[i,i]
            i+=1

        #sum part (0,size-1),(1,size-2)... (size-1,0)
        i = 0
        j = self.__size -1
        while i < self.__size:
            diag_sum += self.arr[i,j]
            i+=1
            j-=1

        #center has been summed twice, must decrease by 1
        diag_sum -=1
        return diag_sum

if __name__ == "__main__":
    s = 1001 #size of the matrix
    m = Spiral(s)
    m.fill_values()
    print(m.arr)
    print("Sum of diagionals is {}".format(m.sum_diagonals()))

