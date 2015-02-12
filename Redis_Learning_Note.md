## Redis Learning Note

redis.io

[Documentation](http://redis.io/documentation)  
[An introduction to Redis data types and abstractions](http://redis.io/topics/data-types-intro)  
[Redis interactive tutorial](http://try.redis.io/)  


### Installation

You can download redis from redis.io or from http://download.redis.io/redis-stable.tar.gz to download stable version.  

Compile Redis follow this steps:  

```
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make
```

After the compilation the src directory inside the Redis distribution is populated with the different executables that are part of Redis:  

- **redis-server** is the Redis Server itself.
- **redis-sentinel** is the Redis Sentinel executable (monitoring and failover).
- **redis-cli** is the command line interface utility to talk with Redis.
- **redis-benchmark** is used to check Redis performances.
- **redis-check-aof** and **redis-check-dump** are useful in the rare event of corrupted data files  

Recommend steps:

    # sudo cp src/redis-server /usr/local/bin/
    # sudo cp src/redis-cli /usr/local/bin/


### Starting

Just run `src/redis-server` to start redis and `src/redis-cli` to start command line utility, if you did the recommend steps above, just run `redis-server` and `redis-cli`.  

**Start Redis with a configuration file:**  

    $ redis-server /etc/redis.conf

The first thing to do in order to check if Redis is working properly is sending a PING command using redis-cli:  

    $ redis-cli ping
    PONG

**Redis-cli** will send commands to the Redis instance running on localhost at port 6379.  


### Redis data types and operations

#### Redis keys

Redis keys are binary safe, this means that you can use any binary sequence as a key.  

- Very long keys are not a good idea. (Memory and efficiency)
- Very short keys are often not a good idea. (Readable)
- Try to stick with a schema.
- The maximum allowed key size is 512 MB.

#### Strings

Using the `SET` and the `GET` commands are the way we set and retrieve a string value. Note that `SET` will replace any existing value already stored into the key.  

The `INCR` command parses the string value as an integer, increments it by one. There are other similar commands like `INCRBY`, `DECR` and `DECRBY`.   
`INCR` is atomic!  

Other String operations:  

- `GETSET`: sets a key to a new value, returning the old value as the result.
- `MSET` and `MGET`: set or retrieve the value of multiple keys in a single command


#### Query

The `EXISTS` command returns 1 or 0 to signal if a given key exists or not in the database.  
The `DEL` command deletes a key and associated value, whatever the value is.  
The `TYPE` command returns the kind of value stored at the specified key.  

    > set mykey hello
    OK
    > exists mykey
    (integer) 1
    > type mykey
    string
    > del mykey
    (integer) 1
    > exists mykey
    (integer) 0
    > type mykey
    none


#### Expires: keys with limited time to live

When the time to live elapses, the key is automatically destroyed, exactly as if the user called the `DEL` command with the key.  

- They can be set both using seconds or milliseconds precision.
- However the expire time resolution is always 1 millisecond.
- Redis saves the date at which a key will expire.  

The `PERSIST` can be used in order to remove the expire and make the key persistent forever.  
The `TTL` check the remaining time to live for the key.  

Set and check expires in milliseconds:  `PEXPIRE` and `PTTL`.  


#### Lists

Redis lists are implemented via Linked Lists.  

- `LPUSH` : adds a new element into a list, on the left (at the head)
- `LPOP` : removes head.
- `RPUSH` : adds a new element into a list ,on the right (at the tail)
- `RPOP` : removes tail.
- `LRANGE` : extracts ranges of elements from lists  


```
> rpush mylist A
(integer) 1
> rpush mylist B
(integer) 2
> lpush mylist first
(integer) 3
> lrange mylist 0 -1
1) "first"
2) "A"
3) "B"
```

You are free to push multiple elements into a list in a single call: `rpush mylist 1 2 3 4 5 "foo bar"`  


`LTRIM`: sets this range as the new list value. All the elements outside the given range are removed.  

Example:

    > rpush mylist 1 2 3 4 5
    (integer) 5
    > ltrim mylist 0 2
    OK
    > lrange mylist 0 -1
    1) "1"
    2) "2"
    3) "3"


