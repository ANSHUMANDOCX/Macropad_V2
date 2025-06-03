# Macropad_V2
- **Title:** Macropad V2
- **Author:** Anshuman Tripathy
- **Description:** Macropad with 20 keys 2 encoders and 2 sliding potentiometers as analog input along with a Oled Display 
- **Created_at:** 2025-06-02
----

# **DAY 1- 2 June: Choosing the MCU**

Started out by planning the number of I/O pins I would require. Since I will be using KMK, I need to find a board with enough GPIOs and also supports CircuitPython. After searching for a bit, I decided on using the SparkFun Pro Micro RP2040.

Time Spent= 1.5hr

---

# **DAY 2 - 3 June : Completed the schematic**

Started out with the Schematic i will be connecting the OLED display to the QWIIC connector on the promicro rp2040.
will be using WS2812B 2020 led for a RGB under glow. I will be making a 5x4 matrix of the keys.
There is pad under the RP2040 that connects to the onboard rgb led i will be utilsing the same pin to connect my leds.

![image](https://github.com/user-attachments/assets/1c466863-970e-4da0-a3bf-179beaf860fe)

Time Spent = 1.5hr
---

