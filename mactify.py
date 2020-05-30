import rumps
import applescript


class Mactify(rumps.App):
    def __init__(self):
        super(Mactify, self).__init__(type(self).__name__, menu=['Next Track', 'Previous Track'], icon='icon/spotify-sketch.png')
    
    @rumps.clicked('Next Track')
    def next_button(self, sender):
        scpt = applescript.AppleScript('''
            on changeToNextTrack()
                if application "Spotify" is running then
                    tell application "Spotify"
                        next track
                    end tell
                else
                    return ""
                end if
            end changeToNextTrack
        ''')
        result = scpt.call('changeToNextTrack')
        if result == "":
            rumps.alert(message='There is no song currently playing', ok='OK!')

    @rumps.clicked('Previous Track')
    def prev_button(self, sender):
        scpt = applescript.AppleScript('''
            on changeToPrevTrack()
                if application "Spotify" is running then
                    tell application "Spotify"
                        previous track
                    end tell
                else
                    return ""
                end if
            end changeToPrevTrack
        ''')
        result = scpt.call('changeToPrevTrack')
        if result == "":
            rumps.alert(message='There is no song currently playing', ok='OK!')
    
    @rumps.timer(1)
    def get_current_song_title(self, sender):
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
                    return "Mactify"
                end if
            end getCurrentlyPlayingTrack
        ''')
        title = scpt.call('getCurrentlyPlayingTrack')
        self.title = title

if __name__ == "__main__":
    Mactify().run()