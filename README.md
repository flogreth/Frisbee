# FRISBEE

## a easy controller for connecting ANY electronic waste finds
![frisbee_generell](https://github.com/user-attachments/assets/d0e34332-de62-476f-91d0-041dcf7d6351)

The Frisbee is a microcontroller designed for prototyping, tailored to fit our  [Tinkertank](https://tinkertank.de/) workshops—where people create new inventions from electronic waste. Its goal is to allow users to easily attach and control any component found in electronic devices, making prototyping simple and accessible.

## hardware features 

- [Raspberry Pi Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/) as brain. I wanted 
- [makey makey](https://makeymakey.com/) functionality as default: crocodile clamp connectors and 2MOhms pulldown resistors 
- BEE: A reverse mounted neopixel shines light through the expoxy layer. This allows the bee on the other side to glow in all possible colors without a recognizable component. Pure magic! The difficulty here was to remove the copper layers on both sides of the PCB at the location of the bee so the light can pass through, but to keep the soldermask and silkscreen layers on the front. I figured out that the light easyly passes the white soldermask but not the black silkscreen bee. It even gets nicely distributed (and a little yellowish) through the pcb epoxy.

  ![ezgif-76ce3407d51d02](https://github.com/user-attachments/assets/f89e12fe-dbe9-41bc-be68-54b9eb192d55)
- L293D dual-h-bridge as motor driver and possibility to add aditional power supply

## programming & learning

### software

I recommend [Thonny](https://thonny.org/) as it is easy to use and has a built-in shell/serial monitor and plotter. It is also able to flash and install circuitpython to the pi pico directly.
It works great with ChatGPT - maybe someday there will be an ai agent for Thonny :)

### examples and default code

for every relevant part that can be connected there is a code example on the mass storage. 

### Cheatsheet

