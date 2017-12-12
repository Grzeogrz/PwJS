#!/bin/bash

l=$(cat agh.log | grep -o AGH | wc -w)
echo $l
