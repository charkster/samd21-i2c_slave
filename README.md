# samd21-i2c_slave
![picture](https://www.okdo.com/us/wp-content/uploads/sites/8/2020/03/Seeedunio-Image.jpg)


This implements an i2c slave with a register map of 256 bytes in sram for the SAMD21, as an arduino sketch. The slave supports multi-byte writes and reads. It uses the "Wire" library.
A Raspberry Pi python script is provided to demonstrate multi-byte writes and reads.

This implementation relys on clock stretching, and has a limitation of 32 bytes for a single multibyte read.

Implementing the multibyte read using the Wire library commands is very simple, but does come at a cost in performance. 65us of clock stretching occurs when doing a read of 1-32 bytes. If the for loop is reduced from 32 to 4, the 65us of stretching is reduced to 15us. The clock stretching happens before the data is driven, which means there is no risk of data loss. If latency and throughput is critical then making the for loop smaller is the way to do that. But if you are worried about latency and throughput, moving to a samd51 is much better choice (3x the clock frequency, for an extra $8) 

UF2 file was created for Seeedino Xiao (SDA is PA8 and SCL is PA9).
