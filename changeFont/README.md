# 폰트 변경 셈플 코드

- 동일 폴더에 ttf파일 폰트를 넣은 후, kv파일에 이하와 같이 font_name 프로퍼티를 변경 하면 됨.

```
Label:
    font_name: "NanumGothicCoding.ttf"
    text: "한글한글"

```

- otf나 ttc등 맥용 폰트들은 사용하려하니xQuartz라는 sdk를 쓰라는데, 다운로드가 오래걸려 못해 봄.
- 전체의 폰트를 한번에 변경하거나, 자동으로 상속받는 등의 코드등을 심화 학습으로 해보겠습니다.

