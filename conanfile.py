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

    options = {
        "build_subfolder": ["ANY"]
    }
    default_options = {
        "build_subfolder": ""
    }

    requires = [
        "fmt/11.2.0",
        "spdlog/1.15.3",
        "cli11/2.6.0",
        "catch2/3.12.0"
    ]

    def layout(self):
        if not self.options.build_subfolder:
            self.folders.build = f"build/{self.settings.build_type}"
            self.folders.generators = f"build/{self.settings.build_type}/conan"
        else:
            self.folders.build = f"build/{self.options.build_subfolder}"
            self.folders.generators = f"build/{self.options.build_subfolder}/conan"

        self.folders.source = "."

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
