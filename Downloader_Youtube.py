from pytube import Playlist
from pytube import Channel
import pafy
import os
from pathlib import Path

def Fundamental(video):
    print('\n********************|*|*|*|*|********************')
    try:
        # Title
        title = video.title
        # Duration
        duration = video.duration
        # Rating
        rating = video.rating
        # Views
        view = video.viewcount
        # Likes
        likes = video.likes
        # Size
        best = video.getbest()
        # Dislike
        dislike = video.dislikes
        # Size in MB ( maximum size )
        Size = best.get_filesize()//(1024**2)
    except Exception:
        pass
    else:
        print(f'\nTitle: {title}')
        print(f'|| Duration: {duration} || Maximum Size: {Size} MB || Views: {view} || Rating: {rating} || Likes: {likes} || Dislikes: {dislike} ||')
    finally:
        return title
    # Author
    # author = video.author
    # Length 
    # length = video.length
    # Description
    # desc = video.description


def Find_Quality(url):
    data = {1: 'Normal', 2: 'Audio', 3: 'Video', 4: 'Best Normal', 5: 'Best Audio', 6: 'Best Video'}
    Loop(data)
    Type = input('\nEnter your choice: ')
    Type = Type.lower()

    Quality = set()
    Extension = set()
    video = pafy.new(url)
    if (Type == 'normal' or Type == '1' or Type == 'best normal' or Type == '4'):
        [Quality.add(i.quality.split('x')[1]) for i in video.streams]
        [Extension.add(i.extension) for i in video.streams]
    elif (Type == 'audio' or Type == '2' or Type == 'best audio' or Type == '5'):
        [Quality.add(i.bitrate) for i in video.audiostreams]
        [Extension.add(i.extension) for i in video.audiostreams]
    elif (Type == 'video' or Type == '3' or Type == 'best video' or Type == '6'):
        [Quality.add(i.quality.split('x')[1]) for i in video.videostreams]
        [Extension.add(i.extension) for i in video.videostreams]

    print('\n', 'Format: ', Extension)
    ext = input('\nEnter Format: ')

    if (Type in ['best normal', 'best audio', 'best video', '4', '5', '6']):
        return Type, None, ext

    print('\n','Quality: ',Quality)
    qlty = input('\nEnter Quality: ')

    return  Type, qlty.lower(), ext.lower()

def Selection(Type, qlty, ext, url):
    
    # Initialization
    video = pafy.new(url)
    if (Type == 'best normal' or Type == '4'):
        best = video.getbest(preftype=ext)
        size = best.get_filesize()//(1024**2)
        return video, best, size
    elif (Type == 'best audio' or Type == '5'):
        bestaudio = video.getbestaudio(preftype=ext)
        size = bestaudio.get_filesize()//(1024**2)
        return video, bestaudio, size
    elif (Type == 'best video' or Type == '6'):
        bestvideo = video.getbestvideo(preftype=ext)
        size = bestvideo.get_filesize()//(1024**2)
        return video, bestvideo, size
    elif (Type == 'normal' or Type == '1'):
        for item in video.streams:
            if (qlty in str(item)) and (ext in str(item)):
                size = item.get_filesize()//(1024**2)
                return video, item, size
    elif (Type == 'audio' or Type == '2'):
        for item in video.audiostreams:
            if (qlty in str(item)) and (ext in str(item)):
                size = item.get_filesize()//(1024**2)
                return video, item, size
    elif (Type == 'video' or Type == '3'):
        for item in video.videostreams:
            if (qlty in str(item)) and (ext in str(item)):
                size = item.get_filesize()//(1024**2)
                return video, item, size