**Use lists as a capped collection**, only remembering the latest N items and discarding all the oldest items(by `LPUSH` and `LTRIM`):  

    LPUSH mylist <some element>
    LTRIM mylist 0 999


**Blocking operations:**  
`BRPOP` and `BLPOP` which are versions of `RPOP` and `LPOP` able to block if the list is empty: they'll return to the caller only when a new element is added to the list, or when a user-specified timeout is reached.  

Example:  

    > brpop tasks 5
    1) "tasks"
    2) "do_something"


**Build safer queues or rotating queues:** `RPOPLPUSH` removes the last element (tail) of the list stored at source, and pushes the element at the first element (head) of the list stored at destination.  



#### Hashes

- `HMSET` sets multiple fields of the hash
- `HGET` retrieves a single field
- `HMGET` returns an array of values:  

Example:  

    > hmset user:1000 username antirez birthyear 1977 verified 1
    OK
    > hget user:1000 username
    "antirez"
    > hget user:1000 birthyear
    "1977"
    > hgetall user:1000
    1) "username"
    2) "antirez"
    3) "birthyear"
    4) "1977"
    5) "verified"
    6) "1"
    > hmget user:1000 username birthyear no-such-field
    1) "antirez"
    2) "1977"
    3) (nil)

Other operations on individual fields:  
- `HDEL`
- `EXISTS`
- `HINCRBY`
- `HINCRBYFLOAT`
- `HLEN`



#### Sets

Redis Sets are unordered collections of strings.  

- `SADD` adds new elements to a set.  
- `SMEMBERS` Get all the members in a set (because set haven't method like RANGE)  
- `SISMEMBER`   
- `SPOP` Remove and return a random member from a set   
- `SRANDMEMBER` Get one or multiple random members from a set   
- `SUNION` Add multiple sets  
- `SUNIONSTORE`  
- `SINTER` Intersect multiple sets  
- `SINTERSTORE`
- `SCARD` Get the number of members in a set  



#### Sorted sets

Like sets, sorted sets are composed of unique, non-repeating string elements.  


**base**

- `ZADD`
- `ZCARD`
- `ZINCRBY`  

**count**

- `ZCOUNT`
- `ZLEXCOUNT` Count the number of members in a sorted set between a given lexicographical range  

**range**

- `ZRANGE` Return a range of members in a sorted set, by index  
- `ZREVRANGE`
- `ZRANGEBYLEX` Return a range of members in a sorted set, by lexicographical range  
- `ZREVRANGEBYLEX`
- `ZRANGEBYSCORE` Return a range of members in a sorted set, by score  
- `ZREVRANGEBYSCORE`  

**check if is member of a set**

- `ZRANK`: Determine the index of a member in a sorted set.  
- `ZREVRANK`  

**remove**

- `ZREM` Remove one or more members from a sorted set  
- `ZREMRANGEBYLEX` Remove all members in a sorted set within the given lexicographical range  
- `ZREMRANGEBYRANK`
- `ZREMRANGEBYSCORE`  


**2 ways to check if a member is in one key**

- `ZRANK`: Determine the index of a member in a sorted set.  
- `ZREVRANK`
- `ZSCORE`: Get the score associated with the given member in a sorted set  

**set operation**

- `ZINTERSTORE`
- `ZUNIONSTORE`



#### Bitmaps

Bitmaps are a set of bit-oriented operations defined on the String type.  

1. binary safe
2. maximum length is 512 MB
3. up to 232 different bits


- `SETBIT`
- `GETBIT`
- `BITCOUNT` reporting the number of bits set to 1.
- `BITPOS` Find first bit set or clear in a string  
- `BITOP`  bitwise operation between multiple keys: AND, OR, XOR and NOT  


















