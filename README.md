# Text-to-speech

A simple text-to-speech program using:

* Python3 GUI ([tkinter](https://docs.python.org/3/library/tkinter.html));
* Google Text-to-Speech Python lib([gTTS](https://gtts.readthedocs.io/en/latest/index.html));

## Setup

### Installing

Install Google Text-to-Speech lib

```console
user@linux:~$ pip install gTTS
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

To show errors, attention and other alert messages

```python
from tkinter import messagebox
```

For Mac OS users, some buttons and icons does not work properly.
Please, use ttk submodule.

```python
from tkinter import ttk
 ```

## Let's Speak

Before running the program, you need to choose the correct player based on your operating system.  

(**_afplay_ is a Mac OS command.**)

### Choosing the player

* For Arch Linux based (Manjaro...)

```console
user@linux:~$ sudo pacman -S mpg123
```

* For Debian Linux based (Ubuntu...)

```console
user@linux:~$ sudo apt-get update
user@linux:~$ sudo apt-get install mpg123
```

* For Redhat Linux based (Fedora, SUSE...)

```console
user@linux:~$ yum install mpg123
```

* For Windows
[mpg123 for Windows](https://mpg123.org/download.shtml)

After successful installation, you can test it.

```console
user@linux:~$ mpg123 <some_audio_file>.mp3
```

### NOTE

It's necessary to change _afplay_ to correct mp3 player at /source/TextToSpeech.py

```Python
#The argument & indicates afplay to run in the background as a job.
os.system("afplay sound/output.mp3 &")
```

License

----

[MIT](https://choosealicense.com/licenses/mit/)
