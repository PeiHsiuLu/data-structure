#這個檔案主要是用來測試程式碼寫得是否正確

this_dic={}
multiply=1
arr = [1,2,3,5]
k=3
for x in arr:
    multiply*=x
    
print(multiply)

for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        this_dic[multiply/arr[j]*arr[i]]=[arr[i],arr[j]]
keys_view = this_dic.keys()
keys_list = list(keys_view)
print(keys_list)

s_key_list=sorted(keys_list)
value=s_key_list[k-1]
print(this_dic[value])