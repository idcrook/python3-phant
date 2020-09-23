# python3-phant

Client library for (defunct) Sparkfun Phant

 - Python3 only (may be trivial to port to Python 2?)
 - Tested on Raspberry Pi Model 2

## Usage


```python
from phant3 import Phant
```

## Documentation

```shell
pydoc3 phant3.Phant
```


## Installing


### As Python 3 package

If you system is already setup for developing/setting up python packages (see below)

```
git clone https://github.com/idcrook/python3-phant.git
cd python3-phant
[sudo] python3 setup.py install
```

### Via `pip` / PyPi

**TBD** Intended to be called `phant3`

### Developing

Using a git clone to develop locally:

```shell
sudo apt install git build-essential python3-dev python3-pip
git clone https://github.com/idcrook/python3-phant.git
cd python3-phant
pip3 install --user -e .
```

The python module is installed as `phant3`

#### check that module loads

```shell
cd bin/
python3 ./test_phant3.py
```

#### to "uninstall" the developer copy version

```shell
pip3 uninstall phant3
```

## CREDITS

#### Client code

 - Code is almost entirely unchanged from @matze's [python-phant](https://github.com/matze/python-phant)
   - it has just been packaged to be used on my Raspberry Pi SBC running Python 3.
