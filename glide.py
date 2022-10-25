def get_vector():
    ret = []
    while 1:
        try:
            while 1:
                xval = int(input("Enter the x value for the vector"))
                yval = int(input("Enter the y value for the vector"))
                coord = xval, yval
                ret.append(coord)
                print("Enter exit once finished")
                prompt = input()
                if prompt == "exit":
                    break
        except:
            print("Invalid input")
        break
    ret = xval. yval
    return ret
def get_cords():
    ret = []
    while 1:
        try:
            while 1:
                xval = int(input("Enter the x value for the point"))
                yval = int(input("Enter the y value for the point"))
                coord = xval, yval
                ret.append(coord)
                print("Enter exit once finished")
                prompt = input()
                if prompt == "exit":
                    break
        except:
            print("Invalid input")
        break
    return ret

def flip(axis, points):
    ret = []
    if axis == "y":
        for coord in points:
            new = coord[0] * -1, coord[1]
            ret.append(new)
    if axis == "x":
        for coord in points:
            new = coord[0], coord[1] * -1
            ret.append(new)
    return ret
def translate(vector, points):
    ret = []
    for i in range(len(points)):
        nx = point[i][0] + vector[i][0]
        ny = point[i][1] + vector[i][1]
        coord = nx, ny
        ret.append(coord)
    return ret

coords = get_cords()        
vectors = get_vector()


print("What axis are you going to flip")
axis = input()
flip(axis, translate(vectors, coords))
