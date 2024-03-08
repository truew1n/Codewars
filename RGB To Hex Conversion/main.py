def rgb(r, g, b):
    r, g, b = [x if x>=0 and x<=255 else (x-(x-255)) if x>255 else 0 for x in [r, g, b]]
    r, g, b = (f"{r:#b}"[2:], f"{g:#b}"[2:], f"{b:#b}"[2:])
    r, g, b = ["{0:0>4X}".format(int(f"{x}", 2))[2:] for x in [r, g, b]]
    return f"{r}{g}{b}"
