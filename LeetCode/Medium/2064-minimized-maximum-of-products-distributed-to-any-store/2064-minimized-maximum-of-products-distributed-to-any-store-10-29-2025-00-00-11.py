class Solution:
    # Optimal Approach
    # Time Complexity: O(n * log(max(quantities)))
    # Space Complexity: O(1)
    def allocateProducts(self, productQuantity, quantities):
        stores = 0;
        for i in range(len(quantities)):
            products = quantities[i] // productQuantity;
            remaining = quantities[i] % productQuantity
            stores += products;
            if remaining != 0:
                stores += 1;          
        return stores;

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        low = 1;
        high = max(quantities);
        if n == 1:
            return quantities[0];

        while low <= high:
            mid = (low + high) // 2;
            numOfStores = self.allocateProducts(mid, quantities);
            if numOfStores <= n:
                high = mid - 1;
            else:
                low = mid + 1;
            
        return low;