def Download_item(video, size, title, i, extension):
    try:
        N1 = str(str(title)+'.'+str(extension))
        N2 = str(str(i+1)+'.'+str(title)+'.'+str(extension))
        my_file1 = 'D:/Coding/Pycharm Projects/projects/Youtube downloader/Downloads/'+N1
        my_file2 = 'D:/Coding/Pycharm Projects/projects/Youtube downloader/Downloads/'+N2
        # if :
        #     print('File already exists.')
        #     return 0
    except Exception as E:
        print('\nSomething wents wrong: ', E)
        return 0
    else:
        if Measure >= Limit:
            exceed = int(input('Data limit exceeded -> (int): '))
            if exceed == 0:
                exit()
            else:
                Limit = Limit + exceed
        try:
            if i == None:
                print(f'|| Size: {size} MB || Downloading video: Inprocess... ||')
                video.download(quiet=False, filepath=my_file1)
            else:
                a = i + 1
                print(f'|| Size: {size} MB || Downloading video {a}: Inprocess... ||')
                video.download(quiet=False, filepath=my_file2)
        except Exception as DownloadError:
            print('\nError in Downloading: ', DownloadError)
            exit()    
        return size
    
def Loop_2(data):
    for i, item in enumerate(data):
        print(i,'.',item)
    
def Loop(data):
    for i in data.keys():
        print(i,'.',data.get(i))

def Sumup():
    cont = input('\nDo you want to continue...? (y/n)')
    if cont.lower() == 'y' or cont.lower() == 'yes':
        loop = True
    else:
        print('\nThanks for visiting us, see you soon...!')
        exit()
    return loop

def main():
    Sr = {1:'Single', 2:'Playlist', 3:'Channel'}
    print('\nStarting youtube downloader... \n')
    Loop(Sr)
    choice = input('\nEnter your choice: ')
    url = input('\nEnter URL: ')
    return url, choice.capitalize()


# Progressive - Audio and Video in a single file
# Adaptive - Audio and video in separated file
    

if __name__ == '__main__':
    
    while True:
        url, choice = main()
        try:
            Limit = int(input('\nEnter Data Limit (in MB): '))
            Measure = 0
            if choice == 'Single' or choice == '1':
                try:
                    Type, qlty, extension = Find_Quality(url)
                    video, data, size = Selection(Type, qlty, extension, url)
                    title = Fundamental(video)
                except Exception as E:
                    print(f'\nError Occured: {E}\n')
                    if Sumup() == True:
                        continue
                else:
                    i = None
                    Measure = Measure + Download_item(data, size, title, i, extension)
                    print('Data Used (in MB):', Measure)

            elif choice == 'Playlist' or choice == '2':
                P = Playlist(url)
                print('\n',P.title)
                D1 = int(input('\nAlready Downloaded: '))
                for i, item in enumerate(P.video_urls):
                    try:
                        if i == 0:
                            Type, qlty, extension = Find_Quality(item)
                        video, data, size = Selection(Type, qlty, extension, item)
                        title = Fundamental(video)
                        print(i, D1)
                    except Exception as E:
                        print(f'\nError Occured: {E}\n')
                        if Sumup() == True:
                            break
                    else:
                        if i < D1:
                            print('Already Downloaded Video')
                        else:
                            Measure = Measure + Download_item(data, size, title, i, extension)
                            print('Data Used (in MB):', Measure)

            elif choice == 'Channel' or choice == '3':
                C = Channel(url)
                print('\n', C.title)
                D1 = int(input('\nAlready Downloaded: '))
                for i, item in enumerate(C.video_urls[D1:]):
                    try:
                        if i == 0:
                            Type, qlty, extension = Find_Quality(item)
                        video, data, size = Selection(Type, qlty, extension, item)
                        title = Fundamental(video)
                        print(i, D1)
                    except Exception as E:
                        print(f'\nError Occured: {E}\n')
                        if Sumup() == True:
                            break
                    else:
                        print(i, D1)
                        if i < D1:
                            print('Already Downloaded Video')
                        else:
                            Measure = Measure + Download_item(data, size, title, i, extension)
                            print('Data Used (in MB):', Measure)

            else:
                print('\nInvalid Input, please try again...!')
                continue

        except Exception as E:
            print('No internet connection...')
            if Sumup() == True:
                continue