import struct 
## convert each char in file into huffman encoded form
def bin_encode(letters_str:str, cipher: dict)->bytes:
    bits_str=[]
    ret_bytes = b""

    for letter in letters_str:
        bits_str.append(cipher[letter])
    bits_str = "".join(bits_str)

    ## process up to last multiple of 8 bits
    number_bytes = len(bits_str) // 8

    for i in range(0, number_bytes*8, 8):
        bite = struct.pack(">B",int(bits_str[i:i+8],2))
        ret_bytes += bite

    ## calculate number of bits to be pre-pended for remainig bits
    remaining_bits = bits_str[number_bytes*8:]
    pad_bits = 8 - len(remaining_bits )
    if pad_bits == 8:
        ret_bytes += struct.pack(">B",0)
    else:
        ret_bytes += struct.pack(">B",int(remaining_bits,2))
    
    return ret_bytes

def bin_decode(bytes_array: bytes)->str:

    bits_str = "".join ( f"{b:08b}" for b in bytes_array[:-2] )     
    pad_bits = bytes_array[-1]
    remaining_bits = f"{bytes_array[-2]:08b}"
    bits_str += remaining_bits[pad_bits:]
    return bits_str