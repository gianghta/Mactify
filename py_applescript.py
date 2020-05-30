import os
import applescript

def get_current_song_playing():
    return os.popen('osascript ./current_song_name_as.AppleScript').read()

def get_current_song_playing_py_applescript():
    scpt = applescript.AppleScript('''
        on getCurrentlyPlayingTrack()
            if application "Spotify" is running then
                tell application "Spotify"
                    if player state is playing then
                        set currentArtist to artist of current track
                        set currentTrack to name of current track
                        
                        return currentArtist & " - " & currentTrack
                    else
                        return "No song is currently being played"
                    end if
                end tell
            else
                return "Spotify is currently off"
            end if
        end getCurrentlyPlayingTrack
    ''')
    return scpt.call('getCurrentlyPlayingTrack')

if __name__ == "__main__":
    print(get_current_song_playing_py_applescript())