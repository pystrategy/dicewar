# 효과음 셈플
## 작업 진행
- 프로그램을 켜고 Test라는 이름의 버튼을 누르면 동일 디렉토리의 ys3_ost.wav가 플레이 됨.
- 코드는 이하와 같음.
```
 SndTestApp._sndObj = SoundLoader.load('ys2_ost.wav')
 SndTestApp._sndObj.play()
```

- mac os 에서는 gstreamer라는 걸 사용하여 플레이를 하는데 ogg 및 mp3를 플레이 하려면 해당 녀석의 플러그인을 깔아 줘야됨
- 기타 os는 확인해 본 봐 없으나 window같은데선 그냥 플레이 되도록 패키징했다는 듯?
- brew를 통해서 이하와 같이 플러그 인을 설치하면 ogg도 출력이 됩니다.

```
brew install gst-plugins-base --with-libvorbis
```

##관련 링크
 - http://kivy.org/docs/api-kivy.core.audio.html
 - http://kivy.org/docs/_modules/kivy/core/audio.html
