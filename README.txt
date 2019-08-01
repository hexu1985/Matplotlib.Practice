1) msys2下安装python3, matplotlib, numpy
$ pacman -S mingw-w64-x86_64-python3
$ pacman -S mingw-w64-x86_64-python3-matplotlib
$ pacman -S mingw-w64-x86_64-python3-numpy

2) ubuntu下安装python3, matplotlib, numpy
$ sudo apt-get install python3
$ sudo apt-get install python3-matplotlib
$ sudo apt-get install python3-numpy

3) ubuntu下中文乱码问题:
a.下载中文字体simhei.ttf, 网址为http://fontzone.net/download/simhei 
b.搜索 matplotlib 字体的安装位置
$ locate -b '\mpl-data'
# 会得到这个路径/usr/share/matplotlib/mpl-data下面有fonts/ttf这个目录, 进入这个目录i, 把刚才下载的simhei.ttf 
# 字体复制到这个目录下, 注意权限和归属是否与其它字体一致

4) ubuntu下matplotlib支持latex渲染: 
$ sudo apt-get install texlive texlive-latex-extra texlive-fonts-recommended dvipng	# 可选的, 如果matplotlib中需要用到latex

