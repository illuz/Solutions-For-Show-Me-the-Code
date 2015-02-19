Python Database Notes - Redis
===

[My Redis Learning Notes](./Redis_Learning_Note.md)
[redis](redis.io)
[Python Redis Package Tutorial](https://pypi.python.org/pypi/redis/)  
[redis-py’s documentation](https://redis-py.readthedocs.org/en/latest/#)  

### install redis-py
    `sudo pip install redis-py`

or
    sudo easy_install redis

or
    sudo python setup.py install

### Get Started

```python
import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
print r.get('foo')
```


*(unfinished)*





