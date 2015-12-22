import imageloader
try:
    img = imageloader.open('src.png')
    #img = img.resize((512, 512))
    img.write('des.png')

except:
    print('error')


