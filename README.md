### Python数据可视化之matplotlib实践 示例代码

![封面](cover.jpg)

#### 环境配置 Ubuntu

1. ubuntu下安装python3, matplotlib, numpy
    ```
    $ sudo apt-get install python3
    $ sudo apt-get install python3-matplotlib
    $ sudo apt-get install python3-numpy
    $ sudo apt-get install python3-scipy
    ```

2. ubuntu下中文乱码问题:
    - 下载中文字体simhei.ttf, 网址为 <http://fontzone.net/download/simhei>
    - 搜索 matplotlib 字体的安装位置
        ```
        $ locate -b '\mpl-data'
        ```
        会得到这个路径/usr/share/matplotlib/mpl-data下面有fonts/ttf这个目录, 进入这个目录, 
        把刚才下载的simhei.ttf字体复制到这个目录下, 注意权限和归属是否与其它字体一致, 另外可能需要清除一下缓存
        ```
        $ rm -rf ~/.cache/matplotlib/
        ```
    - 参考文档 <https://blog.csdn.net/jeff_liu_sky_/article/details/54023745>

3. ubuntu下matplotlib支持latex渲染: 
    ```
    $ sudo apt-get install texlive texlive-latex-extra texlive-fonts-recommended dvipng	# 可选的, 如果matplotlib中需要用到latex
    ```

#### 环境配置 Windows msys2

1. msys2下安装python3, matplotlib, numpy
    ```
    $ pacman -S mingw-w64-x86_64-python3
    $ pacman -S mingw-w64-x86_64-python3-matplotlib
    $ pacman -S mingw-w64-x86_64-python3-numpy
    $ pacman -S mingw-w64-x86_64-python3-scipy
    ```

2. windows下matplotlib支持latex渲染:
    - 下载地址：<http://mirror.ctan.org/systems/texlive/Images/>
    - 执行 `install-tl-windows.bat` 或者 `install-tl-advanced.bat` 开始安装
    - 将texlive的bin目录加到PATH环境变量
    - 参考文档 <https://blog.csdn.net/wr339988/article/details/66611166>
