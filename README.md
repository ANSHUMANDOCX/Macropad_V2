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

![PCB](https://github.com/user-attachments/assets/41598014-921c-4914-a805-9e94776da4a5)![PCB 3D](https://github.com/user-attachments/assets/eb6d715c-195a-485b-98dd-6f98de583ed2)  
![image](https://github.com/user-attachments/assets/85b6b427-408a-4585-9731-09c8eaae9825)

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
| Shipping (LCSC)                  | LCSC              |  3.73       |
| RP2040 Pro Micro + Qwiic        | Electronics Comp | 19.43       |
| Keycaps and Keys                | Stackskb         | 15.88       |
| PCB                              | JLCPCB           | 9.00        |
| Shipping                          | JLCPCB           | 14.00       |
| **Total**                        |                  | **$73.28**   |
