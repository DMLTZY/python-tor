### python + tor

Some website will ban source ip that has abnormal traffic, so we need change source ip.

#### My environments

* OS X EI Capitan 10.11.6
* [tor 0.3.0.9](https://www.torproject.org/projects/torbrowser.html.en)
* python 3.5.2
* pysocks 1.6.7
* [stem 1.5.4](https://stem.torproject.org/)

**tips**: `brew install tor`, `pip install pysocks`, `pip install stem`

#### Modify config file

add below to config file(/usr/local/etc/tor/torrc)

```bash
Socks5Proxy 127.0.0.1:1080 # maybe you don't need this in your country.
ControlPort 9051 #default
SocksPort 9050 #default
# use tor --hash-password "123456" to generate the hashcode
HashedControlPassword 16: xxx-your's hashcode-xxx
```

**notice**: change password whatever you like and paste the hashcode after the last colon.

#### Run

```bash
$ python tor.py
```

that's it, use it, but don't abuse it.

#### References & Thanks

1. [http://www.learn4master.com/programming-language/python/install-and-use-tor-on-ubuntu-for-python-requests](http://www.learn4master.com/programming-language/python/install-and-use-tor-on-ubuntu-for-python-requests)
2. [https://deshmukhsuraj.wordpress.com/2015/03/08/anonymous-web-scraping-using-python-and-tor/](https://deshmukhsuraj.wordpress.com/2015/03/08/anonymous-web-scraping-using-python-and-tor/)
3. [https://gist.github.com/jefftriplett/9748036](https://gist.github.com/jefftriplett/9748036)
4. [https://stackoverflow.com/questions/30286293/make-requests-using-python-over-tor](https://stackoverflow.com/questions/30286293/make-requests-using-python-over-tor)
5. [https://stackoverflow.com/questions/28252649/stem-cant-get-new-ip-with-python-via-tor](https://stackoverflow.com/questions/28252649/stem-cant-get-new-ip-with-python-via-tor)