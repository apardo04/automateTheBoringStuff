import os
#https://automatetheboringstuff.com/chapter8/

#print os.path.getsize('D:\Videos\Doctor.Strange.2016.1080p.HDRip.X264.AC3-EVO[EtHD]\doctorStrange.mkv')
#print os.listdir('D:\Videos\Doctor.Strange.2016.1080p.HDRip.X264.AC3-EVO[EtHD]')


os.path.isabs('.') #false
os.path.isabs(os.path.abspath('.')) #true

if os.path.exists('D:\Downloads\desktop_optimized'):
    totalSize = 0
    for filename in os.listdir('D:\Downloads\desktop_optimized'):
        new_name = filename.replace("-min","")
        old_file = os.path.join('D:\Downloads\desktop_optimized', filename)
        new_file = os.path.join('D:\Downloads\desktop_optimized', new_name)
        os.rename(old_file, new_file)
    #print(totalSize)