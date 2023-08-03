import sys

def file_contents_letters(file_name):
    """
    Takes a file name as input and returns a string consisting of the file's contents
    with all non-letter characters removed.
    
    Parameters:
        file_name: The name of the file.
    
    Returns:
        A string with the contents of <file_name> but with all non-letter characters removed.
    """

    f = open(file_name, "r")
    file_contents = f.read()
    f.close()
    return "".join([c for c in file_contents if c.isalpha()])
    
def edit_distance(s1, s2, ci = 1, cd = 1, cm = 1):
    """
    Computes the edit distance between two strings, s1 and s2.
    
    Parameters:
        s1: The first string.
        s2: The second string.
        ci: The cost of an insertion (1 by default).
        cd: The cost of a deletion (1 by default).
        cm: The cost of a mutation (1 by default).
    
    Returns:
        The edit distance between s1 and s2.
    """
    ##s1=['B','U','R','R','I','T','O']
    ##s2=['E','R','R','O','R']
    n1=len(s1)
    n2=len(s2)
    ##print(n1, n2)
    table=[[0]*(n1+1) for i in range(n2+1)]
    for i in range(n1+1):
        table[0][i]=i
    for i in range(n2+1):
        table[i][0]=i

    for i in range(n2):
        for j in range(n1):
            if s1[j]==s2[i]:
                table[i+1][j+1]=min(table[i][j+1]+ci,table[i+1][j]+cd,table[i][j])
            if s1[j]!=s2[i]:
                table[i+1][j+1]=min(table[i][j+1]+ci,table[i+1][j]+cd,table[i][j]+cm)
    

    # TODO: Implement this function!
    return table[n2][n1]
    
def lcs(s1, s2):
    """
    Computes the length of the longest common subsequence between two strings, s1 and s2.
    
    Parameters:
        s1: The first string.
        s2: The second string.
    
    Returns:
        The length of the longest common subsequence between s1 and s2.
    """
    n1=len(s1)
    n2=len(s2)
    ##print(n1, n2)
    table=[[0 for i in range(n1+1)] for j in range(n2+1)]
    for i in range(n1+1):
        table[0][i]=0
    for i in range(n2+1):
        table[i][0]=0

    for i in range(n2):
        for j in range(n1):
            if s1[j]==s2[i]:
                table[i+1][j+1]=table[i][j]+1
            if s1[j]!=s2[i]:
                table[i+1][j+1]=max(table[i][j+1],table[i+1][j])
    

    # TODO: Implement this function!
    return table[n2][n1]
    
def lcs3(s1, s2, s3):
    """
    Computes the length of the longest common subsequence between three strings: s1, s2, and s3.
    
    Parameters:
        s1: The first string.
        s2: The second string.
        s3: The third string.
    
    Returns:
        The length of the longest common subsequence between s1, s2, and s3.
    """
    n1=len(s1)
    n2=len(s2)
    n3=len(s3)
    table = [[[0 for i in range(n1+1)] for j in range(n2+1)] for k in range(n3+1)]
    for i in range(n1+1):
        table[0][0][i]=0
    for i in range(n2+1):
        table[0][i][0]=0
    for i in range(n3+1):
        table[i][0][0]=0
        
    for i in range(n3):
        for j in range(n2):
            for k in range(n1):
                if(s3[i]==s2[j] and s3[i]==s1[k]):
                    table[i+1][j+1][k+1] = table[i][j][k]+1
                else:
                    table[i+1][j+1][k+1]=max(table[i][j+1][k+1],table[i+1][j][k+1],table[i+1][j+1][k])

    # TODO: Implement this function!
    return table[n3][n2][n1]

s1 = file_contents_letters(sys.argv[1])
s2 = file_contents_letters(sys.argv[2])
if(len(sys.argv)<4):
    print(edit_distance(s1, s2), lcs(s1, s2))
else:
    s3 = file_contents_letters(sys.argv[3])
    print(edit_distance(s1, s2), lcs(s1, s2), lcs3(s1,s2,s3))
