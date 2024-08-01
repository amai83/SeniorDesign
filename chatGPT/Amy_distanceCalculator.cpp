#include <iostream>
#include <string>
#include <cmath>
#include <iomanip>
using namespace std;
int main()
{
    // declaring variables
    double x1, y1, x2, y2;
    double slope, yInt, manDist, eucDist;
    char option;
    // menu display
    cout << "***************************************" << endl;
    cout << "* Welcome to the Distance Calculator *" << endl;
    cout << "***************************************" << endl;
    cout << "Slope - (s/S)" << endl;
    cout << "Manhattan Distance - (m/M)" << endl;
    cout << "Euclidean Distance - (e/E)" << endl;
    cout << "Quit - (q/Q)" << endl;
    // user selects which calculation they want
    cout << "Enter an Option:" << endl;
    cin >> option;
    // sets outputs to 3 decimals
    cout << fixed << setprecision(3);
    // the following section takes in and error checks user input for slope
    switch (option)
    {
    case 's':
    case 'S':
        cout << "Enter a x1 value:" << endl;
        cin >> x1;
        if (x1 > 100)
        {
            cout << "Error: invalid x value, max is 100" << endl;
            return 0;
        }
        cout << "Enter a y1 value:" << endl;
        cin >> y1;
        if (y1 > 150)
        {
            cout << "Error: invalid y value, max is 150" << endl;
            return 0;
        }
        cout << "Enter a x2 value:" << endl;
        cin >> x2;
        if (x2 > 100)
        {
            cout << "Error: invalid x value, max is 100" << endl;
            return 0;
        }
        cout << "Enter a y2 value:" << endl;
        cin >> y2;
        if (y2 > 150)
        {
            cout << "Error: invalid y value, max is 150" << endl;
            return 0;
        }
        if (!cin)
        {
            cout << "Error: invalid input" << endl;
            return 0;
        }
        slope = (y2 - y1) / (x2 - x1);
        yInt = y1 - (slope * x1);
        cout << "Slope: " << slope << endl;
        cout << "Y-interecpt: " << yInt << endl;
        break;
    // the following section takes in and error checks user input for manDist
    case 'm':
    case 'M':
        cout << "Enter a x1 value:" << endl;
        cin >> x1;
        if (x1 > 100)
        {
            cout << "Error: invalid x value, max is 100" << endl;
            return 0;
        }
        cout << "Enter a y1 value:" << endl;
        cin >> y1;
        if (y1 > 150)
        {
            cout << "Error: invalid y value, max is 150" << endl;
            return 0;
        }
        cout << "Enter a x2 value:" << endl;
        cin >> x2;
        if (x2 > 100)
        {
            cout << "Error: invalid x value, max is 100" << endl;
            return 0;
        }
        cout << "Enter a y2 value:" << endl;
        cin >> y2;
        if (y2 > 150)
        {
            cout << "Error: invalid y value, max is 150" << endl;
            return 0;
        }
        if (!cin)
        {
            cout << "Error: invalid input" << endl;
            return 0;
        }
        manDist = abs(x2 - x1) + abs(y2 - y1);
        cout << "Manhattan Distance: " << manDist << endl;
        break;
    // the following section takes in and error checks user input for eucDist
    case 'e':
    case 'E':
        cout << "Enter a x1 value:" << endl;
        cin >> x1;
        if (x1 > 100)
        {
            cout << "Error: invalid x value, max is 100" << endl;
            return 0;
        }
        cout << "Enter a y1 value:" << endl;
        cin >> y1;
        if (y1 > 150)
        {
            cout << "Error: invalid y value, max is 150" << endl;
            return 0;
        }
        cout << "Enter a x2 value:" << endl;
        cin >> x2;
        if (x2 > 100)
        {
            cout << "Error: invalid x value, max is 100" << endl;
            return 0;
        }
        cout << "Enter a y2 value:" << endl;
        cin >> y2;
        if (y2 > 150)
        {
            cout << "Error: invalid y value, max is 150" << endl;
            return 0;
        }
        if (!cin)
        {
            cout << "Error: invalid input" << endl;
            return 0;
        }
        eucDist = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
        cout << "Euclidean Distance: " << eucDist << endl;
        break;
    // The following section is the output if quit is selected
    case 'q':
    case 'Q':
        cout << "Thank you for using the Distance Calculator" << endl;
        break;
    // The following section is if the user inputs something invalid
    default:
        cout << "Error: Invalid selection" << endl;
    }
    return 0;
}