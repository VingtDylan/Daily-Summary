[toc]

# ubuntu配置指南

从系统工具安装到常用软件安装和配置。

##  系统常用工具

从vim开始配置常用的Ubuntu相关软件。

### 更换源

​		![](/home/bree/Desktop/workspace/images/change-aliyun.png)

### 搜狗输入法

减少不必要的问题，先清楚ibus，fcitx等框架

```bash
sudo apt purge ibus*
sudo apt purge fcitx*
sudo apt autoremove
sudo apt-get install fcitx
# download deb文件
sudo dpkg -i sogoupinyin_版本号_amd64.deb
# 如果提示缺少相关依赖
sudo apt -f install
```

安装和配置部分可参考官方文档 [官方安装手册](https://pinyin.sogou.com/linux/help.php)

### 截图编辑

推荐flameshot截图工具。

```bash
sudo apt-get install flameshot
```

添加快捷键设置

![](/home/bree/Desktop/workspace/images/flameshot-configure.png)

### Git安装和配置

git的安装和全局配置

#### git安装

```bash
sudo apt-get install git
```

#### git配置

```bash
git config --global user.name "xxx"
git config --global user.email "xxx"
ssh-keygen -C 'email_address' -t rsa
enter
input your password
confirm

#upload
cd ~/.ssh
gedit id_rsa.pub
copy
# 在github ssh界面创建粘贴即可
link:https://github.com/settings/keys
# 测试
ssh -T git@github.com
```

### Vim相关

包括vim的安装，vundle安装和配置，vimrc的个人配置文档

#### vim安装

```bash
sudo apt-get install vim
```

#### vundle安装

```bash
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

插件的安装需要写在vimrc中，因此需要编写vimrc文件。

#### vimrc和插件安装

Vim 的全局配置一般在/etc/vim/vimrc或者/etc/vimrc，对所有用户生效。用户个人的配置在~/.vimrc，这里没有太大区别。

我的vimrc配置文件如下(百度网盘链接: https://pan.baidu.com/s/10eMJbke9y5Rf3AdQ13MsnA  密码: s1r2)

```
syntax on
" tab宽度和缩进设置为4
set nu
set tabstop=4
set softtabstop=4
set shiftwidth=4
set mouse=a 

set nocompatible
  
" 设置运行时路径
set rtp+=~/.vim/bundle/Vundle.vim
  
call vundle#begin()
  
" 安装的插件
Plugin 'gmarik/Vundle.vim'
Plugin 'kien/rainbow_parentheses.vim'  
Plugin 'majutsushi/tagbar'
Plugin 'vim-scripts/ctags.vim'
Plugin 'scrooloose/syntastic'
Plugin 'klen/ctrlp.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'Lokaltog/vim-powerline'
Plugin 'altercation/vim-colors-solarized'
Plugin 'davidhalter/jedi-vim'
Plugin 'klen/python-mode'
Plugin 'nathanaelkane/vim-indent-guides'

Plugin 'MarcWeber/vim-addon-mw-utils'
Plugin 'tomtom/tlib_vim'
Plugin 'garbas/vim-snipmate'
Plugin 'honza/vim-snippets'
call vundle#end()
  
" filetype off
filetype plugin indent on
let g:pydiction_location = '~/.vim/bundle/pydiction/complete-dict'
let g:pydiction_menu_height = 15

map <F3> :NERDTreeMirror<CR>
map <F3> :NERDTreeToggle<CR>

let g:snipMate = { 'snippet_version' : 1 }
```

编辑好vimrc文件之后

```bash
vim 
# 安装插件
:PluginInstall
# 部分插件可能已经无法使用，在vimrc注释掉即可
```

### Nvidia相关

#### 显卡驱动

```bash
ubuntu-drivers devices
sudo ubuntu-drivers autoinstall
sudo reboot
nvidia-smi
```

#### cuda安装

打算安装11.4.0版本,不同版本的安装方式官方均有。[CUDA Toolkit所有版本](https://developer.nvidia.com/cuda-toolkit-archive)

```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/11.4.1/local_installers/cuda-repo-ubuntu2004-11-4-local_11.4.1-470.57.02-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2004-11-4-local_11.4.1-470.57.02-1_amd64.deb
sudo apt-key add /var/cuda-repo-ubuntu2004-11-4-local/7fa2af80.pub
sudo apt-get update
sudo apt-get -y install cuda
```

已安装的版本和显卡驱动不匹配的话，需要卸载已有的cuda

```bash
sudo apt-get remove cuda
sudo apt autoremove 
sudo apt-get remove cuda*
```

设置环境变量

```bash
sudo vim ~/.bashrc
# type in
export PATH=/usr/local/cuda-11.4/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-11.4/lib64:$LD_LIBRARY_PATH
source ~/.bashrc
nvcc -V
```

#### cudnn安装

进入[官网](https://developer.nvidia.com/rdp/cudnn-download)下载需要的cudnn版本，选择`cuDNN Library for Linux`。

```bash
tar -xzvf cudnn-11.4-linux-x64-v8.2.4.15.tgz
sudo cp cuda/include/cudnn* /usr/local/cuda-11.4/include
sudo cp cuda/lib64/libcudnn* /usr/local/cuda-11.4/lib64
sudo chmod a+r /usr/local/cuda/include/cudnn*  /usr/local/cuda/lib64/libcudnn*
# confirm
cat /usr/local/cuda/include/cudnn_version.h  | grep CUDNN_MAJOR -A 2
```

### OpenCV

包含了opencv_contrib等诸多模块。

下载需要的源码文件。

首先安装cmake等必要的库

```bash
sudo apt-get install cmake
sudo apt-get install build-essential pkg-config libgtk2.0-dev libavcodec-dev libavformat-dev libjpeg-dev libswscale-dev libtiff5-dev
```

推荐安装3.4.1，头铁准备安装4.5.3,安装过程基本一致，版本不一致可能导致许多api版本无法使用，需要对应的修改源代码。

boostdesc等文件可能会在后面失败，下载后拷贝到xfeatures2d/src目录下。

链接: https://pan.baidu.com/s/14T0dDs6BRIvU18x0o_ZY7A  密码: 4ptg

```bash
mkdir build
cd build
sudo cmake -D CMAKE_BUILD_TYPE=Release \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D OPENCV_EXTRA_MODULES_PATH=./../opencv_contrib-4.5.3/modules/ \
      -D WITH_GTK=ON \
      -D OPENCV_GENERATE_PKGCONFIG=YES \
      ..
make -j8
sudo make install

sudo vim /etc/ld.so.conf.d/opencv.conf
# type in
/usr/local/lib
sudo ldconfig
# warnings
sudo ln -sf /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.2.4 /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_adv_train.so.8
sudo ln -sf /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8.2.4 /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8
sudo ln -sf /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8.2.4 /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8
sudo ln -sf /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.2.4 /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8
sudo ln -sf /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_ops_train.so.8.2.4 /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_ops_train.so.8
sudo ln -sf /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.2.4 /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8
sudo ln -sf /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn.so.8.2.4 /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn.so.8
sudo ldconfig

sudo vim /etc/bash.bashrc
# type in
PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig
export PKG_CONFIG_PATH

source /etc/bash.bashrc

pkg-config --modversion opencv4
pkg-config --cflags opencv4
pkg-config --libs opencv4

sudo mv /usr/local/include/opencv4 /usr/local/include/opencv
sudo ln -s /usr/local/include/opencv/opencv2 /usr/local/include/opencv2
sudo ln -s /usr/local/include/opencv/opencv2 /usr/local/include/opencv4
```

### Locate

```bash
sudo apt-get install mlocate
sudo updatedb
//locate eigen3
```

### Eigen

SLAM等需要的一个库

```bash
sudo apt-get install libeigen3-dev
cd /usr/local/include
sudo ln -sf ../../include/eigen3/Eigen Eigen
sudo ln -sf ../../include/eigen3/unsupported unsupported
```

### Fim

```bash
sudo apt-get install fim
```

### Tmux

```bash
sudo apt-get install -y tmux
```

个性化设置

vim ~/.tmux.conf后输入配置即可，GitHub上有很多类似的文件，也可以根据需要设置。

我的配置文件如下：

链接: https://pan.baidu.com/s/1gfWdRissQh3t1H0dQTZQeA  密码: sqjk

```bash
unbind ^b 
set -g prefix C-x 
bind C-x send-prefix  

unbind '"'  
bind v splitw -v  
unbind %  
bind h splitw -h  
bind r source-file ~/.tmux.conf \;

unbind C-[  
unbind C-]  
bind C-n new-session   

bind Tab last-window

#set status-interval 1
set-option -g status on  
set-option -g status-interval 1
set-option -g status-justify "left" 
set-option -g status-left-length 60  
set-option -g status-right-length 90  
#选择分割的窗格
#bind k selectp -U
#bind j selectp -D
#bind h selectp -L
#bind l selectp -R
#重新调整窗格的大小
#bind ^k resizep -U 10
#bind ^j resizep -D 10
#bind ^h resizep -L 10
#bind ^l resizep -R 10
#swap to panels
bind ^u swapp -U
bind ^d swapp -D

set -g status-fg colour055
set -g status-bg colour032
set -g default-terminal "screen-256color"

# 对齐方式
set-option -g status-justify left

# 左下角
# set-option -g status-left '#[bg=black,fg=green][#[fg=blue]#S#[fg=green]]'
set-option -g status-left-length 20
set-option -g allow-rename off  #do not change your window title automaticly.
set-window-option -g window-status-format '#[fg=colour226,bold]#I:#W_#{window_panes}'
## just for mac settings.
## install reattach-to-user-namespace first.
## Copy-paste integration
## Use vim keybindings in copy mode
## Setup 'v' to begin selection as in Vim
# set-option -g default-command "reattach-to-user-namespace -l zsh"
## if your are in osx env , uncomment line up.

# setw -g mode-keys vi
# bind-key -t vi-copy v begin-selection
# bind-key -t vi-copy y copy-pipe "reattach-to-user-namespace pbcopy"
# unbind -t vi-copy Enter
# bind-key -t vi-copy Enter copy-pipe "reattach-to-user-namespace pbcopy"
# bind ] run "reattach-to-user-namespace pbpaste | tmux load-buffer - && tmux paste-buffer"

if "test ! -d ~/.tmux/plugins/tpm" \
  "run 'git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm'"

set-option -g mouse on

# List of plugins
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'nhdaly/tmux-better-mouse-mode'
set -g @plugin 'NHDaly/tmux-scroll-copy-mode'
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-yank'

set -g status-interval 60  
set -g status-justify centre  

# setting for tmux-resurrect 
set -g @resurrect-strategy-vim 'session'
set -g @resurrect-strategy-nvim 'session'
set -g @scroll-down-exit-copy-mode "on"
set -g @scroll-in-moused-over-pane "on"
set -g @scroll-without-changing-pane "on"
set -g @emulate-scroll-for-no-mouse-alternate-buffer "on" 
```

然后激活配置文件

```bash
tmux source-file ~/.tmux.conf
```

### Indicator-multiload

```bash
sudo apt-get install indicator-multiboard
```

### Gnome-tweak-tool

```bash
sudo apt-get install gnome-tweak-tool
```

### Curl

```bash
sudo apt install curl
# 查看天气
curl wttr.in
curl wttr.in/shanghai
```

类似查看天气的好玩插件很多，不做赘述

### Python输出latex符号

例如在matplotlib中需要输入latex语句

```bash
pip install latex
sudo apt-get install dvipng
sudo apt-get install -y texlive texlive-latex-extra texlive-latex-recommended
sudo apt install cm-super
```

### Mp4文件播放

```bash
sudo apt-get update
sudo apt-get install libdvdnav4 libdvdread4 gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly libdvd-pkg
sudo apt-get install ubuntu-restricted-extras
```

### Progress进度

```bash
sudo apt-get install progress
progress -w
watch progress -w
```



## 第三方软件及相关配置

### Typora 安装和配置

#### typora安装

```bash
# or use
# sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE
wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -

# add Typora's repository
sudo add-apt-repository 'deb https://typora.io/linux ./'
sudo apt-get update

# install typora
sudo apt-get install typora
```

#### typora配置和主题安装

Perferences根据需要进行配置即可。

主题从[官网](https://theme.typora.io/)获取即可。

### 百度网盘

[网盘地址](https://pan.baidu.com/download)从官网下载百度网盘后，dpkg -i安装

添加自定义的别名:

```bash
sudo vim ~/.bashrc
# type in
alias pan="/opt/baidunetdisk/baidunetdisk"
source ~/.bashrc
```

以后可以用在命令行输入pan启动百度网盘。

### Anaconda安装配置

#### Anaconda安装

download 安装包 [官网](https://www.anaconda.com/products/individual-d)

```bash
bash Anaconda3-2021.05-Linux-x86_64.sh 
# 跟随指示即可，建议选择conda init
```

#### Anaconda取消自动激活

```
conda config --set auto_activate_base false
```

#### Anaconda 常用指令

创建环境

```bash
conda create -n python36 python=3.6
```

导出依赖文件

```bash
conda env export > requirements.yml
```

`conda activate (xxx)`，`conda deactivate`, `conda remove -n (xxx) --all`指令不做赘述。

### Nodejs

[官网](https://nodejs.org/en/)下载安装即可。

```bash
# 解压
# 添加软链接
sudo ln -s ~/Desktop/workspace/node-v16.11.1-linux-x64/bin/node /usr/bin/node
sudo ln -s ~/Desktop/workspace/node-v16.11.1-linux-x64/bin/npm /usr/bin/npm
# check一下
node -v
# v16.11.1
npm -v
# 8.0.0
```

### VScode

VScode安装和个人配置

### Tex

安装TeXStudio

```bash
sudo add-apt-repository ppa:sunderme/texstudio
sudo apt install texstudio
texstudio --version
```

可以测试一下[`PlotNeuralNet`](https://github.com/HarisIqbal88/PlotNeuralNet)能否运行，非常牛逼。

#### VScode 安装

[官网](https://code.visualstudio.com/)下载安装即可。

```bash
sudo dpkg -i code_1.60.0-1630494279_amd64.deb 
```

不需要添加自定义的别名，终端输入`code`即可启动VSCode

#### VSCode插件

可以安装以下插件。

```bash
adpyke.codesnap-1.3.4
christian-kohler.path-intellisense-2.4.0
clemenspeters.format-json-1.0.2
coenraads.bracket-pair-colorizer-1.0.61
dbaeumer.vscode-eslint-2.1.25
donjayamanne.githistory-0.6.18
eamodio.gitlens-11.6.0
esbenp.prettier-vscode-8.1.0
grapecity.gc-excelviewer-3.0.44
gruntfuggly.todo-tree-0.0.214
hookyqr.beautify-1.5.0
kisstkondoros.vscode-gutter-preview-0.27.1
mechatroner.rainbow-csv-1.9.1
mhutchie.git-graph-1.30.0
ms-python.python-2021.9.1230869389
ms-python.vscode-pylance-2021.9.1
ms-toolsai.jupyter-2021.8.2041215044
ms-toolsai.jupyter-keymap-1.0.0
ms-vscode.cpptools-1.6.0
oderwat.indent-rainbow-8.0.0
seanwu.vscode-qt-for-python-1.1.4
usernamehw.errorlens-3.4.0
visualstudioexptteam.vscodeintellicode-1.2.14
vscode-icons-team.vscode-icons-11.6.0
xyz.local-history-1.8.1
zhucy.project-tree-0.3.0
```

查看已经安装的插件集

```bash
code --list-extensions
```

### CLion(C++)

ubuntu16以后可以从命令行一键安装

```bash
sudo snap install clion --classic
```

[仙人指路](https://zhile.io/2020/11/18/jetbrains-eval-reset-da33a93d.html)

CLion_MJ.jar安装包 

链接: https://pan.baidu.com/s/1QCXCikzHd09uEmf-77VYcg  密码: fi4f

## 常用的指令

### 查看序列号

```
lsblk --nodeps -no serial /dev/sda
# W9AFY5ZD
```

### 查看内存使用

```bash
top
```

### 压缩,解压指令

[参考链接](https://linux265.com/news/3343.html)

#### tar

```bash
打包归档：
tar -cvf examples.tar examples   

释放解压：
tar -xvf examples.tar 
tar -xvf examples.tar  -C /path 
```

#### tar.gz tgz

```bash
打包压缩：
tar -zcvf examples.tgz examples  

释放解压：
tar -zxvf examples.tar 
tar -zxvf examples.tar  -C /path 
```

#### tar.bz

```bash
打包压缩：
tar -jcvf examples.tar.bz examples  

释放解压：
tar -jxvf examples.tar.bz 
tar -jxvf examples.tar.bz  -C /path 
```

#### tar.bz2

同上。zip等不做赘述。推荐tgz格式。

### 软链接

**命令功能** : 
Linux文件系统中，有所谓的链接(link)，我们可以将其视为档案的别名，而链接又可分为两种 :  硬链接(hard link)与软链接(symbolic  link)，硬链接的意思是一个档案可以有多个名称，而软链接的方式则是产生一个特殊的档案，该档案的内容是指向另一个档案的位置。硬链接是存在同一个文件系统中，而软链接却可以跨越不同的文件系统。

不论是硬链接或软链接都不会将原本的档案复制一份，只会占用非常少量的磁碟空间。

**软链接**：

-   1.软链接，以路径的形式存在。类似于Windows操作系统中的快捷方式
-   2.软链接可以 跨文件系统 ，硬链接不可以
-   3.软链接可以对一个不存在的文件名进行链接
-   4.软链接可以对目录进行链接

**硬链接**：

-   1.硬链接，以文件副本的形式存在。但不占用实际空间。
-   2.不允许给目录创建硬链接
-   3.硬链接只有在同一个文件系统中才能创建

```bash
ln [参数][源文件或目录][目标文件或目录]
ln -s source target
# 别问我经历了什么。。。
sudo mv /home/bree/Desktop/workspace/datasets/Driving/ /usr/local/datasets/
ln -s /usr/local/datasets/Driving /home/bree/Desktop/workspace/datasets/Driving
 
sudo mv /home/bree/Desktop/workspace/datasets/FlyingChairs_release/ /usr/local/datasets/
ln -s /usr/local/datasets/FlyingChairs_release /home/bree/Desktop/workspace/datasets/FlyingChairs_release
 
sudo mv /home/bree/Desktop/workspace/datasets/HD1k/ /usr/local/datasets/
ln -s /usr/local/datasets/HD1k /home/bree/Desktop/workspace/datasets/HD1k
 
sudo mv /home/bree/Desktop/workspace/datasets/Monkaa/ /usr/local/datasets/
ln -s /usr/local/datasets/Monkaa /home/bree/Desktop/workspace/datasets/Monkaa
 
sudo mv /home/bree/Desktop/workspace/datasets/KITTI/ /usr/local/datasets/
ln -s /usr/local/datasets/KITTI /home/bree/Desktop/workspace/datasets/KITTI
 
sudo mv /home/bree/Desktop/workspace/datasets/Sintel/ /usr/local/datasets/
ln -s /usr/local/datasets/Sintel /home/bree/Desktop/workspace/datasets/Sintel

sudo mv /home/bree/Desktop/workspace/datasets/Uname/ /usr/local/datasets/
ln -s /usr/local/datasets/Uname /home/bree/Desktop/workspace/datasets/Uname
```

### 移动文件

```bash
mv [options] source dest
mv [options] source directory
```

mv 参数设置与运行结果

|      命令格式      |                           运行结果                           |
| :----------------: | :----------------------------------------------------------: |
| **mv sfile dfile** |       将源文件名 source_file 改为目标文件名 dest_file        |
| **mv sfile  ddir** |     将文件 source_file 移动到目标目录 dest_directory 中      |
|  **mv sdir ddir**  | 目录名 dest_directory 已存在，将 source_directory 移动到目录名 dest_directory 中；目录名 dest_directory 不存在则 source_directory 改名为目录名 dest_directory |
| **mv sdir  dfile** |                             出错                             |

### cp,mv进度可视化

```bash
# 安装progress sudo apt install progress
sudo apt-get install libncurses5-dev
progress -w
```

### oh-my-zsh终端美化





### TODO

