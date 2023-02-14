
<div align="center">
  
  <h1> Micro Pico </h1>
  <p> Simple start with pico! </p>
  
  <div>
    <a href="">
      <img src="https://img.shields.io/github/last-commit/psp515/MicroPico" alt="last update" />
    </a>
    <a href="https://github.com/psp515/MicroPico/network/members">
      <img src="https://img.shields.io/github/forks/psp515/MicroPico" alt="forks" />
    </a>
    <a href="https://github.com/psp515/MicroPico/stargazers">
      <img src="https://img.shields.io/github/stars/psp515/MicroPico" alt="stars" />
    </a>
    <a href="https://github.com/psp515/MicroPico/issues/">
      <img src="https://img.shields.io/github/issues/psp515/MicroPico" alt="open issues" />
    </a>
    <a href="https://github.com/psp515/MicroPico/blob/master/LICENSE">
      <img src="https://img.shields.io/github/license/psp515/MicroPico" alt="license" />
    </a>
  </div>
</div>  

<br/>

### About The Project

Project is created in order to get acquainted with microcontrollers programming and some basics IOT.
<br/>
This repository will contain code with usage exaples (with example connections) for different elements (lcd, keyboards, etc.).
Most examples will be created with micropython, yet examples with c/c++ might occur.
<br/>
Also each example contains short element and example description.

Also in futre I am planning to create few project based on knowledge gained here. (Links will be added when they appear)

<b>Used boards:</b>
<div>
  <a href="">
    <img src="https://img.shields.io/badge/Raspberry Pi Pico-Code?&logo=raspberrypi&logoColor=black&color=F1C232" />
  </a>
  <br>
  <a href="">     
    <img src="https://img.shields.io/badge/Raspberry Pi Pico W-Code?&logo=raspberrypi&logoColor=black&color=F1C232" />
  </a>
</div>

### Built With

<div>
  <a>
    <img src="https://img.shields.io/badge/-Micropyhon-FFFFFF?logo=micropyhon" />
  </a>
  <a>
    <img src="https://img.shields.io/badge/-Python-FFFFFF?logo=python" />
  </a>
  <a>
    <img src="https://img.shields.io/badge/-Fritzing-FFFFFF?logo=fritzing" />
  </a>
</div>

### Getting Started

To use this project simply downolad the [ThonnyIDE](https://thonny.org/) and this repository.
<br/>
Ofcourse you need to have any Raspberry Pi Pico board (with micropython) and element you want to check.
(In order to use it on Raspbery Pi some functions may need some slight fixes)

With thonny IDE open Micropico projcet and upload src folder and micropico.py to your raspberry pi pico and you are ready to run some examples.

### Usage 

You may want to use this repository in order to see how easy is to create programs with micropython or to see how elements might work and how to connect them properly.

### Roadmap

Elements with examples.

#### Pooling

Polling periodicall checks if device needs attention. This can be done in a sequential manner or in a priority-based manner (if some devices are more important).

Element  | Lib Code | Example | Schema | Tested
:-: | :-: | :-: | :-: | :-:
Led | ✅  | ✅  | ✅ | ✅
RGB Led | ✅  | ✅ | ✅ | ✅
Keypad | ✅ | ✅ | ✅ |✅
PIR / IR Break Sensor | ✅  | ✅ | ✅ | ✅
Button | ✅  | ✅ | ✅ | ✅
Potentiometer | ✅  | ✅ | ✅ | ✅
Photoresistor  | ✅  | ✅ | ✅ | ✅
Ultrasonic | ✅  | ✅ | ✅ | ✅
DHT11 | ✅ | ✅ | ✅ | ✅
Rotary Encoder | ✅ | ✅ | 🔜 | ✅
I2C LCD | ❌  | ❌ | ❌ | ❌

(Lib Code - means libary code for input/output device,
Example - means meas small showcase of working functions,
Schema - means screen with connection example to board ,
Tested - means example working as expected)

#### Interrupts

Interrupts allert CPU when a device needs attention, causing the CPU to pause its current task, handle the interrupt request, and then resume the original task.

Element  | Lib Code | Example | Schema | Tested
:-: | :-: | :-: | :-: | :-:
Button | 🚧  | 🚧 | 🚧 | 🚧
PIR / IR Break Sensor | 🚧  | 🚧 | 🚧 | 🚧
Rotary Encoder | 🚧  | 🚧 | 🚧 | 🚧
NEC IR | 🚧  | 🚧 | 🚧 | 🚧

See the [open issues](https://github.com/psp515/MicroPico/issues) for a full list of tasks (and known issues).

### License

Distributed under the MIT License. See `LICENSE.txt` for more information.

### Contact

<div align="center">
  <a href="https://www.linkedin.com/in/lukasz-psp515-kolber/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://twitter.com/psp515">
    <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter" />
  </a>
</div>

