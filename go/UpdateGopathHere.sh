#!/bin/bash
# Change do directory you want to work with first..

function ugph () {
    export GOPATH=`pwd`
    export GOBIN=`pwd`/bin
    echo $GOPATH
    echo $GOBIN
}
