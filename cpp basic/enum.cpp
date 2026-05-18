#include <iostream>

enum class state {
    Stand,
    Run,
    Jump,
    Die,
};

void update(state s1) {
    switch (s1) {
        case(state::Stand): {
            std::cout << "The role is standing..." << std::endl;
            break;
        }
        case(state::Run): {
            std::cout << "The role is running..." << std::endl;
            break;
        }
        case(state::Jump): {
            std::cout << "The role is jumping..." << std::endl;
            break;
        }
        case(state::Die): {
            std::cout << "Game over." << std::endl;
            break;
        }
        default: {}
    }
}

int main() {
    state s1;
    s1 = state::Stand;
    update(s1);
    s1 = state::Run;
    update(s1);
    s1 = state::Die;
    update(s1);
    return 0;
}