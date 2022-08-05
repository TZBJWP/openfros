## 源码说明
该源码为fros固件基于openwrt系统修改的源码，不包含独立的fros ipk插件（类似于android的apk）。
### 基础仓库地址
https://github.com/coolsnowwolf/lede

### 修改内容
- 所有适配fros固件的linux内核patch
- 基于openwrt修改后的源码
- 增加编译脚本

### 如何编译  
- 编译环境搭建  
请参照lede基础仓库中的编译说明，准备好编译环境，包括ubuntu系统安装、基础软件包安装、源码下载、feeds更新等
- 选择编译产品  
通用的做法是通过make menuconfig选择产品，为了保持配置的一致性，将支持的产品配置放在了product目录，可以快速的生成产品配置。  

- 基础版本编译
进入openfros源码根目录执行以下命令  
`./build.sh -l x86_64`  
即可进行x86_64固件编译  
也可以一次编译多个产品，比如  
`./build.sh -l x86_64 redmi_ac2100 r2s r4s`  
这样会按顺序编译完所有输入的产品，当然产品名称必须在product目录存在  

- 自定义插件编译  
以上的做法只是按照默认配置编译，如果你想要自定义插件，需要通过make menuconfig选择插件后编译，build.sh只是提供了一种快捷方式。   

- 如何安装fros插件   
如果你已经通过该源码编译出了固件，可以直接安装fros插件，安装后可以使用fros固件相同功能   
1. 通过ssh进入固件后台  
2. 下载fros插件包  
3. 解压安装包，并选择自己的设备对应芯片架构的安装包，上传的固件后台/tmp目录  
4. 安装应用层插件  
推荐安装顺序（具体根据依赖关系修复报错）：  
libfros_uci  
libfros_util  
libfros_status  
libuci_config  
libuk  
rule_apply  
license  
appfilter  
fros_files  
apid  
web_cgi  

5. 安装内核插件  
应用层插件安装完成后就可以进行内核模块安装了  
内核插件一般通过opkg命令安装会失败，校验了编译hash，所以我们需要解压后手动安装  
- 找到内核模块kmod-dpi_filter ipk，如7621芯片对应的为kmod-dpi_filter_5.4.173-1_mipsel_24kc.ipk  
- 创建解压目录  
mkdir /tmp/kmod  
- 解压ipk到指定目录  
tar -zxvf kmod-dpi_filter_5.4.173-1_mipsel_24kc.ipk -C /tmp/kmod   
- 这样会出现三个压缩文件  
root@FROS:/tmp/kmod# ls   
control.tar.gz  data.tar.gz     debian-binary   
- 进入/tmp/kmod目录加压data.tar.gz  
`cd /tmp/kmod`
`tar -zxvf data.tar.gz`
- 测试ko文件是否兼容当前固件  
解压后会生成lib目录，lib目录的最底层包含ko内核模块，我们可以先检测ko模块是否兼容当前固件  
直接执行insmod加载命令  

`insmod lib/modules/$linux_version/dpi_filter.ko`  
其中linux_version为内核版本号，不同设备可能不一样，比如5.4.173  
则执行  
`insmod lib/modules/5.4.173/dpi_filter.ko`  
执行后如果系统没有报任何错误表示可以安装成功，如果系统直接重启表示固件内核参数存在冲突，可以安装默认的内核配置编译固件再试，并终止插件安装。  

- 安装内核模块  
如果测试ko文件可用，直接将内核模块安装到系统   
命令    
cp lib/modules/$linux_version/dpi_filter.ko lib/modules/$linux_version/dpi_filter.ko   

linux_version定义同上，根据实际目录名修改  

- 安装完成，重启系统生效  
如果重启后没有进入到fros界面，可以尝试清除浏览器缓存  
或者直接访问192.168.66.1/index.html，如果还是不行修改下/etc/config/uhttpd配置，将index默认界面的修改为index.html   

