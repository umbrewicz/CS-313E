#  File: Adjacency.py
#  Description: Converts an edge list into an adjacency matrix
#  Student Name: Nick Umbrewicz
#  Student UT EID: nju96
#  Course Name: CS 313E
#  Unique Number: 52520

def edge_to_adjacency(edge_list):
    vertices = []

    for edge in edge_list:
        if edge[0] not in vertices:
            vertices.append(edge[0])
        if edge[1] not in vertices:
            vertices.append(edge[1])

    nVert = len(vertices)

    dict_vertices = {}

    for edge in edge_list:
        dict_vertices[edge[0]] = {}
    for edge in edge_list:
        dict_vertices[edge[0]][edge[1]] = edge[2]

    keys = []

    for key in dict_vertices:
        keys.append(key)
    
        for adjacent_key in dict_vertices[key]:
            keys.append(adjacent_key)

    keys = sorted(set(keys))
    matrix = [[0 for i in range(nVert)] for i in range(nVert)]
    
    for i in range(len(dict_vertices)):
        if keys[i] in dict_vertices:
            for key in dict_vertices[keys[i]]:
                matrix[i][keys.index(key)] = dict_vertices[keys[i]][key]

    return matrix

# ------ DO NOT CHANGE BELOW HERE ------ #
import ast

def main():
    matrix = edge_to_adjacency(ast.literal_eval(input()))

    print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))

if __name__ == "__main__":
    main()
