#!/bin/sh
export OSV_BRIDGE=virbr0
brctl addif $OSV_BRIDGE $1
brctl stp $OSV_BRIDGE off
ip link set dev $1 up
