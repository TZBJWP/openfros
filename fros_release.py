
import os
import sys
import hashlib
firmware_dict={
"openwrt-x86-64-generic":"fros-x86-64", 
"openwrt-ramips-mt7621":"fros",
"openwrt-ipq807x-generic":"fros",
"openwrt-rockchip-armv8-friendlyarm":"fros",
"openwrt-ipq40xx":"fros",
"openwrt-bcm53xx-generic":"fros",
"openwrt-bcm27xx":"fros",
"openwrt-ramips-mt7620":"fros"
}
release_path="./release"
version="2.0.7"
def rename_file(old, new):
    for a,b,c in os.walk("./"):
        for file in c:
            index=file.find(old)
            if (index == 0):
                split_str=file[len(old):]
                new_name=new+split_str
                index2=new_name.find(".")
                prefix=new_name[0:index2]
                file_type=new_name[index2:]
                new_name2=prefix+"-"+version+file_type
                print("%s---->%s"%(file,new_name2))
                fp=open(file, 'rb')
                content=fp.read()
                fp.close
                print("%s---->%s"%(file,new_name2))
                md5=hashlib.md5(content).hexdigest()
                print(md5)
                os.system("echo %s %s >>fros%s/md5sum.txt"%(new_name2, md5, version))
                os.system("cp %s fros%s/%s"%(file, version, new_name2))

if __name__=="__main__":
    if len(sys.argv) < 3:
        print("invalid param, $1: path, $2: version")
        exit(0)
    else:
        release_path=sys.argv[1]
        version=sys.argv[2]
    print("release path = %s"%(release_path))
    print("version = %s"%(version))
    os.chdir(release_path)
    os.system("mkdir fros%s"%(version))
    for k,v in firmware_dict.items():
        rename_file(k,v)

