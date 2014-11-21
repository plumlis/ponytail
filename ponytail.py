# Ponytail是一个抓取Konachan和yanre上图片的工具，抓取的方式取决于tag和其他的信息。


from core import connect
from catcher import kona


# profile = configparser.ConfigParser()
# if not check.check_conf('config.ini'):
#     error(404)

newwold = kona.main('/HDD/Development/Ponytail_cli/config/yanre.ini')

gotchalist = ['']
for i in newwold.urllist:
    print(i)
    raw = connect.make_connections(i)
    gotchalist.append(kona.decode(raw))

print(gotchalist)
