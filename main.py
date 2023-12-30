import re

arkan = {
    1: "mafaa'ilon",
    2: "faa'elaaton",
    3: "mostaf'elon",
    4: "mafaa'ilo",
    5: "faa'elaato",
    6: "mostaf'elo",
    7: "mafaa'elon",
    8: "fa'alaaton",
    9: "mofta'elon",
    10: "fa'alaato",
    11: "mafaa'elo",
    12: "fa'alon",
    13: "faa'elon",
    14: "fa'oolon",
    15: "maf'oolon",
    16: "maf'oolo",
    17: "fa'laano",
    18: "fa'al",
    19: "fa' lon",
    20: "fa'",
    21: "faa'elo",
    22: "motafaa'elon",
    23: "mostaf'elaton",
    24: "mafaa'elaton",
    25: "motafaa'elaton",
    26: "motafaa'elaaton",
    27: "motafa'elon"
}

vazn_ha = {
    1: [([14, 14, 14, 18], "shaahnaame")],
    2: [([1, 1, 14], "dobeyti")],
    3: [([2, 2, 2, 13], "")],
    4: [([7, 8, 7, 12], ""), ([7, 8, 7, 19], "degargoon shode")],
    5: [([16, 5, 4, 13], "")],
    6: [([8, 7, 12], ""), ([8, 7, 19], "degargoon shode")],
    7: [([2, 2, 13], "masnavi")],
    8: [([8, 8, 8, 12], ""), ([8, 8, 8, 19], "degargoon shode")],
    9: [([1, 1, 1, 1], "")],
    10: [([16, 4, 4, 14], "")],
    11: [([16, 4, 4, 18], "robaa'i")],
    12: [([16, 7, 14], "")],
    13: [([9, 9, 13], ""), ([7, 9, 13], "degargoon shode"), ([9, 7, 13], "degargoon shode")],
    14: [([16, 2, 16, 2], "")],
    15: [([14, 14, 14, 14], "")],
    16: [([9, 13, 9, 13], ""), ([7, 13, 9, 13], "degargoon shode"), ([9, 13, 7, 13], "degargoon shode")],
    17: [([8, 8, 12], ""), ([8, 8, 19], "degargoon shode")],
    18: [([9, 5, 9, 20], ""), ([7, 5, 9, 20], "degargoon shode"), ([9, 5, 7, 20], "degargoon shode")],
    19: [([3, 3, 3, 3], "")],
    20: [([16, 1, 16, 1], "")],
    21: [([9, 7, 9, 7], ""), ([7, 7, 9, 7], "degargoon shode"), ([9, 7, 7, 7], "degargoon shode")],
    22: [([7, 8, 7, 8], "")],
    23: [([16, 7, 1], "")],
    24: [([10, 2, 10, 2], "")],
    25: [([], "-")],
    26: [([8, 8, 8, 8], "")],
    27: [([2, 2, 2, 2], "")],
    28: [([16, 5, 1], "")],
    29: [([16, 4, 2], "")],
    30: [([13, 1, 13, 1], "")],
    31: [([8, 8, 8, 20], "")],
    32: [([3, 20, 3, 20], "")],
    33: [([22, 22, 22, 22], "")],
    34: [([23, 23], "")],
    35: [([9, 9, 9, 9], ""), ([7, 9, 9, 9], "degargoon shode"), ([9, 9, 7, 9], "degargoon shode")],
    36: [([7, 20, 7, 20, 7, 20, 7, 20], "")],
    37: [([16, 13, 16, 13], "")],
    38: [([3, 12, 3, 12], ""), ([3, 19, 3, 12], "degargoon shode"), ([3, 12, 3, 19], "degargoon shode")],
    39: [([2, 2, 2], "")],
    40: [([8, 7, 8, 7], "")],
    41: [([16, 24, 12], "")],
    42: [([7, 7, 7, 7], "")],
    43: [([16, 4, 13], "")],
    44: [([7, 20, 7, 20], "")],
    45: [([4, 14, 4, 14], "")],
    46: [([14, 7, 14, 7], "")],
    47: [([9, 5, 9], ""), ([7, 5, 9], "degargoon shode"), ([9, 5, 7], "degargoon shode")],
    48: [([16, 5, 1], "")],
    49: [([5, 20, 5, 20], "")],
    50: [([4, 4, 4, 14], "")],
    51: [([25, 25], "")],
    52: [([3, 3, 3, 20], "")],
    53: [([9, 20, 9, 20], "")],
    54: [([16, 5, 4, 20], "")],
    55: [([13, 13, 2], "")],
    56: [([7, 7, 7], "")],
    57: [([9, 9, 9, 20], ""), ([7, 9, 9, 20], "degargoon shode"), ([9, 7, 9, 20], "degargoon shode"), ([9, 9, 7, 20], "degargoon shode")],
    58: [([13, 13, 13, 20], "")],
    59: [([3, 3, 13], "")],
    60: [([16, 5, 4, 2], "")],
    61: [([2, 2, 2, 20], "")],
    62: [([16, 5, 14], "")],
    63: [([3, 3], "")],
    64: [([7, 13, 7, 13], "")],
    65: [([13, 2, 13, 2], "")],
    66: [([2, 20, 2, 20], "")],
    67: [([1, 1, 1], "")],
    68: [([3, 3, 3], "")],
    69: [([4, 4, 14], "")],
    70: [([9, 9, 9], "")],
    71: [([13, 13, 13, 13], "")],
    72: [([26, 26], "")],
    73: [([3, 2, 3, 2], "")],
    74: [([2, 13, 2, 13], "")],
    75: [([9, 9, 20, 9, 9, 20], "")],
    76: [([5, 20, 5, 20, 5, 20, 5, 20], "")],
    77: [([4, 4, 4, 14], "")],
    78: [([5, 9, 5, 9], "")],
    79: [([2, 2, 2, 13, 2, 13], "")],
    80: [([8, 12, 8, 12], ""), ([8, 19, 8, 12], "degargoon shode"), ([8, 12, 8, 19], "degargoon shode")],
    81: [([14, 14, 14], "")],
    82: [([8, 8, 8, 12, 8, 12], ""), ([8, 8, 8, 19, 8, 12], "degargoon shode"), ([8, 8, 8, 12, 8, 19], "degargoon shode")],
    83: [([15, 15, 15, 15], "")],
    84: [([16, 16, 2], "")],
    85: [([16, 5, 15], "")],
    86: [([4, 4, 13], "")],
    87: [([9, 9, 13, 18], "")],
    88: [([25, 25, 25, 25], "")],
    89: [([13, 15, 13, 15], "")],
    90: [([9, 20, 9, 20, 9, 20, 9, 20], "")],
    91: [([4, 5, 4, 13], "")],
    92: [([8, 7, 8], "")],
    93: [([7, 14, 7, 14], "")],
    94: [([4, 13], "")],
    95: [([16, 15, 1, 14], "")],
    96: [([3, 8, 3, 8], "")],
    97: [([7, 15, 7, 15], "")],
    98: [([3, 12, 3, 20], ""), ([3, 19, 3, 20], "degargoon shode")],
    99: [([22, 22, 22], "")],
    100: [([16, 2, 16, 13], "")],
    101: [([5, 15, 5, 15], "")],
    102: [([10, 12, 10, 12], ""), ([10, 19, 10, 12], "degargoon shode"), ([10, 12, 10, 19], "degargoon shode")],
    103: [([3, 3, 20], "")],
    104: [([2, 20, 24], "")],
    105: [([15, 20, 15, 20], "")],
    106: [([4, 14, 7], "")],
    107: [([5, 15, 5, 9], "")],
    108: [([3, 3, 14], "")],
    109: [([16, 5, 18], "")],
    110: [([5, 12, 5, 12], ""), ([5, 19, 5, 12], "degargoon shode"), ([5, 12, 5, 19], "degargoon shode")],
    111: [([9, 20, 7, 20], "")],
    112: [([3, 3, 15], "")],
    113: [([16, 4, 9], "")],
    114: [([9, 9, 14, 14], "")],
    115: [([14, 1, 14, 1], "")],
    116: [([1, 1, 14, 8], "")],
    117: [([10, 19, 10, 19], "")],
    118: [([4, 5, 16, 13], "")],
    119: [([2, 2, 20, 2], "")],
    120: [([9, 14, 9, 14], "")],
    121: [([2, 2, 2, 14, 13], "")],
    122: [([21, 21, 21, 21, 20], ""), ([21, 19, 21, 21, 20], "degargoon shode"), ([21, 21, 19, 21, 20], "degargoon shode"), ([21, 21, 21, 19, 20], "degargoon shode")],
    123: [([3, 20, 3, 13], "")],
    124: [([16, 18, 16, 18], "")],
    125: [([16, 7, 16, 7], "")],
    126: [([1, 1, 1, 18], "")],
    127: [([13, 7, 20, 13, 7, 20], "")],
    128: [([16, 9, 16, 9], "")],
    129: [([3, 8, 20], "")],
    130: [([9, 9, 16, 1], "")],
    131: [([14, 14, 7], "")],
    132: [([14, 7, 1], "")],
    133: [([16, 1, 12], ""), ([16, 1, 19], "degargoon shode")],
    134: [([1, 1], "")],
    135: [([8, 8, 8], "")],
    136: [([16, 1, 18], "")],
    137: [([16, 7, 15], "")],
    138: [([24, 24, 24, 24], "")],
    139: [([7, 7, 13], "")],
    140: [([22, 22], "")],
    141: [([9, 20, 9, 9, 20, 9], "")],
    142: [([10, 6, 20, 10, 6, 20], "")],
    143: [([8, 7, 20, 8, 7, 20], "")],
    144: [([10, 2, 10, 12], ""), ([10, 2, 10, 19], "degargoon shode")],
    145: [([14, 14, 14, 14, 14, 18], "")],
    146: [([14, 14, 14, 14, 14], "")],
    147: [([4, 9, 20, 4, 9, 20], "")],
    148: [([10, 2, 10, 13], "")],
    149: [([1, 14, 1, 14], "")],
    150: [([16, 4, 14, 15], "")],
    151: [([2, 7, 2, 7], "")],
    152: [([8, 8, 18], "")],
    153: [([16, 2, 16, 20], "")],
    154: [([8, 2, 8, 2], "")],
    155: [([9, 19, 9, 19], "")],
    156: [([3, 15, 3, 19], "")],
    157: [([16, 4, 1, 20], "")],
    158: [([16, 2, 1], "")],
    159: [([1, 1, 1, 14], "")],
    160: [([16, 2, 15], "")],
    161: [([27, 27, 27, 27], "")],
    162: [([15, 15, 15, 19], "")],
    163: [([16, 4, 4, 1], "")]
}

