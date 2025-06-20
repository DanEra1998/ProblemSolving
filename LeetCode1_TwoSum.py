from typing import List

class TwoSumSolver:
    def brute_force(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def optimal(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[nums[i]] = i
        return []

    def print_complexities(self):
        print("🔍 Brute Force Method:")
        print("   Time Complexity: O(n^2)")
        print("   Space Complexity: O(1)\n")

        print("⚡ Optimal Method (Hash Map):")
        print("   Time Complexity: O(n)")
        print("   Space Complexity: O(n)")

# Example usage
if __name__ == "__main__":
    solver = TwoSumSolver()
    nums = [2, 7, 11, 15]
    target = 9

    print("Brute Force Result:", solver.brute_force(nums, target))
    print("Optimal Result:", solver.optimal(nums, target))
    solver.print_complexities()
