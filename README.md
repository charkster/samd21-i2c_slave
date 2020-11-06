# samd21-i2c_slave
This implements an i2c slave with a register map of 256 bytes in sram for the SAMD21, as an arduino sketch. The slave supports multi-byte writes and reads. It uses the "Wire" library.
A Raspberry Pi python script is provided to demonstrate multi-byte writes and reads.

This implementation relys on clock stretching, and has a limitation of 32 bytes for a single multibyte read.
