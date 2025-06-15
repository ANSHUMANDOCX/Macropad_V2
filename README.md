## MACROPAD

This is a 20-key macropad with 2 rotary encoders, 2 analog slide potentiometers, and a 0.91" OLED display.

---

## List of Components

- Pro Micro RP2040  
- SSD1306 0.91" OLED  
- 20 MX-style keys  
- 2 Encoders  
- 2 PTA0643 Slide Potentiometers  
- WS2812B 2020 RGB LEDs  

---

## Plan

I wanted to make a macropad with enough keys for my purpose. I started out by getting a microcontroller with enough pins and one that is able to run CircuitPython, since I wanted to use KMK as the firmware. This can be programmed for MIDI control as well.  
It also has RGB LEDs for underglow.

The OLED screen will be attached via the QWIIC connector onboard.

---

## PCB and Case

![image](https://github.com/user-attachments/assets/e42be3b8-7988-4dc3-9d23-640f70d91f03)
![image](https://github.com/user-attachments/assets/b2a50ad9-cabd-49ae-9ad5-298939459c0c)
![image](https://github.com/user-attachments/assets/d5b3bbad-2846-4d30-97e7-8c9c928f1a3e)



## BOM 
### 📦 Component Cost Table

| Item                             | Supplier         | Price (USD) |
|----------------------------------|------------------|-------------|
| Screw & bolt                     | LCSC             | 0.34        |
| Rotary Encoder (DIP-5)           | LCSC             | 3.01        |
| PTA6043 Potentiometer (10kΩ)     | LCSC             | 3.37        |
| 1N4148 Diode                     | LCSC             | 0.84        |
|WS2812B 2020 RGB led              | LCSC             | 1.67        |
|SSD1306 0.91" OLED Display       | LCSC             | 2.01        |
| SL2.1A                          | LCSC             |1.22 |
| USB A Female                    | LCSC             |0.74 |
| Shipping (LCSC)                  | LCSC              |  3.73       |
| RP2040 Pro Micro + Qwiic        | Electronics Comp | 19.43       |
| Keycaps and Keys                | Stackskb         | 15.88       |
| PCB                              | JLCPCB           | 9.00        |
| Shipping                          | JLCPCB           | 14.00       |
| **Total**                        |                  | **$75.24**   |
