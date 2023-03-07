def det(A):
  n = len(A)
  if n == 1:
    return A
  elif n == 2:
    return A[0][0] * A[1][1] - A[0][1] * A [1][0]
  else:
    
    #determinant formula
    sum = 0
    submatrix = [[0 for j in range(n-1)] for i in range(n-1)]
    for j in range(1, n+1):
      
      #fills in submatrix for each element a1j
      for a in range(len(A)):
        for b in range(len(A)):
          if a == 0 or b == j - 1:
            continue
          else:
            submatrix[a-1][b-1] = A[a][b]            
            
      sum += (-1 ** (1+j)) * matrix[0][j-1] * det(submatrix)
    return sum

#Runs program until exit is entered into the terminal. Handles improper inputs.
print("Type 'exit' into the terminal to quit.\n")
while True:
  n = input("What is the dimension of matrix A?:\n")
  if n.strip().lower() == 'exit':
    break
  try:
    int(n)
  except:
    print("Enter the dimension as a number in the proper format:\n")
    continue
  else:
    n = int(n)
    
    #constructs matrix from user input
    matrix = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
      for j in range(n):
        
        #Keeps asking for entry until entered in proper format
        while True:
          entry = input("Enter element a{0}{1}:\n".format(i+1, j+1))
          try:
            int(entry)
          except:
            print("Enter the element as a number in the correct format.\n")
            continue
          else:
            break
        matrix[i][j] = int(entry)

    print("Det A = {0}\n".format(det(matrix)))
