from collections import Counter

nums = [2,2,3]

#這個檔案主要是用來測試程式碼寫得是否正確
c=Counter(nums)
N=len(nums)
print(max(c.items()))
