T = int(input())

for tc in range(1, T + 1):
    hex_to_dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                  'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    dec_to_bin = {0: '0000', 1: '0001', 2: '0010', 3: '0011', 4: '0100', 5: '0101', 6: '0110', 7: '0111',
                  8: '1000', 9: '1001', 10: '1010', 11: '1011', 12: '1100', 13: '1101', 14: '1110', 15: '1111'}

    hex_ = input()
    bin_ = ''
    for i in hex_:
        bin_ += dec_to_bin[hex_to_dec[i]]

    i = 0
    while i < len(bin_):
        if bin_[i:i+7] == '0000000':
            i += 4
            continue
        current_bin = bin_[i:i + 7]
        current_bin = reversed(current_bin)
        bin__ = 1
        dec_ = 0
        for j in current_bin:
            if j == '1':
                dec_ += bin__
            bin__ *= 2
        print(dec_, end=' ')
        i += 7
    print()

