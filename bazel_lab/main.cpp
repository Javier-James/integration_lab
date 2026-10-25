#include <iostream>
#include "scanner/scanner.h" 


int main(){
    std::cout << "[SYSTEM] Starting ASML Main Controller..." << std::endl;
    Asml::Scanner scanner;
    scanner.initialize();
    return 0;

}
