import imageloader
try:
    img = imageloader.open('icon1024.png')
    img = img.resize((512,512))
    img.write('icon512.png')
except:
    print('load error')


