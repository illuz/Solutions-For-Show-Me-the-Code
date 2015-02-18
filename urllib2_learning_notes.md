# urllib2 Learning Notes

[**HOWTO Fetch Internet Resources Using urllib2**](https://docs.python.org/2/howto/urllib2.html)

*The urllib2 module has been split across several modules in Python 3 named urllib.request and urllib.error.*


### urllib2

- `urllib2.urlopen(url[, data[, timeout[, cafile[, capath[, cadefault[, context]]]]])`
    + `url` - stirng or *Request*
    + `data` - formated string, be POST request, formated by urllib.urlencode(map)
    + `timeout` - seconds, only works for HTTP, HTTPS and FTP
    + `cafile, capath` - trusted CA certificates for HTTPS requests
    + `context` - ssl.SSLContext instance
    + returns a file-like object with
        - `geturl()` - real URL
        - `info()` - `httplib.HTTPMessage` instance, a dictionary-like object that describes the page fetched
        - `getcode()` - HTTP status code

    ```python
    import urllib2
    page = urllib2.urlopen('http://www.python.org/')
    # displays the first 100 bytes
    print page.read(100)
    ```


- `urllib2.install_opener(opener)` and `urllib2.build_opener([handler, ...])`
    + `build_opener` return an `OpenerDirector` instance, which chains the handlers in the order given.
    + Then the `OpenerDirector` can use `opener.open(url)` simply
    + Or use `install_opener` install the openner globally

    ```python
    import urllib2
    # Create an OpenerDirector with support for Basic HTTP Authentication...
    auth_handler = urllib2.HTTPBasicAuthHandler()
    auth_handler.add_password(realm='PDQ Application',
                              uri='https://mahler:8092/site-updates.py',
                              user='klem',
                              passwd='kadidd!ehopper')
    opener = urllib2.build_opener(auth_handler)
    # use opener to open url
    opener.open('http://www.example.com/login.html')
    # ...and install it globally so it can be used with urlopen.
    urllib2.install_opener(opener)
    urllib2.urlopen('http://www.example.com/login.html')
    ```


- exception
    + `urllib2.URLError` - reason
    + `urllib2.HTTPError` - code, reason

---

### Request

`class urllib2.Request(url[, data][, headers][, origin_req_host][, unverifiable])`

**argument**:

- `url` - string
- `data` - the same as the data argument of `urllib2.urlopen()`
- `headers` - dictionary, such as `{('User-agent', 'Mozilla/5.0')}`
- `origin_req_host` - the request-host of the origin transaction
- `unverifiable` - whether the request is unverifiable

**method**:

- `Request.add_data(data)`
- `Request.has_data()`
- `Request.get_data()`
- `Request.get_method()` - return 'GET' or 'POST'
- `Request.add_header(key, val)`
- `Request.add_unredirected_header(key, header)`
- `Request.had_header(header)`
- `Request.get_header(header_name, default=None)`
- `Request.header_items()` - get a list of tuples of header values
- `Request.get_full_url()`
- `Request.get_host()`
- `Request.get_selector()`
- `Request.set_proxy(host, type)`
- `Request.get_origin_req_host()`
- `Request.is_unverifiable()`

---

### BaseHandler

This is the base class for all registered handlers — and handles only the simple mechanics of registration.

**method**:

- `BaseHandler.add_parent(director)` - add a director as parent
- `BaseHandler.close()` - remove all parents
- `BaseHandler.parent` - return a `OpenerDirector`



---

### Fetching URLs with Data and Headers

```python
import urllib
import urllib2

url = 'http://www.someserver.com/cgi-bin/register.cgi'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }
headers = { 'User-Agent' : user_agent }

data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()
```

---
