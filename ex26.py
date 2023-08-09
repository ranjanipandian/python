#matrix problem

row1=['😍','😍','😍']
row2=['😍','😍','😍']
row3=['😍','😍','😍']
matrix=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Enter the position where you want to hide money:")
rowno=int(position[0])
colno=int(position[1])
row_selected=matrix[rowno-1]
row_selected[colno-1]='X'
print(f"{row1}\n{row2}\n{row3}")

