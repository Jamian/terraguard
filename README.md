# Terraguard

[![Build Status](https://api.travis-ci.com/Jamian/terraguard.svg?branch=master)](https://api.travis-ci.com/Jamian/terraguard.svg?branch=master)

Terraguard is a simple python CLI tool for quickly and easily safe guarding your Terraform plans against a set of yaml defined rulesets.
___
:warning: Terraguard is currently under active developing and is still very much in a beta if not alpha state. Feel free to dive in and help get the project up to speed with more Terraform providers.
___

### Table of Contents  
[Getting Started](#getting-started)  
[Development](#development)  
&nbsp;&nbsp;&nbsp;&nbsp;[Manual Testing](#testing-manually)  
&nbsp;&nbsp;&nbsp;&nbsp;[Unit Testing](#unit-testing)
 
# Getting Started

1. Run `pip install terraguard`
2. Create a `terraguard.yaml` file in the root of the Terraform project that you want to test (no support for multiple projects just yet!). A simple example, that just asserts that all instances have a `Name` tag, might look something like:
```
rulesets:
  aws_instance:
    - expression: tags
      must_contain:
        - Name
```
3. Run `terraguard`
  * This will run a `terraform plan` for you and output the contents to a file which will then be migrated to JSON and loaded into the tool.
  * Once the JSON is loaded into memory, the resources will be validated against your rulesets.
  * You'll hopefully see no errors! :smile: 

# Development

Run through the following steps (it won't take long!) to get a development environment set up.
1. Clone the repo to your local machine and cd into the root of the project
2. Run `virtualenv -p python3 venv`
3. Run `source venv/bin/activate`
4. Run `pip install -r dev-requirements.txt`
5. Run `pip install -e .`

## Testing Manually
During development, you'll want to have a test Terraform project that you can work with. It doesn't have to be (and ideally isn't) any existing infrastructure, just a `main.tf` and a single resource will do.
1. In the root of the TF project dir, create a `terraguard.yaml` and start defining your rulesets.
2. When you want to test, run `terraguard` and see how it goes!

## Unit Testing
Please write at least some basic unit tests for new functionality. Tests are found under `/test` and can be ran by running `pytest` in the project root.

