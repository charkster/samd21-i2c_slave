# samd21-i2c_slave
![picture](https://www.okdo.com/us/wp-content/uploads/sites/8/2020/03/Seeedunio-Image.jpg)


This implements an i2c slave with a register map of 256 bytes in sram for the SAMD21, as an arduino sketch. The slave supports multi-byte writes and reads. It uses the "Wire" library.
A Raspberry Pi python script is provided to demonstrate multi-byte writes and reads.

This implementation relys on clock stretching, and has a limitation of 32 bytes for a single multibyte read.

Implementing the multibyte read using the Wire library commands is very simple, but does come at a cost in performance. 65us of clock stretching occurs when doing a read of 1-32 bytes. If the for loop is reduced from 32 to 4, the 65us of stretching is reduced to 15us. The clock stretching happens before the data is driven, which means there is no risk of data loss. If latency and throughput is critical then making the for loop smaller is the way to do that. But if you are worried about latency and throughput, moving to a samd51 is much better choice (3x the clock frequency, for an extra $8) 

UF2 file was created for Seeedino Xiao (SDA is PA8 and SCL is PA9).

I created 256 uf2 files for the Adafruit QT PY SAMD21 in the [uf2_files](https://github.com/charkster/samd21-i2c_slave/tree/main/uf2_files) directory... one for every possible slave_id. Feel free to drag-n-drop a uf2 file to make a specific I2C slave.

--> See my **new** [i2c_slave](https://github.com/charkster/i2c_slave) repo which supports Xiao RP2040, Xiao RP2350 and QT PY SAMD21 boards. It includes pre-built UF2 files for all possible Slave IDs and has options for 16bit addressing. 
