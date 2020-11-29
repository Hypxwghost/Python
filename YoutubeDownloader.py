# This script is not 100% functional,some videos have no audio !
import pytube
filetype = int(input('''File type:
            [1] - Mp4/video
            [2] - Mp4/audio'''))
video_list = []
while True:
    url = input('Enters URLs: [Terminate by "STOP"]')
    if url == 'STOP':
        break
    video_list.append(url)

for x, video in enumerate(video_list):
    try:
        v = pytube.YouTube(video)
        if filetype == 1:
            print('Some videos may have no audio')
            confirm = input('Download in 1080p(all my tests results in video without audio)?  [Y/N]').upper().strip()[0]
            if filetype == 1 and confirm == 'Y': # here script starts trying all resolutions
                stream = v.streams.get_by_itag(137)
                print(f'Downloading {x}')
                stream.download()
                print('Done')
            else:
                try:
                    stream = v.streams.get_by_itag(22)
                    print('Download in 1080p failed,trying 720p...')
                    print(f'Downloading {x}')
                    stream.download()
                    print('Done')
                except:
                    try:
                        stream = v.streams.get_by_itag(135)
                        print('Download in 720p failed,trying 480p....')
                        print(f'Downloading {x}')
                        stream.download()
                        print('Done')
                    except:
                        try:
                            stream = v.streams.get_by_itag(18)
                            print('Download in 480p failed,trying 360p.....')
                            print(f'Downloading {x}')
                            stream.download()
                            print('Done')
                        except:
                            try:
                                stream = v.streams.get_by_itag(133)
                                print('Download in 360p failed,trying 240p.....')
                                print(f'Downloading {x}')
                                stream.download()
                                print('Done')
                            except:
                                try:
                                    stream = v.streams.get_by_itag(160)
                                    print('Download in 240p failed,trying 144p.......')
                                    print(f'Downloading {x}')
                                    stream.download()
                                    print('Done')
                                except:
                                    print('\033[4;31mAll downloads failed,verify URL or try another video')
    except:
        print('Everything failed')
if filetype == 2: # audio
    try:
        print('Downloading..')
        stream = v.streams.get_by_itag(140)
        stream.download()
        print('Done')
    except:
        print('An error was ocurred')
