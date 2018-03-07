# swift-image-gen
generator image struct for swift 

## usage

use yml with config file

so,you need install yaml with pip

```
pip3 install PyYaml
```

> second in console:

```term
python3 SwiftImageGen.py 
```

> in swift

```swift
ImageConst.Image.SXW-40002.toUIImage()
```

### yml config
yml is config file
have three properties

```yml
targetFile: 'Assert.swift' # generate swift file path 
gen-struct-name: 'ImageConst' # struct-name
imagePath: ['../assert','/Users/cai/PycharmProjects/PythonProject/qrcode/qrcode/qrcode'] # your image path
```


### swift style
generate swift file

```swift
import UIKit

/// The 3-Clause BSD License
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



import UIKit

struct ImageConst {

        struct Assert {

            static let icon_sxw = "icon_sxw"

            static let icon_sxw_trans = "icon_sxw_trans"

        }

        struct Qrcode {

            static let SXW-40010 = "SXW-40010"

            static let SXW-40008 = "SXW-40008"

            static let SXW-40001 = "SXW-40001"

            static let SXW-40003 = "SXW-40003"

            static let SXW-40005 = "SXW-40005"

            static let SXW-40007 = "SXW-40007"

            static let SXW-40006 = "SXW-40006"

            static let SXW-40009 = "SXW-40009"

            static let SXW-40002 = "SXW-40002"

            static let SXW-40004 = "SXW-40004"

            struct Test1 {

                static let BJJY-1588 = "BJJY-1588"

            }
        }

}

extension String {
    
    func toUIImage() -> UIImage? {
        return UIImage(named: self)
    }
    
}

extension String {
    
    func toUIImage() -> UIImage? {
        return UIImage(named: self)
    }
    
}
```

## LINCENSE

BSD 3
