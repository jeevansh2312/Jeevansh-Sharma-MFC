# Jeevansh-Sharma-MFC
# Sorting Algorithm Comparison

A Python implementation comparing **Bubble Sort**, **Insertion Sort**, and **Merge Sort**, with theoretical and practical time complexity analysis.

## Algorithms Implemented
1. **Bubble Sort**  
2. **Insertion Sort**  
3. **Merge Sort**  

---

## Time Complexity Analysis

### 1. Bubble Sort
**Mechanism**  
```python
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]: swap
```
- **Best Case**: `O(n)`  
  - Achieved when input is already sorted  
  - Early exit via `swapped` flag (only 1 pass needed)  

- **Average/Worst Case**: `O(n²)`  
  - Nested loops:  
    - Outer loop runs `n` times  
    - Inner loop processes `n-i-1` elements each iteration  
  - Total comparisons ≈ <code>n(n-1)/2</code>  

### 2. Insertion Sort
**Mechanism**  
```python
for i in range(1, len(arr)):
    while j >= 0 and key < arr[j]: shift elements
```
- **Best Case**: `O(n)`  
  - Input already sorted → only 1 comparison per element  

- **Average/Worst Case**: `O(n²)`  
  - Worst when input is reverse-sorted  
  - Total shifts ≈ <code>n(n-1)/2</code>  

### 3. Merge Sort
**Mechanism**  
```python
def merge_sort(arr):
    split → merge_sort(left) → merge_sort(right) → merge
```
- **All Cases**: `O(n log n)`  
  - **Division Phase**:  
    - Input divided into halves → `log₂n` levels  
  - **Merge Phase**:  
    - `O(n)` operations at each level  
  - Total operations = <code>n × log₂n</code>  

---

Sorting Algorithm Comparison
This project compares the time complexity of three sorting algorithms: Bubble Sort, Insertion Sort, and Merge Sort. The analysis is purely theoretical, focusing on how each algorithm performs as the input size grows.

Time Complexity Analysis
1. Bubble Sort
How it works:
Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order. This process continues until no swaps are needed, meaning the list is sorted.

Time Complexity:

Best Case: O(n)

Happens when the input list is already sorted. The algorithm makes one pass through the list and stops early.

Average Case: O(n²)

Occurs when the input list is randomly ordered. The algorithm makes multiple passes, and each pass compares and swaps elements.

Worst Case: O(n²)

Happens when the input list is sorted in reverse order. The algorithm requires the maximum number of comparisons and swaps.

2. Insertion Sort
How it works:
Insertion Sort builds the sorted list one element at a time. It takes each element and inserts it into its correct position in the already sorted part of the list.

Time Complexity:

Best Case: O(n)

Happens when the input list is already sorted. The algorithm simply inserts each element in its correct position without shifting.

Average Case: O(n²)

Occurs when the input list is randomly ordered. The algorithm may need to shift many elements to insert each new element.

Worst Case: O(n²)

Happens when the input list is sorted in reverse order. The algorithm must shift all elements to insert each new element.

3. Merge Sort
How it works:
Merge Sort uses a divide-and-conquer approach. It splits the list into two halves, recursively sorts each half, and then merges the two sorted halves into a single sorted list.

Time Complexity:

Best Case: O(n log n)

Merge Sort always divides the list into halves and merges them, regardless of the input order.

Average Case: O(n log n)

The algorithm consistently performs the same operations, making it efficient for all input types.

Worst Case: O(n log n)

Even in the worst-case scenario, Merge Sort maintains its efficiency due to its divide-and-conquer nature.


