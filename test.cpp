#define CATCH_CONFIG_MAIN // This provides the main() function
#include <catch2/catch_test_macros.hpp>

TEST_CASE( "Test test", "[test]" ) {
    REQUIRE( true );
}
