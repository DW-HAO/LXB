# fnmatch模块

## fnmatch.fnmatch(name, pat)用来匹配文件名字

### 测试name，是否符合pat

例子

```python
import fnmatch
# 测试makerbean 是否有ma*an字样
print(fnmatch.fnmatch('makerbean', 'ma*an'))
# 测试makerbean 是否有a*d字样
print(fnmatch.fnmatch('makerbean', 'a*d'))
```

结果

```python
True
False
```

### 该模块应用于匹配文件名称的匹配

例子（匹配路径 'D:\\LWHPython\\auto_work' 中带后缀 ‘.py’ 的文件，并打印出来）

```python
import fnmatch
import os
for file in os.listdir('D:\\LWHPython\\auto_work'):
    if fnmatch.fnmatch(file, '*py'):
        print(file)
    else:
        print('这个是文件夹', file)
```

结果

```python
file_work.py
os_mode.py
这个是文件夹 test
```

