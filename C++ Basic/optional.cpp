#include <iostream>
#include <optional>
#include <string>
#include <vector>

struct PartyInfo {
    std::string name;
    std::string time;
    std::string site;
};

class PartyInfoQuery {
public:
    PartyInfoQuery() {
        party_info_.emplace_back(PartyInfo{"linhaoran", "2014-03", "1"});
    }
    std::optional<PartyInfo> query(std::string name) {
        for (auto info : party_info_) {
            if (name == info.name) return info;
        }
        return std::nullopt;
    }
private:
    std::vector<PartyInfo> party_info_;
};

int main() {
    PartyInfoQuery* party_info_query = new PartyInfoQuery;
    std::string name;
    std::cout << "Input your name:" << std::endl;
    std::cin >> name;
    auto query1 = party_info_query->query(name);
    if (query1.has_value()) {
        std::cout << "time:" << query1->time << "\n" << "site:" << query1->site << std::endl;
    } else {
        std::cout << "Not exist" << std::endl;
    }
    delete party_info_query;
    return 0;
}