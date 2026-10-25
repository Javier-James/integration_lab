#include <iostream>

void process_buffer(){

   int* sensor_data = new int[100];
   sensor_data[0] = 42;

  std::cout << "[DEBUG] Processing sensor buffer: " <<sensor_data[0] << std::endl;


}

void corrupt_stack_demo(){

  int small_array[5] = {1,2,3,4,5}; 
  small_array[10] = 999;

  std::cout << "[DEBUG] Stackbuffer initialized." << std::endl;

}

int main(){
   std:: cout << "[SYSTEM] Starting Memory Diagnostic Lab..." << std::endl;
   process_buffer(); 
   corrupt_stack_demo();
   std::cout << "[SYSTEM] Shutting down." << std::endl;

   return 0;
}

