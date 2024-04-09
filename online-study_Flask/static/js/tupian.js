function show(f){
    var rd = new FileReader();//创建文件读取对象
    var files = f.files[0];//获取file组件中的文件
    rd.readAsDataURL(files);//文件读取装换为base64类型
    
    //显示在页面上，取消display:none;
    $("#display_none").show();
    rd.onloadend = function(e) {
        //加载完毕之后，在div中添加一个元素
        $("#display_none").html("<img src='"+this.result+"' width=\"400\" height=\"400\"/>")
    }
}