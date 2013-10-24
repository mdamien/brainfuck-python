import sys

def execute(code):
	code = ''.join([x for x in code if x in '.,+-<>[]'])
	cells,ptr,i = [0]*3000,0,0
	while i < len(code):
		c = code[i]
		if c == '>': ptr += 1
		if c == '<': ptr -= 1
		if c == '+': cells[ptr] += 1
		if c == '-': cells[ptr] -= 1
		if c == '.': sys.stdout.write(chr(cells[ptr]))
		if c == ',': cells[ptr] = ord(sys.stdin.read(1))
		if c == '[' and cells[ptr] == 0: i = code.find("]",i)
		if c == ']': i = code[:i].find('[')-1
		i += 1

if __name__ == '__main__':
	hello_world = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
	execute(hello_world)
	
	#read_print = ",[.,]"
	#while True: #REPL
	#	execute(raw_input(">>>"))	}
