#include <fmt/core.h> 
#include <spdlog/spdlog.h>

int main() {
    std::string s = "Hello, world!";
    spdlog::info(fmt::format("{}", "Hello, world!", s));
    return 0;
}
