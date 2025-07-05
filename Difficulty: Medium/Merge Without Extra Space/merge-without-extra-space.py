class Solution:
    def merge(self, a, b):
        left, right = 0, 0;
        len_a = len(a);
        len_b = len(b);
        temp = [];
        while(left < len_a and right < len_b):
            if a[left] < b[right]:
                temp.append(a[left]);
                left += 1;
            else:
                temp.append(b[right]);
                right += 1;
        while (left < len_a):
            temp.append(a[left]);
            left += 1;
        while (right < len_b):
            temp.append(b[right]);
            right += 1;
        return temp;
                  
    def mergeArrays(self, a, b):
        # code here
        len_a = len(a);
        len_b = len(b);
        arr = self.merge(a, b);
        for i in range(0, len_a):
            a[i] = arr[i];
        for j in range(len_b):
            b[j] = arr[len_a + j];
    
        return a, b;