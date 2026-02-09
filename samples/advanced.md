# fast-slides 高级功能演示

## 1. 渐变垂直幻灯片

渐变垂直幻灯片可以实现内容的渐入效果。

++++

这是第一部分内容，会渐入显示。

++++

这是第二部分内容，会在第一部分之后渐入显示。

++++

这是第三部分内容，会在第二部分之后渐入显示。

---

## 2. 数学公式

支持 LaTeX 数学公式：

行内公式：$E = mc^2$

块级公式：

$$
\int_0^1 x^2 dx = \frac{1}{3}
$$

---

## 3. 多语言代码高亮

### Python

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

### JavaScript

```javascript
function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

console.log(fibonacci(10)); // 55
```

### C++

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, fast-slides!" << endl;
    return 0;
}
```

---

## 4. 图片布局

### 居中图片

<img class="float-center" src="https://via.placeholder.com/400x300" alt="居中图片">

### 右对齐图片

<img class="float-right" src="https://via.placeholder.com/200x200" alt="右对齐图片">

这是右对齐图片旁边的文本。右对齐图片不会占据文本流的空间，所以文本会环绕在图片周围。

---

## 5. 复杂列表

### 嵌套列表

- 一级列表项 1
  - 二级列表项 1.1
  - 二级列表项 1.2
- 一级列表项 2
  - 二级列表项 2.1
    - 三级列表项 2.1.1
    - 三级列表项 2.1.2

### 任务列表

- [x] 已完成任务 1
- [x] 已完成任务 2
- [ ] 未完成任务 1
- [ ] 未完成任务 2
