# Unet이란 어떤 아이디어인가?
1. Unet ?
- U자 모향을 Architecture를 구성한다
    - 내리막에서  Contracing patch (수축경로)
        - Contracting path 에서는 2D Conv, maxpooling을 반복하여 채널은 두배로 늘리고, featuremap은 절반으로 줄인다.

    - 오르막에서 Expanding patch (확장경로)
        - Expanding path에서는 up-conv를 통해 채널을 줄이고 feature map 크기를 두배로 늘려나간다.
        - up-conv?
            - up sample, transposed conv 두가지가 있다
            - up sampling 하는 방법은 다양하다.
                - DACON 동확책님이 정리한걸 공부 [포스팅](https://dacon.io/forum/406022?page&dtype&ptype)
                - transposed convolution 에서 stride수에 따라 달라지는건 꼭 기억하자.
    - 아! Contracing path - Expanding path는 encoder-decoder라 불리기도 한다.

2. Unet의 핵심 아이디어: Skip Architecture(connetcion)
- 매번 un-conv step마다 Contracting path의 feature map을 expanding path feature map 크기에 맞춰 crop 한 뒤 붙인다.

3. Sequential layer를 대략적으로 보면
아직 torch가 약해서 이분걸로 공부해보려 한다.
[포스팅](https://hyunlee103.tistory.com/57)

# stable diffusion에서 어떻게 사용되는가?
- Unet의 ouput인 noise reesidual 을 dnoised latent image를 계산하기 위해 사용된다.
- 그 과정에서 scheduler algorithm을 사용하는데 그럼 스케쥴러 알고리즘은 뭐지?
    1. scheduler algorithm
    - 해환123님의 T스토리 설명으로는 PNDM(기본)/DDIM/K-LMS가 주로 사용된다 한다.
    - 흔히 알고있는 OS에서의 scheduler algorithm? 아니면 Learning rate scheduler와는 다른건가? -> NO

    2. Pseudo numerical methods for diffusion models(PNDM) 
    [huggingapi](https://huggingface.co/docs/diffusers/api/schedulers/pndm)
    - diffusers git을 clone하면 다양한 schedulers를 볼 수 있었다. [깃](https://github.com/huggingface/diffusers/blob/main/src/diffusers/schedulers/scheduling_pndm.py)
    - 왜케 어렵지 ㅋㅋ  

