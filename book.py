# -*- coding: utf-8 -*-

import requests
from config import getconfig
from inline import order
config = getconfig.Config()
s = requests.session()

c = getconfig.Config()
o = order.Order(c,s,"https://inline.app/booking/-LzoDiSgrwoz1PHLtibz:inline-live-1/-LzoDjNruO8RBsVIMQ9W")
o.checkdetail()
o.sendorder()