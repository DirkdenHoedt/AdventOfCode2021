from math import prod

hex_to_bin = {
    '0':"0000",
    '1':"0001",
    '2':"0010",
    '3':"0011",
    '4':"0100",
    '5':"0101",
    '6':"0110",
    '7':"0111",
    '8':"1000",
    '9':"1001",
    'A':"1010",
    'B':"1011",
    'C':"1100",
    'D':"1101",
    'E':"1110",
    'F':"1111",
}

def parse_packet(data):
    version = int(data[:3], 2)
    typeid = int(data[3:6], 2)
    if typeid == 4:
        value_bits = ""
        idx = 6
        while True:
            segment = data[idx:idx+5]
            value_bits += segment[1:5]
            idx += 5
            if segment[0] == "0":
                break
        return idx, (version, typeid, int(value_bits, 2))
    else:
        if data[6] == '0':
            subpacket_length = int(data[7:22], 2)
            sub_data = data[22:22+subpacket_length]
            parsed = []
            while sub_data:
                idx, packet = parse_packet(sub_data)
                sub_data = sub_data[idx:]
                parsed.append(packet)
            return 22 + subpacket_length, (version, typeid, parsed)
        else:
            packet_count = int(data[7:18], 2)
            idx = 18
            parsed = []
            for _ in range(packet_count):
                new_id, packet = parse_packet(data[idx:])
                idx += new_id
                parsed.append(packet)
            return idx, (version, typeid, parsed)

def calculate(packet):
    typeid = packet[1]
    match typeid:
        case 0:
            return sum(calculate(x) for x in packet[2])
        case 1:
            return prod(calculate(x) for x in packet[2])
        case 2:
            return min(calculate(x) for x in packet[2])
        case 3:
            return max(calculate(x) for x in packet[2])
        case 4:
            return packet[2]
        case 5:
            return (calculate(packet[2][0]) > calculate(packet[2][1]))
        case 6:
            return (calculate(packet[2][0]) < calculate(packet[2][1]))
        case 7:
            return (calculate(packet[2][0]) == calculate(packet[2][1]))

def part2(path):
    bin_data = ""
    with open(path) as input:
        bin_data = "".join([hex_to_bin[x] for x in input.readline()])
    parsed = parse_packet(bin_data)[1]
    return calculate(parsed)