user_tag
========

user_tag 表   # 一条记录
{   
	'idfa': xx,
	'app':xx,
	'tag':{
		tag1:[1,10,10,21],   # view save fav total
		tag2:[ , , , ],
		tag3:[ , , , ],
		...
	}
}

程序思路：
1：遍历user_tag表，构建成一个字典,  
   dict_user_tag ：{'idfa1':{'app':xx, tag1:[ , , , ], tag2:[ , , , ], tag3:[ , , , ]...},  'idfa2':{ ... }}
   
2: 遍历某一天的log文件，构建一个用户使用图片的字典  dict_user_pic
 {'idfa': {'app':xx,  'app_v': xx, 'v':[xx, xx, xx, xx ...], 's':[...], 'f':[...] }}
 
3:遍历dict_user_pic, 每一个idfa中的图片， 查找redis中的 pic-tag关系，获得tag列表，再一次修改该idfa下的tag键对应的值

4：将修改后的dict_user_tag 字典，转换结构存入字典。
