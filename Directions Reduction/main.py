def dirReduc(arr):
    joined = " ".join(arr)
    for x in range(len(arr)):
        joined = joined.replace("NORTH SOUTH", '#').replace("SOUTH NORTH", '#').replace("WEST EAST", '#').replace("EAST WEST", '#')
        joined = joined.replace('# ', '').replace('#', '').replace(' #', '')
    return [x for x in joined.split(' ') if x != '']
