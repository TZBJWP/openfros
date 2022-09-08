## 源码说明
该源码基于lean的openwrt源码进行修改，修改了部分脚本、配置和内核patch，用于适配fros插件安装

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
[如何安装fros插件](https://github.com/destan19/openfros/wiki/%E5%A6%82%E4%BD%95%E5%AE%89%E8%A3%85fros%E6%8F%92%E4%BB%B6)   
[X86_64固件安装fros插件详细操作步骤](https://github.com/destan19/openfros/wiki/X86_64%E5%9B%BA%E4%BB%B6%E5%AE%89%E8%A3%85FROS%E6%8F%92%E4%BB%B6%E8%AF%A6%E7%BB%86%E6%AD%A5%E9%AA%A4)  

### 版本发布  
在release中会发布基于该源码编译的热门固件和fros插件，可以直接在固件中安装fros插件  
### 基础仓库地址
https://github.com/coolsnowwolf/lede


