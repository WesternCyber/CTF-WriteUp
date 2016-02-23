# Internetwache 2016 : The Secret Store (web70)

**Category:** web |
**Points:** 70 |
**Name:** The Secret Store |
**Solves:** 285 |
**Description:**

> We all love secrets. Without them, our lives would be dull. A student wrote a secure secret store, however he was babbling about problems with the database. Maybe I shouldn't use the 'admin' account. Hint1: Account deletion is intentional. Hint2: I can't handle long usernames.
>
> Service: https://the-secret-store.ctf.internetwache.org/

___

## Write-up

### Part One
There was a big hint given, when they said **I can't handle long usernames.**
So we just overflowed the username with 1000+ A's, and it brought us to this screen with the flag ^.^

<img src="src/web70screenie.jpg" width="250">