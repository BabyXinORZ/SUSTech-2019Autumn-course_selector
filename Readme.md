# 课程选择器

## 配置

| 环境         | 版本          |
| ------------ | ------------- |
| python       | 3.7.3         |
| selenium     | 3.141.0       |
| chrome       | 76.0.3809.132 |
| chromedriver | 76.0.3809.126 |

### 配置selenium
命令行输入
```shell
pip install selenium
```
### 配置chrome和chromedriver
如果你的chrome并非此版本,请在下方网址根据chrome版本下载对应版本的chromedriver
https://sites.google.com/a/chromium.org/chromedriver/downloads

## 使用

### 修改文件参数

- username
  用户名(学号)
- password
  密码
- course
  key 为课程编号, value为所希望选择的课程的选课按钮对应的`xpath`

### 使用教程

1. 修改文件参数.
   因为使用该脚本需要提前预知课程对应的`xpath`,所以需要在抢课之前进入选课网站将文件参数修改好

2. 在**提前**于选课时间13:00三到四分钟在命令行输入

   ```shell
   python course_selector.py
   ```

3. 选到想要的课程后,不要大声张扬,在github上点个**⭐**就好。
   没有选到也不用灰心丧气,因为明天也可能选不到。


## TODO

1. 还希望添加xrld模块，读取excel表格，让调整文件参数更轻松

2. 希望提供一种算法在不使用xpath的情况下保持功能。因为xpath太鸡儿不稳定了，每学期选课都要改。