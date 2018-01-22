import os
#https://automatetheboringstuff.com/chapter8/

#print os.path.getsize('D:\Videos\Doctor.Strange.2016.1080p.HDRip.X264.AC3-EVO[EtHD]\doctorStrange.mkv')
#print os.listdir('D:\Videos\Doctor.Strange.2016.1080p.HDRip.X264.AC3-EVO[EtHD]')


os.path.isabs('.') #false
os.path.isabs(os.path.abspath('.')) #true

if os.path.exists('D:\Downloads\Samurai Jack'):
    totalSize = 0
    for filename in os.listdir('D:\Downloads\Samurai Jack'):
        totalSize = totalSize + os.path.getsize(os.path.join('D:\Downloads\Samurai Jack', filename))
        #print os.path.join('D:\Videos\Samurai Jack', filename)
        for filename2 in os.listdir(os.path.join('D:\Downloads\Samurai Jack', filename)):
            totalSize = totalSize + os.path.getsize(os.path.join('D:\Downloads\Samurai Jack', filename, filename2))
            print os.path.join('D:\Downloads\Samurai Jack', filename, filename2)
            #print os.path.join('D:\Videos\Samurai Jack', filename, filename2)
    print(totalSize)