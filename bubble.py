# Bubble Sort Algorithm

class Bubble:

    def __init__(self, arr) -> None:
        self.arr = arr

    def logic(self):
        n = len(self.arr)
        swap = False

        for i in range(n):
            for j in range(0, n-i-1):
                if self.arr[j] >= self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    swap = True
            
            if swap == False:
                break

if __name__ == '__main__':
    arr = [10, 5, -3, 0, -5, 2, 5, 1]
    sort = Bubble(arr=arr)
    sort.logic()
    print('Sorted Array:')
    for i in range(len(arr)):
        print(arr[i], end=' ')