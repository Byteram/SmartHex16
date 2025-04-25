import secrets

class SmartHex16:
    def generate(self):
        # Generate 14 hex digits (56 bits)
        raw_bytes = secrets.token_bytes(7)
        base_hex = raw_bytes.hex().upper()

        # Calculate checksum on base
        check = self._check_digits(base_hex)
        return base_hex + check

    def validate(self, id_hex):
        if len(id_hex) != 16:
            return False
        base, check = id_hex[:14], id_hex[14:]
        return self._check_digits(base) == check.upper()

    def _check_digits(self, base_hex):
        # Simple custom checksum: XOR all digits and mod
        total = 0
        for c in base_hex:
            total ^= int(c, 16)
        return f"{total:02X}"
