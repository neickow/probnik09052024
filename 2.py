print('s x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f=(z==(not(x))) <= ((w<=(not(y))) and (y<=x))
                sm=x+y+z+w
                if f and sm==3:
                    print('1', x, y, z, w)
                if not(f) and sm<=2:
                    print('2', x, y , z, w)
                elif not(f) and sm<=3:
                    print('3', x , y, z, w)