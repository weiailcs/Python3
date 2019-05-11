$(function () {
    var passwordhtml = document.getElementById("password_template").innerHTML;
    var qrcodehtml = document.getElementById("qrcode_template").innerHTML;
    $("#login_content").html(passwordhtml);
    var setting = {
        imageWidth: 1680,
        imageHeight: 1050
    };
    var windowHeight = $(window).height();
    var windowWidth = $(window).width();
    var init = function () {
        $(".login_conatiner").height(windowHeight).width(windowWidth);
        $("#container_bg").height(windowHeight).width(windowWidth);
        $("#login_right_box").height(windowHeight);
        var imgW = setting.imageWidth;
        var imgH = setting.imageHeight;
        var ratio = imgH / imgW; //图片的高宽比

        imgW = windowWidth; //图片的宽度等于窗口宽度
        imgH = Math.round(windowWidth * ratio); //图片高度等于图片宽度 乘以 高宽比

        if (imgH < windowHeight) { //但如果图片高度小于窗口高度的话
            imgH = windowHeight; //让图片高度等于窗口高度
            imgW = Math.round(imgH / ratio); //图片宽度等于图片高度 除以 高宽比
        }

        $(".login_img_01").width(imgW).height(imgH);  //设置图片高度和宽度
    };

    init();

    $(window).resize(function () {
        init();
    });

    //点击记住用户名
    $("#rememberName").change(function () {
        if ($(this).is(":checked")) {
            var $u = $("#un").val();
            if ($.trim($u) == '') {
                $("#errormsg").text("账号不能为空。").show();
                $(this).removeClass("checked");
            } else {
                //不等于空，写cookie
                setCookie('dlut_cas_un', $u, 365);
            }
        } else {
            //反选之后清空cookie
            clearCookie('dlut_cas_un');
        }
    });

    //展开收起
    var bottom = "0";
    var right = "10";
    var bottomBf = "35%";
    var rightBf = "184px";
    if (1366 <= windowWidth && windowWidth <= 1440) {
        rightBf = "10%";
    }
    if (1024 <= windowWidth && windowWidth <= 1250) {
        right = "10px";
    }
    if (windowHeight <= 900) {
        bottomBf = (windowHeight - 395) * 0.5;
    }
    if (windowHeight <= 680) {
        bottomBf = (windowHeight - 395) * 0.3;
    }
    $(".toggle_btn").hover(function () {

        if ($(this).attr("name") == "0") {
            $(this).html("收起");

        } else {
            $(this).html("展开");

        }
    }, function () {
        if ($(this).attr("name") == "0") {
            $(this).html("<span class='minus'></span>");

        } else {
            $(this).html("<span class='plus'></span>");

        }
    });
    $(".toggle_btn").click(function () {
        if ($(this).attr("name") == "0") {
            $(this).parent().animate({bottom: bottom, right: right, height: "41px"}, 400);
            $(this).parent().addClass("box-open");
            $(this).append("<span class='plus'></span>");
            $(this).attr("name", "1");
        } else {
            $(this).parent().animate({bottom: bottomBf, right: rightBf, height: "395px"}, 400);
            $(this).parent().removeClass("box-open");
            $(this).append("<span class='minus'></span>");
            $(this).attr("name", "0");
        }
    });
    var lqrcode = new loginQRCode("qrcode", 153, 153);
    //点击账号登陆
    $("#password_login").click(function () {
        $("#password_login").addClass("active");
        $("#qrcode_login").removeClass("active");
        $("#login_content").html(passwordhtml);
        lqrcode.clear();
        window.location.reload();
    });
    //点击扫码登陆
    $("#qrcode_login").click(function () {
        $("#password_login").removeClass("active");
        $("#qrcode_login").addClass("active");
        $("#login_content").html(qrcodehtml);
        lqrcode.generateLoginQRCode(function (token) {
            var service = getParameter(window.location.search, "service", "http%3A%2F%2Fxyfw.cug.edu.cn%2Ftp_up%2F")
            window.location.href = "qRCodeAction?service=" + service + "&token=" + token;
        });
//		//获取token及扫码地址
//		$.ajax({
//	        type : "get",      
//	        url : "qrcodesso", 
//	        dataType : "text",
//	        data :
//	        {
//	        	"type" : "getToken"
//	        },
//	        success : function(result)
//	        {
//	        	var token = result.substring(0,result.indexOf(","));
//	        	var content = result.substring(result.indexOf(",")+1);
//	        	//生成二维码
//	        	setQrcode(content);
//	        	//扫码登录
//	    		qrcodeLogin(content, token);
//	        },
//	        error : function(xhr, status, errMsg)
//	        {
//	             alert("获取token失败");
//	        }
//	    });
    });
    //登录按钮触发
    $("#index_login_btn").click(function () {
        login();
    });

    //用户名文本域keyup事件
    $("#un").keyup(function (e) {
        if (e.which == 13) {
            login();
        }
    }).keydown(function (e) {
        $("#errormsg").hide();
    }).focus();

    //密码文本域keyup事件
    $("#pd").keyup(function (e) {
        if (e.which == 13) {
            login();
        }
    }).keydown(function (e) {
        $("#errormsg").hide();
    });

    //如果有错误信息，则显示
    if ($("#errormsghide").text()) {
        var errorMsg = $("#errormsghide").text() + "，可尝试<a href='pwd'>修改密码</a>";
        $("#errormsg").html(errorMsg).show();
    }

    //获取cookie值
    var cookie = getCookie('dlut_cas_un');
    if (cookie) $("#un").val(cookie);

    //重新获取验证码
    $("#a_changeCode").click(function () {
        getImageCode();
    });

});

