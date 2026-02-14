#include <string>
#include <fmt/core.h>

std::string foo_work(const std::string& a, const std::string& b, int n) {
    std::string aa;
    std::string bb;
    for(int i = 0 ; i < n ; ++i) {
        aa += a;
        bb += b;
    }
    return fmt::format("{}_{}", aa, bb);
}
