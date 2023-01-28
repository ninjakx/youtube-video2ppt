# Color
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

function red {
    printf "${RED}$@${NC}\n"
}

function green {
    printf "${GREEN}$@${NC}\n"
}

function yellow {
    printf "${YELLOW}$@${NC}\n"
}

function blue {
    printf "${BLUE}$@${NC}\n"
}

# echo $(red apple) $(yellow banana)


# echo "
# |￣￣￣￣￣￣￣￣￣￣￣|
#   Welcome to vid2ppt
#    Command Utility 
# |＿＿＿＿＿＿＿＿＿＿＿| 
#                   ||
#                   ||
#            (\__/) ||
#            (•ㅅ•) ||
#            / 　 づ
# "

echo -e "\e[0;32m
             ____________________________________________________
            /                                                    \‎
           |    _____________________________________________     |
           |   |                                             |    |
           |   |  C:\> _                                     |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |      Welcome To Video to PPT Command        |    |
           |   |                  Utility                    |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |_____________________________________________|    |
           |                                                      |
            \_____________________________________________________/
                   \_______________________________________/
                _______________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- '-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.'-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.- __ . .-.-.-.'-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.'-_
 _-'.-.-.-.-.-. .---.-. .-----------------------------. .-.---. .---.-.-.-.'-_
:-----------------------------------------------------------------------------:
'---._.-----------------------------------------------------------------._.---'

\e[0m"

red "Enter url without any new line:"
read url

# echo "$url"
url="https:${url##*https:}"
# url=$(echo "$url" | egrep -o 'https?://[^ ")]+')

allFormat=$(youtube-dl -F "$url")
echo "$allFormat" 1>&2 

blue "\nEnter format to download video (choose 244 for video only) by default 244:"
read vformat

green "Enter directory to download:"
read -r dpath

green "Enter start time to skip the video in s:"
read stime

title=$(youtube-dl --get-title "$url")
# echo "$title"

mod_title=$(echo "$title" | tr ' ' '_' | tr ':' '@')

echo $vformat
echo "$dpath/$mod_title" 

l=$(youtube-dl -f "${vformat:-244}" --verbose --newline -o "$dpath/$mod_title/$title.mp4" "$url" | grep --line-buffered -oP '^\[download\].*?\K([0-9.]+\%|#\d+ of \d)' |
    zenity --progress \
    --width=400 \
  --title="Downloading youtube video" \
  --text="Downloading..." \
  --percentage=0)
echo "$l"

python save_yl_slide.py -s $stime -p "$dpath/$mod_title" 

