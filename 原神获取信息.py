# coding:utf-8
import requests
import json
import ast

cookies = {
	"aliyungf_tc":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
	"acw_tc":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
	"cookie_token":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
	"ltoken":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
	"ltuid":"xxxxxxxxxxxxxxxxx",
	"login_ticket":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
	"account_id":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
	"_MHYUUID":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
	"_ga":"xxxxxxxxxxxxxxxxxxxxxxxxxx",
	"_gid":"xxxxxxxxxxxxxxxxxxxxxxxxxx",
}

headers = {
	
	"Upgrade-Insecure-Requests": "1",
	"User-Agent":"Mozilla/5.0 (Linux; Android 6.0.1; BLA-AL00 Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36 miHoYoBBS/2.21.2",
	"Accept": "application/json, text/plain, */*",
	"Ds": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
	"Origin": "https://webstatic.mihoyo.com",
	"X-Rpc-App_version": "2.21.2",
	"User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; BLA-AL00 Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36 miHoYoBBS/2.21.2",
	"X-Rpc-Client_type": "5",
	"Referer": "https://webstatic.mihoyo.com/app/community-game-records/index.html?bbs_presentation_style=fullscreen",
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "zh-CN,en-US;q=0.8",
	"X-Requested-With": "com.mihoyo.hyperion",
	"Connection": "close",
}
res = requests.get("https://api-takumi-record.mihoyo.com/game_record/app/genshin/api/dailyNote?role_id=184413539&server=cn_gf01",cookies=cookies,headers=headers).content

# 目前体力
print json.loads(res)['data']["current_resin"]
# 洞天宝钱
print json.loads(res)['data']["current_home_coin"]
# 周本强敌
print json.loads(res)['data']["remain_resin_discount_num"]








'''
GET /game_record/app/genshin/api/dailyNote?role_id=184413539&server=cn_gf01 HTTP/1.1
Host: api-takumi-record.mihoyo.com
Cookie: xxxxxxxxxxxxxxxxxxxx
Accept: application/json, text/plain, */*
Ds: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Origin: https://webstatic.mihoyo.com
X-Rpc-App_version: 2.21.2
User-Agent: Mozilla/5.0 (Linux; Android 6.0.1; BLA-AL00 Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36 miHoYoBBS/2.21.2
X-Rpc-Client_type: 5
Referer: https://webstatic.mihoyo.com/app/community-game-records/index.html?bbs_presentation_style=fullscreen
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,en-US;q=0.8
X-Requested-With: com.mihoyo.hyperion
Connection: close







HTTP/1.1 200 OK
Date: Tue, 12 Apr 2022 15:50:51 GMT
Content-Type: application/json
Content-Length: 1415
Connection: close
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Origin,X-Requested-With,Content-Type,Accept,gameName,Channel,DS
Access-Control-Allow-Methods: GET,POST,OPTIONS,DELETE
Access-Control-Allow-Origin: https://webstatic.mihoyo.com
Set-Cookie: xxxxxxxxxxxxxxxxxxxxxx
Set-Cookie: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Vary: Accept-Encoding
X-Powered-By: takumi
X-Trace-Id: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Strict-Transport-Security: xxxxxxxxxxxxxxxxxxxxxxxxxxxxx

{"retcode":0,"message":"OK","data":{"current_resin":82,"max_resin":160,"resin_recovery_time":"37360","finished_task_num":4,"total_task_num":4,"is_extra_task_reward_received":true,"remain_resin_discount_num":3,"resin_discount_num_limit":3,"current_expedition_num":5,"max_expedition_num":5,"expeditions":[{"avatar_side_icon":"https://upload-bbs.mihoyo.com/game_record/genshin/character_side_icon/UI_AvatarIcon_Side_Keqing.png","status":"Finished","remained_time":"0"},{"avatar_side_icon":"https://upload-bbs.mihoyo.com/game_record/genshin/character_side_icon/UI_AvatarIcon_Side_Fischl.png","status":"Finished","remained_time":"0"},{"avatar_side_icon":"https://upload-bbs.mihoyo.com/game_record/genshin/character_side_icon/UI_AvatarIcon_Side_Chongyun.png","status":"Finished","remained_time":"0"},{"avatar_side_icon":"https://upload-bbs.mihoyo.com/game_record/genshin/character_side_icon/UI_AvatarIcon_Side_Sara.png","status":"Finished","remained_time":"0"},{"avatar_side_icon":"https://upload-bbs.mihoyo.com/game_record/genshin/character_side_icon/UI_AvatarIcon_Side_Bennett.png","status":"Finished","remained_time":"0"}],"current_home_coin":364,"max_home_coin":2400,"home_coin_recovery_time":"283794","calendar_url":"","transformer":{"obtained":true,"recovery_time":{"Day":0,"Hour":0,"Minute":0,"Second":0,"reached":true},"wiki":"https://bbs.mihoyo.com/ys/obc/content/1562/detail?bbs_presentation_style=no_header"}}}
'''


