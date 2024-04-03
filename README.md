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
```python
# 創建一個整數陣列
my_array = [1, 2, 3, 4, 5]

# 創建一個字符串陣列
str_array = ["apple", "banana", "orange"]
```

# Linked List

Linked list是一種常見的線性數據結構，它由一系列節點組成，每個節點包含數據域和指向下一個節點的指針。

## 特點

- Linked list中的每個節點包含兩個字段：數據域用於存儲數據，指針域用於指向下一個節點。
- 最後一個節點的指針域通常為空，表示結尾。
- Linked list可以是單向的或雙向的。

## 優點

- 動態分配內存，大小不固定。
- 插入和刪除操作的時間複雜度為O(1)，即使在中間插入或刪除節點也是如此。

## 缺點

- 不支持隨機訪問，訪問某個元素的時間複雜度為O(n)。
- 需要額外的空間來存儲指針。

## 類型

1. 單向鏈表（Singly Linked List）
2. 雙向鏈表（Doubly Linked List）
3. 循環鏈表（Circular Linked List）

## 範例程式碼（Python）

### 單向鏈表

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

# 使用範例
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.print_list()
```
### 雙向鏈表
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

# 使用範例
if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.print_list()
```
# 專題連結區


