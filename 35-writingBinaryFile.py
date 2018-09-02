
print("----------------------- 1 -----------------------")
# When writing binary files, we must use ".write()" function.
# Use "bytes()" if wanting to write the binaries of some integers.
with open("35-binary", "bw") as binary_file:
	binary_file.write(bytes(range(17)))

with open("35-binary", "br") as bin_file:
	for b in bin_file:
		print(b)

print("----------------------- 2 -----------------------")
# Here we try to write more integers into bytes. Notice the "big/little" parameter. "big" means that the most
# significant bytes are stored first in the memory. "little" means the least significant bytes are stored first.
# This could cause a problem as you read the binary expression wrong as showed on the last 2 lines of code.
# Those 2 lines represent the same integer but only one read the binary expression correctly due to "big/little."
a = 65534 # FF FE
b = 65535 # FF FF
c = 65536 # 00 01 00 00
x = 2998302 # 02 2D C0 1E

with open("35-binary2", "bw") as bin_file:
	bin_file.write(a.to_bytes(2, "big"))
	bin_file.write(b.to_bytes(2, "big"))
	bin_file.write(c.to_bytes(4, "big"))
	bin_file.write(x.to_bytes(4, "big"))
	bin_file.write(x.to_bytes(4, "little"))

with open("35-binary2", "br") as binary_file:
	for line in binary_file:
		print(line)

with open("35-binary2", "br") as bin_file:
	e = int.from_bytes(bin_file.read(2), "big") # This represents "a"
	print(e)
	f = int.from_bytes(bin_file.read(2), "big") # This represents "b"
	print(f)
	g = int.from_bytes(bin_file.read(4), "big") # This represents "c"
	print(g)
	h = int.from_bytes(bin_file.read(4), "big") # This represents "x" with "big"
	print(h)
	i = int.from_bytes(bin_file.read(4), "big") # This represents "x" with "little"
	print(i)