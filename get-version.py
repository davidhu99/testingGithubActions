#!/usr/bin/env python
import sys
print()
if __name__ == "__main__":
	with open('version.txt', 'w+') as f:
		hash = sys.argv[1]
		f.write(hash)
