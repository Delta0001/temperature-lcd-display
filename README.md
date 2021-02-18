# temperature-lcd-display

Temperature Monitor I made to monitoring the temperature of broodling quail chicks.

Parts:
- Raspberry Pi Zero (non-wireless because I had a spare non W version lying around and those are practically useless for most projects)
- ds18b20 temperature sensor (left over from Uni and 1-wire is an awesome interface to work with on the pi)
- 16x2 LCD Display Module (I wish I had an i2c module to cut down on wires)
- Raspberry Pi Zero LCD Brackets (3d printed, designed by by clarionut;found [here](https://www.thingiverse.com/thing:1605814))

Setup:
- Add ``dtoverlay=w1-gpio`` to ``/boot/config/`` to enable 1-Wire kernel module
- Add ``dtoverlay=dwc2`` to ``/boot/config.txt`` and ``modules-load=dwc2,g_ether`` after ``rootwait`` in ``/boot/cmdline.txt`` to the enable OTG Ethernet module (for debugging since we don't have wifi)
- ``pip install PILCD``

1.  VSS - GND
2.  VDD - 5V
3.  V0  - GPIO11 (pin23)
4.  RS  - GPIO0  (pin27)
5.  RW  - GND
6.  E   - GPIO5  (pin29)
7.  D0  - NC
8.  D1  - NC
9.  D2  - NC
10. D3  - NC
11. D4  - GPIO6  (pin31)
12. D5  - GPIO13 (pin33)
13. D6  - GPIO19 (pin35)
14. D7  - GPIO26 (pin37)
15. A   - 5V     
16. K   - GND

## Name of the game:
Display the temperature value found in /sys/bus/w1/devices/28-XXXXXXXXXXXX/temperature (default Celcius) on the LCD display



References:
- https://rplcd.readthedocs.io/en/stable/
- https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/