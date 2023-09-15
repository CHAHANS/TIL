# GAN (Generative Adversarial Networks)
- 
## 개념과 핵심용어
- Discriminator : 분별자 
    - 실제값과 Generator가 생성한 값을 비교함..
    - Discriminator가 분별하지 못할때 까지 학습
- Generator : 생성자
    - DL Encoder/Decoder 에서 Decoder로 -> 가상 값(이미지)를 생성

## 모델구성
- Generator가 만든 x페이크 
- Discriminator에 z로 생성

## 이미지의 확률분포가 유사하게 생성?
- 이미지는 고정된 픽셀값을 갖는데 확률분포가 존제하는가?
    - 이부분은 facebook TensorFlow KR에서 임정섭님도 동일한 의문을 품고 포스팅한 내용이 있었다.
    - 확률분포를 유사하게 한다는 건 이미지의 특징 x1,x2,x3의 출현빈도를 유사하게 사용한다는 것이다.
    - 이것을 활용하면 segment처럼 픽셀단위 확율을 갖는경우 더 진짜같은 이미지를 생성하게 될것 같다.
- 그럼 여기서 이미지의 특징 x1,x2,x3는 CNN을 통해 생성되는 채널의 (픽셀값or채널전체)와 같은 개념으로 이해해도 되는가? 