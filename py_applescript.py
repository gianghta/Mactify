import os

def get_current_song_playing():
    return os.popen('osascript ./current_song_name_as.AppleScript').read()

if __name__ == "__main__":
    print(get_current_song_playing())