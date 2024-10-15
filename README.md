# RC4 Brute Force Script

This Python script brute-forces an RC4-encrypted message using a key of user-defined length. It attempts all possible combinations of lowercase letters, uppercase letters, and digits, and provides a progress bar to track the decryption process.

## Features

- Supports decryption of RC4-encrypted hex strings.
- Allows the user to specify the key length.
- Brute-forces all possible combinations of uppercase, lowercase letters, and digits.
- Provides a progress bar to monitor the brute-force attempts.
- Prints the decrypted message and the correct key once found.

## Requirements

The script uses the following Python libraries:
- `pycryptodome` (for RC4 encryption and decryption)
- `tqdm` (for displaying the progress bar)

To install the required libraries, use the provided `requirements.txt` file.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jlevija/RC4-Brute-Force.git
