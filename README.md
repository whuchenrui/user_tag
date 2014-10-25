user_tag
========

user_tag 表   # 一条记录
{   
	'_id': idfa,
	'app': xx,
	'like': [tag1, tag2, tag3]   # 保存用户使用最多的tag名称, tag1 > tag2 > tag3
	'tag': tag1==1==10==10==21&&tag2==0==0==0==0&&tag3==0==0==0==0....
}

程序思路：
1: 遍历某一天的log文件，构建一个用户使用图片的字典  dict_user_pic
 {'idfa': {'app':xx,  'v':[xx, xx, xx, xx ...], 's':[...], 'f':[...] }}
 
2:遍历dict_user_pic, 每一个idfa中的图片， 查找redis中的 pic-tag关系，获得tag列表，再一次修改该idfa下的tag键对应的值
 {tag1: [1,1,1,3], tag2: [2,2,2,6]}

3：将修改后的dict_user_tag 字典更新到mongodb中。

-----2014-10-24---
数据库增加新表status, 记录数据一些参数的记录.
{'type': 'tag', 'time': [time1, time2, time3]}

注意:
tag标签中避免使用 ==   && 这样的符号