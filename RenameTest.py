import os
import shutil

#设置输出根目录
out_path = '../final/'
txt1_path = '../final/'
txt1_name = 'path_list.txt'

txt2_path = '../final/'
txt2_name = 'src_dst_list.txt'

log_path = '../final/'
log_name = 'process_log.txt'

person_num = 0  #人数
folder_num = 0  #每个人下面的子文件夹数
init = '00000'  #文件名格式默认为5位
exist_names = {} 

f1 = open(txt1_path + txt1_name, 'w')
f2 = open(txt2_path + txt2_name, 'w')
f3 = open(log_path + log_name, 'w')

pwd = os.getcwd()
f2.write('数据集名： ' + os.path.split(pwd)[-1] + '\n')
f3.write('数据集名： ' + os.path.split(pwd)[-1] + '\n')

print('开始......')
f3.write('开始......' + '\n\n')
for file_name in os.listdir("."): #循环遍历文件夹
	
	if file_name[-2: ] == 'py':
		continue

	#取出原来的文件夹名
	temp = file_name.split("_",1)
	floder_name = temp[0]	
	
	print('正在处理: ' + file_name)
	f3.write('正在处理: ' + file_name + '\n')

	subpath = file_name +'/' 

	jpgFlag = False  #文件是否缺失标志位
	wrlFlag = False
	for subfile_name in os.listdir(subpath): 
		if subfile_name[-4: ] == '.jpg':
			jpgFlag = True
		if subfile_name[-4: ] == '.wrl':
			wrlFlag = True

	#当需要的文件都有才处理，否则跳过
	if  jpgFlag and wrlFlag :

		if not floder_name in exist_names:  #判断重复的文件夹名
			exist_names[floder_name] = 1;
			person_num += 1
		else:
			exist_names[floder_name] = exist_names.get(floder_name) + 1

		length = len(str(person_num))
		list_name = init[0 : -length] + str(person_num)  #每个人的文件夹序号
		new_name = init[0 : -length] + str(person_num) + '_0' + str(exist_names[floder_name]) #新文件夹名

		print('新文件夹名: ' +  new_name)
		f3.write('新文件夹名: ' +  new_name + '\n')

		if not os.path.exists(out_path + list_name): 
			os.mkdir(out_path + list_name)  #建立每个人的 根文件夹

		for subfile_name in os.listdir(subpath):  #文件夹下循环遍历子文件
			if os.path.isfile(subpath + subfile_name) :  #过滤掉文件夹
				if subfile_name[-4: ] == '.jpg' or subfile_name[-4: ] == '.wrl': #过滤掉其他格式的文件
					oldname= subpath + subfile_name
					newname= out_path + list_name + '/' + new_name + subfile_name[-4: ]
						
					print(oldname + '  ' + newname)
					f3.write(oldname + '  ' + newname + '\n')

					f1.write(newname[3: ] + '\n')
					f2.write(oldname + '    ' + newname[9: ] + '\n') #用四个空格分割

					shutil.copyfile(oldname,newname)
	else:
		print('***文件未达到要求***')
		print()
		f3.write('***文件未达到要求***' + '\n\n')
		continue
	
	print()
	f3.write('\n')

f1.close()
f2.close()

print('处理结束，共收集到 ' + str(person_num) + ' 个人的数据!')
f3.write('处理结束，共收集到 ' + str(person_num) + ' 个人的数据!')


	
