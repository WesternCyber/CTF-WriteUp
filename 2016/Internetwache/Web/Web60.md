# Internetwache 2016 : Replace with Grace (web60)

**Category:** web |
**Points:** 60 |
**Name:** Replace with Grace |
**Solves:** 268 |
**Description:**

> Regular expressions are pretty useful. Especially when you need to search and replace complex terms.
>
> Service: https://replace-with-grace.ctf.internetwache.org/

___

## Write-up

### Part One
Entering into the page, we are met with three fields which we assumed represented the **preg_match** function in php (it's a html page hosted on a web server, so why not assume its just php).

<img src="src/web60screenie1.jpg" width="500">

Looking for exploits on php preg_match, we came across [this page](http://www.madirish.net/402).

Seems like using **/(.*)/e** as the regex, will cause php to run the second parameter literally.

