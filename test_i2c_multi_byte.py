#!/usr/bin/python
import smbus

bus = smbus.SMBus(1)
bus.write_i2c_block_data(0x0A, 0x01, [0x04, 0x06, 0x08, 0x0A, 0x14, 0x16, 0x18, 0x1A])
read_list = bus.read_i2c_block_data(0x0A, 0x00, 4)
for data in read_list:
	print("Read data 0x%02x" % data)



