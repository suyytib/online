function bindEmailcaptchaClick() {
  var btn = document.getElementById("_button"); //获取点击按钮
  btn.addEventListener("click", function () {
    var time = 59; //定义剩下的秒数
    var email = $("input[name='email']").val();
    btn.disabled = true; //点击按钮实现禁用

    $.ajax({
      url: "/login/register?email=" + email,
      method: "GET",
      success: function (result) {
        var code = result["code"];
        if (code == 200) {
          var countdown = 60;

          //开始倒计时之前，就取消点击事件
          $this.off("click");
          var timer = setInterval(function () {
            $this.text(countdown);
            countdown -= 1;
            if (countdown <= 0) {
              //清掉定时器，就不倒计时了
              clearInterval(timer);
              $this.text("获取验证码");
              bindEmailcaptchaClick();
              // 重新绑定事件
            }
          }, 1000);

          alert("邮件发送成功！");
        } else {
          alert(result["message"]);
        }
      },
      fail: function (error) {
        console.log(error);
      },
    });
  });
}
$(function () {
  bindEmailcaptchaClick();
});
