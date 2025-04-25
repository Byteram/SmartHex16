#!/usr/bin/env python3
from smarthex import SmartHex

def main():
    """Command-line interface for generating SmartHex identifiers."""
    smart_hex = SmartHex()
    print(smart_hex.generate())

if __name__ == "__main__":
    main() 