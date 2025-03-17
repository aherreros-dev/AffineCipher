## Affine Cipher Decoder & Letter Frequency Analyzer

### Overview

This repository provides two Python scripts designed for cryptographic analysis and text processing. These tools are useful for cryptographers, security researchers, and anyone interested in classical ciphers and frequency analysis.

### Features

#### 1. Affine Cipher Decoder

A script to decrypt messages encoded with the Affine Cipher, a classical encryption method based on modular arithmetic.

Deciphers messages using a known decimation constant, shift value, and custom alphabet.

Applies the mathematical decryption formula to recover the original message.

Displays the decoded text in the console.

Provides an option to save the decrypted message to a file for future reference.

#### 2. Letter Frequency Analyzer

A script to analyze letter frequency in a given text file, aiding cryptanalysis and language pattern recognition.

Reads an input .txt file and counts letter occurrences.

Computes the relative frequency distribution of letters.

Outputs structured results for easy interpretation.

### Installation

Ensure you have Python installed on your system (Python 3 recommended). Then, clone this repository:
```bash
git clone https://github.com/aherreros-dev/AffineCipher.git
cd AffineCipher
```
No additional dependencies are required.

### Usage

### Affine Cipher Decoder

Run the script and provide the necessary inputs:
```bash
python affine_decoder.py
```
Follow the on-screen prompts to enter the decimation constant, shift value, and the encrypted text.

### Letter Frequency Analyzer

Analyze a text file by running:

```bash
python letter_frequency.py input.txt
```

This will output letter counts and their frequency distribution.

## Example Output

### Affine Cipher Decoder
```bash
Decrypted Message: "THIS IS A SECRET MESSAGE"
```
### Letter Frequency Analyzer

```bash
A: 12 (8.5%)
B: 5 (3.5%)
C: 9 (6.4%)
...
```

### License

This project is licensed under the MIT License. See the LICENSE file for details.





