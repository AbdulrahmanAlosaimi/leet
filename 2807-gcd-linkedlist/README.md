Given the head of a linked list `head`, in which each node contains an integer value.


Between every pair of adjacent nodes, insert a new node with a value equal to the **greatest common divisor** of them.


Return *the linked list after insertion.*


The **greatest common divisor** of two numbers is the largest positive integer that evenly divides both numbers.



**Example 1:**

![image](https://github.com/AbdulrahmanAlosaimi/leet/assets/76831852/1cd396a7-5dd9-48ae-a7d9-24c3127811a9)

>**Input:** head = [18,6,10,3]<br>**Output:** [18,6,6,2,10,1,3]<br>**Explanation:** The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).<br>- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.<br>- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.<br>- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.<br>There are no more adjacent nodes, so we return the linked list.



Example 2:

![image](https://github.com/AbdulrahmanAlosaimi/leet/assets/76831852/7a649931-e922-45d8-ab7d-68091e3916c2)

>**Input:** head = [7]<br>**Output:** [7]<br>Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.<br>There are no pairs of adjacent nodes, so we return the initial linked list.
 


**Constraints:**


- The number of nodes in the list is in the range `[1, 5000]`.
- `1 <= Node.val <= 1000`

---
[Problem link](https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/)
