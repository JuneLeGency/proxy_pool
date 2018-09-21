import requests
import time

def get_proxies():
	return requests.get("http://127.0.0.1:5010/get_all").json()
class Proxy(object):
	def __init__(self,proxy):
		self.proxy = proxy
	def test(self,url):
		try:
			self.tts = 4*1000
			self.success = False
			t1 = time.clock()
			proxies = {"http": "http://{proxy}".format(proxy=self.proxy)}
			r = requests.get(url, proxies=proxies, timeout=4, verify=False)
			if r.status_code == 200:
				self.tts = (time.clock()-t1)*1000
				self.success = True 
		except Exception as e:
			print e
			self.success = False
			pass
l = list()
for proxy in get_proxies():
	p  = Proxy(proxy)
	p.test("https://flight.qunar.com/")
	if(p.success):
		l.append(p)
l.sort(key = lambda p:p.tts)
for p in l:
	print p.proxy,p.tts