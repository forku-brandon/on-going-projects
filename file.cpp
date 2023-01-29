// C++ program to read contents from
// one file and write it to another file
#include<bits/stdc++.h>
using namespace std;
  
// Driver code
int main()
{  
  // Input file stream object to 
  // read from file.txt
  ifstream in("/usr/share/john/password.lst");

    
  // Output file stream object to 
  // write to file2.txt
  ofstream n("/home/brandon/Desktop/brand.zip");
      
  // Reading file.txt completely using 
  // END OF FILE eof() method
  while(!in.eof())
  {
    // string to extract line from 
    // file.txt
    string text;
        
    // extracting line from file.txt
    getline(in, text);

        
    // Writing the extracted line in 
    // file2.txt
    n << text << endl;
  }
  return 0;
}