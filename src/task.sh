#!/usr/bin/env bash
set -e

run() {
    if [[ $1 =~ .*.sh$ ]]; then
        shellcheck $1
    fi
}

task() {
    echo "Running Task"

    foreach_changed_file run
}
