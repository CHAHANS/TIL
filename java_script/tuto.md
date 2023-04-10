# java script 기초 

## 변수
    ```javascript
    let name = Hansol;
    // let name = Hansols; 는 애러발생
    name = Hansols; //name이 재정이 됨
    const age = 32;
    // age는 재정의 변경 불가
    consol.log(name);
    consol.log(age);
    ```
    - let, const로 변수의 무분별한 사용을 방지
    - 변경이 가능해야 하다면 let
    - 변경되면 안되는 경우 const 사용
    
## 자료형
- 변수를 지정할 때 python과 같이 별도로 문자형, 숫자형을 지정해줄 필요가 없어 편하다.

1. 문자열
    ```javascript
    let name = "Hansol";
    let age = 33;

    let say = `${name}'s ${age} years old`;
    console.log(say);
    ```
- 따옴표, 쌍따옴표, 백틱(backtick)으로 표현
- 파이썬 처럼 이스케이프와 함께 따옴표 안에서 땅모표를 사용가능하고, 백틱은 ${[변수]}로 사용하여 fomat형식으로 사용가능
- 문자열 덧샘 가능

2. 숫자형
    ```javascript
    let myage = 33;
    let gfage = 31;

    console.log(myage-gfage); //2
    console.log(myage+gfage); //64
    console.log(myage/gfage); //1.064516129032258
    console.log(myage*gfage); //1023
    console.log(myage%gfage); //2 (나머지)
    ```
- 기본적인 사칙연산과 나머지 연산이 가능하다.
- 단, 0으로 숫자열과 문자열을 나누게 되면 Infinity(무한대)로 표기된다.
- 문자열과 숫자열을 더하게 되면 문자열로 전환됨

3. 불린
    ```javascript
    let myage = 33;
    let gfage = 31;
    console.log(myage>gfage); //True
    console.log(myage<gfage); //False
    console.log(myage==gfage); //False
    ```
- >=, <= 의 연산도 동일하게 사용가능하다.

4. typeof
    ```javascript
    let myage = 33;
    let gfage = 31;
    let name = "Hansol"; 
    console.log(typeof myage); // number
    console.log(typeof(myage)); // 이렇게도 사용가능

    console.log(typeof name); // string
    console.log(typeof myage>gfage); // boolean
    console.log(typeof null); // object
    console.log(typeof undefind); // undifind
    ```
- null 이 object로 나오는건 오류다. 하위 버전 호환을 위해 변경되지 않았다.

## 대화상자
- alert()
- prompt
- confirm

1. 상호작용해보기
    ```javascript
    const name = prompt("이름을 입력하세요.");
    alert("환영합니다" + name + "님");
    // alert(`환영합니다 ${name}님`);
    ```

2. prompt의 기본값 사용
    ```javascript
    const name = prompt("예약일을 입력해주세요.", "2022-04-");
    ```

3. comfirm 
    ```javascript
    const isAdult = confirm("성인입니까?");
    console.log(isAdult);
    ```
    - 확인 => True, 취소 => False가 적용됨

## 형변환
- String()
- Number()
    ```javascript
    const mathScore = prompt("수학점수를 입력하세요");
    const engScore = prompt("영어점수를 입력하세요");
    const result = (Number(mathScore) + Number(engScore)/2);
    console.log(result);

    // 주의사항
    Number(null) //=> 0
    Number(undefined) //=> NaN
    ```
- Boolean()
    ```javascript
    Boolean("yesmans")
    Boolean("12")


    //주의사항
    Boolean(0) //=> false
    Boolean('0') //=> true

    Boolean('') // => false
    Boolean(' ') // => true
    ```

## 연산
- +, - , * , %
    ```javascript
    let a = 1
    let b = 0
    a = ++a // a==2
    b = a++ // b==2, a==3
    let c = a**b // c==9 거듭제곱
    ```
- */ 는 +-보다 우선순위를 갖는다.

## 비교연산, 조건, 논리연산
1. 비교연산
- <, >, <=, >=, ==, !=
    ```javascript
    console.log(10>5);
    console.log(10 == 5);
    const a = 1;
    const b = '1';
    console.log(a==b); // ture를 반환
    console.log(a===b); // type까지 비교
    ```
2. 조건
- if, else, elif
    ```javascript
    let age = 18;
    if (age > 19){
    console.log('환영합니다.');
    } else if(age ===18) {
        console.log('수능 잘보세요');
    } else {
    console.log('미성년자는 접근 불가입니다.');
    }
    ```
3. 논리연산
- || (OR), && (AND), ! (NOT)
    ```javascript
    let age = 16;
    const name = "hansol";
    let engScore = 80;
    // if (age > 19 && name == 'eunsol' || engScore>60)
    // &&연산이 ||보다 우선시 되게 때문에 위 주석된 논리연산과 아래 괄호가 추가된 연산은 같은 의미가 된다.
    // if ((age > 19 && name == 'eunsol') || engScore>60)

    // 19세 초과, 은솔 or enScore가 60이상으로 구분하면 false로 처리된다.
    if (age > 19 && (name == 'eunsol' || engScore>60)){
    console.log('환영합니다.');
    } else if(age ===18) {
    console.log('수능 잘보세요');
    } else {
    console.log('미성년자는 접근 불가입니다.');
    }
    ```

## 반복문
1. for, while
```javascript
// for, i 초깃값->비교연산->i증가 -> 구문실행 -> 비교연산
for(let i=0;i < 10;i++){
    console.log(i);
}

//while
let i =0;
while(i<10){
    console.log(i);
    i++;
}
//do while
let i =0;
do{
    console.log(i);
    i++;
} while(i<10)
``` 
2. 반복문 탈출
- break : 멈추고 빠져나옴
- continue : 멈추고 다음 반복으로 진행
8번째 
```javascript

```


