# 网易云音乐下载器 by `Python`

### 特色

- 纯手动操作
- 下载整个歌单
- 跳过无版权/VIP 歌曲
- 极速下载
- 向 mp3 添加标题,歌手,专辑,播放列表信息

### 开始使用

1. 克隆仓库

```bash
git clone https://gitee.com/TimFangDev/nmd.git
```

2. 补全依赖库

```bash
pip install requests
pip install eyed3
```

3. 运行 main.py

```
Read json / Input Link ?  (1/2)  
```
使用已存在的json / 输入歌单链接 (1/2)  

> 当输入 1  
> 直接读取当前目录下`get.json`  

> 当输入 2  
> 输入歌单链接 (如 https://music.163.com/#/my/m/music/playlist?id=2724783329 )  
> 登录网页版网易云,并访问生成的链接 (如 https://music.163.com/api/playlist/detail?id=2724783329 )  
> 复制所有内容,保存至`get.json`,编码utf-8  
> 然后敲一个换行,开始下载  

文件统一保存至 ./download  
(如果没有请手动创建)  