
'''
Write a program to find whether a given number is a power of 2 or not.

Input format:
The first line of the input contains the number n for which you have to find whether it is a power of 2 or not.

Output Format:
Print 'YES' or 'NO' accordingly without quotes.

Example:

Input:
32

Output:
YES

Input:
26

Output:
NO

Explanation:
In the first example, 32 is actually 25 so the answer is YES.
The second number is not a power of 2 hence the answer is NO.

'''
def power_of_two():   
    n=int(input())
    if n>0:
      while n%2==1:
        n=n/2
      if n==0:
        print("YES",end="")
    if n==1 or n!=0:
      print("NO",end="")
  
