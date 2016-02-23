# Internetwache 2016 : Reversing (90)

**Category:** Reversing |
**Points:** 90 |
**Name:** The Cube |
**Solves:** 240 |
**Description:**

> I really like Rubik's Cubes, so I created a challenge for you. I put the flag on the white tiles and scrambled the cube. Once you solved the cube, you'll know my secret.
>

___

## Write-up

Scrambling:
F' D' U' L' U' F2 B2 D2 F' U D2 B' U' B2 R2 D2 B' R' U B2 L U R' U' L'


White side:
-------
|{|3| |
| |D|R|
| |W| |
-------

Orange side:
-------
| | | |
| | | |
| | | |
-------

Yellow side:
-------
|}| | |
|3| | |
| | | |
-------


Red side:
-------
|I| | |
| | | |
| | |C|
-------

Green side:
-------
| | | |
| | | |
| | | |
-------

Blue side:
-------
| | | |
| | | |
| | | |
-------

We basically bruteforced this one. We knew that the letters that formed the key were : 3,D,R,W,3,I,C,{,}
we could get rid of the two brackets and IW, so we're left with 3,D,R,3, and C.

we tried inputing every combination of the 5 characters into the ctf page, and it eventually worked, with:

IW{3DRC3}
