#Zero Matrix in python
#ctci 1.8

def nullifyRow(matrix,row):
	for j in range(len(matrix[0])):
		matrix[row][j]=0

def nullifyCol(matrix,col):
	for i in range(len(matrix)):
		matrix[i][col]=0


def setZeros(matrix):
	row = [None]*len(matrix)
	col = [None]*len(matrix[0])

	for i in range(len(row)):
		for j in range(len(col)):
			if matrix[i][j]==0:
				row[i]=True
				col[j]=True

	#Nullify Row
	for i in range(len(row)):
		if row[i]:
			nullifyRow(matrix,i)

	#Nullify Col
	for j in range(len(col)):
		if col[j]:
			nullifyCol(matrix,j)

	return matrix

matrix = [[1,2,3],[1,0,3],[1,1,1],[0,1,1]]
print setZeros(matrix)