#!/usr/local/bin/python3

import sys
sys.path.append('http://raisack.hacca.jp/TexhEnglish/api/api_test/manage.py')　　※djangoプロジェクトをおいた場所(pwdで表示された場所）

#CGI スクリプトのトレースバック管理機構を有効
import cgitb
cgitb.enable()

from wsgiref.handlers import CGIHandler
from techenglish.wsgi import application　　※「app」はプロジェクト名

CGIHandler().run(application)