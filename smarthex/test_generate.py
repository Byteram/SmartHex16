from smarthex import SmartHex

def main():
    s = SmartHex()
    print("Generated 50 SmartHex IDs:")
    print("-" * 50)
    for i in range(50):
        hex_id = s.generate()
        print(f"{i+1:2d}. {hex_id}")

if __name__ == "__main__":
    main()