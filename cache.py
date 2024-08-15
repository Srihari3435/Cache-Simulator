# Direct mapped cache simulator
import math

def init_table(n):
    matrix = []
    for i in range(n):
        row = [i]  # Assigning the index value as the first element of each row
        for _ in range(1):
            row.append(0)
            row.append("0")
        matrix.append(row)
    return matrix

def print_cache(matrix):
    print("Index\t    Valid bit\t       Tag")
    for row in matrix:
        for element in row:
            print(element, end="\t\t")
        print()

def main():
    cache_size = int(input("Enter cache size in bytes: "))
    block_size = int(input("Enter block size in bytes: "))
    memory_size = int(input("Enter memory size in bytes: "))

    line = cache_size // block_size

    mem_bits = int(math.log2(memory_size))
    line_bits = int(math.log2(line)) #index
    block_bits = int(math.log2(block_size)) #offset
    tag_bits = mem_bits - line_bits - block_bits

    print(f"\nTag\tLine\tWord")
    print(f"{tag_bits}\t{line_bits}\t{block_bits}\n")
    cache_table = []

    cache_table = init_table(line)

    print_cache(cache_table)
    hit = 0
    miss = 0
    hit_rate=0.00
    miss_rate=0.00
    while True:
        instr = int(input("Enter the instrution in decimal (-1 to end):"))
        if instr == -1:
            break

        mem_addr = bin(instr)[2:].zfill(mem_bits)
        tag_bin = mem_addr[0:tag_bits]
        index_bin = mem_addr[tag_bits:tag_bits+line_bits] # In string
        index_dec = int(index_bin, 2) # In decimal
        offset_bin = mem_addr[tag_bits+line_bits:] # In string

        print("\nMemory Address:\n")
        print("Tag\t         Index\t      Offset")
        print(f"{tag_bin}\t   {index_bin}\t\t {offset_bin}")

        print("\n------Checking Valid Bit------\n")

        if cache_table[index_dec][1] == 0:
            print("Valid bit is 0")
            print("Cache Miss\n")
            miss = miss+1
            cache_table[index_dec][1] = 1  # Make valid bit 1
            cache_table[index_dec][2] = tag_bin # Update the value

        elif cache_table[index_dec][1] == 1:
            if cache_table[index_dec][2] == tag_bin:
                print("Cache Hit")
                hit = hit+1
            else:
                print("Cache Miss")
                miss = miss+1
                cache_table[index_dec][2] = tag_bin
        
        print_cache(cache_table)
        hit_rate = round((hit/(hit+miss))*100,2)
        miss_rate = round((miss/(hit+miss))*100,2)
        print(f"\nHit Rate: {hit_rate}%\nMiss Rate: {miss_rate}%") 

    print("\n------Final Cache Table------\n")
    print_cache(cache_table)
    print()
    print(f"\n No.of Hits : {hit}\n No.of Misses : {miss}")
    print(f"\nHit Rate: {hit_rate}%\nMiss Rate: {miss_rate}%")

if __name__ == "__main__":
    main()