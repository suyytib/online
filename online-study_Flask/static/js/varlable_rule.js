function varlableRule()
{
    var varlable = document.getElementById("checkVarlable").value;
    if(varlable[0]!='_' && !(varlable[0]>='A' && varlable[0]<='Z')&&!(varlable[0]>='a' && varlable[0]<='z')){
        alert("错误命名");
        return;
    }
    for (var i = 1; i <varlable.length; ++i) {
        if(varlable[0]!='_' && !(varlable[0]>='A' && varlable[0]<='Z')&&!(varlable[0]>='a' && varlable[0]<='z') &&!(varlable[0]<='9' && varlable[0]>='0')){
            alert("错误命名");
            return;
        }     
    }
    alert("正确命名");  
}