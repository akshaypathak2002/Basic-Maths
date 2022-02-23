def product_array(arr):
    count = 0  # for the apperance of zero
    prod = 1  # for the product
    ans = []
    for i in range(len(arr)):
        if arr[i] != 0:  # element is not zero
            prod *= arr[i]
        else:
            count += 1  # That means zero appear
    # Now if only 1 zero we find index of it
    if count == 1:
        index = arr.index(0)
        # Then we need to place the product value on that index where zero appear
        for i in range(len(arr)):
            if i == index:
                ans.insert(i, prod)  # This will insert product at i postion
            else:
                ans.insert(i, 0)  # remaining postion fill with zero
        return ans 
    if count == 2:
        for i in range(len(arr)):
            # If there are 2 zeros then all elements will become zero
            ans.append(0)
        return ans     
    # If no zero has appear
    for i in range(len(arr)):
        ans.insert(i, int(prod/arr[i]))
    return ans


n = int(input())
arr = [int(x) for x in input().split()]
ans = product_array(arr)
# For printing the output
for i in range(len(ans)):
    print(ans[i], end=' ')
