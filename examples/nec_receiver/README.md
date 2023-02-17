<div align="center">
  <h1> NEC Receiver </h1>
  <p> Let's receive some waves 🌊 🌊  </p>
</div>  
<br/>

NEC is a infrared transmission protocol.The NEC IR uses pulse distance encoding of the message bits at frequency of 38kHz. It's designed to transmit data over short distances. It is used commonly in TV pilots. We can distinguish two major versions 8-bit and 16-bit.

NEC 8 - is a simpler version of the protocol used in consumer electronics.

NEC 16 -  is a more advanced version used in more complex applications (industrial applications).

Device is best to use with interrupts.

### Example 

Example every few seconds displays number of received commands and number of valid received commands.
If any message will be received by IR sensor program additionally displays received command.

#### Schema
<img src="https://github.com/psp515/MicroPico/blob/main/images/nec_receiver/ex_schema.png" alt="schema" height=256/>

