class _foreground:
    BLACK='\33[30m'
    RED='\33[31m'
    GREEN='\33[32m'
    YELLOW='\33[33m'
    BLUE='\33[34m'
    VIOLET='\33[35m'
    BEIGE='\33[36m'
    WHITE='\33[37m'

    GREY='\33[90m'
    RED2='\33[91m'
    GREEN2='\33[92m'
    YELLOW2='\33[93m'
    BLUE2='\33[94m'
    VIOLET2='\33[95m'
    BEIGE2='\33[96m'
    WHITE2='\33[97m' 

    RESET='\033[39m'

class _background:
    BLACK='\33[40m'
    RED='\33[41m'
    GREEN='\33[42m'
    YELLOW='\33[43m'
    BLUE='\33[44m'
    VIOLET='\33[45m'
    BEIGE='\33[46m'
    WHITE='\33[47m'

    GREY='\33[100m'
    RED2='\33[101m'
    GREEN2='\33[102m'
    YELLOW2='\33[103m'
    BLUE2='\33[104m'
    VIOLET2='\33[105m'
    BEIGE2='\33[106m'
    WHITE2='\33[107m'

    RESET='\033[49m'

class _style:
    END='\33[0m'
    BOLD='\33[1m'
    ITALIC='\33[3m'
    URL='\33[4m'
    BLINK='\33[5m'
    BLINK2='\33[6m'
    SELECTED='\33[7m'   

    RESET_ALL='\033[0m'

class Color:
    fg=_foreground
    style=_style
    bg=_background

if __name__=="__main__":
    print(Color.fg.GREEN,"\rTest :: ",__file__,Color.fg.WHITE)