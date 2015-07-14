# 폰트 변경 셈플 코드

- 동일 폴더에 ttf파일 폰트를 넣은 후, kv파일에 이하와 같이 font_name 프로퍼티를 변경 하면 됨.

```
Label:
    font_name: "NanumGothicCoding.ttf"
    text: "한글한글"

```

- otf나 ttc등 맥용 폰트들은 사용하려하니xQuartz라는 sdk를 쓰라는데, 다운로드가 오래걸려 못해 봄.
- kv에서 이하와 같이 하면 모든 폰트가 변경됩니다.

```
<Label>:
    font_name: 'NanumGothicCoding.ttf'

BoxLayout:
    Label:
        text: "한글한글"

    Button:
        text: "여기도 한글 버튼?"
```


- 뒤지다 안 사실인데 label에 마크업 기능이 있음.

```
    Label:
        markup: True
        text: '[size=45][b][color=00BFFF]한글?[/color][/b][/size]'
```
