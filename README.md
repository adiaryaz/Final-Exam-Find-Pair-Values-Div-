# Final Exam Find Pair Values (Div)

Final Exam - A program to find two numbers in an array where one number divided by the other equals a target value.

## 📝 Description

Write a Python function, `find_pair_with_div(arr, target)`, that takes a list of integers and a target integer as input. The function should return a tuple of two numbers (a, b) from the array such that $b / a = \text{target}$. If no such pair exists, return "No proceed".

-----

## 🎯 Problem Statement

### Input:

  * Input 1: An array (list) of integers.
  * Input 2: A target integer (the divisor).

### Output:

  * A tuple `(a, b)` where $b / a = \text{target}$.
  * "No proceed" if no such pair exists or if the target is 0.

### Rules:

1.  The function must find a pair of numbers $(a, b)$ in the array that satisfies the equation $b / a = \text{target}$.
2.  If the `target` is 0, the program must return "No proceed".
3.  If no pair satisfies the condition, return "No proceed".

-----

## 💡 Examples

### Example 1 (Sample 1)

**Input:**

```
[10, 20, 30, 40]
2
```

**Output:**

```
(10, 20)
```

**Explanation:** The pair (10, 20) satisfies the condition, as $20 / 10 = 2$.

### Example 2 (Sample 2)

**Input:**

```
[1, 2, 8, 6, 4]
3
```

**Output:**

```
(2, 6)
```

**Explanation:** The pair (2, 6) satisfies the condition, as $6 / 2 = 3$.

### Example 3 (Sample 3)

**Input:**

```
[10, 30, 40, 50]
100
```

**Output:**

```
No proceed
```

**Explanation:** No pair in the list satisfies the condition.

-----

## 🚀 How to Use

1.  **Clone this repository**

    ```bash
    git clone https://github.com/adiaryaz/find-pair-div.git
    cd find-pair-div
    ```

2.  **Run the program** (assuming the file is `Find Pair Values (Div)_UAS-L4.py`):

    ```bash
    python "Find Pair Values (Div)_UAS-L4.py"
    ```

    Enter the array (e.g., `[10, 20]`) and target on separate lines.

-----
