KindEditor.ready(function(K) {
    var csrfitems = document.getElementsByName("csrfmiddlewaretoken");
    var csrftoken = "";
    if(csrfitems.length > 0)
    {
        csrftoken = csrfitems[0].value;
    }
    window.editor = K.create('textarea[name=content]',{
        width:500,
        height:300,
        items:[
        'source', '|', 'undo', 'redo', '|', 'preview', 'print', 'template', 'code', 'cut', 'copy', 'paste',
        'plainpaste', 'wordpaste', '|', 'justifyleft', 'justifycenter', 'justifyright',
        'justifyfull', 'insertorderedlist', 'insertunorderedlist', 'indent', 'outdent', 'subscript',
        'superscript', 'clearhtml', 'quickformat', 'selectall', '|', 'fullscreen', '/',
        'formatblock', 'fontname', 'fontsize', '|', 'forecolor', 'hilitecolor', 'bold',
        'italic', 'underline', 'strikethrough', 'lineheight', 'removeformat', '|', 'image', 'multiimage',
        'insertfile', 'table', 'hr', 'emoticons', 'pagebreak',
        'anchor', 'link', 'unlink', '|', 'about'
        ],
        uploadJson: '/upload_img/',
        allowFlashUpload: false,
        allowMediaUpload:false,
        allowFileUpload:false,
        allowFileManager:false,
        allowImageRemote:false,
        autoHeightMode: true,
        extraFileUploadParams:{
            csrfmiddlewaretoken: csrftoken,
        },
        afterUpload : function(url, data, name) { //上传文件后执行的回调函数，必须为3个参数
            if(name=="image" || name=="multiimage"){ //单个和批量上传图片时
                var img = new Image(); img.src = url;
                img.onload = function(){ //图片必须加载完成才能获取尺寸
                    if(img.width>600) editor.html(editor.html().replace('<img src="' + url + '"','<img src="' + url + '" width="600"'))
                }
            }
        },
    });
});