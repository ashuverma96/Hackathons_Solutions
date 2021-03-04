### Dhruthzuci Questions
#### Question1 :
Write API: Using Python Flask or ExpressJS, Write a REST API that reads the body and  returns JSON.
 
 API Method POST
 URL : /find_symbols_in_names
 
 Input JSON Body of the API:
{
    "chemicals": ['Amazon', 'Microsoft', 'Google'],
    "symbols": ['I', 'Am', 'cro', 'Na', 'le', 'abc']
}
 
 Output: display the chemical names with their symbol surrounded by square brackets:
{
    "result": "[Am]azon, Mi[cro]soft, Goog[le]"
}

### Output of Question1



#### Question 2:
Given two arrays, write a function to compute their intersection.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
 
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:
Each element in the result must be unique.
The result can be in any order.

#### Question 3:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Example 1:
Input: "()"
Output: true
Example 2:
Input: "()[]{}"
Output: true
Example 3:
Input: "(]"
Output: false

#### Question 4:
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:
Input: [2,2,1]
Output: 1
 
Example 2:
Input: [4,1,2,1,2]
Output: 4

