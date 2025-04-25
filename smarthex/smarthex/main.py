import secrets

class SmartHex:
    def generate(self):
        """Generate a 16-character hex identifier with checksum."""
        raw_bytes = secrets.token_bytes(7)
        base_hex = raw_bytes.hex().upper()
        return base_hex + self._compute_checksum(base_hex)

    def validate(self, id_hex):
        """Validate a 16-character hex identifier."""
        if len(id_hex) != 16:
            return False
        base, check = id_hex[:14], id_hex[14:]
        return self._compute_checksum(base) == check.upper()

    def _compute_checksum(self, base_hex):
        """
        Compute a robust checksum using polynomial weighting.
        
        The checksum is computed as:
        Σ (digit_i * (i + 1)) mod 256
        
        This provides:
        - Perfect detection of single-digit errors
        - High detection rate of transpositions
        - Uniform distribution of checksum values
        """
        # Convert hex string to list of integers
        digits = [int(c, 16) for c in base_hex]
        
        # Compute weighted sum using polynomial weights
        checksum = sum(d * (i + 1) for i, d in enumerate(digits))
        
        # Normalize to 8-bit value and convert to hex
        return f"{(checksum & 0xFF):02X}" 
