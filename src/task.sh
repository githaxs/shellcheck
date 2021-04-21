#!/usr/bin/env bash
set -e
exit_code=0

run_shellcheck() {
    if [[ $1 =~ .*.sh$ ]]; then
        shellcheck $1
        # If any checks fail we want the entire task to fail
        ret=$?
        (( exit_code += $ret ))
    fi
}
task() {
    foreach_changed_file run_shellcheck

    exit $exit_code
}