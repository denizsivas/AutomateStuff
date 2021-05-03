from pytube import YouTube

#YouTube('https://www.youtube.com/watch?v=MeV3oWbPmSQ').streams.get_audio_only().download()

YouTube('https://www.youtube.com/watch?v=MeV3oWbPmSQ').streams.first().download()
