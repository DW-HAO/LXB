# glob模块

## glob.glob()

### glob是一个操作文件的相关模块，用它可以查找符合特定规则的文件路径名

例子

```python
import
print(glob.glob('*.py'))
```

结果

```python
['file_work.py', 'os_mode.py']
```

#### ”*” 匹配0个或多个字符

#### ”?” 匹配单个字符

#### ”[ ]” 匹配指定范围内的字符，如：[0-9]匹配数字



### 注意：当没有找到匹配的文件时，返回一个空列表

例子

```python
import glob
print(glob.glob('??.py'))
```

结果

```python
[]
```

### 把隐藏在指定文件夹很多层下面的文件都找出来

例子

```python
import glob
print(glob.glob('D:/LWHPython/auto_work/**/*.py', recursive=True))
```

结果

```python
D:/LWHPython/auto_work/file_work.py
['D:/LWHPython/auto_work\\file_work.py', 'D:/LWHPython/auto_work\\os_mode.py', 'D:/LWHPython/auto_work\\test\\test1\\None.py']
```

### recursive = True会不断进入文件夹内（逐层打开文件夹）

