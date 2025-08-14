# FRISBEE

## An easy controller for connecting ANY electronic waste finds
![frisbee_generell](https://github.com/user-attachments/assets/d0e34332-de62-476f-91d0-041dcf7d6351)

The Frisbee is a microcontroller designed for prototyping, tailored to fit our  [Tinkertank](https://tinkertank.de/) workshops—where people create new inventions from electronic waste. Its goal is to allow users to easily attach and control any component found in electronic devices, making prototyping simple and accessible.

## hardware features 

- [Raspberry Pi Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/) as brain. I chose Circuitpython as language bcause you don't have to compile it into machine language like arduino. it an be interpreted live and all source codes can stay on the mass storage. so any tinkering project code remains on the mirocontroller and not only on the computer. It also makes it faster to iterate and rapidly prototype new versions. nevertheless, this clearly outweighs the slower speed of the system compared to arduino.
- [makey makey](https://makeymakey.com/) functionality as default: crocodile clamp connectors and 2 MOhms pull-down resistors. As default code, the Pi pico acts as an USB host controller and sends button inputs to your computer when circuits are being closed. So anything conductive can be a button for your custom made game controller. 
- The bee: A reverse mounted neopixel shines light through the epoxy layer. This allows the bee on the other side to glow in all possible colors without a recognizable component. Pure magic! The difficulty here was to remove the copper layers on both sides of the PCB at the location of the bee, so the light can pass through, but to keep the solder mask and silkscreen layers on the front. I figured out that the light easily passes the white solder mask but not the black silkscreen bee. It even gets nicely distributed (and a little yellowish) through the PCB epoxy. PLUS: The bee has a small solderpad layer outline that works as a touch sensor. in default mode, the bee glows up yellow if you touch it. that way you can check if the frisbee is powered and the code is running.

  ![ezgif-76ce3407d51d02](https://github.com/user-attachments/assets/f89e12fe-dbe9-41bc-be68-54b9eb192d55)
- L293D dual-h-bridge as motor driver and possibility to add additional power supply. 

## Programming & Learning

### software

I recommend [Thonny](https://thonny.org/) as it is easy to use and has a built-in shell/serial monitor and plotter. It is also able to flash and install circuitpython on the Pi pico directly.
It works great with ChatGPT; maybe someday there will be an AI agent for Thonny :)

### examples and default code

for every relevant part that can be connected, there is a code example on the mass storage. 
