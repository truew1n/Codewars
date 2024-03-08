def clockwise(matrix):
    result = []
    for x in range(len(matrix[0])):
        buffer = []
        for y in range(len(matrix)):
            buffer.append(matrix[y][x])
        result.append(buffer[::-1])
    return result
            
            
def rotate(matrix, direction):
    if direction == "clockwise":
        return clockwise(matrix) 
                
    elif direction == "counter-clockwise":
        return [x[::-1] for x in clockwise(matrix)][::-1]
