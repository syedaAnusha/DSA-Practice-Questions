class Solution:
    # Optimal Approach - 02
    # Time Complexity: O(n)
    # Space Complexity: O(3) // atmost 3 unique elements 
    def totalFruit(self, fruits: List[int]) -> int:
        maxFruits = 0;
        totalFruits = len(fruits);
        left = right = 0;
        setBasket = {};
        while right < totalFruits:
            if fruits[right] in setBasket:
                setBasket[fruits[right]] += 1;
            else:
                setBasket[fruits[right]] = 1;
            if len(setBasket) <= 2:
                maxFruits = max(maxFruits,right-left+1);
            if len(setBasket) > 2:
                setBasket[fruits[left]] -= 1;
                if setBasket[fruits[left]] == 0:
                    setBasket.pop(fruits[left]);
                left += 1;
            right += 1;
        return maxFruits;