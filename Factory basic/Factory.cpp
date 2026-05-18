#include <iostream>

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
    virtual Transport* selectVehicle(double distance) = 0;
    virtual ~TransportFactory() {};
};

class TruckTransportationFactory : public TransportFactory {
public:
    Transport* selectVehicle(double distance) override {
        return new Truck(distance);
    }
};

class PlaneTransportationFactory : public TransportFactory {
public:
    Transport* selectVehicle(double distance) override {
        return new Plane(distance);
    }
};

int main() {
    double distance = 100;
    TransportFactory* trucktranspor = new TruckTransportationFactory;
    if (trucktranspor->selectVehicle(distance)) {
        std::cout << "cost:" << trucktranspor->selectVehicle(distance)->calculateCost() << std::endl;
        std::cout << "time:" << trucktranspor->selectVehicle(distance)->getDeliveryTime() << std::endl;
        delete trucktranspor->selectVehicle(distance);
    }
    return 0;
}

#include <iostream>

#if 0

class AbstrctSmile {
public:
    virtual void transform() = 0;
    virtual void ability() = 0;
    virtual ~AbstrctSmile() {};
};

class GoatSmile : public AbstrctSmile {
public:
    void transform() override {
        std::cout << "transformed into goat" << std::endl;
    }
    void ability() override {
        std::cout << "goat horn" << std::endl;
    }
};

class LionSmile : public AbstrctSmile {
public:
    void transform() override {
        std::cout << "transformed into lion" << std::endl;
    }
    void ability() override {
        std::cout << "fire ball" << std::endl;
    }
};

class BatSmile : public AbstrctSmile {
public:
    void transform() override {
        std::cout << "transformed into bat" << std::endl;
    }
    void ability() override {
        std::cout << "ultrasound" << std::endl;
    }
};

class NonSmile : public AbstrctSmile {
public:
    void transform() override {
        std::cout << "human" << std::endl;
    }
    void ability() override {
        std::cout << "laugh..." << std::endl;
    }
};

enum class SmileType {
    Goat = 1,
    Lion = 2,
    Bat = 3,
};

class SmileFactory {
public:
    AbstrctSmile* CreateSmile(SmileType type) {
        switch (type) {
            case(SmileType::Goat) : {
                return new GoatSmile;
            }
            case(SmileType::Lion) : {
                return new LionSmile;
            }
            case(SmileType::Bat) : {
                return new BatSmile;
            }
            default: {
                return new NonSmile;
            }
        }
    }
};

int main() {
    SmileFactory* sf = new SmileFactory;
    AbstrctSmile* p1 = sf->CreateSmile(SmileType::Lion);
    p1->transform();
    p1->ability();
    delete p1;
    delete sf;
    return 0;
}

#endif

#if 1

class AbstrctSmile {
public:
    virtual void transform() = 0;
    virtual void ability() = 0;
    virtual ~AbstrctSmile() {};
};

class GoatSmile : public AbstrctSmile {
public:
    void transform() override {
        std::cout << "transformed into goat" << std::endl;
    }
    void ability() override {
        std::cout << "goat horn" << std::endl;
    }
};

class LionSmile : public AbstrctSmile {
public:
    void transform() override {
        std::cout << "transformed into lion" << std::endl;
    }
    void ability() override {
        std::cout << "fire ball" << std::endl;
    }
};

class BatSmile : public AbstrctSmile {
public:
    void transform() override {
        std::cout << "transformed into bat" << std::endl;
    }
    void ability() override {
        std::cout << "ultrasound" << std::endl;
    }
};

class AbstractFactory {
public:
    virtual AbstrctSmile* CreateSmile() = 0;
    virtual ~AbstractFactory() {}
};

class GoatFactory : public AbstractFactory {
public:
    virtual AbstrctSmile* CreateSmile() override {
        return new GoatSmile;
    }
};

class LionFactory : public AbstractFactory {
public:
    virtual AbstrctSmile* CreateSmile() override {
        return new LionSmile;
    }
};

class BatFactory : public AbstractFactory {
public:
    virtual AbstrctSmile* CreateSmile() {
        return new BatSmile;
    }
};

int main() {
    AbstractFactory* goat = new GoatFactory;
    AbstrctSmile* p1 = goat->CreateSmile();
    p1->transform();
    p1->ability();
    delete p1;
    delete goat;
    return 0;
}

#endif