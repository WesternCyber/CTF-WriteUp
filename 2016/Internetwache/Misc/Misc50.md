# Internetwache 2016 : Misc (50)

**Category:** misc |
**Points:** 50 |
**Name:** The hidden message |
**Solves:** 347 |
**Description:**

> My friend really can't remember passwords. So he uses some kind of obfuscation. Can you restore the plaintext?
>
> File: 
> 0000000 126 062 126 163 142 103 102 153 142 062 065 154 111 121 157 113
0000020 122 155 170 150 132 172 157 147 123 126 144 067 124 152 102 146
0000040 115 107 065 154 130 062 116 150 142 154 071 172 144 104 102 167
0000060 130 063 153 167 144 130 060 113 012
0000071


___

## Write-up

0000000 126 062 126 163 142 103 102 153 142 062 065 154 111 121 157 113

0000020 122 155 170 150 132 172 157 147 123 126 144 067 124 152 102 146

0000040 115 107 065 154 130 062 116 150 142 154 071 172 144 104 102 167

0000060 130 063 153 167 144 130 060 113 012

0000071


We noticed that the numbers go up to 7, so we assumed they were octal numbers. We converted these to hex:

56 32 56 73 62 43 42 6b 62 32 35 6c 49 51 6f 4b
52 6d 78 68 5a 7a 6f 67 53 56 64 37 54 6a 42 66
4d 47 35 6c 58 32 4e 68 62 6c 39 7a 64 44 42 77
58 33 6b 77 64 58 30 4b a

We converted this into text, giving us a base64:

V2VsbCBkb25lIQoKRmxhZzogSVd7TjBfMG5lX2Nhbl9zdDBwX3kwdX0K

Converting the base64 into text gives us:

Well done!

Flag: IW{N0_0ne_can_st0p_y0u}