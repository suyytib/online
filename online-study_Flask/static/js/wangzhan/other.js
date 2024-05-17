//register.js
function get_captcha() {
  // 监听id为button函数的点击事件
  $("#button").click(function (event) {
    var $this = $(this);
    // 阻止默认事件
    event.preventDefault();
    // 获取邮箱信息
    var email = $("input[name='email']").val();
    $.ajax({
      url: "/login/register/email_send/?email=" + email,
      method: "GET",
      success: function (result) {
        // 获取result中的code值,其中result值是访问的python视图函数的返回的json数据
        var code = result["code"];
        if (code == 200) {
          var time = 60;
          $this.off("click"); // 禁止监听按钮功能
          var timer = setInterval(function () {
            //设置计时器
            $this.text(time); // 将缓冲时间显示在按钮文本上
            time -= 1;
            if (time <= 0) {
              clearInterval(timer); //清楚计时器
              $this.text("获取验证码"); //回复按钮文本
              get_captcha(); //重新开始监听指定id的按钮(通过重新执行该函数实现)
            }
          }, 1000);
        } else {
          alert("发送异常!");
        }
      },
      error: function (error) {
        alert("发送请求失败!");
      },
    });
  });
}


//retrieve.js
function get_captchb() {
  // 监听id为button函数的点击事件
  $("#button").click(function (event) {
    var $this = $(this);
    // 阻止默认事件
    event.preventDefault();
    // 获取邮箱信息
    var email = $("input[name='email']").val();
    $.ajax({
      url: "/login/retrieve/retrieve_send/?email=" + email,
      method: "GET",
      success: function (result) {
        // 获取result中的code值,其中result值是访问的python视图函数的返回的json数据
        var code = result["code"];
        if (code == 200) {
          var time = 60;
          $this.off("click"); // 禁止监听按钮功能
          var timer = setInterval(function () {
            //设置计时器
            $this.text(time); // 将缓冲时间显示在按钮文本上
            time -= 1;
            if (time <= 0) {
              clearInterval(timer); //清楚计时器
              $this.text("获取验证码"); //回复按钮文本
              get_captchab(); //重新开始监听指定id的按钮(通过重新执行该函数实现)
            }
          }, 1000);
        } else {
          alert("发送异常!");
        }
      },
      error: function (error) {
        alert("发送请求失败!");
      },
    });
  });
}


//deeplearning/A3.js
function show(f) {
  var rd = new FileReader();//创建文件读取对象
  var files = f.files[0];//获取file组件中的文件
  rd.readAsDataURL(files);//文件读取装换为base64类型
  if (rd == 0)
    alert("请输入图片");
  else {
    $("#display_none").show();
    rd.onloadend = function (e) {
      //加载完毕之后，在div中添加一个元素
      $("#display_none").html("<img src='" + this.result + "' style=\"max-width:250px;max-height:250px;\"/>")
    }
  }
}
function onlinetesting() {
  $("#button").click(function (event) {
    var $this = $(this);
    document.getElementById("testing").style.visibility = "visible";//显示
  })
}


//login.js
var code;  //在全局   
function createCode() {     //生成函数
  code = "";
  var codeLength = 6; //码的长度    
  var checkCode = document.getElementById("checkCode");   //获得一个对象  
  if (checkCode != null) {
    checkCode.value = "";
    var selectChar = new Array(1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z');
    for (var i = 0; i < codeLength; i++) {
      var charIndex = Math.floor(Math.random() * 100);
      //向下取整随机找字符
      code += selectChar[charIndex];
    }
    if (code.length != codeLength) {
      createCode(); //重新生成码
    }
    checkCode.value = code;
  }
}
function validate() {    //比对函数
  var button = document.getElementById('myButton'); // 获取按钮元素
  if (button != null) {
    button.value = 0;
    var inputCode = document.getElementById("input1").value.toUpperCase();//字母转大写来验证   
    var codeToUp = code.toUpperCase();
    if (inputCode.length <= 0) {
      alert("请输入验证码！");   //弹出信息    
    }
    else if (inputCode != codeToUp) {
      alert("验证码输入错误！");
      createCode();
    }
    else {
      button.value = 1;
    }
  }
}

