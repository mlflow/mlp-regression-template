#!/usr/bin/env bash

set -ex

function retry-with-backoff() {
    for BACKOFF in 0 1 2 4 8 16 32 64; do
        sleep $BACKOFF
        if "$@"; then
            return 0
        fi
    done
    return 1
}

# Cleanup apt repository to make room for tests.
sudo apt clean
df -h

python --version
pip install --upgrade pip wheel
pip --version

pip install -e . --upgrade
export MLFLOW_PIPELINE_EXAMPLE=$(pwd)

req_files=""
# Install Python test dependencies only if we're running Python tests
if [[ "$INSTALL_SKLEARN_PIPELINE_DEPS" == "true" ]]; then
  # When downloading large packages from PyPI, the connection is sometimes aborted by the
  # remote host. See https://github.com/pypa/pip/issues/8510.
  # As a workaround, we retry installation of large packages.
  req_files+=" -r requirements.txt"
fi

if [[ ! -z $req_files ]]; then
  retry-with-backoff pip install $req_files
fi

# Print current environment info
python .github/workflows/scripts/show_package_release_dates.py
which mlflow
echo $MLFLOW_PIPELINE_EXAMPLE

# Print mlflow version
mlflow --version

# Turn off trace output & exit-on-errors
set +ex