def csl(s):
    # long vowels
    s = re.sub(r"(?:aa|ee|o[ow]|i(?!y)|u)", "L", s)
    # short vowels
    s = re.sub(r"(?:(?<!a)a(?!a)|(?<!o)o(?![ow])|e|i(?=y))", "S", s)
    # consonants
    s = re.sub(r"(?:['bdfhjlmpqrtvxy]|ch|g[h]?|k[h]?|s[h]?|z[h]?)", "C", s)
    # N
    s = re.sub(r"(?<=L)n(?![LS])", "", s)
    s = re.sub(r"n", "C", s)

    # hamzeh
    s = re.sub(r"(?:(?<=[LS] )L|^L)", "CL", s)
    s = re.sub(r"(?:(?<=[LS] )S|^S)", "CS", s)

    # remove spaces
    s = re.sub(r" ", "", s)

    return s

def heja(s):
    s = csl(s)

    # heja
    s = re.sub(r"CLCC(?![LS])|CLC(?![LS])|CSCC(?![LS])", "_U", s)
    s = re.sub(r"CSC(?![LS])|CL", "_", s)
    s = re.sub(r"CS", "U", s)

    return s

def heja_w_special(s):
    s = heja(s)

    # special cases
    s = re.sub(r"UUU", "UU_", s)
    s = re.sub(r"_U$", "_", s)

    return s

