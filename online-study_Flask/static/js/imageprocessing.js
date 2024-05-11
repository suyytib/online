function post_pic(f) {
    var rd = new FileReader();//创建文件读取对象
    var files = f.files[0];//获取file组件中的文件
    rd.readAsDataURL(files);//文件读取装换为base64类型
    if (rd == 0)
        alert("请输入图片");
    else {
        $("#display_none").show();
        rd.onloadend = function (e) {
            $("#display_none").html("<img src='" + this.result + "' style=\"max-width:250px;max-height:250px;\"/>")
            $.ajax({
                url: "/imageprocessing/A1/",
                method: "POST",
                data: {
                    'data': this.result
                },
                success: function (result) {
                    // 获取result中的code值,其中result值是访问的python视图函数的返回的json数据
                    var code = result["code"];
                    if (code == 200) {
                        $("#display_none1").show();
                        //加载完毕之后，在div中添加一个元素
                        $("#display_none1").html("<img src='data:image/jpeg;base64," + result["datas"] + "' style=\"max-width:250px;max-height:250px;\"/>")
                    } else {
                        alert("发送异常!");
                    }
                },
                error: function (error) {
                    alert("发送请求失败!");
                },
            });
        }
    }
}
function post_pic1(f) {
    var rd = new FileReader();//创建文件读取对象
    var files = f.files[0];//获取file组件中的文件
    rd.readAsDataURL(files);//文件读取装换为base64类型
    if (rd == 0)
        alert("请输入图片");
    else {
        $("#display_none2").show();
        rd.onloadend = function (e) {
            $("#display_none2").html("<img src='" + this.result + "' style=\"max-width:250px;max-height:250px;\"/>")
            $.ajax({
                url: "/imageprocessing/A2/",
                method: "POST",
                data: {
                    'data': this.result
                },
                success: function (result) {
                    // 获取result中的code值,其中result值是访问的python视图函数的返回的json数据
                    var code = result["code"];
                    if (code == 200) {
                        $("#display_none3").show();
                        //加载完毕之后，在div中添加一个元素
                        $("#display_none3").html("<img src='data:image/jpeg;base64," + result["datas"] + "' style=\"max-width:250px;max-height:250px;\"/>")
                    } else {
                        alert("发送异常!");
                    }
                },
                error: function (error) {
                    alert("发送请求失败!");
                },
            });
        }
    }
}
function post_pic2(f) {
    var rd = new FileReader();//创建文件读取对象
    var files = f.files[0];//获取file组件中的文件
    rd.readAsDataURL(files);//文件读取装换为base64类型
    if (rd == 0)
        alert("请输入图片");
    else {
        $("#display_none4").show();
        rd.onloadend = function (e) {
            $("#display_none4").html("<img src='" + this.result + "' style=\"max-width:250px;max-height:250px;\"/>")
            $.ajax({
                url: "/imageprocessing/A3/",
                method: "POST",
                data: {
                    'data': this.result
                },
                success: function (result) {
                    // 获取result中的code值,其中result值是访问的python视图函数的返回的json数据
                    var code = result["code"];
                    if (code == 200) {
                        $("#display_none5").show();
                        //加载完毕之后，在div中添加一个元素
                        $("#display_none5").html("<img src='data:image/jpeg;base64," + result["datas"] + "' style=\"max-width:250px;max-height:250px;\"/>")
                    } else {
                        alert("发送异常!");
                    }
                },
                error: function (error) {
                    alert("发送请求失败!");
                },
            });
        }
    }
}
function post_pic3(f) {
    var rd = new FileReader();//创建文件读取对象
    var rd1 = new FileReader();//创建文件读取对象
    if (f.files.length <2)
        alert("请输入2张图片");
    var files = f.files[0];//获取file组件中的文件
    var files1 = f.files[1];//获取file组件中的文件
    rd.readAsDataURL(files);//文件读取装换为base64类型
    rd1.readAsDataURL(files1);//文件读取装换为base64类型
    if (rd == 0 || rd1 == 0)
        alert("请输入图片");
    else {
        rd.onloadend = function (e) {
            $("#display_none6").show();
            $("#display_none6").html("<img src='" + rd.result + "' style=\"max-width:250px;max-height:250px;\"/>")
            rd1.onloadend = function (e) {
                $("#display_none7").show();
                $("#display_none7").html("<img src='" + rd1.result + "' style=\"max-width:250px;max-height:250px;\"/>")
                $.ajax({
                    url: "/imageprocessing/A4/",
                    method: "POST",
                    data: {
                        'data': rd.result,
                        'data1': rd1.result
                    },
                    success: function (result) {
                        // 获取result中的code值,其中result值是访问的python视图函数的返回的json数据
                        var code = result["code"];
                        if (code == 200) {
                            $("#display_none8").show();
                            //加载完毕之后，在div中添加一个元素
                            $("#display_none8").html("<img src='data:image/jpeg;base64," + result["datas"] + "' style=\"max-width:250px;max-height:250px;\"/>")
                        } else {
                            alert("发送异常!");
                        }
                    },
                    error: function (error) {
                        alert("发送请求失败!");
                    },
                });
            }
        }
    }
}
function post_pic4(f) {
    var rd = new FileReader();//创建文件读取对象
    var rd1 = new FileReader();//创建文件读取对象
    if (f.files.length <2)
        alert("请输入2张图片");
    var files = f.files[0];//获取file组件中的文件
    var files1 = f.files[1];//获取file组件中的文件
    rd.readAsDataURL(files);//文件读取装换为base64类型
    rd1.readAsDataURL(files1);//文件读取装换为base64类型
    if (rd == 0||rd1==0)
        alert("请输入2张图片");
    else {
        rd.onloadend = function (e) {
            $("#display_none9").show();
            $("#display_none9").html("<img src='" + rd.result + "' style=\"max-width:250px;max-height:250px;\"/>")
            rd1.onloadend = function (e) {
                $("#display_none10").show();
                $("#display_none10").html("<img src='" + rd1.result + "' style=\"max-width:250px;max-height:250px;\"/>")
                $.ajax({
                    url: "/imageprocessing/A5/",
                    method: "POST",
                    data: {
                        'data': rd.result,
                        'data1': rd1.result
                    },
                    success: function (result) {
                        // 获取result中的code值,其中result值是访问的python视图函数的返回的json数据
                        var code = result["code"];
                        if (code == 200) {
                            $("#display_none11").show();
                            //加载完毕之后，在div中添加一个元素
                            $("#display_none11").html("<img src='data:image/jpeg;base64," + result["datas"] + "' style=\"max-width:250px;max-height:250px;\"/>")
                        } else {
                            alert("发送异常!");
                        }
                    },
                    error: function (error) {
                        alert("发送请求失败!");
                    },
                });
            }
        }
    }
}
$(function () {
    // 延迟函数在网页在加载完毕后执行
    post_pic();
    post_pic1();
    post_pic2();
    post_pic3();
    post_pic4();
});