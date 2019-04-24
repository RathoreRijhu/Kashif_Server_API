import logging
import collections
import time
from singleton_decorator import singleton
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
#logger = logging.getLogger(__name__)


# get list of proxies and rotate
# this should be singleton
# noinspection SpellCheckingInspection
@singleton
class ProxyRotator:
    def __init__(self, file_name=None):
        """
        Rotator default constructor

        :param file_name: name of the proxy file
        :type file_name: file (txt)
        """
        #logger.info('initiating proxy rotator')
        #logger.debug('proxy file name: {file}'.format(file=file_name))
        self.proxy_file_name = file_name
        self.proxies = []

        if self.get_proxies():
            self.proxy_queue = collections.deque(self.proxies)
        else:
            self.proxy_queue = None

    def get_proxies(self):
        """
        Read list of proxies from file
        :return:
        """
        #logger.info('reading proxy file: {file}'.format(file=self.proxy_file_name))

        if self.proxy_file_name is not None:
            try:
                proxy_file = open(self.proxy_file_name, 'r')
                proxy_list = [line.strip() for line in proxy_file.readlines()]

                for proxy in proxy_list:
                    content = proxy.split()
                    proxy = {
                        'http': 'http://{user}:{passwd}@{ip}:{port}'.format(user=content[3], passwd=content[4],
                                                                            ip=content[0], port=content[1]),
                        'https': 'socks5://{user}:{passwd}@{ip}:{port}'.format(user=content[3], passwd=content[4],
                                                                               ip=content[0], port=content[2])
                    }
                    self.proxies.append(proxy)
                proxy_file.close()
                return True
            except Exception as e:
                print e
                #logger.exception('{exception}'.format(exception=e.message))
                return False
        else:
            print("no file ")

    def get_proxy(self):
        try:
            if self.proxy_queue is not None:
                proxy = self.proxy_queue[0]
                self.proxy_queue.rotate(1)
                #logger.debug('generating proxy: {proxy}'.format(proxy=proxy))
                print(proxy)
                return proxy
            else:
                return None
        except Exception as e:
            logger.exception(e.message)
# i=1
# my_url="https://www.amazon.com/dp/B011VFNNHY/ref=twister_dp_update?_encoding=UTF8&th=1&psc=1"
# while i<5:
#     rotator = ProxyRotator('Proxies.txt')
#     print(rotator.get_proxy())
#     options=Options()
#     options.add_argument('headless')
#     options.add_argument('--no-sandbox')
#     options.add_argument('--proxy-server %s' % rotator.get_proxy())
#     options.add_argument('--user-agent= Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0')
#     browser = Chrome(chrome_options=options)
#     browser.get(my_url)
#     time.sleep(10)
#     print(browser.title)
#     browser.close()
#     i+=1
