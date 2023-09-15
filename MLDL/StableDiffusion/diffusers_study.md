# Diffusers 패키지를 천천히 읽어보자. [diffusion.ipynb](https://colab.research.google.com/drive/1EsEk0FfgR7F4P6dFEWYWHfZl8npRr_70#scrollTo=PzW5ublpBuUt)

들어가기 전 확인한 bolg posts
- Liliian Weng's, OpenAI, [introductory post](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/)
- Yang Song's, Stanford, [introductory post](https://yang-song.net/blog/2021/score/)

1. 구성요소
    1. Piplines: 빠른생성을 위해 준비된 클래스
    2. Models: 새로운 diffusion models을 학습시키기 위해 많이 사용된 아키텍쳐들 
    3. Schedulers: 노이즈/이미지 생성과 훈련에 사용되는 기술

<<<<<<< HEAD:MLDLstudy/StableDiffusion/diffusers_study.md
2. 원리
    1. Latent vector 생성
    2. unet
    3. text conditioning -> unet
    4. vae
    
=======
2. 원리(논문리뷰&GAN,VAE,UNET)
- 우선 이미지 생성에 대한 배경지식이 필요하다. GAN, VAE, Diffusion의 원리와 차이를 알고 Unet을 알아야 한다.
- stable diffusion은 VAE에서 노이즈를 추가하는 함수과정을 diffusion처럼 여러차래 나눠 진행하고 Unet을 활용한다? 해당관정을 Scheduler 종류를 다양하게 제공하는 것으로 보인다.
>>>>>>> b92358ad728938ae4e5415e13b5e1811e89bcffe:MLDL/StableDiffusion/diffusers_study.md

3. 학습시키기 -> 구조 파악
- [그림으로이해하기](https://velog.io/@hammerimpact/%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%9D%B4%ED%95%B4%ED%95%98%EB%8A%94-Stable-Diffusion-%EB%B2%88%EC%97%AD)

1. text clip으로 image
![img](https://velog.velcdn.com/images/hammerimpact/post/0b04c06a-6484-4a78-aca2-a700a77428ae/image.png)