# Python Network Security Tools

Educational collection of Python-based networking and cybersecurity tools built while learning Linux networking, automation, and security fundamentals.

This repository focuses on understanding how networking tools work internally rather than relying on external utilities.

---

## Current Tools

### MAC Changer

Simple Linux MAC address changer written in Python using the `subprocess` module and Linux `ip` utilities.

#### Features

- Change MAC addresses programmatically
- Safe subprocess usage without `shell=True`
- Interface management using Linux `ip` commands
- Beginner-friendly implementation
- Interactive user input

#### Concepts Practiced

- Python subprocess module
- Linux networking commands
- Network interface management
- Command execution
- Privilege handling with `sudo`
- MAC address fundamentals
- Linux terminal workflows

---

## Example Usage

```bash
python3 mac_changer.py
