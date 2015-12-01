## 01/12/2015

Added `modules` and `lib`.

`modules` contains all of the bot's functionalities we're developing.

`lib` is for external dependencies and libraries, please do try to initalize everything that's not written by us here and then import whatever file wee need on main.

Ideally we want to avoid:
```
import some_library
import another_library
import and_yet_another_one
from a_tiny_library import useless_function

useless_function('hello world')

```

It's cumbersome and pollutes the code. Put whatever we need on one file and let another handle dependencies
