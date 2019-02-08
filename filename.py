import os
def filename():
    base_path = os.path.dirname(os.path.abspath(__file__))
    bible_path = base_path + '/bible/' # / pre-attached
    for file in os.listdir(base_path+'/bible'):
        if not file.endswith('.html'):
            os.rename(bible_path+file, bible_path+file.replace('.html','.html'))
        if len(file) != 10:
            print('file ends with .html')
            os.rename(bible_path+file, bible_path+file[:3]+'0'+file[-6:])
