# BCTF 2016 : catvideo (150)

**Category:** forensics |
**Points:** 150 |
**Name:** catvideo |
**Solves:** 135 |
**Description:**

> cat_video.mp4 Google Drive
> 
> cat_video.mp4 pan.baidu.com
> 
> cat_video.mp4 Dropbox
> 
> cat_video.mp4 MEGA

___

## Write-up

### Part One
Opening the mp4 we get this splash of colors, and squinting real hard you can make out the outlines of a cat.

On the first 100 or so frames, you can see there's text under the cat, so we just assumed the flag is there. Throwing on the motion detection of VLC, you can sort of make out the flag which is:

![](Screenie.png)

```
BCTF{cute&fat_cats_does_not_like_drinking}
```