function login() {
    var $u = $("#un");
    var $p = $("#pd");


    var u = $u.val().trim();
    if (u == "") {
        $u.focus();
        $("#errormsg").text("账号不能为空。");
        return;
    }

    var p = $p.val().trim();
    if (p == "") {
        $p.focus();
        $("#errormsg").text("密码不能为空。");
        return;
    }

    $u.attr("disabled", "disabled");
    $p.attr("disabled", "disabled");

    var lt = $("#lt").val();

    //setMaxDigits(130);
    $("#ul").val(u.length);
    $("#pl").val(p.length);
    $("#rsa").val(strEnc(u + p + lt, '1', '2', '3'));
    $("#loginForm")[0].submit();
}

function setQrcode(content) {
    $("#qrcode").qrcode({width: 143, height: 143, text: content});
}

function qrcodeLogin(content, token) {
    var search = location.search;
    //跳转url
    var service = getParameter(search, "service", "");
    $.ajax({
        type: "get",
        url: "qrcodesso",
        dataType: "text",
        data:
            {
                "type": "qrcodeLogin",
                "service": service,
                "token": token,
                "content": content
            },
        success: function (result) {
            window.location.href = decodeURIComponent(service);
//        	if(result == "ok"){
//        		window.location.href = decodeURIComponent(service);
//        	}else if(result == "out"){
////        		alert("扫码超时");
//        		window.location.href = decodeURIComponent(service);
//        	}else if(result == "error"){
//        		alert("二维码失效");
//        	}
        },
        error: function (xhr, status, errMsg) {
            alert("扫码失败刷新后重试");
        }
    });
}

function getImageCode() {
    if ($("#mc").length > 0) {
        $("#vali")[0].src = "";
        $("#vali")[0].src = "/tpass/code?" + Math.random();
    }
    ;
}

function getParameter(hash, name, nvl) {
    if (!nvl) {
        nvl = "";
    }
    var svalue = hash.match(new RegExp("[\?\&]?" + name + "=([^\&\#]*)(\&?)", "i"));
    if (svalue == null) {
        return nvl;
    } else {
        svalue = svalue ? svalue[1] : svalue;
        svalue = svalue.replace(/<script>/gi, "").replace(/<\/script>/gi, "").replace(/<html>/gi, "").replace(/<\/html>/gi, "").replace(/alert/gi, "").replace(/<span>/gi, "").replace(/<\/span>/gi, "").replace(/<div>/gi, "").replace(/<\/div>/gi, "");
        return svalue;
    }
}

//设置cookie
function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
}

//获取cookie
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1);
        if (c.indexOf(name) != -1) return c.substring(name.length, c.length);
    }
    return "";
}

//清除cookie  
function clearCookie(name) {
    setCookie(name, "", -1);
} 