def vazn(s, dist_func, threshold):
    heja_s = heja_w_special(s)
    ozan = []
    for k, v_all in vazn_ha.items():
        for (i, v) in enumerate(v_all):
            vzn = ""
            for j in v[0]:
                vzn = vzn + heja(arkan[j])
            if check_matching(vzn, heja_s, dist_func, threshold):
                ozan += [(k, i)]
    return ozan

def check_matching(vzn, heja, dist_func, threshold):
    if check_match_or_transform(vzn, heja, dist_func, threshold):
        return True
    # heja_alt = re.sub(r"_U$", "_", heja)
    # if heja_alt != heja and \
    #     check_match_or_transform(vzn, heja_alt, dist_func, threshold):
    #     return True
    vzn_alt = re.sub(r"^UU__", "_U__", vzn)
    if vzn_alt != vzn and \
        check_match_or_transform(vzn_alt, heja, dist_func, threshold):
        return True
    # if vzn_alt != vzn and \
    #     heja_alt != heja and \
    #     check_match_or_transform(vzn_alt, heja_alt, dist_func, threshold):
    #     return True
    return False

def check_match_or_transform(vzn, heja, dist_func, threshold):
    if dist_func(heja, vzn) <= threshold \
        or match_UU_transform(vzn, heja, dist_func, threshold):
        # or matchUUtransform(vzn, heja, dist_func, threshold):
        return True
    return False

