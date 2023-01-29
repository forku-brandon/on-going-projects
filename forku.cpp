#include <iostream>
#include <math.h>
#include <string.h>

using namespace std;

void intru(string k) {
  cout << " \\\        ///  ||||||||    |||       ///||||||||\\      //|||||\\ "
          "         |||  ||||      ||||||      "
       << endl;
  cout << " \\\       ///   |||         |||      |||                ||     ||  "
          "      /// \\\//\\\        ||    "
       << endl;
  cout << "  \\ //\\ ///    |||||||     |||      |||                ||     ||  "
          "     ///        \\     |||||      "
       << endl;
  cout << "   \\\|| |///    |||         |||      |||                ||     ||  "
          "    ///          \\    |||          "
       << endl;
  cout << "               |||||||     |||||||  \\\||\\||||||//        "
          "\\\|||///                         ||||||       "
       << endl;

  cout << "...................................................................."
          ".............................."
       << endl;
  cout << "ONCE MORE WELCOME " << k
       << " YOU HAVE FINALLY LOG IN INTO YOUR ACCOUT" << endl;
  cout << "...................................................................."
          ".............................."
       << endl;
}

void next() {
  string l;
  cout << "THE FOLLOWING ARE THE VERIOUSE COURSEES WE WILL BE LEARNING THIS "
          "CEMISTER"
       << endl;
  cout << "***PROGRAMING" << endl;
  cout << "***DATA COLLECTION" << endl;
  cout << "***CRYPTOGRAPHY" << endl;
  cout << "***CYBER SECURITY" << endl;
  cout << "***ETHICAL HACKING" << endl;
  cout << "...................................................................."
          "......................................."
       << endl;
  while (l != "X") {
    cout << ".................................................................."
            "........................................"
         << endl;
    cout << "click the following letters to begin with courses listed===>>>"
         << endl;
    cout << "PROGRAMING===> click > p " << endl;
    cout << " DATA COLLECTION=====> clck > d " << endl;
    cout << " CRYPTOGRAPHY ====> click > c " << endl;
    cout << "CYBER SECURITY ====> click > cy " << endl;
    cout << "ETHICAL HACKING =====> click > e " << endl;
    cout << "TO EXIT THIS APP =====>CLICK > x " << endl;
    cout << ".................................................................."
            "............................"
         << endl;
    cout << "====>: " << endl;
    cin >> l;
    if (l == "P") {
      cout << "THERE YOU GO===> " << endl;
      string ans;
      int result;
      result = 0;
      cout << "welcome to the programing course" << endl;
      cout << "________________________________________________________________"
              "________________________________"
           << endl;
      cout << "|TO BE SURE THAT YOU HAVE UNDERSTOOD EVERY THING YOOU READ, YOU "
              "WILL HAVE TO ANSWER A LITTLE MSQ QUIZ"
           << endl;
      cout << "----------------------------------------------------------------"
              "-------------------------------"
           << endl;
      cout << "[1]. what is the mearning of programing " << endl;
      cout << "(A)==> something" << endl;
      cout << "(B)==>anything " << endl;
      cout << "(C)=>everyting " << endl;
      cout << "(D)==>nothing " << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "A" || ans == "B" || ans == "C") {
        result = result + 0;
      } else if (ans == "D") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "[2]. who are you ? " << endl;
      cout << "(A)==> someone" << endl;
      cout << "(B)==>anyane " << endl;
      cout << "(C)=>everyone " << endl;
      cout << "(D)==>no one " << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "D" || ans == "B" || ans == "C") {
        result = result + 0;
      } else if (ans == "A") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "[3]. what is your name? " << endl;
      cout << "(A)==> brandon" << endl;
      cout << "(B)==>brando" << endl;
      cout << "(C)=>brenda " << endl;
      cout << "(D)==>brandi " << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "D" || ans == "A" || ans == "C") {
        result = result + 0;
      } else if (ans == "B") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "[4]. which town are you from " << endl;
      cout << "(A)==> bamenda" << endl;
      cout << "(B)==>deuala" << endl;
      cout << "(C)=>buea" << endl;
      cout << "(D)==>bafusam" << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "D" || ans == "A" || ans == "C") {
        result = result + 0;
      } else if (ans == "B") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "[5]. what is your fathers name" << endl;
      cout << "(A)==> mr john" << endl;
      cout << "(B)==> mr paul" << endl;
      cout << "(C)=>  mr kingsly" << endl;
      cout << "(D)==> mr awa" << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "D" || ans == "A" || ans == "C") {
        result = result + 0;
      } else if (ans == "B") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "________________________________________________________________"
              "_______"
           << endl;
      cout << "YOUR TOTAL MARKS IS ...." << endl;
      cout << "_______________________" << endl;
      cout << "||" << result << "/5    ||" << endl;
      cout << " ---------------------" << endl;
      if (result < 3) {
        cout << "....SORRY YOU FAILED THE QUIZ I WILL ADVICE YOU REPEAT THE "
                "COURSE AGIAN..."
             << endl;
      } else {
        cout << "....CONGRATULATION!  YOU PASS THE QUIZ NOW YOU CAN TAKE THE "
                "NEXT COURSE..."
             << endl;
      }

    } else if (l == "D") {
      int result;
      string ans;
      result = 0;
      cout << "THERE YOU GO===> " << endl;
      cout << "welcome to the data collection course" << endl;
      cout << "________________________________________________________________"
              "________________________________"
           << endl;
      cout << "|TO BE SURE THAT YOU HAVE UNDERSTOOD EVERY THING YOOU READ, YOU "
              "WILL HAVE TO ANSWER A LITTLE MSQ QUIZ"
           << endl;
      cout << "----------------------------------------------------------------"
              "-------------------------------"
           << endl;
      cout << "[1]. what is the mearning of programing " << endl;
      cout << "(A)==> something" << endl;
      cout << "(B)==>anything " << endl;
      cout << "(C)=>everyting " << endl;
      cout << "(D)==>nothing " << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "A" || ans == "B" || ans == "C") {
        result = result + 0;
      } else if (ans == "D") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "[2]. who are you ? " << endl;
      cout << "(A)==> someone" << endl;
      cout << "(B)==>anyane " << endl;
      cout << "(C)=>everyone " << endl;
      cout << "(D)==>no one " << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "D" || ans == "B" || ans == "C") {
        result = result + 0;
      } else if (ans == "A") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "[3]. what is your name? " << endl;
      cout << "(A)==> brandon" << endl;
      cout << "(B)==>brando" << endl;
      cout << "(C)=>brenda " << endl;
      cout << "(D)==>brandi " << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "D" || ans == "A" || ans == "C") {
        result = result + 0;
      } else if (ans == "B") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "[4]. which town are you from " << endl;
      cout << "(A)==> bamenda" << endl;
      cout << "(B)==>deuala" << endl;
      cout << "(C)=>buea" << endl;
      cout << "(D)==>bafusam" << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "D" || ans == "A" || ans == "C") {
        result = result + 0;
      } else if (ans == "B") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "[5]. what is your fathers name" << endl;
      cout << "(A)==> mr john" << endl;
      cout << "(B)==> mr paul" << endl;
      cout << "(C)=>  mr kingsly" << endl;
      cout << "(D)==> mr awa" << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "D" || ans == "A" || ans == "C") {
        result = result + 0;
      } else if (ans == "B") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "________________________________________________________________"
              "_______"
           << endl;
      cout << "YOUR TOTAL MARKS IS ...." << endl;
      cout << "_______________________" << endl;
      cout << "||  " << result << "/5    ||" << endl;
      cout << " ---------------------" << endl;
      if (result < 3) {
        cout << "....SORRY YOU FAILED THE QUIZ I WILL ADVICE YOU REPEAT THE "
                "COURSE AGIAN..."
             << endl;
      } else {
        cout << "....CONGRATULATION!  YOU PASS THE QUIZ NOW YOU CAN TAKE THE "
                "NEXT COURSE..."
             << endl;
      }

    } else if (l == "C") {
      cout << "THERE YOU GO===> " << endl;

      cout << "welcome to the cryptography couse" << endl;
      cout << "________________________________________________________________"
              "________________________________"
           << endl;
      cout << "|TO BE SURE THAT YOU HAVE UNDERSTOOD EVERY THING YOOU READ, YOU "
              "WILL HAVE TO ANSWER A LITTLE MSQ QUIZ"
           << endl;
      cout << "----------------------------------------------------------------"
              "-------------------------------"
           << endl;
      string ans;
      int result = 0;
      cout << "[1]. what is the mearning of programing " << endl;
      cout << "(A)==> something" << endl;
      cout << "(B)==>anything " << endl;
      cout << "(C)=>everyting " << endl;
      cout << "(D)==>nothing " << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "A" || ans == "B" || ans == "C") {
        result = result + 0;
      } else if (ans == "D") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "[2]. who are you ? " << endl;
      cout << "(A)==> someone" << endl;
      cout << "(B)==>anyane " << endl;
      cout << "(C)=>everyone " << endl;
      cout << "(D)==>no one " << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "D" || ans == "B" || ans == "C") {
        result = result + 0;
      } else if (ans == "A") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "[3]. what is your name? " << endl;
      cout << "(A)==> brandon" << endl;
      cout << "(B)==>brando" << endl;
      cout << "(C)=>brenda " << endl;
      cout << "(D)==>brandi " << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "D" || ans == "A" || ans == "C") {
        result = result + 0;
      } else if (ans == "B") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "[4]. which town are you from " << endl;
      cout << "(A)==> bamenda" << endl;
      cout << "(B)==>deuala" << endl;
      cout << "(C)=>buea" << endl;
      cout << "(D)==>bafusam" << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "D" || ans == "A" || ans == "C") {
        result = result + 0;
      } else if (ans == "B") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "[5]. what is your fathers name" << endl;
      cout << "(A)==> mr john" << endl;
      cout << "(B)==> mr paul" << endl;
      cout << "(C)=>  mr kingsly" << endl;
      cout << "(D)==> mr awa" << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "D" || ans == "A" || ans == "C") {
        result = result + 0;
      } else if (ans == "B") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "________________________________________________________________"
              "_______"
           << endl;
      cout << "YOUR TOTAL MARKS IS ...." << endl;
      cout << "_______________________" << endl;
      cout << "||" << result << "/5    ||" << endl;
      cout << " ---------------------" << endl;
      if (result < 3) {
        cout << "....SORRY YOU FAILED THE QUIZ I WILL ADVICE YOU REPEAT THE "
                "COURSE AGIAN..."
             << endl;
      } else {
        cout << "....CONGRATULATION!  YOU PASS THE QUIZ NOW YOU CAN TAKE THE "
                "NEXT COURSE..."
             << endl;
      }

    } else if (l == "CY") {
      cout << "THERE YOU GO===> " << endl;

      cout << "welcome to the cyber security class" << endl;
      cout << "________________________________________________________________"
              "________________________________"
           << endl;
      cout << "|TO BE SURE THAT YOU HAVE UNDERSTOOD EVERY THING YOOU READ, YOU "
              "WILL HAVE TO ANSWER A LITTLE MSQ QUIZ"
           << endl;
      cout << "----------------------------------------------------------------"
              "-------------------------------"
           << endl;

      string ans;
      int result = 0;
      cout << "[1]. what is the mearning of programing " << endl;
      cout << "(A)==> something" << endl;
      cout << "(B)==>anything " << endl;
      cout << "(C)=>everyting " << endl;
      cout << "(D)==>nothing " << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "A" || ans == "B" || ans == "C") {
        result = result + 0;
      } else if (ans == "D") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "[2]. who are you ? " << endl;
      cout << "(A)==> someone" << endl;
      cout << "(B)==>anyane " << endl;
      cout << "(C)=>everyone " << endl;
      cout << "(D)==>no one " << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "D" || ans == "B" || ans == "C") {
        result = result + 0;
      } else if (ans == "A") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "[3]. what is your name? " << endl;
      cout << "(A)==> brandon" << endl;
      cout << "(B)==>brando" << endl;
      cout << "(C)=>brenda " << endl;
      cout << "(D)==>brandi " << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "D" || ans == "A" || ans == "C") {
        result = result + 0;
      } else if (ans == "B") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "[4]. which town are you from " << endl;
      cout << "(A)==> bamenda" << endl;
      cout << "(B)==>deuala" << endl;
      cout << "(C)=>buea" << endl;
      cout << "(D)==>bafusam" << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "D" || ans == "A" || ans == "C") {
        result = result + 0;
      } else if (ans == "B") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "[5]. what is your fathers name" << endl;
      cout << "(A)==> mr john" << endl;
      cout << "(B)==> mr paul" << endl;
      cout << "(C)=>  mr kingsly" << endl;
      cout << "(D)==> mr awa" << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "D" || ans == "A" || ans == "C") {
        result = result + 0;
      } else if (ans == "B") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "________________________________________________________________"
              "_______"
           << endl;
      cout << "YOUR TOTAL MARKS IS ...." << endl;
      cout << "_______________________" << endl;
      cout << "||" << result << "/5    ||" << endl;
      cout << " ---------------------" << endl;
      if (result < 3) {
        cout << "....SORRY YOU FAILED THE QUIZ I WILL ADVICE YOU REPEAT THE "
                "COURSE AGIAN..."
             << endl;
      } else {
        cout << "....CONGRATULATION!  YOU PASS THE QUIZ NOW YOU CAN TAKE THE "
                "NEXT COURSE..."
             << endl;
      }
      cout << "THERE YOU GO===> " << endl;
      cout << "welcome to the ethical hacking class" << endl;
      cout << "________________________________________________________________"
              "________________________________"
           << endl;
      cout << "|TO BE SURE THAT YOU HAVE UNDERSTOOD EVERY THING YOOU READ, YOU "
              "WILL HAVE TO ANSWER A LITTLE MSQ QUIZ"
           << endl;
      cout << "----------------------------------------------------------------"
              "-------------------------------"
           << endl;
      cout << "[1]. what is the mearning of programing " << endl;
      cout << "(A)==> something" << endl;
      cout << "(B)==>anything " << endl;
      cout << "(C)=>everyting " << endl;
      cout << "(D)==>nothing " << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "A" || ans == "B" || ans == "C") {
        result = result + 0;
      } else if (ans == "D") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "[2]. who are you ? " << endl;
      cout << "(A)==> someone" << endl;
      cout << "(B)==>anyane " << endl;
      cout << "(C)=>everyone " << endl;
      cout << "(D)==>no one " << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "D" || ans == "B" || ans == "C") {
        result = result + 0;
      } else if (ans == "A") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "[3]. what is your name? " << endl;
      cout << "(A)==> brandon" << endl;
      cout << "(B)==>brando" << endl;
      cout << "(C)=>brenda " << endl;
      cout << "(D)==>brandi " << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "D" || ans == "A" || ans == "C") {
        result = result + 0;
      } else if (ans == "B") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "[4]. which town are you from " << endl;
      cout << "(A)==> bamenda" << endl;
      cout << "(B)==>deuala" << endl;
      cout << "(C)=>buea" << endl;
      cout << "(D)==>bafusam" << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "D" || ans == "A" || ans == "C") {
        result = result + 0;
      } else if (ans == "B") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "[5]. what is your fathers name" << endl;
      cout << "(A)==> mr john" << endl;
      cout << "(B)==> mr paul" << endl;
      cout << "(C)=>  mr kingsly" << endl;
      cout << "(D)==> mr awa" << endl;
      cout << " ANSWER===>: " << endl;
      cin >> ans;
      if (ans == "D" || ans == "A" || ans == "C") {
        result = result + 0;
      } else if (ans == "B") {
        result = result + 1;
      } else {
        cout << "INVALID INPUT" << endl;
        result = result + 0;
      }
      cout << "________________________________________________________________"
              "_______"
           << endl;
      cout << "YOUR TOTAL MARKS IS ...." << endl;
      cout << "_______________________" << endl;
      cout << "||" << result << "/5    ||" << endl;
      cout << " ---------------------" << endl;
      if (result < 3) {
        cout << "....SORRY YOU FAILED THE QUIZ I WILL ADVICE YOU REPEAT THE "
                "COURSE AGIAN..."
             << endl;
      } else {
        cout << "....CONGRATULATION!  YOU PASS THE QUIZ NOW YOU CAN TAKE THE "
                "NEXT COURSE..."
             << endl;
      }
      if (l == "X") {
        cout << "######  succesful exit  ###########3" << endl;
      } else {
        cout << "INVALID INPUT PLEASE TRY AGAIN" << endl;
      }
    }
  }
}
int main() {
  string x;
  string y;
  string z;
  string B;
  cout << "\\\\\\\\WELCOME USER THIS PROGRAM WILL TAKE YOU A LONG WAY IN "
          "LEARNING MUCH ABOUT TECHNOLOGY///////////"
       << endl;
  cout << "____________________________________________________________________"
          "_____________________________"
       << endl;

  cout << "                      > TO BEGIN PLEASE FILL THE INFORMATION LISTED "
          "BELLOW TO BE ABLE TO >>LOG IN"
       << endl;
  while (x != "BRANDON") {

    cout << "                                     "
            "__________________________________________________    "
         << endl;
    cout << "                                      ||CLICK THE > capsLock "
            "botton < ON YOUR KEY BOARD||     "
         << endl;
    cout << "                                     "
            "---------------------------------------------------      "
         << endl;
    cout << "Enter your name please==>: " << endl;
    getline(cin, x);

    cout << "enter your email please==>: " << endl;
    getline(cin, y);

    cout << "Enter your password=>: " << endl;
    getline(cin, z);
    if (x != "BRANDON" && y == y && z == z) {
      cout << "sorry invalid input please check your work and try agian"
           << endl;
    } else {
      cout << "\\\\\\\\\\\\\\\\\\\\THANKS NOW LET MOVE TO THE NEXT "
              "LEVEL////////////////////////////////"
           << endl;
      cout << "================================================================"
              "======================================================"
           << endl;
    }
    intru(x);
    next();
  }
  return 0;
}
