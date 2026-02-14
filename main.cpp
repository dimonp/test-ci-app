#include <spdlog/spdlog.h>

std::string foo_work(const std::string& a, const std::string& b, int n);

int main() {
    std::string s = "Hello, world!";
    spdlog::info(foo_work("Hello, world!", s, 5));
    return 0;
}
