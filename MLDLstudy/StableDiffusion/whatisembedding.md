# 내가 오늘 알고싶은 것!
- text to image 과정에서 image와 text를 어떻게 embedding 해주는지 잘 모르겠다.
- 아니 원리보다는 코드로 구현을 어떻게 해야할지 머리에 잘 안그려진다.

# Text Embedding
- 워드 임베딩은 단어를 컴퓨터가 이해할 수 있도록 벡터화 해주는 기술

## Encoding
- 자연어를 기계가 이해할 수 있도록 변환해주는 작업: 예) 정수인코딩, 원 핫 인코딩
1. 간단한 Encoding
    ```python
    text = "오늘도 공부를 하는 중인데 나는 어떤 엔지니어가 될 수 있을까?"

    tokens = [x for x in text.split(' ')]
    unique = set(tokens)
    unique = list(unique)

    token2idx = {}
    for i in range(len(unique)):
        token2idx[uniqe[i]] = i

    encode = [token2idx[x] for x in tokens]
    encode
    ```
    출력결과 `[4, 0, 1, 9, 8, 3, 2, 7, 5, 6]`

    token2idx를 출력하면 `{'공부를': 0,
    '하는': 1,
    '엔지니어가': 2,
    '어떤': 3,
    '오늘도': 4,
    '수': 5,
    '있을까?': 6,
    '될': 7,
    '나는': 8,
    '중인데': 9}`각 워드에 인덱스가 부여된걸 알 수있다.

 2. keras를 이용한 정수 인코딩
    ```python
    from tensorflow.keras.preprocessing.text import Tokenizer
    text = "오늘도 공부를 하는 중인데 나는 어떤 엔지니어가 될 수 있을까?"

    t= Tokenizer()
    t.fit_on_texts([text])
    print(t.word_index)

    encoded = t.texts_tosequences([text])[0]
    print(encoded)
    ```
    - 더 많이 사용되는 one-hot은 정수변환해서 100% 변환한거다.
    - 이밖에도 tensorflow 등 다양한 패키지에서 임베딩이 가능하도록 제공하고 있다.
    - 이수안컴퓨터연구소 영상으로 기초 강의를 들으면 이해가 편하다 [유튜브링크](https://www.youtube.com/watch?v=hR8Rvp-YNGg)

## 그래서..  Image랑 Text embedding을 unet으로 엮은거냐고
    

