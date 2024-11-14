# Control LED with Hand Gestures using OpenCV, Mediapipe, and Arduino

This project enables controlling an LED using hand gestures by combining computer vision (OpenCV and Mediapipe) with Arduino hardware. The system detects specific gestures to control the LED, allowing it to turn on, off, or perform other actions based on recognized hand movements.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)

## Overview
- **OpenCV**: Captures video and processes frames.
- **Mediapipe**: Provides real-time hand tracking and gesture detection.
- **Arduino**: Receives commands to control an LED based on recognized gestures.

## Features
- Real-time hand tracking and gesture recognition.
- Gesture-based LED control (e.g., turning on/off).
- Extendable for additional gestures or hardware.

## Requirements

### Software
- **Python 3.7+**
- **Arduino IDE**
  
### Hardware
- **Arduino Uno** or compatible board
- **LED**
- **330Ω Resistor**
- **Jumper Wires**

## Setup Instructions
- Install Python Libraries: Use the provided requirements.txt file to install all necessary Python libraries.

 ### Arduino Setup:
 - Connect the LED and resistor to the specified digital pin on the Arduino.
Ensure the Arduino IDE is installed and serial communication is configured for a baud rate of 9600.
Upload the Arduino code for receiving commands and controlling the LED.
Configure Python Script:

- Verify the correct serial port (e.g., COM3 or /dev/ttyUSB0 based on your system) is specified in the Python script.
Ensure the camera is working and accessible for OpenCV to capture video frames.

