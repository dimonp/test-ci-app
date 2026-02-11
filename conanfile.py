from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class MyPkg(ConanFile):
    name = "my_package"
    version = "1.0"
    #generators = "CMakeDeps", "CMakeToolchain"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*"

    requires = [
        "fmt/11.2.0",
        "spdlog/1.15.3",
        "cli11/2.6.0",
        "catch2/3.12.0"
    ]

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.user_presets_path = 'ConanPresets.json'
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
