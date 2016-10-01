#!/usr/bin/env bash

g++ hello_world.cpp -o hello
./hello  > output

DIFF=$(diff output test)
if [ "$DIFF" != "" ] 
then
	echo "Test Failed. Expected output >>Hello World!<<, got output >>"$(cat output)"<<"
fi

