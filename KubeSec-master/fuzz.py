import scanner
import parser
import graphtaint

if __name__ == '__main__':
    # Fuzzing Method 1
    graphtaint.getYAMLFiles(True)

    # Fuzzing Method 2
    scanner.isValidUserName(1.00)
    
    # Fuzzing Method 3
    parser.checkIfValidK8SYaml("\\")
                               
    # Fuzzing Method 4
    scanner.isValidPasswordName("0..0")

    # Fuzzing Method 5
    parser.checkIfWeirdYAML(False)
