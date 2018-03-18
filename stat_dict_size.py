import os

#定义统计单个文件大小的函数
def stat_file(file):
	'''
	这个函数用来统计单个文件的大小
	'''
	#通过os中的stat()方法获取相关信息，提取并返回文件大小信息
	info = os.stat(file)
	big = info.st_size   #单位为B（字节）
	#将file文件的大小单位转化为KB
	big = big/1000           #计算机中计算内存大小时使用的是1000，而不是1024
	#返回文件的大小（单位为KB）  
	return big

#测试统计文件的函数
#print(stat_file("12.jpg"))


#sum_data为目录的初始大小 
sum_data = 0
#定义统计目录的函数
def stat_dir(dir1):   	
	'''
	这个函数是实现统计dir1目录大小的作用
	'''
	#申明全局变量
	global sum_data   
	#获取目录中的文件列表
	dirlist = os.listdir(dir1) 
	#遍历目录，对目录中的文件和子目录进行大小统计
	for i in dirlist:
		#获取单个文件的目录路径
		file1 = os.path.join(dir1,i)
		#判断是文件还是目录，并进行相应的操作
		if os.path.isfile(file1):
			sum_data += stat_file(file1)    #是文件，就加
		elif os.path.isdir(file1):
			stat_dir(file1)           #是目录，递归
	#返回该目录的大小
	return sum_data/1000         #计算机中计算内存大小时使用的是1000，而不是1024


#测试统计目录的函数
data_big = stat_dir("./mydir1")
print("This directory is",data_big,"MB.")
