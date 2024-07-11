from pytube import YouTube
import pprint


def infoObj(name, views, length, author, save_path, quality):
    return {
        "Name": name,
        "Views": views,
        "Length": length,
        "Author": author,
        "SavePath": save_path,
        "Quality": quality,
    }


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        data = infoObj(
            yt.title, yt.views, yt.length, yt.author, save_path, highest_res_stream
        )
        pprint.pprint(data)
        highest_res_stream.download(output_path=save_path)

        print("Video Downloaded Successfully!")

    except Exception as e:
        print(e)


url = input("URL Of the YouTube Video: ")
save_path = "/home/matrix/Videos"


download_video(url, save_path)
