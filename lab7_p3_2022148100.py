
class not2DError(Exception):
# Error for 1D list
    def __str__(self):
        return '[ERROR]: list is not 2D.'

class unevenListError(Exception):
# Error for uneven list
    def __str__(self):
        return '[ERROR]: inner lists are not same in length.'

class improperMatrixError(Exception):
# Error for incompatible matmul pair
    def __str__(self):
        return '[ERROR]: [a][b]*[c][d] not b==c.'


def mul1d(arr1,arr2):
    # arr1 * arr2
    # [1,2,3] * [4,5,6]
    # return  1*4 + 2*5 + 3*6
    sum = 0
    for i in range(len(arr1)):
        sum += arr1[i] * arr2[i]
    return sum

class list_D2(list):
    def __init__(self, arr):
        # Check if arr is a 2D list and if all inner lists are of the same length
        if not all(isinstance(inner, list) for inner in arr):
            raise not2DError()
        if not all(len(inner) == len(arr[0]) for inner in arr):
            raise unevenListError()
        self.extend(arr)

    def __str__(self):
        # Return the dimensions of the 2D list
        return f'list_2D: {len(self)}*{len(self[0])}' if self else 'list_2D: 0*0'

    def transpose(self):
        # Transpose the 2D list
        return list_D2([list(row) for row in zip(*self)])

    def __matmul__(self, other):
        # Matrix multiplication
        if len(self[0]) != len(other):
            raise improperMatrixError()
        result = [[mul1d(row, col) for col in zip(*other)] for row in self]
        return list_D2(result)

    def avg(self):
        # Calculate the average of all elements
        total_elements = sum(len(row) for row in self)
        total_sum = sum(sum(row) for row in self)
        return total_sum / total_elements if total_elements > 0 else 0
