<!-- login -->
const muserid = document.querySelector('#muserid');
const mpasswd = document.querySelector('#mpasswd');
const loginbtn = document.querySelector('#loginbtn');
const logoutbtn = document.querySelector('#logoutbtn');


try {
    loginbtn.addEventListener('click', () => {
        if (muserid.value == '') {
            alert('아이디를 입력하세요!!');
            muserid.focus();
        } else if (mpasswd.value == '') {
            alert('비밀번호를 입력하세요!!');
            mpasswd.focus();
        } else {
            // document.loginfrm.action = '{% url 'login' %}';
            document.loginfrm.action = '/login/';
            document.loginfrm.submit();
        }
    });
} catch (e) {

}

try {
    logoutbtn.addEventListener('click', () => {
    location.href = '/logout/';
});
}catch (e){

}

<!-- search id -->
//ajax로 넘겨야 디자인이 안 깨짐!
const email=document.querySelector('#semail')
const suserid=document.querySelector('#suserid');
const searchbtn = document.querySelector('#searchbtn');
const wmsg= document.querySelector('#wmsg');

// try {searchbtn.addEventListener('click',()=>{
//     let qry = '?email=' +email.value;
//     location.href='/searchid/' + qry
// });}
// catch (e) {
//
// }

searchbtn.addEventListener('click', () => {
        let qry = '?email=' + email.value;
        fetch('/searchid/' + qry)
            .then(response => response.text())
            .then(text => searchID(text));
    });

const searchID = (emails)=>{
    console.log(emails);
    emails = JSON.parse(emails);  // 문자열을 JSON객체로 변환
    console.log(emails[0]);

    let fuserid = '';
    let msg=''

    emails.forEach((data, idx)=>{
        fuserid=data.fields.userid;
        suserid.value=fuserid;
    });
    if (suserid.value==0){
        msg='아이디가 존재하지 않습니다.'
    };
    wmsg.innerHTML=msg;
}

<!-- 닫기 버튼/이전페이지 버튼 누를 시 아이디 조회 input에 남아있는 값들 다 지움 -->
const cmdlbtn = document.querySelector('#cmdlbtn');
cmdlbtn.addEventListener('click', ()=>{
    email.value='';
    suserid.value='';
    wmsg.innerHTML='';
});

const backbtn = document.querySelector('#backbtn');
backbtn.addEventListener('click', ()=>{
    email.value='';
    suserid.value='';
    wmsg.innerHTML='';
});


// session

const facebook=document.getElementById("facebook");
const instagram=document.getElementById("instagram");
const youtube=document.getElementById("youtube");

// 로그인 시 생성되는 request.session('myteam')을 받아와야 함
let sessionval1 = document.querySelector('#sessionval1');
myteam1=sessionval1.value
// alert(myteam); //세션변수가 제대로 뜨는지 확인
// myteam이 팀 이름일 때, 이미지 src와 상단 SNS 링크 교체
if (myteam1 == '강원FC') {
   facebook.href="https://www.facebook.com/gangwonfc";
   instagram.href="https://www.instagram.com/gangwon_fc/";
   youtube.href="https://www.youtube.com/user/gangwonfc/featured";
}

else if (myteam1 == '김천 상무 프로축구단') {
   facebook.href="https://www.facebook.com/gimcheonsangmu";
   instagram.href="https://www.instagram.com/gimcheonfc/";
   youtube.href="https://www.youtube.com/channel/UCSZ-CvpbBm6JnZnWYmiNrlQ";
}

else if (myteam1 == '대구FC') {
   facebook.href="https://www.facebook.com/daegufc2002";
   instagram.href="https://www.instagram.com/daegufc.co.kr/";
   youtube.href="https://www.youtube.com/user/TheDaeguFC";
}

else if (myteam1 == 'FC서울') {
   facebook.href="https://www.facebook.com/fcseoul";
   instagram.href="https://www.instagram.com/fcseoul/";
   youtube.href="https://www.youtube.com/user/FCSEOUL";
}

else if (myteam1 == '성남FC') {
   facebook.href="https://www.facebook.com/SFC.Seongnam/?fref=nf";
   instagram.href="https://www.instagram.com/sfc.seongnam/";
   youtube.href="https://www.youtube.com/channel/UCt7aHRANCzaUDnEcTxnXhgg";
}

else if (myteam1 == '수원 삼성 블루윙즈') {
   facebook.href="https://www.facebook.com/SuwonSamsungFC";
   instagram.href="https://www.instagram.com/suwonsamsungfc/";
   youtube.href="https://www.youtube.com/user/bluewingsfc";
}

else if (myteam1 == '수원FC') {
   facebook.href="https://www.facebook.com/suwonfc2003";
   instagram.href="https://www.instagram.com/suwonfc/";
   youtube.href="https://www.youtube.com/channel/UCHPiDeQQyVcYe-nhyUanSWg";
}

else if (myteam1 == '울산 현대 축구단') {
   facebook.href="https://www.facebook.com/ulsanfc";
   instagram.href="https://www.instagram.com/ulsanhyundaifootballclub/";
   youtube.href="https://www.youtube.com/user/ULSANHYUNDAI";
}

else if (myteam1 == '인천 유나이티드') {
   facebook.href="https://www.facebook.com/incheonutd2003";
   instagram.href="https://www.instagram.com/incheonutd/";
   youtube.href="https://www.youtube.com/channel/UCGA9gUrYCb4hRk_wHBzB_nQ";
}

else if (myteam1 == '전북 현대 모터스') {
   facebook.href="https://www.facebook.com/jeonbuk1994";
   instagram.href="https://www.instagram.com/jeonbuk1994/";
   youtube.href="https://www.youtube.com/user/JEONBUKHYUNDAI";
}

else if (myteam1 == '제주 유나이티드') {
   facebook.href="https://www.facebook.com/JejuUnitedFootballClub/";
   instagram.href="https://www.instagram.com/jejuunitedfc/";
   youtube.href="https://www.youtube.com/channel/UCQfQeoiJTN2EVqde4_0PlUA/featured";
}

else if (myteam1 == '포항 스틸러스') {
   facebook.href="https://www.facebook.com/fcpohangsteelers";
   instagram.href="https://www.instagram.com/fc.pohangsteelers/";
   youtube.href="https://www.youtube.com/channel/UCOZQIw1I6ixjQZ_va_eCn7w";
}