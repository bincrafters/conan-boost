## This repository holds a conan recipe for Boost.

[Conan.io](https://conan.io) package for [Boost](https://github.com/Boostorg/boost) project

This is a special "meta-package" which includes all other bincrafters boost packages as conan dependencies. By adding this package to your Conan project, you effectively get "All of Boost" libraries with one `requires` statement.  Doing so is perpendicular to the primary purpose of the bincrafters packages, which is to provide a new modular option for including Boost libraries in Conan projects. However, there are some use cases for creating this metapackage, thus we provide the option for completeness so that others don't have to create it themselves. 

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/bincrafters/public-conan/Boost%3Abincrafters).

## For Users: Use this package

### Basic setup

    $ conan install Boost/1.64.0@bincrafters/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    Boost/1.64.0@bincrafters/stable

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..
	
Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git. 

## For Packagers: Publish this Package

The example below shows the commands used to publish to bincrafters conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly. 

## Build  

This is a header only library, so nothing needs to be built.

## Package 

    $ conan create bincrafters/stable
	
## Add Remote

	$ conan remote add bincrafters "https://api.bintray.com/conan/bincrafters/public-conan"

## Upload

    $ conan upload Boost/1.64.0@bincrafters/stable --all -r bincrafters

### License
[Boost](www.boost.org/LICENSE_1_0.txt)