# def matchUUtransform(vzn, heja, dist_func, threshold):
#     i = -1
#     while True:
#         l = i
#         i = vzn.find("UU", l+1)
#         if i < 0:
#             return False
#         if dist_func(vzn[:i] + "_" + vzn[i+2:], heja) <= threshold:
#             return True

def match_UU_transform(vzn, heja, dist_func, threshold):
    i = -1
    while True:
        l = i
        i = vzn.find("_UU_", l+4)
        if i < 0:
            return False
        if dist_func(vzn[:i] + "U_U_" + vzn[i+4:], heja) <= threshold:
            return True

def try_add_ee(scan, dist_func, threshold):
    i = -1
    while True:
        l = i
        i = scan.find("e ", l+2)
        if i < 0:
            return ""
        if len(vazn(scan[:i] + "ee " + scan[i+2:], dist_func, threshold)) > 0:
            return "Yek \"e\" be aakhare \"...{}\" ezaafe konid.".format(scan[i-4:i+1])

def try_fixes(scan, dist_func, threshold):
    fixes = ""
    alt_aa = re.sub(r"(?<!a)a ", "aa ", scan)
    if len(vazn(alt_aa, dist_func, threshold)):
        fixes += "Bejaaye \"aa\" jaahaayi az \"a\" estefade karde'id.\n"
    alt_ow = re.sub(r"(?<!o)o ", "ow ", scan)
    if len(vazn(alt_ow, dist_func, threshold)):
        fixes += "Ba'zi az kalamaat maanande \"to\" va \"beshno\" mitavaanand be soorate \"now\" va \"beshenow\" dar khaande shavand.\n"
    fixes += try_add_ee(scan, dist_func, threshold) + "\n"
    return fixes

if __name__ == "__main__":
    scan = input("Yek mesraa' raa be finglish vared konid:\n").strip().lower()
    print(heja_w_special(scan))

    # import jellyfish
    # dist_func = jellyfish.hamming_distance
    # threshold = 1
    dist_func = lambda s1, s2: 0 if s1 == s2 else 1
    threshold = 0
    ozan = vazn(scan, dist_func, threshold)
    print("{}".format(ozan))

    if threshold == 0 and len(ozan) == 0:
        fixes = try_fixes(scan, dist_func, threshold)
        if fixes != "":
            print("Moshkelaate ehtemaali:")
            print(fixes)
