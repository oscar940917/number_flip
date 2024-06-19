import sys
def main():
    input_number = sys.stdin.read().strip()
    if input_number:
        reversed_number = input_number[::-1].lstrip('0')
        if not reversed_number:
            reversed_number = '0'
        print(reversed_number)
if __name__ == "__main__":
    main()
