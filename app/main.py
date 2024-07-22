import sys
from .scanner import Scanner
from .streamer import StdErrStream, Streamer

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)
    exitcode = 0

    with open(filename) as file:
        file_contents = file.read()

    scanner = Scanner(file_contents)
    stderr_stream = StdErrStream()
    std_stream = Streamer()

    if file_contents:
        scanner.scan(stderr_stream=stderr_stream, std_stream=std_stream)
    else:
        pass
    if stderr_stream.buffer:
        stderr_stream.print()
        exitcode = 65

    std_stream.print()
    
    scanner.print_eof()
    exit(exitcode)

if __name__ == "__main__":
    main()
