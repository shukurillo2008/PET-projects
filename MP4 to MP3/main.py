def mp4_mp3(video):
    import moviepy.editor
    from pathlib import  Path
    video_file = Path(video)
    video_f = moviepy.editor.VideoFileClip(video)
    audio = video_f.audio
    return audio.write_audiofile(f'{video_file.stem}.mp3')


mp4_mp3(input("videoni kirgiz:  "))