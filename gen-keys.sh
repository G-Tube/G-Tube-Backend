#!/bin/bash

# Set directory and filenames
KEYS_DIR="./keys"
PRIVATE_KEY="$KEYS_DIR/private.pem"

# Create keys directory if it doesn't exist
mkdir -p "$KEYS_DIR"

# Generate private key
ssh-keygen -t rsa -b 2048 -m PEM -f "$PRIVATE_KEY" -N ""

# Output success message
echo "✅ Keys generated successfully!"
echo "🔑 Private Key: $PRIVATE_KEY"
echo "🔓 Public Key: $PRIVATE_KEY.pub"
