from kivy.app import App
from kivy.core.audio import SoundLoader


#snd_sample = SoundLoader.load('sounds/appear.wav')


"""
class TestForm(BoxLayout):
    @staticmethod
    def pressTestButton():
        print("Explicit is better than Implicit")
"""

class SndTestApp(App):
    _sndObj  = None

    @staticmethod
    def pressTestButton():

        if SndTestApp._sndObj == None:
            SndTestApp._sndObj = SoundLoader.load('ys2_ost.wav')

            if SndTestApp._sndObj == None:
                print( '#  load sound failed.' )
                return

            print("Sound is %.3f seconds" % SndTestApp._sndObj.length)

            SndTestApp._sndObj.play()

        else:
            SndTestApp._sndObj.stop()
            SndTestApp._sndObj.unload()
            SndTestApp._sndObj = None


if __name__ == '__main__':
    SndTestApp().run()
