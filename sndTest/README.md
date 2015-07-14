# 효과음 셈플
## 작업 진행
- 프로그램을 켜고 Test라는 이름의 버튼을 누르면 동일 디렉토리의 ys3_ost.wav가 플레이 됨.
- ogg 및 mp3는 현제 맥에서 플레이가 안되는데 플러그인 관련된 이슈가 좀 있어보임 확인 중.

```
 SndTestApp._sndObj = SoundLoader.load('ys2_ost.wav')
 SndTestApp._sndObj.play()
```



##관련 링크
 - http://kivy.org/docs/api-kivy.core.audio.html
 - http://kivy.org/docs/_modules/kivy/core/audio.html
