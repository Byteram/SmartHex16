# SmartHex16 — Technical Specification

Author: Victor Matos (@spacemany2k38, @vvrmatos)  
Email: contact@byteram.co  
Date: 2025-04-25  
Title: Applied Mathematician

## Overview
SmartHex16 is a 16-character hexadecimal identifier system combining 14 random digits with a 2-digit checksum. It provides a balance of entropy, compactness, and error detection for modern applications. The checksum enables detection of common data entry errors but provides no cryptographic security or tamper resistance. Checksum detects accidental errors, not intentional modification.

## Technical Specifications

### Entropy & Space
- 14 random hex digits (56 bits of entropy)
- Total unique IDs: 72,057,594,037,927,936 (72 quadrillion)
- Practical collision threshold: ~96 million IDs for 1% collision probability

#### Mathematical Foundation
1. **Basic Entropy Calculation**:
   - Each hex digit: 16 values (0-9, A-F) = 4 bits
   - 14 digits × 4 bits = 56 bits total entropy
   - Total unique combinations = 16^14 = 72,057,594,037,927,936

2. **Scale Comparison**:
   - 1 million IDs/second → 2,285 years to exhaust
   - 1 billion IDs/second → 2.28 years to exhaust
   - 1 trillion IDs/second → 20 hours to exhaust

3. **Collision Probability (Birthday Problem)**:
   ```
   P(collision) ≈ 1 - e^(-n(n-1)/(2N))
   where:
   - n = number of IDs generated
   - N = 72,057,594,037,927,936 (total possible IDs)
   ```

4. **Practical Limits**:
   - 1% collision probability: ~96 million IDs
   - 50% collision probability: ~2.5 billion IDs
   - 99% collision probability: ~11.5 billion IDs

5. **Comparison with Common Systems**:
   - UUIDv4: 122 bits (5.3 × 10^36 unique values)
   - MongoDB ObjectId: 96 bits (7.9 × 10^28 unique values)
   - SmartHex16: 56 bits (7.2 × 10^16 unique values)
   - Suitable for: Most applications generating < 100 million IDs

### Structure
- Format: `[14 random hex][2 checksum hex]`
- Fixed length: 16 characters
- Case-insensitive validation

### Checksum Algorithm
- Polynomial weighting (position × value)
- Modulo 256 reduction
- Properties:
  - Single-digit error detection
  - Adjacent transposition detection
  - O(n) computational complexity
- Security Limitations:
  - No cryptographic properties
  - Easily forgeable
  - Designed for error detection only
  - Detects accidental errors, not intentional modification

## Use Cases
- Database record identifiers
- URL-safe resource references
- QR code content
- Edge/embedded system IDs
- High-volume tracking numbers
- Temporary access tokens

## Security Considerations
- Cryptographically secure random generation
- Checksum for error detection only (not security)
- Not suitable for:
  - API keys or authentication tokens
  - Cryptographic signatures
  - Tamper-proof systems
  - Century-scale high-volume systems
  - Any security-sensitive applications

## Future Considerations
- Potential expansion to SmartHex32 for increased entropy
- Maintains current benefits while scaling entropy
- Note: Increased entropy does not improve security properties

---
