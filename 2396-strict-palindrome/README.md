An integer `n` is **strictly palindromic** if, for **every** base `b` between `2` and `n - 2` (**inclusive**), the string representation of the integer `n` in base `b` is **palindromic**.



Given an integer `n`, return `true` _if_ `n` _is **strictly palindromic** and_ `false` _otherwise_.



A string is **palindromic** if it reads the same forward and backward.




**Example 1:**



>**Input:** n = 9<br>**Output:** false<br>**Explanation:** In base 2: 9 = 1001 (base 2), which is palindromic.<br>In base 3: 9 = 100 (base 3), which is not palindromic.<br>Therefore, 9 is not strictly palindromic so we return false.<br>Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.



**Example 2:**


>**Input:** n = 4<br>**Output:** false<br>**Explanation:** We only consider base 2: 4 = 100 (base 2), which is not palindromic.<br>Therefore, we return false.


**Constraints:**


- `4 <= n <= 105`
