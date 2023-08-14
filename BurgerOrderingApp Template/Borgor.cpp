#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

struct Burger {
    string size;
    vector<string> toppings;
    int totalPriceInCents;
};

const int SMALL_PRICE_CENTS = 300;
const int MEDIUM_PRICE_CENTS = 550;
const int LARGE_PRICE_CENTS = 725;

const int CHEESE_PRICE_CENTS = 80;
const int SALAD_PRICE_CENTS = 50;
const int BACON_PRICE_CENTS = 100;
const int KETCHUP_PRICE_CENTS = 30;
const int MAYO_PRICE_CENTS = 30;
const int EXTRA_BURGER_PRICE_CENTS = 150;

int creditsInCents = 0;
vector<Burger> recentOrders;

void displayMenu() {
    cout << "------------------------------------" << endl;
    cout << "       Burger Size Menu             " << endl;
    cout << "------------------------------------" << endl;
    cout << "1. Small: $" << static_cast<double>(SMALL_PRICE_CENTS) / 100 << endl;
    cout << "2. Medium: $" << static_cast<double>(MEDIUM_PRICE_CENTS) / 100 << endl;
    cout << "3. Large: $" << static_cast<double>(LARGE_PRICE_CENTS) / 100 << endl;
}

void displayToppingsMenu() {
    cout << "------------------------------------" << endl;
    cout << "        Toppings Menu               " << endl;
    cout << "------------------------------------" << endl;
    cout << "1. Cheese: $" << static_cast<double>(CHEESE_PRICE_CENTS) / 100 << endl;
    cout << "2. Salad: $" << static_cast<double>(SALAD_PRICE_CENTS) / 100 << endl;
    cout << "3. Bacon: $" << static_cast<double>(BACON_PRICE_CENTS) / 100 << endl;
    cout << "4. Ketchup: $" << static_cast<double>(KETCHUP_PRICE_CENTS) / 100 << endl;
    cout << "5. Mayo: $" << static_cast<double>(MAYO_PRICE_CENTS) / 100 << endl;
    cout << "6. Extra Burger: $" << static_cast<double>(EXTRA_BURGER_PRICE_CENTS) / 100 << endl;
}

void addCredits() {
    double amount;
    cout << "Enter credits to add: ";
    cin >> amount;
    creditsInCents += static_cast<int>(amount * 100);
    cout << "Credits added successfully!" << endl;
}

string getBurgerSize() {
    int choice;
    cout << "------------------------------------" << endl;
    cout << "       Burger Size Menu             " << endl;
    cout << "------------------------------------" << endl;
    cout << "Select burger size (1-3):" << endl;
    displayMenu();

    while (true) {
        cin >> choice;
        if (choice >= 1 && choice <= 3) {
            break;
        } else {
            cout << "Invalid input. Please select a valid burger size (1-3):" << endl;
        }
    }

    switch (choice) {
        case 1:
            return "Small";
        case 2:
            return "Medium";
        case 3:
            return "Large";
    }

    return "Invalid Size"; 
}

void selectToppings(Burger& burger) {
    int choice;
    cout << "------------------------------------" << endl;
    cout << "        Toppings Menu               " << endl;
    cout << "------------------------------------" << endl;
    cout << "Select toppings (1-6, 0 to finish):" << endl;
    displayToppingsMenu();

    while (true) {
        cin >> choice;
        if (choice >= 0 && choice <= 6) {
            if (choice == 0) {
                break;
            }

            burger.toppings.push_back(""); 
            switch (choice) {
                case 1:
                    burger.toppings.back() = "Cheese";
                    burger.totalPriceInCents += CHEESE_PRICE_CENTS;
                    break;
                case 2:
                    burger.toppings.back() = "Salad";
                    burger.totalPriceInCents += SALAD_PRICE_CENTS;
                    break;
                case 3:
                    burger.toppings.back() = "Bacon";
                    burger.totalPriceInCents += BACON_PRICE_CENTS;
                    break;
                case 4:
                    burger.toppings.back() = "Ketchup";
                    burger.totalPriceInCents += KETCHUP_PRICE_CENTS;
                    break;
                case 5:
                    burger.toppings.back() = "Mayo";
                    burger.totalPriceInCents += MAYO_PRICE_CENTS;
                    break;
                case 6:
                    burger.toppings.back() = "Extra Burger";
                    burger.totalPriceInCents += EXTRA_BURGER_PRICE_CENTS;
                    break;
            }
        } else {
            cout << "Invalid input. Please select a valid topping (1-6) or 0 to finish:" << endl;
        }
    }
}

void checkout(Burger& burger) {
    if (creditsInCents >= burger.totalPriceInCents) {
        creditsInCents -= burger.totalPriceInCents;
        recentOrders.push_back(burger);
        cout << "Order successful. Remaining credits: $" << fixed << setprecision(2) << static_cast<double>(creditsInCents) / 100 << endl;
    } else {
        cout << "Insufficient credits. Please add more credits." << endl;
    }
}

void viewRecentOrders() {
    cout << "------------------------------------" << endl;
    cout << "        Recent Orders               " << endl;
    cout << "------------------------------------" << endl;
    for (const auto& order : recentOrders) {
        cout << "Burger Size: " << order.size << endl;
        cout << "Toppings: ";
        for (const auto& topping : order.toppings) {
            cout << topping << ", ";
        }
        cout << endl;
        cout << "Total Price: $" << fixed << setprecision(2) << static_cast<double>(order.totalPriceInCents) / 100 << endl;
        cout << "----------------------" << endl;
    }
}

void displayMainMenu() {
    cout << "------------------------------------" << endl;
    cout << "           Main Menu                " << endl;
    cout << "------------------------------------" << endl;
    cout << "Your current credits: $" << fixed << setprecision(2) << static_cast<double>(creditsInCents) / 100 << endl;
    cout << "Please choose an option:" << endl;
    cout << "1. Add Credits" << endl;
    cout << "2. Order Burger" << endl;
    cout << "3. View Recent Orders" << endl;
    cout << "0. Exit" << endl;
}

int main() {
    int choice;
    while (true) {
        displayMainMenu();
        cout << "Enter the number corresponding to your desired action: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                addCredits();
                break;
            }
            case 2: {
                Burger newBurger;
                newBurger.size = getBurgerSize();
                newBurger.totalPriceInCents = 0;

                if (newBurger.size != "Invalid Size") {
                    selectToppings(newBurger);
                    cout << "------------------------------------" << endl;
                    cout << "       Order Summary               " << endl;
                    cout << "------------------------------------" << endl;
                    cout << "Burger Size: " << newBurger.size << endl;
                    cout << "Toppings: ";
                    for (const auto& topping : newBurger.toppings) {
                        cout << topping << ", ";
                    }
                    cout << endl;
                    cout << "Total Price: $" << fixed << setprecision(2) << static_cast<double>(newBurger.totalPriceInCents) / 100 << endl;
                    checkout(newBurger);
                } else {
                    cout << "Invalid input. Please try again." << endl;
                }
                break;
            }
            case 3:
                viewRecentOrders();
                break;
            case 0:
                cout << "Goodbye! Thank you for using our burger ordering application." << endl;
                return 0;
            default:
                cout << "Invalid choice. Please enter a valid option number." << endl;
                break;
        }
    }

    return 0;
}
