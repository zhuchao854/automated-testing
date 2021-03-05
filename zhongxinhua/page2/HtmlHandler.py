# -*- coding: utf-8 -*-
from lxml import etree


class HtmlHandler:
    def __init__(self, htmldata):
        self.htmldata = htmldata

    def getElementAttr(self, selector, attribute):

        xpath = selector + '/@' + attribute
        html = etree.HTML(self.htmldata, etree.HTMLParser())
        result = html.xpath(xpath)
        return result[0]

    def getElementText(self, selector):

        xpath = selector + '/text()'
        html = etree.HTML(self.htmldata, etree.HTMLParser())
        result = html.xpath(xpath)

        return result[0]

    def getElementParaDict(self, selector, key, value):

        xpath = selector
        html = etree.HTML(self.htmldata, etree.HTMLParser())
        result = html.xpath(xpath)
        ls = dict()
        for rs in result:
            ls[rs.get(key)] = rs.get(value)

        return ls

    def getElementCount(self, selector):

        xpath = selector
        html = etree.HTML(self.htmldata, etree.HTMLParser())
        try:
            result = html.xpath(xpath)
            element_cnt = len(result)
        except:
            element_cnt = 0

        return element_cnt


if __name__ == "__main__":
    h = '''



<script src="/system/js/callJlcPlugin-4355cf840c.js" type="text/javascript"></script>
<script src="/system/js/iframeMessenger-fa8ca294cf.js" type="text/javascript"></script>





<html>
<head>
<script src="/client/jQuery/jquery-1.3.2.min.js" type="text/javascript"></script>
<link href="/css/ct-style-9852ccdce8.css" rel="stylesheet"></link>
<script src="/system/js/pubfunctions-e94dd690ca.js" type="text/javascript"></script>
<script src="/system/js/pub-1a7ff356c0.js" type="text/javascript"></script>
<script src="/system/calendar/calendar-3fa5e5a637.js" type="text/javascript"></script>
<script src="/product/smt/js/smt_order-4061c84fdf.js" type="text/javascript"></script>
<script src="/product/smt/js/overseas_smt_order-664b91d206.js" type="text/javascript"></script>

<script type="text/javascript">var contextPath = "";</script>
<link href="/css/ct-style-9852ccdce8.css" rel="stylesheet"></link>
<link href="/system/css/plugin-d41d8cd98f.css" rel="stylesheet"></link>
<script src="/client/jQuery/jquery-1.3.2.min.js" type="text/javascript"></script>
<script src="/system/js/function-007544b52a.js" type="text/javascript"></script>
<script src="/system/js/plugin-32915bf27a.js" type="text/javascript"></script>
<script type="text/javascript">$(function(){ showOperateResult("下单完成！"); });</script>

<title>系统管理</title>
<input type="hidden" id="webRoot" value="" />
<style type="text/css">
	.table_list tr td{
		text-align: center;
	}
	.ask_div{ margin:0 auto; border:3px solid #777;width:795px; padding-bottom:20px; background:#fff; top:0px; margin-top:5%; color:#444; }
	.ask_nr{width:497px; margin:0 auto; font-size:12px; border:0px solid red; padding-top:10px; color: #777777}
</style>

<script type="text/javascript">

	//选中行效果
	function trOnClick(trObj){
		autoSelectRow(trObj.parentNode.rows,'tr_',trObj.sectionRowIndex);
	}

	//查询
	function search(){
		
		var form=document.getElementById("allProjectFrom");
		form.action="/smt/SmtOrderAction!submitSmtOrderToFactory.action";
		form.submit();
	}
	
	// 提取
	function pickUpFile() {
		
		$("#pickUpFileBtn").attr('disabled', true);
		
		if ($("input[type=radio]:checked").length != 1 ) {
			
			alert("请选择您要提取的订单！");
			$("#pickUpFileBtn").attr('disabled', false);
			
			return false;
		}
		
		var form=document.getElementById("allProjectFrom");
		
		form.action="/smt/SmtOrderAction!pickUpSmtProjectFile.action";
		
		form.submit();
	}
	
	//提取  按内编
	function pickUpFileByInnerNumber(){
		
		$("#pickUpFileBtnByIncodeNumber").attr('disabled', true);
		
		if ($("input[type=radio]:checked").length != 1 ) {
			
			alert("请选择您要提取的订单！");
			$("#pickUpFileBtnByIncodeNumber").attr('disabled', false);
			
			return false;
		}
		
		var insideNumber = $("input[type=radio]:checked").attr('insideNumber');
		
		if(insideNumber == null || $.trim(insideNumber) == ''){
			
			alert("该订单还未上传内部编号！");
			$("#pickUpFileBtnByIncodeNumber").attr('disabled', false);
			return false;
		}
		
		var url="/smt/SmtOrderAction!pickUpSmtProjectFileByIncodeNumber.action?incodeNumber=" + insideNumber;
	 	document.location.href=url;
	}
	
	// 完成
	function setPickUpFinish() {
		
		$("#setPickUpFinishBtn").attr('disabled', true);
		
		if ($("input[type=radio]:checked").length != 1 ) {
			
			alert("请选择您要完成提取的订单！");
			$("#setPickUpFinishBtn").attr('disabled', false);
			
			return false;
		}
		
		var form=document.getElementById("allProjectFrom");
		
		form.action="/smt/SmtOrderAction!setPickUpFinish.action";
		
		form.submit();
	}
	
	// 扫描工程文件
	function scanProjectFile() {
		
		$("#scanBtn").attr("disabled","disabled");
		
		if (!confirm("扫描工程文件耗时较长，您确定要进行此操作吗？")) {
			
			$("#scanBtn").removeAttr("disabled");
			
			return false;
		}
		
		var form=document.getElementById("allProjectFrom");
		
		form.action="/smt/SmtOrderAction!scanProjectFile.action";
		
		form.submit();
	}
	
	// 下载内部编号下的文件
	function downloadIncodeNumberFile(){
		
		var incodeNumber = $('#incodeNumber').val();
		if(incodeNumber.trim() == ''){
			
			alert("请输入内部编号!");
			$('#incodeNumber').focus();
			return;
		}
		
		/* if ($("input[type=radio]:checked").length != 1 ) {
			
			alert("请选择您要下载文件的订单！");
			return false;
		}
		
		var insideNumber = $("input[type=radio]:checked").attr('insideNumber');
		
		if(insideNumber == null || $.trim(insideNumber) == ''){
			
			alert("该订单还未上传内部编号！");
			return false;
		} */
		
		var url="/smt/SmtOrderAction!downloadIncodeNumberFile.action?incodeNumber=" + incodeNumber;
	 	document.location.href=url;
	}
	
	// 选中记录下载
	function downloadSingleIncodeNumberFile() {

		var idList = $('input[name=idList]:checked');
		if (idList.length == 0) {

			alert("请选中一条记录下载!");
			return;
		}

		var url = "/smt/SmtOrderAction!downloadIncodeNumberFile.action?idList=" + idList.val();
		document.location.href = url;
	}
	
	//打开下钢网订单页面
	function openAddSteelmeshOrder(){

		var incodeNumber = $('#incodeNumber').val();
		
		if(incodeNumber == null || incodeNumber.trim() == ''){
			
			if ($("input[type=radio]:checked").length != 1 ) {
				
				alert("请输入内部编号或选择您要下钢网的SMT订单！");
				return false;
			}
			
			var insideNumber = $("input[type=radio]:checked").attr('insideNumber');
			
			if(insideNumber == null || $.trim(insideNumber) == ''){
				
				alert("该SMT订单还未上传内部编号，暂不能下钢网订单！");
				return false;
			}
			
			incodeNumber = insideNumber;
			
		}
		
		var url="/smt/SmtOrderAction!addSteelmeshOrderInit.action?incodeNumber=" + incodeNumber;
	 	document.location.href=url;
	 	
	}
	
	//查看钢网进度
	function viewSteelmeshProcess(steelmeshOrderRecordId){
		
		var url=basePath+"/steelmesh/steelmeshOrderAction!selectSteelProcessDetails.action?steelmeshOrderRecordId="+steelmeshOrderRecordId;
		var myWinObj= window.open(url,"选择与钢网一起发货",'width=800,height=500 , left=400, resizable=yes,location=no,menubar=no,scrollbars=yes,status=yes,toolbar=no,fullscreen=no,dependent=no,status');
		myWinObj.focus();
	}
	
	//替换文件
	function replaceSmtOrderFile(){
		
		$("#replaceOrderFile").attr('disabled', true);

        var $checkedInput = $(":input[name=idList]:checked");
		if ($checkedInput.length != 1 ) {

			alert("请选择您要替换文件的订单！");
			$("#replaceOrderFile").attr('disabled', false);
			
			return false;
		}

        var overseasType = $checkedInput.attr("overseasType");
        if ("true" == overseasType){
            alert("外贸订单不允许替换文件！");
            $("#replaceOrderFile").attr('disabled', false);
            return false;
        }

		var orderStatus = $checkedInput.attr('orderStatus');
		if(orderStatus != 4){
			
			alert("该订单已发货，不能替换文件！");
			$("#replaceOrderFile").attr('disabled', false);
			return false;
		}

		var insideNumber = $checkedInput.attr('insideNumber');
		
		if (!confirm("替换文件会取消当前SMT订单，确定允许替换文件？\n注意：支付方式非快递代收的会自动退款到预付款中！")) {

			$("#replaceOrderFile").attr('disabled', false);
			return false;
		}

		var deductEnginFee = "0";
		
		if(parseFloat(deductEnginFee) > 0 ){

			if (confirm("是否需要扣取"+deductEnginFee+"元工程费用,如果二次替换将不再收取！")) {

				$("#isDeductEnginFee").val(true);
			}
		}
		
		var form=document.getElementById("allProjectFrom");
		
		form.action="/smt/SmtOrderAction!updateSmtReplaceFile.action";
		
		form.submit();
	}
	
	// 下载拼版资料
	function downloadIncodePasteBoardFile() {
		
		var incodeNumber = $('#incodeNumber').val();
		
		if(!incodeNumber.trim()){
			
			alert("请输入内部编号!");
			$('#incodeNumber').focus();
			return;
		}
		
		var url = "/smt/SmtOrderAction!checkIncodePasteBoardFile.action?incodeNumber="+incodeNumber;
		
		// 验证拼版需要的文件是否都存在
		$.ajax({
			type:'post',
			url:url,
			async:false,
			success:function(data) {
				
				if (data == 'success') {
					var url="/smt/SmtOrderAction!downloadIncodePasteBoardFile.action?incodeNumber=" + incodeNumber;
				 	document.location.href=url;
				} else if (data == 'fail') {
					alert('内部编号：' + incodeNumber + '下没有找到SMT单只文件，请稍后再试！');
					return false;
				} else if (data == 'error') {
					alert('内部编号：' + incodeNumber + '下存在未生成的SMT单只文件，请稍后再试！');
					return false;
				} else if (data == 'cancel') {
					alert('内部编号：' + incodeNumber + '下未找到PCB订单光辉文件，请稍后再试！');
					return false;
				} else if (data == 'existed') {
					alert('内部编号：' + incodeNumber + '没有分配拼版，请稍后再试！');
					return false;
				}
			},
			error:function(){
				alert("下载拼版资料出错，请重新操作！");
				return false;
			}
		});
	}

    // 下载SMT拼板文件
    function downloadSmtPasteFile() {

        var incodeNumber = $('#incodeNumber').val();

        if(!incodeNumber.trim()){

            alert("请输入内部编号!");
            $('#incodeNumber').focus();
            return;
        }

        var url="/smt/SmtOrderAction!downloadSmtPasteFile.action?incodeNumber=" + incodeNumber;
        document.location.href=url;
    }

	// 下载上机贴片资料
	function downloadIncodePasteFile() {

		var incodeNumber = $('#incodeNumber').val();

		if(!incodeNumber.trim()){

			alert("请输入内部编号!");
			$('#incodeNumber').focus();
			return;
		}
		$(".btn_href").attr("disabled", "disabled");
		var url="/smt/SmtOrderAction!downloadPasteFileZip.action?incodeNumber=" + incodeNumber;
	 	document.location.href= url;

	 	/*延时3秒放开所有按钮*/
        window.setTimeout(function(){
			$(".btn_href").removeAttr("disabled");
        },3000)
	}

    // 校验下载上机贴片资料
    function checkDownloadPasteFileZip() {

        var incodeNumber = $('#incodeNumber').val();

        if (!incodeNumber.trim()) {

            alert("请输入内部编号!");
            $('#incodeNumber').focus();
            return;
        }
        $(".btn_href").attr("disabled", "disabled");
        var url = "/smt/SmtOrderAction!checkDownloadPasteFileZip.action";
        $.ajax({
            type: "POST",
            url: url,
            data: "incodeNumber=" + incodeNumber,
            success: function (text) {

                if (text == "success") {
                    downloadIncodePasteFile();
                } else {

                    if (confirm(text + ", 点击确定将会忽略错误强制生成上机贴片资料")) {
                        var person = prompt("请输入强制下载密码：", "");
                        if (person == "JLC"){
                            downloadIncodePasteFile();
                        }else{
                            if (person != null && person != ''){
                            	confirm(" 密码错误!");
							}
                            $(".btn_href").removeAttr("disabled");
                        }
                    }else{
                        $(".btn_href").removeAttr("disabled");
					}
                }
            }
            , error: function () {
                alert("系统繁忙，请稍候再试");
                $(".btn_href").removeAttr("disabled");
            }
        });
    }

	function downloadTodaySoNum(){
		var url="/smt/SmtOrderAction!downloadTodaySoNum.action";
	 	document.location.href=url;
	}

	function pickUpFinishByInnerNumber(){

        $("#pickUpFinishByInnerNumberBtn").attr('disabled', true);

        if ($("input[type=radio]:checked").length != 1 ) {

            alert("请选择您要完成的订单！");
            $("#pickUpFinishByInnerNumberBtn").attr('disabled', false);

            return false;
        }

        var insideNumber = $("input[type=radio]:checked").attr('insideNumber');

        if(insideNumber == null || $.trim(insideNumber) == ''){

            alert("该订单还未上传内部编号！");
            $("#pickUpFinishByInnerNumberBtn").attr('disabled', false);
            return false;
        }

        var url="/smt/SmtOrderAction!pickUpFinishByInnerNumber.action?incodeNumber=" + insideNumber;
        document.location.href=url;
	}

    /**
	 * 扫描SMT钢网文件
     */
	function scanSmtSteelmeshFile() {
        var $form = $("#allProjectFrom");
        $form.attr("action", "/smt/SmtOrderAction!scanSmtFile.action");
        $form.submit();
        $form.attr("action", "/smt/SmtOrderAction!submitSmtOrderToFactory.action");
	}

	function smtOrderBack(){

		var selectItem = $(" input[name=idList]:checked");
		if(selectItem.length !=1 ){
			alert('请选择一条记录进行操作！');
			return;
		}

		var orderId =  selectItem.val();
		var url = basePath + "/smt/smtOrderBackAction!checkOrderBack.action";
		$.ajax({
			type: "POST",
			url: url,
			data:"smtOrderId="+orderId,
			dataType: 'text',
			success: function(text){
				if(text == "success"){
					var url = basePath + "/smt/smtOrderBackAction!addOrderBackInit.action?smtOrderId="+orderId;
					var obj=window.open(url, "addOrderBackInit", 'width=1050,height=700, top=100, left=300, resizable=yes,location=no,menubar=no,scrollbars=yes,status=yes,toolbar=no,fullscreen=no,dependent=no,status');
					obj.focus();
				}else {
					alert(text);
				}
			}
			,error :function(){
				alert("系统繁忙，请稍候再试");
			}
		});
	}

    /**
	 * 取消订单前判断是否存在内编
     * @param obj
     * @param smtOrderId
     * @param pcbOrderType
     */
	function decideIfExistInsideNumber(obj,smtOrderId,pcbOrderType) {
	    if($(obj).val() == "cancel"){
            if("" == $("#insideNumber"+smtOrderId).val()){
                cancelSmtOrderInSubmitFactory(obj,smtOrderId,pcbOrderType);
            }else{
                alert("当前smt订单已经有内编，如果需要取消，请通知SMT工程在SMT工程处理列表中取消订单");
            }
		}
    }

    /**
	 * 标记需要修改上机贴片资料初始化
     */
    function addSmtProblemInit() {

        // 业务id
        var businessId = $("#incodeNumber").val();

        if ("" == businessId) {

            alert('请输入内部编号！');
            $("#incodeNumber").focus();
            return false;
        }

        var url = basePath + "/smt/SmtOrderAction!checkOrderByProblem.action";

        $.ajax({
            type: "POST",
            url: url,
            data:"businessId="+businessId,
            dataType: 'text',
            success: function(text){
                if(text == "success"){

                    $("#businessId").val(businessId);

                    if (confirm("是否改上机贴片资料?")) {

                        $("#insideNumberStr").html(businessId);

                        $("#addSmtProbleDiv").show();
                    }

                }else if(text == "nullity"){
                    alert("请输入正确的内部编号！");
                }else if(text == "existed"){
					alert("已标记修改上机贴片资料，不能重复标记！")
				}
            }
            ,error :function(){
                alert("系统繁忙，请稍候再试");
            }
        });
    }

    /**
     * 标记需要修改上机贴片资料初始化
     */
    function selectSmtProblemRecord(incodeNumber) {

        var url = basePath + "/smt/SmtProblemRecordAction!selectUpdateUpPatchData.action";

        var fileUrl = basePath + "/smt/SmtProblemRecordAction!downloadUpdatePatchFile.action";

        $.ajax({
            type: "POST",
            url: url,
            data: {"businessId" : incodeNumber},
            dataType:'json',
            success: function(obj){

                var result = obj.result;

                if(result == "success"){

                    $("#addSmtProbleDiv").show();

                    //内部编号
                    $("#insideNumberStr").html(obj.smtProblemRecord.businessId);

                    //责任人
                    $("#responsibilityBy").find("option[text='"+obj.smtProblemRecord.responsibilityBy+"']").attr("selected",true);

                    $("#responsibilityBy").find("option[value='"+obj.smtProblemRecord.responsibilityBy+"']").attr("selected",true);

                    //责任描述
                    $("#problemReason").val(obj.smtProblemRecord.problemReason);

                    //问题描述
                    $("#problemReasonDescribe").val(obj.smtProblemRecord.problemReasonDescribe);

                    $("#saveSmtProblemTD").hide();

                    $("#cancelSmtProblemDiv").show();

                    //上机贴片资料
                    var smtFileUrl = obj.smtUpdatePatchFileUrl;
                    var smtFileName = obj.smtUpdatePatchFileName;

                    if (null != smtFileUrl) {
                        $("#smtPinBanWorkFile").hide();
                        $("#smtPinBanWorkFileUrl").show();
                        $("#smtPinBanWorkFileUrl").attr("href", fileUrl + '?smtFilePath='+smtFileUrl+'&smtFileName='+smtFileName);
                        $("#smtPinBanWorkFileUrl").attr("text",obj.smtUpdatePatchFileName);
                    }

                }
            }
            ,error :function(){
                alert("系统繁忙，请稍候再试");
            }
        });

    }

    //关闭查询上机贴片资料DIV,并清除数据
    function cancelSmtProblemDiv() {

        $("#addSmtProbleDiv").hide();

        $("#insideNumberStr").html('');

        $("#responsibilityBy").find("option[value='']").attr("selected",true);

        $("#problemReason").val('');

        $("#smtPinBanWorkFile").show();

        $("#problemReasonDescribe").val('');

        $("#smtPinBanWorkFileUrl").hide();

        $("#cancelSmtProblemDiv").hide();

        $("#saveSmtProblemTD").show();
    }

    // 关闭需修改上机贴片资料div
    function closeSmtProblemDiv() {
		$("#addSmtProbleDiv").hide();
    }

    // 提交需修改上机贴片资料原因
    function saveSmtProblem() {

        // 业务id
        var businessId = $("#businessId").val();
        // 责任人
        var responsibilityBy = $("#responsibilityBy option:selected").val();
        // 修改原因
        var problemReason = $("#problemReason").val();
        // 修改问题描述
        var problemReasonDescribe = $("#problemReasonDescribe").val();

        var fileName = $("#smtPinBanWorkFile").val();

        //判断后缀是不是需要的文件类型
        if(fileName != null && fileName != ""){

            var start = fileName.lastIndexOf(".")+1;
            var length = fileName.length;
            var fileType = fileName.substring(start,length);
            if(fileType != "rar" && fileType != "zip"){

                alert("请上传正确格式的文件!仅支持rar、zip压缩包文件。");
                return false;
            }else{

				//获取上传文件的文件名
                var fileName=fileName.replace(/^.+?\\([^\\]+?)(\.[^\.\\]*?)?$/gi,"$1");

				$("#smtPinBanWorkFileName").val(fileName+'.'+fileType);
            }
        }

        if(!businessId){

            alert('请输入内部编号！');
            $("#incodeNumber").focus();
            return false
        }

        if (!responsibilityBy) {
			alert('请选择责任人！');
			return false;
        }
        if (!problemReason) {
			alert('请填写修改原因！');
			$("#problemReason").select();
			return false;
        }

        responsibilityBy = encodeURIComponent(encodeURIComponent(responsibilityBy));
        problemReason = encodeURIComponent(encodeURIComponent(problemReason));
        problemReasonDescribe = encodeURIComponent(encodeURIComponent(problemReasonDescribe));

		var form=document.getElementById("smtProblemFrom");
		form.submit();
    }

    // 取消标记要改上机贴片资料
    function cancelSmtProblem() {

        // 业务id
        var businessId = $("#incodeNumber").val();

        if ("" == businessId) {

            alert('请输入内部编号！');
            $("#incodeNumber").focus();
            return false;
        }

        if (confirm("确定上机贴片资料不用修改了？")) {
            var form=document.getElementById("allProjectFrom");
            form.action="/smt/SmtOrderAction!cancelSmtProblem.action?businessId="+businessId;
            form.submit();
        }
    }

    /*标记订单为禁止返单*/
    function markSmtOrderNotBack(){

        var selectItem = $(" input[name=idList]:checked");
        if(selectItem.length !=1 ){
            alert('请选择一条记录进行操作！');
            return;
        }

        var asLockBack = selectItem.attr("asLockBack");
        if (asLockBack == 'yes'){
            alert('已设置为禁止返单,请不要重复设置！');
            return;
        }
        var orderId =  selectItem.val();
        var url = basePath + "/smt/smtOrderBackAction!markSmtOrderNotBack.action";
        $.ajax({
            type: "POST",
            url: url,
            data:"smtOrderId="+orderId,
            dataType: 'text',
            success: function(text){
                if(text == "success"){
					alert("标记成功")
                    window.location.reload();
                }else {
                    alert(text);
                }
            }
            ,error :function(){
                alert("系统繁忙，请稍候再试");
            }
        });
    }

</script>

</head>
<body >
	<!-- 隐藏页面名称，下面的iframe页面获取 -->
	<input type="hidden" name="hiddenPageName" id="hiddenPageName" value="factory"/>
	
	<form id="allProjectFrom" name="allProjectFrom" action="/smt/SmtOrderAction!submitSmtOrderToFactory.action" method="post">
	<input type="hidden" name="isDeductEnginFee" value="" id="isDeductEnginFee"/>
		<table width="100%" border="0" cellpadding="0" cellspacing="0">
			<tr>
				<td colspan="2" valign="top" align="center" class="bg_qian_gray">
					<table width="100%" border="0" cellspacing="0" cellpadding="0">
						<tr>
							<td class="bg_blue" height="30">
								&nbsp;&nbsp;<img src="/system/images/icon-7b55d7dc16.gif" width="23" height="19" align="absmiddle">
								&nbsp;<span class="font_white_arial">投单管理&gt;提交工厂</span>
							</td>
						</tr>
					</table>
					<div style="margin-top: 20px; padding: 0px 5px 5px 5px; background: white; width: 100%;">
							<table width="100%" cellpadding="3" class="bg_white">
								  <tr>
								    <td colspan="5" valign="bottom" class="font9"><span class="font_gray_kai">已提交工厂</span></td>
								  </tr>
								   <tr>
								    <td  valign="middle" class="font9" align="left" nowrap>
								    	客户编号：
									    <input type="text" name="customerCode" size="10" value="" id="allProjectFrom_customerCode"/>
								    	&nbsp;&nbsp;
								    	订单编号：
									    <input type="text" name="smtOrderCode" size="10" value="" id="allProjectFrom_smtOrderCode"/>
										&nbsp;&nbsp;
										 提取状态：
										<select name="pickUpStatus" id="allProjectFrom_pickUpStatus">
    <option value="">请选择</option>
    <option value="1">未提取</option>
    <option value="2">已提取</option>
    <option value="3">已完成</option>


</select>

 
										&nbsp;&nbsp;
										提取人：
										<input type="text" name="pickUpUserName" size="10" value="" id="allProjectFrom_pickUpUserName"/>
										&nbsp;&nbsp;
										确认时间：
										<input type="text" name="beingOrderTime" size="9" value="2020-02-18" id="beingOrderTime"/>
								     	<label >
									   		<img valign="middle" src="/system/calendar/calendar-81296cff1f.gif"   onClick="new Calendar(2009).show(document.getElementById('beingOrderTime'));" style="cursor:pointer;" />
								      	</label> &nbsp;-&nbsp;
								    	<input type="text" name="endOrderDate" size="9" value="2020-03-18" id="endOrderDate"/>
								     	<label >
									   		<img valign="middle" src="/system/calendar/calendar-81296cff1f.gif"   onClick="new Calendar(2009).show(document.getElementById('endOrderDate'));" style="cursor:pointer;" />
								     	</label>
								     	&nbsp;&nbsp;
										异常金额：
										<input type="text" name="queryErrorPrice" size="10" value="" id="queryErrorPrice"/>&nbsp;&nbsp;
										是否外贸订单&nbsp;<select name="queryOverseasType" id="allProjectFrom_queryOverseasType">
    <option value=""
    >请选择</option>
    <option value="yes">是</option>
    <option value="no">否</option>


</select>

&nbsp;&nbsp;
									</td>
								  </tr>	
								  <tr>
								  	<td align="left" class="font9" >
								  		交期：
										<input type="text" name="beginAchieveDate" size="9" value="" id="beginAchieveDate"/>
								     	<label >
									   		<img valign="middle" src="/system/calendar/calendar-81296cff1f.gif"   onClick="new Calendar(2009).show(document.getElementById('beginAchieveDate'));" style="cursor:pointer;" />
								      	</label> &nbsp;-&nbsp;
								    	<input type="text" name="endAchieveDate" size="9" value="" id="endAchieveDate"/>
								     	<label >
									   		<img valign="middle" src="/system/calendar/calendar-81296cff1f.gif"   onClick="new Calendar(2009).show(document.getElementById('endAchieveDate'));" style="cursor:pointer;" />
								     	</label>&nbsp;&nbsp;
								     	内部编号：
										<input type="text" name="incodeNumber" size="20" value="43H2" id="incodeNumber"/>&nbsp;&nbsp;
										钢网编号：
										<input type="text" name="steelmeshOrderCode" size="20" value="" id="steelmeshOrderCode"/>&nbsp;&nbsp;
										订单类型&nbsp;<select name="orderType" id="allProjectFrom_orderType">
    <option value=""
    >请选择</option>
    <option value="1">样板</option>
    <option value="0">小批量</option>


</select>

&nbsp;&nbsp;
										是否查询已发货&nbsp;<select name="fiveStatus" id="allProjectFrom_fiveStatus">
    <option value="yes">是</option>
    <option value="no" selected="selected">否</option>


</select>

&nbsp;&nbsp;
										<input type="button" class="btn_href" value=" 查 询 " onclick="search();"/>&nbsp;&nbsp;
										
										<input type="button" id="download" class="btn_href" value="下载 " title="下载内部编号下的文件" onclick="downloadIncodeNumberFile();"/>&nbsp;&nbsp;
										<input type="button" id="addSteelmeshOrder" class="btn_href" value="下钢网订单" onclick="openAddSteelmeshOrder();"/>&nbsp;&nbsp;
										<input type="button" id="replaceOrderFile" class="btn_href" value="替换文件" onclick="replaceSmtOrderFile();" />&nbsp;&nbsp;
										
										<input type="button" id="downloadPasteBoardFile" class="btn_href" value="下载拼版资料（四期）" onclick="downloadSmtPasteFile();" />&nbsp;&nbsp;
										<input type="button" id="downloadPasteFile" class="btn_href" value="下载上机贴片资料" onclick="checkDownloadPasteFileZip();" />&nbsp;&nbsp;
										
										

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>功能说明</title>

<script type="text/javascript">
function demandExplainShow(){
	
 	var paramUrl = location.href ;
	var url="/component/demandExplainMangerAction!queryDemandExplainPageByUrl.action?paramUrl="+paramUrl;
    var name='说明文档';                            //网页名称，可为空; 
    var iWidth=1100;                          //弹出窗口的宽度; 
    var iHeight=600;                         //弹出窗口的高度; 
    //获得窗口的垂直位置 
    var iTop = (window.screen.availHeight - 30 - iHeight) / 2; 
    //获得窗口的水平位置 
    var iLeft = (window.screen.availWidth - 10 - iWidth) / 2; 
    var win = window.open(url, name, 'height=' + iHeight + ',,innerHeight=' + iHeight + ',width=' + iWidth + ',innerWidth=' + iWidth + ',top=' + iTop + ',left=' + iLeft + ',status=no,toolbar=no,menubar=no,location=no,resizable=yes,scrollbars=yes,titlebar=no'); 
    if(win){
		win.focus();
	}
}

</script>

</head>
<body>
<input type="button" name="pageButton" value="功能说明"  onclick="demandExplainShow();" class="btn_href">&nbsp;&nbsp;
</body>
</html>
										
										<input type="button" class="btn_href" value="填写SMT返厂记录" onclick="smtOrderBack();"/>&nbsp;&nbsp;
										<input type="button" class="btn_href" value="标记要改上机贴片资料" onclick="addSmtProblemInit();"/>&nbsp;&nbsp;
										<input type="button" class="btn_href" value="取消标记要改上机贴片资料" onclick="cancelSmtProblem();"/>&nbsp;&nbsp;
										<input type="button" class="btn_href" value="标记禁止返单" onclick="markSmtOrderNotBack();"/>&nbsp;&nbsp;
										<input type="button" class="btn_href" value="取消外贸订单"  onclick="cancelOverseasSmtOrderStatusInit(this);" id="cancelOverseasSmtOrderStatusInitInput" />&nbsp;&nbsp;
									</td>
								  </tr>
								</table>
							<table class="table_list" width="100%" border="1" cellspacing="0" cellpadding="0" bordercolor="#b0c4de" style="border-collapse: collapse">
								<tr>
									<th nowrap="nowrap" width="3%">&nbsp;选择&nbsp;</th>
									<th nowrap="nowrap">客户编号</th>
									<th nowrap="nowrap">生产订单编号</th>
									<th nowrap="nowrap">业务代号</th>
									<th nowrap="nowrap">订单编号</th>
									<th nowrap="nowrap">内部编号</th>
									<th nowrap="nowrap">提取状态</th>
									<th nowrap="nowrap">PCB文件</th>
									<th nowrap="nowrap">PCB订单编号</th>
									<!-- <th nowrap="nowrap">BOM清单</th>
									<th nowrap="nowrap">坐标文件</th> -->
									<th nowrap="nowrap">板子长度</th>
									<th nowrap="nowrap">板子宽度</th>
									
									<th nowrap="nowrap">确认时间</th>
									<th nowrap="nowrap">交期</th>
									<th nowrap="nowrap">查看钢网订单</th>
									<th nowrap="nowrap">是否修改上机贴片资料</th>
									<th nowrap="nowrap">发货日期</th>
									<th nowrap="nowrap">快递公司</th>
									<th nowrap="nowrap">快递单号</th>
									<th nowrap="nowrap">PCB订单类型</th>
									<th nowrap="nowrap">是否禁止返单</th>
									<!-- <th nowrap="nowrap">PCB资料类型</th> -->
									<th nowrap="nowrap">备注</th>
								</tr>
								<tbody>
									
										<tr onclick="trOnClick(this);" id="tr_0">
											<label for="smt_431865"> 
												<td align="center">
												  	<input type="radio" id ='smt_431865' name="idList" value='431865' orderStatus='4' insideNumber='43H2' deductEnginFee =''
														   isUpdatePatchData=" " isLockBack="" overseasType="false" />
												</td>
												<td nowrap="nowrap">00012A</td>
												<td align="left" nowrap="nowrap">
													Y3131
												</td>
												<td nowrap="nowrap">AB</td>
												<td nowrap="nowrap">
													<a target="updateSmtOrder" onclick="setid();" 
														href="/smt/SmtOrderAction!selectSmtOrderBySmtOrderId.action?smtOrderId=431865&method=update&updateType=yes&operateType=display&orderType=1" >
														SMT200318001
													</a>
												</td>
												<td align="left" nowrap="nowrap">
													43H2
													<input type="hidden" id="insideNumber431865" value="43H2">
												</td>
													
												
												<td nowrap="nowrap" bgcolor="#F0F8FF">完成</td>
												
												<td>
													<a href="javascript:void(0);" onclick="uploadFilePcb('/orders/download.action','PCB_V1.2_Gerber20181207','E09AAAE1167186AF95210BD4BC05F87B84615B446D56D66201F741A73999C22582F5F30198CDC0DBA95C8F05407FCAACAAE1F5BB872CBF8466DB7C345B771F66820030D1A91BE882')">PCB_V1.2_Gerber20181207</a>
												</td>
												<td nowrap="nowrap">
													Y3131
												</td>
												
												<td nowrap="nowrap">
													50.00&nbsp;CM/SET
												</td>
												<td nowrap="nowrap">
								            		20.00&nbsp;CM/SET
												</td>
												
												<td nowrap="nowrap">2020-03-18 10:55:02&nbsp;</td>
												<td nowrap="nowrap">2020-03-22 20:00:00&nbsp;<a href="javascript:void(0);" onclick="viewWipProcess('431865');">生产进度</a></td>
												<!-- 查看钢网进度 -->
												<td nowrap="nowrap">
													
														<a href="javascript:;" onclick="viewSteelmeshProcess('2067436')">SO200318058</a>
														
													
													
												</td>
												<td nowrap="nowrap">
													
													
												</td>
												<td nowrap="nowrap">2020-03-20 10:55:01&nbsp;</td>
												
												<td nowrap="nowrap">顺丰&nbsp;</td>
												<td nowrap="nowrap">&nbsp;</td>
												
												<td>	
													
													样板
													
													&nbsp;
												</td>
												<td>
													
													
													否
													&nbsp;
												</td>
												<td>嘉立创封装库&nbsp;</td>
											</label>
										</tr>
									
									<tr>
										<td colspan="29"></td>
									</tr>
								</tbody>
							</table>
							<!-- 嵌入分页标签  -->
							
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<script type="text/javascript">
	//页面加载时设置为当前时间，避免加载后立即刷新页面
    window.lastSubmitTime = new Date().getTime();
    var oldOnSubmit = document.allProjectFrom.onsubmit;

    document.allProjectFrom.onsubmit =  function () {
        var nowTime = new Date().getTime();
        if(window.lastSubmitTime && nowTime - window.lastSubmitTime < 500){
            return false;
        }
        window.lastSubmitTime = nowTime;
        if(oldOnSubmit){
            return oldOnSubmit();
        }
    };

	//按回车刷新列表
	document.onkeyup=function(){
		if (event.keyCode==13)
		{
		    //防止快速按Enter键时连续触发多次
			var nowTime = new Date().getTime();
		    if(window.lastSubmitTime && nowTime - window.lastSubmitTime < 500){
		         return;
			}
            window.lastSubmitTime = nowTime;

			getPageList();
		}
	}

</script>
<style type="text/css">

</style>
</head>
<body  >




		<table align="right" width="95%" border="0" cellspacing="2"
			cellpadding="0" style="font-size: 13px; text-decoration: none; margin-top:10px">
			<tr>
				<td align="center">有 <span style="color: red;">
				1 </span> 条记录 共 <span style="color: red;">
				1 </span> 页 当前第 <span style="color: red;">
				1 </span> 页 &nbsp;&nbsp;
				
					
							 <a style="text-decoration: none;" href="javascript:void(0);" title="已经是最前一页" >首页</a>
					
					
				

					 &nbsp;&nbsp; <a href="javascript:void(0);"  style="text-decoration: none;"
					onclick="getPageList('upage')" title="上一页">上一页</a> &nbsp;&nbsp; <a href="javascript:void(0);"  style="text-decoration: none;"
					onclick="getPageList('next')"  title="下一页">下一页</a> &nbsp;&nbsp;
					
					
							 <a style="text-decoration: none;" href="javascript:void(0);"  title="已经是最后一页" >尾页</a>
					
					
				

					</td>
			</tr>

			<tr height="30">

				<td></td>
			</tr>

		</table>



 


	


<input name="currePage" value="1" id="currePage" type="hidden">
<input name="countPage" value="1" id="countPage" type="hidden">
</body>
</html>

					</div>
				</td>
			</tr>
		</table>
	</form>



	<div align="center" >
		<iframe width="100%;" frameborder="0" height="600px;" name="updateSmtOrder" id="updateSmtOrder" style="border: none; " ></iframe>
	</div>
	<!-- 点击客户编号看详情  光标定位到底部   -->
	<a href="#" id="page_bottom"></a>

	<form id="smtProblemFrom" name="smtProblemFrom" action="/smt/SmtOrderAction!saveSmtProblem.action" method="post" enctype="multipart/form-data">
	
	<div id="addSmtProbleDiv" style="display: none; " >
		<div style="z-index: 1000; position: fixed; filter: progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=25,finishOpacity=75);BACKGROUND: #777; WIDTH: 100%; HEIGHT: 1050px; TOP: 0px; LEFT: 0px; opacity: 0.6;"></div>
		<div class="addSmtProbleContentDiv" style="width:650px; padding:20px 20px 20px 30px; height:450px; line-height:30px; position: fixed;  top: 30%; left: 30%; z-index: 99999; border: 1px #666 solid; background-color: #fff;" >

			<input type="hidden" id="businessId" name="businessId" />

			<input type="hidden" id="smtPinBanWorkFileName" name="smtPinBanWorkFileName"/>

			<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse">
				<tr>
					<td><b>填写要修改上机贴片资料的原因：</b></td>
				</tr>

				<tr>
					<td style="color: red; font-size: 13px; padding-top: 5px;">在下面填写要修改的简要原因. 必须填写</td>
				</tr>
				<tr>
					<td style="color: red; font-size: 13px;">填写完成后，还必须人工通知SMT工程. 必须跟工程人员说清要怎么改. 而SMT工程改完后要线下完成修改上机贴片资料.</td>
				</tr>
				<tr>
					<td style="color: red; font-size: 13px;">确实要改的话，还需要去确认是否要删除贴片机上的程序</td>
				</tr>
				<tr>
					<td style="color: red; font-size: 13px;">当前修改上机贴片资料，内部编号为：<span id="insideNumberStr"></span></td>
				</tr>
				<tr>
					<td style="padding-top: 5px; font-size: 14px;">【问题责任人】：</td>
				</tr>
				<tr>
					<td>
						&nbsp;&nbsp;<select name="responsibilityBy" id="responsibilityBy" style="width:200px;">
    <option value=""
    >---请选择---</option>
    <option value="客户">客户</option>
    <option value="市场">市场</option>
    <option value="工程">工程</option>
    <option value="生产">生产</option>
    <option value="公司">公司</option>


</select>


					</td>
				</tr>

				<tr>
					<td style="padding-top: 5px; font-size: 14px;">【简述修改原因】：</td>
				</tr>
				<tr>
					<td>
						&nbsp;&nbsp;<textarea name="problemReason" id="problemReason" cols="80" rows="4" class="textarea"></textarea>
					</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; font-size: 14px;">【简述如何修改】：</td>
				</tr>
				<tr>
					<td>
						&nbsp;&nbsp;<textarea name="problemReasonDescribe" id="problemReasonDescribe" cols="80" rows="4" class="textarea"></textarea>
					</td>
				</tr>
				<tr>
					<td>
						&nbsp;&nbsp;替换上机工程文件:<input type="file" name="smtPinBanWorkFile" id="smtPinBanWorkFile" title="替换上机资料工程文件" class="btn_href">
						<a href="" id="smtPinBanWorkFileUrl" type="hidden"></a>
					</td>
				</tr>
				<tr>
					<td id="saveSmtProblemTD" style="padding-top: 10px;" align="center">
						<input type="button" value="&nbsp;&nbsp;&nbsp;取&nbsp;消&nbsp;&nbsp;&nbsp;" class="btn_href" onclick="closeSmtProblemDiv();" style="margin-right: 130px;">
						<input type="button" value="&nbsp;&nbsp;&nbsp;提&nbsp;交&nbsp;&nbsp;&nbsp;" class="btn_href" onclick= "saveSmtProblem()">
					</td>
					<td id="cancelSmtProblemDiv" style="padding-top: 10px; display:none" align="center">
						<input type="button" value="&nbsp;&nbsp;&nbsp;关&nbsp;闭&nbsp;&nbsp;&nbsp;" onclick="cancelSmtProblemDiv()"/>
					</td>
				</tr>
			</table>
		</div>

	</div>
	</form>




	<!-- 取消外贸订单弹窗 -->
	<div id="cancel_overseas_smt_order_status_div" class="ask_div" style="z-index:1000;height: 280px;width: 500px; display: none;position: absolute;top:50%;margin-top: -150px;left: 50%;margin-left: -250px;">
		<form  method="post" id="cancel_overseas_smt_order_status_form">
			<div>
				<table border="0"  cellpadding="0" cellspacing="0">
					<tr>
						<td width="87%" style="color: #0075df; font-weight: bolder" id="detailsTitle">填写取消外贸订单主要原因</td>
						<td width="3%"><a href="javascript:void(0)" onclick="backCancelOverseasSmtOrderStatus()"><img id="detailsCloseBtn" src="/images/gb_but-0a395e0c53.jpg" border="0" /></a></td>
					</tr>
				</table>
			</div>
			<div class="ask_nr">
				<div>
					<textarea id="cancelOverseasSmtOrderRemark" maxlength="100" name="cancelOverseasSmtOrderRemark" style="width: 100%;height: 224px;"></textarea>
				</div>
			</div>
			<input type="hidden" id="smtId" value="">
			<div class="save_btn_div"align="center" style="padding-top: 4px">
				<input type="button" class="save_btn" style="width:100px;height: 30px; border: 1px solid #00b7ee;color:#00b7ee;background: white" method="submitSmtOrderToFactory" onclick="cancelOverseasSmtOrderStatus(this)" value="保存" id="cancelOverseasSmtOrderStatusSaveInput">
				<input type="button" class="save_btn" style="width:100px;height: 30px; border: 1px solid #00b7ee;color:#00b7ee;background: white" onclick="backCancelOverseasSmtOrderStatus()" value="返回">
			</div>
		</form>
	</div>

</body>

<div class="mask" style="top:0;right: 0;bottom: 0;left: 0;position: absolute;width: 100%;height: 100%;background-color:black;-moz-opacity:0.3;-khtml-opacity: 0.3;opacity: 0.3;filter:alpha(opacity=30);z-index: 999;display: none;"></div>
</html>'''

    html = HtmlHandler(h)
    xpath = '//a[contains(text(),"SO")]'
    print(html.getElementText(xpath))