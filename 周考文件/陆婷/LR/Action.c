Action()
{
	//登录接口
	//定义注册函数
	web_reg_save_param_json(
		"ParamName=loginResp",
		"QueryString=$..error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);

	spdy_submit_data("login",
		"Action=https://snailpet.com/v2/Passport/login",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=password", "Value={password}", ENDITEM,
		"Name=phone", "Value={phone}", ENDITEM,
		"Name=shop_id", "Value=null", ENDITEM,
		LAST);

	//lr_output_message(lr_eval_string("{loginResp}"));
	//lr_output_message(lr_eval_string("{password}"));
	//lr_output_message(lr_eval_string("{password}"));
	if (atoi(lr_eval_string("{loginResp}"))== 1){
	    	lr_output_message(" login fail");
	    }else{
	    	lr_output_message(" login success");
	    }
	
	//新增商品接口
	web_reg_save_param_json(
		"ParamName=add_resp",
		"QueryString=$..error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);

	
	
	spdy_submit_data("spdy_submit_data",
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

	//lr_output_message(lr_eval_string("{add_resp}"));
	//lr_output_message(lr_eval_string("{name}"));
	//lr_output_message(lr_eval_string("{opt}"));
	
	if (atoi(lr_eval_string("{add_resp}"))== 1){
	    	lr_output_message(" add fail");
	    }else{
	    	lr_output_message(" add success");
	    }
	
	//删除商品
	web_reg_save_param_json(
		"ParamName=del_resp",
		"QueryString=$..data",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);

	web_submit_data("del_product",
		"Action=https://snailpet.com/v2/Product/delByIds",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=shopId", "Value={shopid}", ENDITEM,
		"Name=product_ids", "Value={product_id}", ENDITEM,
		"Name=shop_id", "Value=17539", ENDITEM,
		LAST);

	//lr_output_message(lr_eval_string("{del_resp}"));
	if (atoi(lr_eval_string("{del_resp}"))== atoi(lr_eval_string("null"))){
	    	lr_output_message(" del fail");
	    }else{
	    	lr_output_message(" del success");
	    }
	
	
	//报表查找当日信息
	web_reg_save_param_json(
		"ParamName=query_resp",
		"QueryString=$..error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);

	
	
	web_custom_request("web_custom_request",
		"URL=https://snailpet.com/v2/analysis_es/action",
		"Method=post",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=aplication/json",
		"Body=[\"shop_id\": 17539,\"ex_current_page\": \"报表\",\"ex_kind\": \"点击\",\"ex_next_page\": \"{nextPage}\",\"ex_title\": \"分类_按利润\"]",
		LAST);

	//lr_output_message(lr_eval_string("{query_resp}"));
	//lr_output_message(lr_eval_string("{nextPage}"));
	//lr_output_message(lr_eval_string("{nextPage}"));
	
	if (atoi(lr_eval_string("{query_resp}"))== 1){
	    	lr_output_message(" query fail");
	    }else{
	    	lr_output_message(" query success");
	    }
	
	//入库接口
	web_reg_save_param_json(
		"ParamName=stock_resp",
		"QueryString=$..error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);

	web_submit_data("stock",
		"Action=https://snailpet.com/v2/product/update/stocks",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=exp_time", "Value=null", ENDITEM,
		"Name=inPrice", "Value=2800", ENDITEM,
		"Name=mark", "Value=", ENDITEM,
		"Name=number", "Value={num}", ENDITEM,
		"Name=productId", "Value={productID}", ENDITEM,
		"Name=production_time", "Value=null", ENDITEM,
		"Name=shelf_life", "Value=0", ENDITEM,
		"Name=shop_id", "Value=17539", ENDITEM,
		"Name=shopId", "Value=17539", ENDITEM,
		LAST);

	lr_output_message(lr_eval_string("{stock_resp}"));
	lr_output_message(lr_eval_string("{num}"));
	lr_output_message(lr_eval_string("{productID}"));
	
	
	return 0;
}
