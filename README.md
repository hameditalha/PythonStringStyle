# PythonStringStyle

Styling Python string outputs using [**Colorama.py**](https://pypi.org/project/colorama/)

### CHEAT SHEET

##### via Function name

- **Style** -> DIM, NORMAL, BRIGHT, RESET_ALL.
- **Fore** -> BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
- **Back** -> BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.

##### via ASCII code
###### Style
- **ESC [ 0 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*RESET_ALL*
- **ESC [ 1 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*BIRGHT*
- **ESC [ 2 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*DIM*
- **ESC [ 22 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; *NORMAL*
###### Fore
- **ESC [ 30 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*BLACK*
- **ESC [ 31 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*RED*
- **ESC [ 32 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*GREEN*
- **ESC [ 33 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*YELLOW*
- **ESC [ 34 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*BLUE*
- **ESC [ 35 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*MAGENTA*
- **ESC [ 36 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*CYAN*
- **ESC [ 37 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*WHITE*
- **ESC [ 39 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*RESET*
###### Back
- **ESC [ 40 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*BLACK*
- **ESC [ 41 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*RED*
- **ESC [ 42 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*GREEN*
- **ESC [ 43 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*YELLOW*
- **ESC [ 44 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*BLUE*
- **ESC [ 45 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*MAGENTA*
- **ESC [ 46 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*CYAN*
- **ESC [ 47 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*WHITE*
- **ESC [ 49 m**&thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp; &thinsp;*RESET*
