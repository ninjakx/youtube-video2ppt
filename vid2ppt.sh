# Color
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
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

echo $(red "Enter url:")
read url

echo $(green "Enter directory to download:")
read -r dpath

echo $(green "Enter start time to skip the video in s:")
read stime

# echo "$url"
url="https:${url##*https:}"
# url=$(echo "$url" | egrep -o 'https?://[^ ")]+')

title=$(youtube-dl --get-title "$url")
# echo "$title"
mod_title=$(echo "$title" | tr ' ' '_' | tr ':' '@')

l=$(youtube-dl -o "$dpath/$mod_title/$title.mp4" "$url")
echo "$l"

python save_yl_slide.py -s $stime -p "$dpath/$mod_title" 


