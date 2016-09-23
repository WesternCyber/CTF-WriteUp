# CSAW CTF 2016 : Forensics (50)

**Category:** forensics |
**Points:** 50 |
**Name:** kill|
**Solves:** ? |
**Description:**

> Is kill can fix? Sign the autopsy file?

> kill.pcapng

___

## Write-up

We could not open the file with Wireshark. 
We noticed that the file was unencrypted, so we ran the string command on it:

```
$ strings kill.pcapng | grep -i flag
=flag{roses_r_blue_violets_r_r3d_mayb3_harambae_is_not_kill}
```
 