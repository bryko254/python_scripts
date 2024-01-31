import requests
from tqdm import tqdm

def download_video(url, save_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    bytes_downloaded = 0
    
    with open(save_path, 'wb') as f, tqdm(
        desc="Downloading",
        total=total_size,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    ) as pbar:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                bytes_downloaded += len(chunk)
                pbar.update(len(chunk))

    print("Video downloaded successfully.")

# Example usage:
video_url = "https://player.vimeo.com/progressive_redirect/playback/840626220/rendition/1080p/file.mp4?loc=external&signature=ddbaf014542c3cc8805bb0f5804506c405e6c9901bc8b943fd1f3a0d2c9784b9"
save_path = "video.mp4"
download_video(video_url, save_path)
