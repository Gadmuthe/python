Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
x = [[12,7,3],
     [4,5,6],
     [7,8,9]]
y = [[5,8,1,2],
     [6,7,3,0],
     [4,5,9,1]]
result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][i] += x[i][k] * y[k][j]
            for r in result:
                print(r)

                
[60, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[102, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[114, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[210, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[259, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[274, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[286, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[307, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[334, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[358, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[358, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[361, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[361, 0, 0, 0]
[0, 20, 0, 0]
[0, 0, 0, 0]
[361, 0, 0, 0]
[0, 50, 0, 0]
[0, 0, 0, 0]
[361, 0, 0, 0]
[0, 74, 0, 0]
[0, 0, 0, 0]
[361, 0, 0, 0]
[0, 106, 0, 0]
[0, 0, 0, 0]
[361, 0, 0, 0]
[0, 141, 0, 0]
[0, 0, 0, 0]
[361, 0, 0, 0]
[0, 171, 0, 0]
[0, 0, 0, 0]
[361, 0, 0, 0]
[0, 175, 0, 0]
[0, 0, 0, 0]
[361, 0, 0, 0]
[0, 190, 0, 0]
[0, 0, 0, 0]
[361, 0, 0, 0]
[0, 244, 0, 0]
[0, 0, 0, 0]
[361, 0, 0, 0]
[0, 252, 0, 0]
[0, 0, 0, 0]
[361, 0, 0, 0]
[0, 252, 0, 0]
[0, 0, 0, 0]
[361, 0, 0, 0]
[0, 258, 0, 0]
[0, 0, 0, 0]
[361, 0, 0, 0]
[0, 258, 0, 0]
[0, 0, 35, 0]
[361, 0, 0, 0]
[0, 258, 0, 0]
[0, 0, 83, 0]
[361, 0, 0, 0]
[0, 258, 0, 0]
[0, 0, 119, 0]
[361, 0, 0, 0]
[0, 258, 0, 0]
[0, 0, 175, 0]
[361, 0, 0, 0]
[0, 258, 0, 0]
[0, 0, 231, 0]
[361, 0, 0, 0]
[0, 258, 0, 0]
[0, 0, 276, 0]
[361, 0, 0, 0]
[0, 258, 0, 0]
[0, 0, 283, 0]
[361, 0, 0, 0]
[0, 258, 0, 0]
[0, 0, 307, 0]
[361, 0, 0, 0]
[0, 258, 0, 0]
[0, 0, 388, 0]
[361, 0, 0, 0]
[0, 258, 0, 0]
[0, 0, 402, 0]
[361, 0, 0, 0]
[0, 258, 0, 0]
[0, 0, 402, 0]
[361, 0, 0, 0]
[0, 258, 0, 0]
[0, 0, 411, 0]
>>> 
>>> 
>>> x = [[12,7,3],
...      [4,5,6],
...      [7,8,9]]
>>> y = [[5,8,1,2],
...      [6,7,3,0],
...      [4,5,9,1]]
>>> result = [[sum(a*b for a,b in zip(x_row, y_col)) for y_col in zip(*y)]for x_row in x]
>>> for r in result:
...     print(r)
... 
...     
[114, 160, 60, 27]
[74, 97, 73, 14]
[119, 157, 112, 23]