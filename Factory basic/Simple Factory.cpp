#include <iostream>
#include <string>

class Transport {
public:
    virtual double calculateCost() = 0;
    virtual double getDeliveryTime() = 0;
    virtual ~Transport() {}
};

class Truck : public Transport {
public:
    Truck(int x) : distance(x) {}
    double calculateCost() override {
        return distance / speed * cost_coeff;
    }
    double getDeliveryTime() override {
        return distance / speed;
    }

private:
    int cost_coeff = 10;
    int speed = 50;
    double distance;
};

class Plane : public Transport {
public:
    Plane(int x) : distance(x) {}
    double calculateCost() override {
        return distance / speed * cost_coeff;
    }
    double getDeliveryTime() override {
        return distance / speed;
    }

private:
    int cost_coeff = 50;
    int speed = 500;
    double distance;
};

class TransportFactory {
public:
    static Transport* selectVehicle(std::string vehicle, double distance) {
        if (vehicle == "Truck") return new Truck(distance);
        else if (vehicle == "Plane") return new Plane(distance);
        return nullptr;
    }
};

int main() {
    std::string vehicle = "Plane";
    double distance = 100;
    Transport* transport = TransportFactory::selectVehicle(vehicle, distance);
    if (transport != nullptr) {
        std::cout << "cost:" << transport->calculateCost() << std::endl;
        std::cout << "time:" << transport->getDeliveryTime() << std::endl;
        delete transport;
    }
    return 0;
}