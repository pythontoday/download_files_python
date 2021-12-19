import requests
import wget

img_url = 'img_url'
video_url = 'video_url'

img2_url = 'img_url'
video2_url = 'video_url'


def download_img(url=''):
    
    try:
        response = requests.get(url=url)
        
        with open('req_img.jpg', 'wb') as file:
            file.write(response.content)
            
        return 'Img successfully downloaded!'
    
    except Exception as _ex:
        return 'Upps... Check the URL please!'
    
    
def download_video(url=''):
    
    try:    
        response = requests.get(url=url, stream=True)
        
        with open('req_video.mp4', 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    file.write(chunk)
            
        return 'Video successfully downloaded!'
    
    except Exception as _ex:
        return 'Upps... Check the URL please!'
    
    
def download_wget(url='', file_type='video'):
    
    try:
        if file_type == 'video':
            wget.download(url=url, out=f'wget_{file_type}.mp4')
        else:
            wget.download(url=url, out=f'wget_{file_type}.jpg')
            
    except Exception as _ex:
        return 'Upps... Check the URL please!'
    
    
def main():
    print(download_img(url=img_url))
    print(download_video(url=video_url))
    
    download_wget(url=img2_url, file_type='img')
    download_wget(url=video2_url, file_type='video')
    
    
if __name__ == '__main__':
    main()
