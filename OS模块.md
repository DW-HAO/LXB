# OS模块

## os.getcwd( )		获取当前目录绝对路径

例子（当前目录 D:\LWHPython\auto_work）

```python
import os
print(os.getcwd())
```

结果

```python
D:\LWHPython\auto_work
```





## os.listdir(path)		列出目录下的所有文件

### path：指定的绝对路径或相对路径，默认为当前目录

例子

```python
import os
print(os.listdir())
print(os.listdir('D:\\跑操'))
```

结果

```python
['os_mode.py']
['1', '12跑操 结束_缩混.mp3', '12跑操 跳绳 放松 结束.mp3', '12跑操 跳绳 结束.mp3', '15跑操 结束_缩混.mp3', '15跑操 跳绳 放松 结束.mp3', '15跑操 跳绳 结束.mp3']

# 注意：返回的结果是一个列表
```





## os.path.isdir(path)		判断目录是文件或者是文件夹（文件夹返回True，文件返回False）

### path：要判断的文件或者文件夹路径

例子（auto_work是一个文件夹，os_mode.py是一个文件）

```python
import os
print(os.path.isdir('D:\\LWHPython\\auto_work\\os_mode.py'))
print(os.path.isdir('D:\\LWHPython\\auto_work'))
```

结果

```python
False
True
```



例子（判断一个目录下的所有文件或文件夹）

```python
import os
for item in os.listdir('D:\\dir'):
    print(item, os.path.isdir('D:\\dir\\' + item))
```

结果

```python
PYTHON.txt False
python1.txt False
Python2.txt False
文件夹1 True
文件夹2 True
文档.docx False
记事本.txt False
```





## os.scandir(path)		目录迭代法

### 该方法直接print（）会返回一个DirEntry迭代器对象，初学者可用for循环来遍历

例子

```python
import os
for file in os.scandir('D:\\dir'):
    print(file.name, file.path, file.is_dir())
```

结果

```python
PYTHON.txt D:\dir\PYTHON.txt False
python1.txt D:\dir\python1.txt False
Python2.txt D:\dir\Python2.txt False
文件夹1 D:\dir\文件夹1 True
文件夹2 D:\dir\文件夹2 True
文档.docx D:\dir\文档.docx False
记事本.txt D:\dir\记事本.txt False
```





## os.walk(path[topdown])		遍历指定路径的所以文件以及文件夹

### path：指定的一个路径（不能为空）

### topdown：遍历顺序从外到内或者从内到外（True：从外到内  False：从内到外  默认为True）

例子

```python
'''从外到内'''
import os
for dirpath, dirnames, filenames in os.walk('./'):
    print(f'发现文件夹{dirpath}')
    print("文件夹路径:{}\n子文件夹列表:{}\n文件列表:{}\n".format(dirpath, dirnames, filenames))
    
'''从内到外'''
import os
for dirpath, dirnames, filenames in os.walk('./', topdown=False):
    print(f'发现文件夹{dirpath}')
    print("文件夹路径:{}\n子文件夹列表:{}\n文件列表:{}\n".format(dirpath, dirnames, filenames))
```

结果

```python
'''从外到内'''
发现文件夹./
文件夹路径:./
子文件夹列表:['test']
文件列表:['file_work.py', 'os_mode.py']

发现文件夹./test
文件夹路径:./test
子文件夹列表:['test1']
文件列表:[]

发现文件夹./test\test1
文件夹路径:./test\test1
子文件夹列表:[]
文件列表:['None.py']
    
'''从内到外'''
发现文件夹./test\test1
文件夹路径:./test\test1
子文件夹列表:[]
文件列表:['None.py']

发现文件夹./test
文件夹路径:./test
子文件夹列表:['test1']
文件列表:[]

发现文件夹./
文件夹路径:./
子文件夹列表:['test']
文件列表:['file_work.py', 'os_mode.py']
```





## .startswith()和.endswith()

### 判断字符串是否以指定字符或子字符串开头（结尾）

例子

```python
print('abc.txt'.startswith('abc'))
print('abc.txt'.endswith('.txt'))
print('abc.txt'.startswith('.txt'))
```

结果

```python
True
True
False
```



# 练习：

- 找出'D:\\dir'目录下所有非文件夹的文件

- 统计其中包含有“python”单词的文件数量

- 不区分大小写

- 输出文件数量

  ![](D:\dir图片.png)

```python
import os
n = 0
for files in os.scandir('D:\\dir'):
    if files.is_dir() == False:
        print(files)
        if "python" in files.name.lower():
            n +=1
print("文件夹dir中含有'python'的非文件夹有{}个".format(n))
```

结果

```python
<DirEntry 'PYTHON.txt'>
<DirEntry 'python1.txt'>
<DirEntry 'Python2.txt'>
<DirEntry '文档.docx'>
<DirEntry '记事本.txt'>
文件夹dir中含有'python'的非文件夹有3个
```
