import requests
import json
import eyed3
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)) + "\\download")
httpsession = requests.session()
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
}


def download_json():
    f = json.loads(
        open(os.path.dirname(os.path.realpath(__file__)) + "\\get.json",
             encoding="utf-8").read())['result']['tracks']
    num = 0
    oknum = 0
    for index in f:
        print("\r",
              num + 1,
              "/",
              len(f),
              " |",
              "▮" * int(num / len(f) * 20) + " " * int(
                  (len(f) - num) / len(f) * 20),
              "| ",
              round(num / len(f) * 100, 1),
              "% ",
              index['name'],
              sep="",
              end=" " * 50 + "\r")
        f_get = httpsession.get(
            url="http://music.163.com/song/media/outer/url?id=" +
            str(index['id']) + ".mp3",
            headers=headers)
        try:
            a = f_get.headers['content-length']
            error = 0
        except:
            error = 1
        if (error == 0):
            song_name = str(index['name'])
            song_name = song_name.replace("/", "_")
            song_name = song_name.replace("?", "_")
            f_out = open(song_name + ".mp3", "wb")
            f_out.write(f_get.content)
            f_out.close()
            f_out = eyed3.load(song_name + ".mp3")
            f_out.initTag()
            f_out.tag.title = index['name']
            f_out.tag.artist = index['artists'][0]['name']
            f_out.tag.album = index['album']['name']
            f_out.tag.album_artist = index['album']['artist']['name']
            f_out.tag.track_num = num
            f_out.tag.save()
            oknum += 1
        num += 1
    print("")
    print("Download completed!")
    print("File saved to",
          os.path.dirname(os.path.realpath(__file__)) + "\\download")
    print("Total", oknum, "files")
    input("press ENTER")


download_type = input("Read json / Input Link ?  (1/2) ")
if (download_type == "1"):
    download_json()
elif (download_type == "2"):
    link = input("Song list URL: ")
    # link = "https://music.163.com/#/my/m/music/playlist?id=2724783329"
    print("Please open :")
    print("https://music.163.com/api/playlist/detail?id=" +
          link[link.find("playlist?id=") + 12:])
    print("And copy the content to get.json")
    input("then press ENTER")
    download_json()
else:
    print("Error")
