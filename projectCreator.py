import os, shutil, subprocess

skeletons = [
# test
[{
    "<name>":[
        "<main>",
        {"socks":[]},
        {"modules": ["<.mods>"]}
    ]
}],

# server
[{
    "<name>": [
        "<main>",
        {"socks": []},
        {"modules": ["<.mods>"]},
        {"D": []},
        {".ISABELLa": []}, # Interchange Service for Augmentation of (to-be-)Bound External Libraries and Layers
    ]
}],

]

def create_dir(structure: dict, path):
    for dir_name in structure.keys():
        print(f"creating dir {dir_name} with stubs {structure[list(structure.keys())[0]]}")
        if dir_name=="<name>":
            dir_name = input("project name?\n>> ")
        os.mkdir(path+dir_name)
        create(f"{path}/{dir_name}/", structure[list(structure.keys())[0]])
def create(path, structure=skeletons[1]):
    for node in structure:
        print(f"making {type(node)} {node}")
        if type(node)==dict:
            create_dir(node, path)
        if type(node)==list:
            create(node, path)
        if type(node)==str:
            name = node
            if name=="<.core>":
                shutil.copytree("/mnt/data/dev/apollo/.core/", path+".core/")
            if name=="<.mods>":
                print(f"cp -r /mnt/data/dev/apollo/.core/build/ {path}")
                subprocess.call("cd .core && make", shell=True)
                subprocess.call(f"cp -r /mnt/data/dev/apollo/.core/build/ {path}", shell=True)
                # shutil.copytree("/mnt/data/dev/apollo/.core/build/", path+".mods/")
            else:
                if name=="<main>":
                    name = input("project main executable name?\n>> ")
                print(f"making {path+name}")
                os.mknod(path+name)
            
create(os.getcwd()+"/")
