Action()
{



	//1登录接口测试
	lr_think_time(5);
	web_reg_save_param_json(
		"ParamName=logindata",
		"QueryString=$.error",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);


	web_submit_data("login_request",
		"Action=https://snailpet.com/v2/Passport/login",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=phone", "Value={phone}", ENDITEM,
		"Name=password", "Value={password}", ENDITEM,
		"Name=shop_id", "Value=null", ENDITEM,
		LAST);
	

	lr_output_message(lr_eval_string("{logindata}"));
	if(atoi(lr_eval_string("{logindata}")) == 1){
		lr_output_message("login_success");
	}else{
		lr_output_message("login_fail");
	}
 
	lr_think_time(5);

	//2增加会员接口测试
	web_reg_save_param_json(
		"ParamName=addCheck",
		"QueryString=$.error",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	web_custom_request("add_customer",
		"URL=https://snailpet.com/v2/Shop/setMemberLevel",
		"Method=post",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Body={\"name\":\"haha\",\"minPrice\":\10\,\"enablePlus\":\0\,\"background\":\0\,\"discount\":\10\,\"discountForService\":\10\,\"discount_for_combination\":\10\,\"shopId\":\17530\,\"shop_id\":\17530\}",LAST);
  
  
	lr_output_message(lr_eval_string("{addCheck}"));
	if(atoi(lr_eval_string("{addCheck}")) == 1){
		lr_output_message("add_success");
	}else{
		lr_output_message("add_fail");
	}
	
	lr_think_time(5);
 
  //3消费支出记一笔测试
  	web_reg_save_param_json(
		"ParamName=shoppingCheck",
		"QueryString=$.error",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	

	web_submit_data("shopping",
		"Action=https://snailpet.com/v2/Shop/addSpending",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=actionTime", "Value=1585238400", ENDITEM,
		"Name=type", "Value=18", ENDITEM,
		"Name=mark", "Value=${mark}", ENDITEM,
		"Name=amount", "Value=${amount}", ENDITEM,
		"Name=shopId", "Value=17530", ENDITEM,
		"Name=shop_id", "Value=17530", ENDITEM,
		LAST);

  		lr_output_message(lr_eval_string("{shoppingCheck}"));
	if(atoi(lr_eval_string("{shoppingCheck}")) == 1){
		lr_output_message("shopping_success");
	}else{
		lr_output_message("shopping_fail");
	}
  		
  	lr_think_time(5);
  		
	//4商品管理 查询库存
  	web_reg_save_param_json(
		"ParamName=goodsCheck",
		"QueryString=$.error",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
  		
  	web_submit_data("queryGoods",
		"Action=https://snailpet.com/v2/Product/getList?page=1&statistics=1&keywords=11111&categoryId=0&tags=&tag_is_in=1&order_by=updated&is_order_asc=0&shopId=17530&shop_id=17530",
		"Method=GET",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		LAST); 	
  		
  	 lr_output_message(lr_eval_string("{goodsCheck}"));
	if(atoi(lr_eval_string("{goodsCheck}")) == 1){
		lr_output_message("queryGoods_success");
	}else{
		lr_output_message("queryGoods_fail");
	}

  	 //5商品管理 库存出库
  	 
  	 web_reg_save_param_json(
		"ParamName=salesCheck",
		"QueryString=$.error",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
  	 
	 web_custom_request("sales_stock",
		"URL=https://snailpet.com/v2/product/update/stocks",
		"Method=post",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Body={\"productId\":\2133552\,\"shopId\":\17530\,\"number\":\-2\,\"mark\": \"\",\"shelf_life\":\0\,\"production_time\":\null\,\"exp_time\":\null\,\"out_of_price\":\100\,\"shop_id\":\17530\}",LAST);
  	
  	lr_output_message(lr_eval_string("{salesCheck}"));
	if(atoi(lr_eval_string("{salesCheck}")) == 1){
		lr_output_message("saleGoods_success");
	}else{
		lr_output_message("saleGoods_fail");
	}
  		
	return 0;
}
