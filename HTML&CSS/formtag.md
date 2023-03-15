# formtag가 뭘까

1. html 형식과 속성
```html
<form action="/action_page.php" method="get">
  <label for="fname">First name:</label>
  <input type="text" id="fname" name="fname"><br><br>
  <label for="lname">Last name:</label>
  <input type="text" id="lname" name="lname"><br><br>
  <input type="submit" value="Submit">
</form>
```
- action : value는 URL이고 submitted 되면 폼데이터를 url로 전달한게 된다.
- label : input의 타이틀같은거고 for는 누굴위할지 적는다.
- input : 말그래도 input이고 type에 text 등 다양하다. id의 고유값으로 for와 엮고 name은 input의 이름이다.
- input의 submit이 있어야 action이 가능하다.

2. 작동방법
- get 방식와 post방식이 있다.
- 입력으로 fname에 123, lname에 456을 입력하고 submit한 경우
    - get: action으로 지정한 /action_page.php?fname=123&lanme=123
    - post: /action_page.php
- url이 변경되지 않는 post방식을 많이 사용할것 같다.


3. 참고
[w3schools](https://www.w3schools.com/tags/tag_form.asp)