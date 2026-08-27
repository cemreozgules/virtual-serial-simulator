# virtual-serial-simulator
A multi threaded Python simulation for mocking serial communication. Ideal for testing rembedded systems software without a real microcontroller.

# Virtual Serial Port Simulator

A lightweight, multi-threaded Python application designed to simulate UART / Serial communication channels in-memory. This tool allows developers to test embedded systems software, data parsers, and logging mechanisms without needing physical microcontrollers (like Arduino or ESP32) or complex virtual driver setups (such as com0com).

---

# Tech Stack & Concepts
* Language: Python 3.x
* Concurrency:`threading` (For running concurrent producer/consumer loops)
* Data Structures: `queue.Queue` (Thread-safe in-memory FIFO buffer mimicking serial byte streams)

---

# How It Works
The simulator uses a multi-threaded architecture:
1.Producer Thread (Microcontroller Simulation): Generates dummy telemetry or sensor data (e.g., temperature values) at regular intervals and pushes them into a thread-safe queue.
2.Consumer Thread (Application/User Script): Listens to the queue asynchronously, simulates `readline()` behavior, parses incoming strings, and logs timestamps.

---

#Installation & Usage

1.Clone the repository:
   ```bash
   git clone [https://github.com/cemreozgules/virtual-serial-simulator.git](https://github.com/cemreozgules/virtual-serial-simulator.git)
   cd virtual-serial-simulator
