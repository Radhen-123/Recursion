def Find_All_Possible_Path(Rows, Columns):          #Find all possible number of path in m x n Matrix
    if(Rows == 1 or Columns == 1):                  #base condition
        return 1
    else:
        return Find_All_Possible_Path(Rows-1, Columns) + Find_All_Possible_Path(Rows, Columns-1)
        
print(Find_All_Possible_Path(2,3))
