from __future__ import print_function # for using Python3 print

#https://www.python.org/doc/essays/graphs/
def find_all_paths(graph, start, end, path=[]):
		#import pdb; pdb.set_trace()
		path = path + [start]
		if start == end:
			return [path]
		if not graph.has_key(start):
			return []
		paths = []
		for node in graph[start]:
			if node not in path:
				newpaths = find_all_paths(graph, node, end, path)
				for newpath in newpaths:
					paths.append(newpath)
		return paths



# Starting program
print("Give me n")
n = int( raw_input() )
print("Give me m")
m = int( raw_input() )

print( "you want a matrix "+str(n)+"x"+str(m))

# Generate graph 
root = {}
for row in range( 0, n ) :
	if row == n-1:
		print("last row")
		for col in range(0,m):
			print(str(row) + ","+str(col)+" ", end="")
			if col == m-1:
				print("last element")
				root[ str(row) + ","+str(col) ] = []
				root[ str(row) + ","+str(col) ].append( "None" )
			else : 
				root[ str(row) + ","+str(col) ] = []
				root[ str(row) + ","+str(col) ].append( str(row) + ","+str(col+1) ) 	# izquierda

	else : 		
		for col in range( 0, m ) :
			print(str(row) + ","+str(col)+" ", end="")
			if col == m-1:
				print("last col")
				root[ str(row) + ","+str(col) ] = []
				root[ str(row) + ","+str(col) ].append( str(row+1) + ","+str(col) )
			else : 
				root[ str(row) + ","+str(col) ] = []
				root[ str(row) + ","+str(col) ].append( str(row+1) + ","+str(col) ) 	# abajo
				root[ str(row) + ","+str(col) ].append( str(row+1) + ","+str(col+1) ) 	# diagonal
				root[ str(row) + ","+str(col) ].append( str(row) + ","+str(col+1) ) 	# izquierda

	print("")

# Find all roads
p=[]
p = find_all_paths(root, "0,0", str(n-1)+","+str(m-1), p)

import pdb; pdb.set_trace()




