from internal import parser, utils
import sys
import requests

def main():
    if sys.argv[1:]:
        if len(sys.argv[1:][0]) == 6 and (sys.argv[1:][0].isdigit()):
            year, month  = utils.convert_date(sys.argv[1:][0][2:], sys.argv[1:][0][:2])
            res = sys.argv[1:][1]
        else:
            print("Incorrent format data:", sys.argv[1:], "Example: 082021")
            exit(0)
    else:
        year, month = utils.get_default_date()
        res = "1920x1080"

    url = "https://www.smashingmagazine.com/%s/%s/desktop-wallpaper-calendars-%s-%s/" % (
        year, month, utils.get_month(int(month)+1), year
    )
    r = requests.get(url) #отправляем HTTP запрос
    parser.parse_url(r, res)

if __name__ == "__main__":
    main()