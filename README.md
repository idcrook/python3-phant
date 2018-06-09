# python3-phant

Client library for (defunct) Sparkfun Phant

 - Python3 only.
 - Tested on Raspberry Pi Model 2


## Usage


```python
from phant3 import VERSION
from phant3 import Phant
```


## Installing


### Via `pip` / PyPi

**TBD**

## Developing

Using a git clone to develop locally:

```shell
git clone https://github.com/idcrook/python3-phant.git
cd python3-phant
pip3 install --user -e .

# check that module loads
cd bin/
python3 ./test_phant3.py
```


## Documentation


```shell
pydoc3 phant3.Phant
```
