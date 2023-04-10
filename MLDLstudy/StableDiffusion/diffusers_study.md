# Diffusers 패키지를 천천히 읽어보자. [diffusion.ipynb](https://colab.research.google.com/drive/1EsEk0FfgR7F4P6dFEWYWHfZl8npRr_70#scrollTo=PzW5ublpBuUt)

들어가기 전 확인한 bolg posts
- Liliian Weng's, OpenAI, [introductory post](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/)
- Yang Song's, Stanford, [introductory post](https://yang-song.net/blog/2021/score/)

1. 구성요소
    1. Piplines: 빠른생성을 위해 준비된 클래스
    2. Models: 새로운 diffusion models을 학습시키기 위해 많이 사용된 아키텍쳐들 
    3. Schedulers: 노이즈/이미지 생성과 훈련에 사용되는 기술

2. 원리(논문리뷰&GAN,VAE,UNET)
- 우선 이미지 생성에 대한 배경지식이 필요하다. GAN, VAE, Diffusion의 원리와 차이를 알고 Unet을 알아야 한다.
- stable diffusion은 VAE에서 노이즈를 추가하는 함수과정을 diffusion처럼 여러차래 나눠 진행하고 Unet을 활용한다? 해당관정을 Scheduler 종류를 다양하게 제공하는 것으로 보인다.

3. 학습시키기 -> 구조 파악