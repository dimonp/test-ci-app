#define CATCH_CONFIG_MAIN // This provides the main() function
#include <catch2/catch_test_macros.hpp>

std::string foo_work(const std::string& a, const std::string& b, int n);

TEST_CASE( "Test test", "[test]" )
{
    auto result = foo_work("aa", "bb", 1);
    REQUIRE(result == "aa_bb");
}
