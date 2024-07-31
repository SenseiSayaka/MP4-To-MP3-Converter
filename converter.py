from moviepy.editor import * 

def convert_mp4_to_mp3(mp4_path_file):
    video = VideoFileClip(mp4_path_file)
    audio = video.audio
    mp3_file_path = mp4_path_file[:-4] + '.mp3'
    audio.write_audiofile(mp3_file_path)
    return "MP4 File successfully converted to MP3"
    