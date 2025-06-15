# Macropad_V2
- **Title:** Macropad V2
- **Author:** Anshuman Tripathy
- **Description:** Macropad with 20 keys 2 encoders and 2 sliding potentiometers as analog input along with a Oled Display 
- **Created_at:** 2025-06-02
- Total Time Spent: 14 hr
----

# **DAY 1- 2 June: Choosing the MCU**

Started out by planning the number of I/O pins I would require. Since I will be using KMK, I need to find a board with enough GPIOs and also supports CircuitPython. After searching for a bit, I decided on using the SparkFun Pro Micro RP2040.

**Time Spent= 1.5hr**

---

# **DAY 2 - 3 June : Completed the schematic**

Started out with the Schematic i will be connecting the OLED display to the QWIIC connector on the promicro rp2040.
will be using WS2812B 2020 led for a RGB under glow. I will be making a 5x4 matrix of the keys.
There is pad under the RP2040 that connects to the onboard rgb led i will be utilsing the same pin to connect my leds.

![image](https://github.com/user-attachments/assets/1c466863-970e-4da0-a3bf-179beaf860fe)

**Time Spent = 1.5hr**

---
# **DAY 3 - 4th June : Started out with the PCB layout**

Started and complted the PCB layout and Routing. Used the Keyboard layout website to generate the layout and used the Kicad plugin to arrange the keys. 

![image](https://github.com/user-attachments/assets/f444d515-379d-4082-a875-a946fd4f3278)

**Time Spent- 2hr**

---

# **DAY 4 - 6 June: Started out with the 3d model**

Complted the PCB and added the mounting holes for the PCB and started and completed the Base plate of the case

![image](https://github.com/user-attachments/assets/788db24c-838c-47b5-bb24-2164372c27d4)

**Time Spent- 2hr**
---
# **DAY 5 - 7 June: Completed the CAD**

Started out with the front plate for the case and complted it. Also imported the PCB step file and checked all the fitting and complted the cad Modelling. Generated the cutouts for the keys from a website. Had to make many iterations for the front plate to make it a proper fit.

![image](https://github.com/user-attachments/assets/eb685503-8581-4f17-9959-5ede198b3fe6)
![image](https://github.com/user-attachments/assets/a23a0130-67c2-449a-893e-647a78857138)


**Time Spent- 3hr**

# **DAY 6 - 15 June: Made Slight asthetical changes**

added a ~5 degree tilt to the macropad, Designed Knobs( had planned to use premade one but decided not to) also added a translucent mid layer for having a better rgb look. 
Also added the feaure of a usb hub a the empty place that was above the MCU. it has 3 ports. 

![image](https://github.com/user-attachments/assets/2ce3232c-d99d-4d77-b93a-3be6ed60c192)
![image](https://github.com/user-attachments/assets/22a24f21-bd23-4ee8-878a-6efaf25336af)
![image](https://github.com/user-attachments/assets/2a5bf920-9a21-404e-a3ab-a58d5b8ddf37)


**Time spent 4hr**



