# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:28:37 2024

@author: Arjun
"""

def hofstadter_q(n):
    result = [0, 1, 1]
    for i in range(3, n+1):
        result.append(result[i-result[i-1]] + result[i-result[i-2]])
    
    result.pop(0)
    print(result.pop())
    return 1

def main():
    hofstadter_q(1000)
    
main()