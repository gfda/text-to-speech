# text-to-speech
A simple text-to-speech program using:
 * Python3 GUI ( [tkinter](https://docs.python.org/3/library/tkinter.html));
 * Google Text-to-Speech Python lib( [gTTS](https://gtts.readthedocs.io/en/latest/index.html));

## Setup

### Installing
Install Google Text-to-Speech lib
```shell
$ pip install gTTS
```
### Imports
Google Text-to-Speech
```python
from gtts import gTTS
```

To use operating system funcionalities, import Python OS module
```python
import os
```

Tkinter Python GUI
```python
from tkinter import *
```

For MAC OS users, some buttons and icons does not work properly. 
Please, use ttk submodule.
```python
from tkinter import ttk
 ```

