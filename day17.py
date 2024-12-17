import time
from typing import List

class RunningProgram():

    def __init__(self):
        self.A: int = 0
        self.B: int = 0
        self.C: int = 0
        self.idx = 0
        self.outp = []

    def get_combo(self, num) -> int:
        if 0<=num<4:
            return num
        elif num == 4:
            return self.A
        elif num == 5:
            return self.B
        elif num == 6:
            return self.C
        print("Invalid combo number")
        return -1
        
    def adv(self, num):
        numerator, denominator = self.A, 2**(self.get_combo(num))
        self.A = numerator // denominator

    def bxl(self, num):
        self.B ^= num

    def bst(self, num):
        self.B = self.get_combo(num) % 8

    def jnz(self, num):
        if self.A != 0:
            self.idx = num-2
    
    def bxc(self, num):
        self.B = self.B ^ self.C

    def out(self, num):
        self.outp.append(self.get_combo(num)%8)

    def bdv(self, num):
        numerator, denominator = self.A, 2**(self.get_combo(num))
        self.A = numerator // denominator

    def cdv(self, num):
        numerator, denominator = self.A, 2**(self.get_combo(num))
        self.C = numerator // denominator

    def run(self, program) -> str:
        self.idx = 0
        while self.idx < len(program):
            
            opcode = program[self.idx]
            argument = program[self.idx+1]
            if opcode == 0:
                self.adv(argument)
            elif opcode == 1:
                self.bxl(argument)
            elif opcode == 2:
                self.bst(argument)
            elif opcode == 3:
                self.jnz(argument)
            elif opcode == 4:
                self.bxc(argument)
            elif opcode == 5:
                self.out(argument)
            elif opcode == 6:
                self.bdv(argument)
            elif opcode == 7:
                self.cdv(argument)
            self.idx += 2

        r = ",".join([str(x) for x in self.outp])
        return r


def part1():
    with open("inputs/input_17.txt", "r") as f:
        lines = []
        for line in f.readlines():
            if ":" in line:
                lines.append(line.strip())
        rp = RunningProgram()
        rp.A = int(lines[0].split(":")[1])
        rp.B = int(lines[1].split(":")[1])
        rp.C = int(lines[2].split(":")[1])
        program = list(map(int,lines[3].split(":")[1].split(",")))
        r = rp.run(program)
        print(f"Part 1: {r}")

def inverse_quick_loop(b, a) -> List[int]:
    A_base = a * 8
    r = []
    for remainder in range(8):
        A_test = A_base + remainder
        
        b_test = ((remainder) ^ 3)
        c_test = A_test // (2 ** b_test)
        b_test = b_test ^ 5
        b_test = b_test ^ c_test
        b_test = b_test % 8
        
        if b_test == b:
            r.append(A_test)
            
    return r

def search_for_A(tgt, a_values) -> List[int]:
    for i, obj in enumerate(tgt):
        new_a = []
        for a in a_values:
            next_a = inverse_quick_loop(obj, a)
            new_a.extend(next_a)
        a_values = new_a

    return a_values

def part2():
    lines = []
    with open("inputs/input_17.txt", "r") as f:
        for line in f.readlines():
            if ":" in line:
                lines.append(line.strip())
        program_str = lines[3].split(":")[1].strip()
    
        program = list(map(int,program_str.split(",")))
        t0 = time.time()
        for i in range(10_000_000_000):
            a_values = search_for_A(program[::-1], [i])
            if len(a_values) > 0:
                final_a = sorted(a_values)[0]
                print(f"Part 2: {final_a}")
                break

if __name__ == "__main__":
    part1()
    part2()