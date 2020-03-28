Action()
{
	//定义事务开始
	lr_start_transaction("login");

	//登录
	web_url("openpage",
		"URL=https://snailpet.com",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);

	web_reg_save_param_json(
		"ParamName=loginphone",
		"QueryString=$..error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);

//	web_submit_data("login_request",
//		"Action=https://snailpet.com/v2/Passport/login",
//		"Method=POST",
//		"TargetFrame=",
//		"Referer=",
//		ITEMDATA,
//		"Name=phone", "Value=17766086297", ENDITEM,
//		"Name=password", "Value=123456", ENDITEM,
//		"Name=shop_id", "Value=17569", ENDITEM,
//		LAST);

	web_custom_request("web_custom_request",
		"URL=https://snailpet.com/v2/Passport/login",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"phone\":\"17766086297\",\"password\":\"123456\",\"shop_id\":\"17569\"}",
		LAST);

	//lr_output_message(lr_eval_string("{loginphone}"));
	
	if(atoi(lr_eval_string("{loginphone}")) == 0){
		lr_output_message("login successful");
	}else {lr_output_message("login fail");
	}
		
	lr_end_transaction("login", LR_AUTO);
	
	
	
	lr_start_transaction("add");


	//增加会员
	web_reg_save_param_json(
		"ParamName=addcustomer",
		"QueryString=$..error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	web_custom_request("web_custom_request",
		"URL=https://snailpet.com/v2/Members/add",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"addr\": \"\",\"cardNumber\": \"\",\"mark\": \"\",\"name\": \"拉拉\",\"pets\": [{\"birthday\": \"\",\"mark\": \"\",\"name\": \"猫\",\"sex\": \"\",\"color\": \"\",\"weight_new\": 0,\"speciesId\": \"\"}],\"phone\": \"17743679634\",\"spare_phone\": \"\",\"sex\": \"\",\"is_spending_msg\": 1,\"is_open_upgrade\": 1,\"shopId\": \"17569\",\"member_tags\": \"\",\"shop_id\": 17569\}",
		LAST);

	if(atoi(lr_eval_string("{addcustomer}")) == 0){
		lr_output_message("add successful");
	}else {lr_output_message("add fail");
	}
	lr_end_transaction("add", LR_AUTO);

	return 0;
}
