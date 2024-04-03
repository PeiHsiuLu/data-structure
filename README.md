# 112-2 師大科技系資料結構 
授課教師：蔡芸琤教授  
姓名：呂沛修  
系級：科技系二年級

# 基礎資料結構

# 陣列 (Array)

## 一、概述

### 1.1 定義
陣列是一種常見的資料結構，用於存儲相同類型的元素集合。

### 1.2 特性
- **固定大小**：一旦創建，大小無法更改。
- **隨機訪問**：可通過索引直接訪問任何元素，訪問時間為常量時間（O(1)）。
- **連續記憶體空間**：元素在記憶體中佔據連續位置，提高訪問效率。
- **相同類型的元素**：所有元素應該是相同類型的。

## 二、操作

### 2.1 基本操作
- **創建陣列**：指定大小和元素類型。
- **訪問元素**：通過索引訪問特定元素。
- **修改元素**：通過索引修改元素。
- **添加元素**：某些語言提供在末尾添加元素的方法。
- **刪除元素**：某些語言提供刪除特定元素的方法。
- **查找元素**：查找特定元素的索引或是否存在。

### 2.2 實現方式
- **靜態陣列（Static Array）**：編譯時分配固定大小的記憶體。
- **動態陣列（Dynamic Array）**：運行時分配記憶體，大小可以動態調整。

## 三、時間複雜度

| 操作           | 時間複雜度     |
|----------------|--------------|
| 訪問元素       | O(1)         |
| 插入/刪除（特定位置）| O(n)      |
| 插入/刪除（末尾）     | O(1) 或 O(n)|
| 搜索元素       | O(n) 或 O(log n) |

（二分搜索僅適用於已排序陣列）

這些是陣列的基本概念、操作和時間複雜度，它們提供了一個有效的方法來組織和存儲數據。  

## 四、例子  

### 4.1 創建陣列
```markdown
# 創建一個整數陣列
my_array = [1, 2, 3, 4, 5]

# 創建一個字符串陣列
str_array = ["apple", "banana", "orange"]

專題連結區
課程筆記區
