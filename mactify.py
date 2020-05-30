import rumps
import applescript

rumps.debug_mode(True)

class AwesomeStatusBarApp(rumps.App):
    def __init__(self):
        self.config = {
            "app_name": "Awesome App",
        }
        super(AwesomeStatusBarApp, self).__init__("Awesome App")
        self.app = rumps.App(self.config["app_name"])
        self.menu = ["Preferences", "Silly button", "Say hi"]
    
    # @rumps.clicked("Get Current Song playing")
    # def get_spotify_current_song(self, _):
    #     scpt = applescript.AppleScript('''
    #     on getCurrentlyPlayingTrack()
    #       tell application "Spotify"
    #         set currentArtist to artist of current track as string
    #         set currentTrack to name of current track as string
          
    #         return currentArtist & " - " & currentTrack
    #       end tell
    #     end getCurrentlyPlayingTrack
    #     ''')

    @rumps.clicked("Change title")
    def change_title(self, sender):
        sender.title = "It's been changed!"


    @rumps.clicked("Preferences")
    def prefs(self, _):
        rumps.alert("jk! no preferences available!")

    @rumps.clicked("Silly button")
    def onoff(self, sender):
        sender.state = not sender.state

    @rumps.clicked("Say hi")
    def sayhi(self, _):
        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")

if __name__ == "__main__":
    AwesomeStatusBarApp().run()