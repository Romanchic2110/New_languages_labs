def normalize_bits(binary):
    max_lengh = max(len(bits) for bits in binary)
    return [bits.zfill(max_lengh) for bits in binary]


