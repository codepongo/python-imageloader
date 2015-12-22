import imageloader
def sub_img(im, x,y):
    f = '%d%d.png' % (y, x)
    left = 5 + (67 + 5) * x
    top = 41 + (67 + 5) * y
    sub = im.cut(left, top, 67, 67)
    sub.write(f)

try:
    #img = imageloader.open('src.png')
    #img = img.resize(256, 256)
    #img.write_png('des.png')
    img = imageloader.open('12306.jpg')
    #char = img.cut(0,0,293,30)
    #char.write('char.png')
    for x in range(0, 3):
        for y in range(0, 2):
            sub_img(img,x,y)


except:
    print('error')


