# Internetwache 2016 : 404 Flag not found (misc80)

**Category:** misc |
**Points:** 80 |
**Name:** 404 Flag not found |
**Solves:** 294 |
**Description:**

> I tried to download the flag, but somehow received only 404 errors :(
>
> Attachment: [misc80.zip](src/misc80.zip)

___

## Write-up

### Part One
Unzipping the package given to us we get a readme with
```
You can do it!
```

and a gzipped pcap.

Throwing the pcap onto wireshark, we see lots of DNS requests and responses.

### Part Two
Took us a bit to notice this, but it seems the IPv4 and IPv6 urls requested were a chunk of base64 encoded item followed by .2015.ctf.internetwache.org

Taking all this out into a file, we get this

```
496e2074686520656e642c206974277320616c6c2061626f757420666c61
67732e0a5768657468657220796f752077696e206f72206c6f736520646f
65736e2774206d61747465722e0a7b4f66632c2077696e6e696e67206973
20636f6f6c65720a44696420796f752066696e64206f7468657220666c61
67733f0a4e6f626f62792066696e6473206f7468657220666c616773210a
53757065726d616e206973206d79206865726f2e0a5f4845524f2121215f
0a48656c70206d65206d7920667269656e642c2049276d206c6f73742069
6e206d79206f776e206d696e642e0a416c776179732c20616c776179732c
20666f72206576657220616c6f6e652e0a437279696e6720756e74696c20
49276d206479696e672e0a4b696e6773206e65766572206469652e0a536f
20646f20492e0a7d210a
```

And converting this out to ascii we get the flag in the first character of each line

```
In the end, it's all about flags.
Whether you win or lose doesn't matter.
{Ofc, winning is cooler
Did you find other flags?
Noboby finds other flags!
Superman is my hero.
_HERO!!!_
Help me my friend, I'm lost in my own mind.
Always, always, for ever alone.
Crying until I'm dying.
Kings never die.
So do I.
}!
```

Sooo the flag is: 
```
IW{DNS_HACKS}
```
^.^