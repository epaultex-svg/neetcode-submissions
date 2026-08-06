class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l,r = 0, len(matrix) - 1

        mid = 0

        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][-1] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                break

        l,r = 0, len(matrix[mid]) - 1
        mat = matrix[mid]

        while l <= r:
            mid = (l+r)//2

            if mat[mid] > target:
                r = mid - 1
            elif mat[mid] < target:
                l = mid + 1
            else:
                return True
        
        return False










