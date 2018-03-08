# 生成ios Swift Image
# 思路来源于SwiftGen 项目,代码为独立编写
# 用于生成一个类,用于维护整体的项目资源
#
# The 3-Clause BSD License
# SPDX short identifier: BSD-3-Clause
#
# Note: This license has also been called the "New BSD License" or "Modified BSD License". See also the 2-clause BSD License.
#
# Copyright 2018 Caijinglong
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
#
# THIS SOFTWAR# E IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

LICENSE = """/// The 3-Clause BSD License
/// SPDX short identifier: BSD-3-Clause
/// 
/// Note: This license has also been called the "New BSD License" or "Modified BSD License". See also the 2-clause BSD License.
/// 
/// Copyright 2018 Caijinglong
/// 
/// Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
/// 
/// 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
/// 
/// 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
/// 
/// 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
/// 
/// THIS SOFTWAR# E IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

/// auto generator by python
/// author caijinglong 
/// email to me : cjl_spy@163.com
/// github : https://github.com/Caijinglong


"""

doc = """ /// # ImageAssert constant
/// use %s.%s.%s.toUIImage()
"""

import os

import yaml

targetFile = ""
imagePath = []
struct_name = ""


def loadConfig():
    f = open('SwiftGen.yml')
    config = yaml.load(f)
    print(config)
    global targetFile
    targetFile = config.get('targetFile')

    global imagePath
    imagePath = config.get('imagePath')

    global struct_name
    struct_name = config.get('gen-struct-name')
    pass


loadConfig()


def make_tab(index):
    return "    " * index


def first_upper(s: str):
    return s[0].upper() + s[1:]


# 定义一个类,用于描述文件夹
class Path:
    def __init__(self, self_path):
        self.selfPath = self_path
        self.parent = ""
        self.images = []
        self.subPathList = []

    def scan_image(self):
        if os.path.isdir(self.selfPath):
            dirs = os.listdir(self.selfPath)
            for d in dirs:
                a_path = "%s/%s" % (self.selfPath, d)
                if d.endswith(".png") or d.endswith(".jpg"):
                    self.images.append(d)
                elif os.path.isdir(a_path):
                    sub = Path(a_path)
                    sub.scan_image()
                    self.subPathList.append(sub)
        pass

    pass

    @staticmethod
    def fix_name(name: str):
        return name.replace("-", "_").replace(".", "_")

    def make_image_name(self, index):
        r = ""
        tab = make_tab(index)
        names = set()
        for img_path in self.images:
            p: str = img_path
            rindex = p.rindex(".")
            name = p[:rindex].replace("@2x", "").replace("@3x", "").replace("@1x", "")
            if not p.endswith(".png"):
                name += p[rindex:]
            names.add(name)

        for name in names:
            r += '%sstatic let %s = "%s"\n\n' % (tab, Path.fix_name(name), name)
        return r

    def make_file_string(self, index=1):
        tab = make_tab(index)
        r = "%sstruct %s {\n\n" % (tab, self.path_name())

        r += self.make_image_name(index + 1)

        for f in self.subPathList:
            p: Path = f
            r += p.make_file_string(index + 1)

        r += "%s}\n" % tab
        return r

    def path_name(self):
        p: str = self.selfPath
        try:
            rindex = p.rindex("/")
            return first_upper(p[rindex + 1:])
        except:
            return first_upper(p)
            pass


# 获取所有图片文件夹
allDirs = []

if type(imagePath) is list:
    for path in imagePath:
        allDirs.append(path)
elif type(imagePath) is str:
    allDirs.append(imagePath)

pathList = []

result = ""

result += LICENSE

result += "import UIKit\n\n"

for path in allDirs:
    obj = Path(path)
    pathList.append(obj)
    obj.scan_image()

# doc = doc % (struct_name, pathList[0].path_name(), pathList[0].images[])
# print(doc)

result += "struct %s {\n\n" % struct_name
for path in pathList:
    p: Path = path
    result += p.make_file_string(2)
    result += "\n"

result += '}'

# extension
ext = """

extension String {
    
    func toUIImage() -> UIImage? {
        return UIImage(named: self)
    }
    
}

"""

result += ext

print(result)

with open(targetFile, 'w') as t:
    t.write(result)
