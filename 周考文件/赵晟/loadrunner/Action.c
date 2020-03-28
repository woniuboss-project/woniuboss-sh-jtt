Action()
	
{	web_reg_save_param_json(
		"ParamName=loginresult",
		"QueryString=$..error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);

	
	
	//定义一个登录事务
	lr_start_transaction("login");
	
	// 定义一个思考时间
	lr_think_time(2);
	
	web_custom_request("login",
		"URL=https://snailpet.com/v2/Passport/login",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Body={\"password\":\"{password}\",\"phone\":\"{phone}\",\"shop_id\":\null\}",
		LAST);

	lr_convert_string_encoding(lr_eval_string("{loginresult}"),"utf-8",NULL,"loginresults");
	lr_output_message(lr_eval_string("{loginresult}"));
	
	
	//断言
	if (atoi(lr_eval_string("{loginresult}")) == 0) {

		lr_end_transaction("login", LR_PASS);

	} else {

		lr_end_transaction("login", LR_FAIL);

	}
	
	
	
	
	//新增会员
	web_reg_save_param_json(
		"ParamName=addcustomerresult",
		"QueryString=$..error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	lr_start_transaction("add customer");
	
	//新增会员接口请求
	web_custom_request("add_customer_request",
		"URL=https://snailpet.com/v2/Members/add",
		"Method=post",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"addr\": "",\"cardNumber\": "",\"mark\": "",\"name\": \"mmmm\",\"pets\": [{\"birthday\": "",\"mark\": "",\"name\": \"小狗\",\"sex\": "",\"color\": "",\"weight_new\": 0,\"speciesId\": ""}],\"phone\": \"13099983221\",\"spare_phone\": "",\"sex\": "",\"is_spending_msg\": 1,\"is_open_upgrade\": 1,\"shopId\": \"17555\",\"member_tags\": "",\"shop_id\": 17555}",
		LAST);
	
	
	lr_output_message(lr_eval_string("{addcustomerresult}"));
	//断言
	if (atoi(lr_eval_string("{addcustomerresult}")) == 0) {

		lr_end_transaction("add customer", LR_PASS);

	} else {

		lr_end_transaction("add customer", LR_FAIL);

	}
	
	//查询会员
	web_reg_save_param_json(
		"ParamName=querycustomerresult",
		"QueryString=$..error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	lr_start_transaction("querycustomer");
	
	
	web_custom_request("querycustomer",
		"URL=https://snailpet.com/v2/Members/get_list/new_simple?page=1&keywords=%E7%BA%AA%E6%9C%88%E6%B5%A9&birthday=&petSpecies=&petAge=&balance=&lastConsumption=&sex=&prescription_status=&member_card_status=&card_id=&shopping_card_id=0&tags=&loss_time=&sterilization_status=&orderBy=updated&is_order_asc=0&is_mini_login=0&shopId=17539&shop_id=17539",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Body=",
		LAST);

	lr_output_message(lr_eval_string("{querycustomerresult}"));
	//断言
	if (atoi(lr_eval_string("{querycustomerresult}")) == 0) {

		lr_end_transaction("querycustomer", LR_PASS);

	} else {

		lr_end_transaction("querycustomer", LR_FAIL);

	}
	
	
	//新增货物
	web_reg_save_param_json(
		"ParamName=addgoodsresult",
		"QueryString=$..error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	lr_start_transaction("addgoods");
	
	spdy_submit_data("addgoods",
		"Action=https://snailpet.com/v2/Product/add",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=shopId", "Value=17539", ENDITEM,
		"Name=productId", "Value=0", ENDITEM,
		"Name=isServer", "Value=0", ENDITEM,
		"Name=name", "Value={name}", ENDITEM,
		"Name=categoryId", "Value=840279", ENDITEM,
		"Name=inPrice", "Value={inprice}", ENDITEM,
		"Name=outPrice", "Value={opt}", ENDITEM,
		"Name=percentage", "Value=0", ENDITEM,
		"Name=notice_stocks", "Value=1", ENDITEM,
		"Name=weight", "Value=0", ENDITEM,
		"Name=logo_images", "Value=", ENDITEM,
		"Name=detail_images", "Value=", ENDITEM,
		"Name=production_time", "Value=", ENDITEM,
		"Name=brand_name", "Value=", ENDITEM,
		"Name=version", "Value=1", ENDITEM,
		"Name=shop_id", "Value=17539", ENDITEM,
		LAST);

	
	lr_output_message(lr_eval_string("{addgoodsresult}"));
	//断言
	if (atoi(lr_eval_string("{addgoodsresult}")) == 0) {

		lr_end_transaction("addgoods", LR_PASS);

	} else {

		lr_end_transaction("addgoods", LR_FAIL);

	}
	
		//查询货物
	web_reg_save_param_json(
		"ParamName=querygoodsresult",
		"QueryString=$..error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
		
		
	lr_start_transaction("querygoods");
	
	lr_think_time(2);
	
	web_custom_request("querygoods",
		"URL=https://snailpet.com/v2/Product/getList?page=1&statistics=1&keywords=%E7%8B%97%E7%B2%AE&categoryId=0&tags=&tag_is_in=1&order_by=updated&is_order_asc=0&shopId=17539&shop_id=17539",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Body=",
		LAST);

	lr_output_message(lr_eval_string("{querygoodsresult}"));
	//断言
	if (atoi(lr_eval_string("{querygoodsresult}")) == 0) {

		lr_end_transaction("querygoods", LR_PASS);

	} else {

		lr_end_transaction("querygoods", LR_FAIL);

	}
	
	return 0;
}
