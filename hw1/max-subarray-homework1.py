import sys
import time

# Usage when run from the command line: python max_subarray_algs.py <filename>.
# Example usage:                        python max_subarray_algs.py num_array_500.txt

file_name = sys.argv[1]

f = open(file_name, "r")
A = [int(num) for num in f.readline().strip().split(" ")]
f.close()

def max_subarray_enumeration(A):
    """
    Computes the value of a maximum subarray of the input array by "enumeration."
    
    Parameters:
        A: A list (array) of n >= 1 integers.
    
    Returns:
        The sum of the elements in a maximum subarray of A.
    """

    max=-5000
    n=len(A)
    for i in range(n):
        for j in range(i,n):
            sum=0
            for k in range(i,j+1):
                sum+=A[k]
                if sum > max:
                    max=sum
                    ii=i
                    jj=j
    print(max,ii,jj)


    # TODO: Implement this function!
    return (max,ii,jj)
    
def max_subarray_iteration(A):
    """
    Computes the value of a maximum subarray of the input array by "iteration."
    
    Parameters:
        A: A list (array) of n >= 1 integers.
    
    Returns:
        The sum of the elements in a maximum subarray of A.
    """
    max=-5000
    n=len(A)
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=A[j]
            if sum > max:
                max=sum
                ii=i
                jj=j
    print(max,ii,jj)

    # TODO: Implement this function!
    return (max,ii,jj)
  
def max_subarray_simplification_delegation(A):
    """
    Computes the value of a maximum subarray of the input array by "simplification and delegation."
    
    Parameters:
        A: A list (array) of n >= 1 integers.
    
    Returns:
        The sum of the elements in a maximum subarray of A.
    """

    # TODO: Implement this function!
    return None
    
def max_subarray_recursion_inversion(A):
    """
    Computes the value of a maximum subarray of the input array by "recursion inversion."
    
    Parameters:
        A: A list (array) of n >= 1 integers.
    
    Returns:
        The sum of the elements in a maximum subarray of A.
    """

    # TODO: Implement this function!
    return None
  
def time_alg(alg, A):
    """
    Runs an algorithm for the maximum subarray problem on a test array and times how long it takes.
    
    Parameters:
        alg: An algorithm for the maximum subarray problem.
        A: A list (array) of n >= 1 integers.
    
    Returns:
        A pair consisting of the value of alg(A) and the time needed to execute alg(A) in milliseconds.
    """

    start_time = time.monotonic_ns() // (10 ** 6) # The start time in milliseconds.
    max_subarray_val = alg(A)
    end_time   = time.monotonic_ns() // (10 ** 6) # The end time in milliseconds.
    return max_subarray_val, end_time - start_time

for alg in [max_subarray_enumeration, max_subarray_iteration,
            max_subarray_simplification_delegation, max_subarray_recursion_inversion]:
    print(file_name, time_alg(alg, A))

