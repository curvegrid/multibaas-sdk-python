#!/bin/bash -e
# Copyright (c) 2022 Curvegrid Inc.

# Generate the Python Multibaas SDK
cd "$(dirname "$0")"

# Set the openapi-generator version
if [[ -n "${OPENAPI_GENERATOR_VERSION}" ]]; then
    npx @openapitools/openapi-generator-cli version-manager set ${OPENAPI_GENERATOR_VERSION}
fi

# If a package version is given as an argument, set it
VERSION="$1"
if [[ "${VERSION}" =~ ^[0-9]+\.[0-9]+\.[0-9]+(-.+)?$ ]]; then
    perl -pi -e "s/packageVersion: [0-9]+\.[0-9]+\.[0-9]+(-.+)?/packageVersion: ${VERSION}/g" openapi-generator.yaml
fi

# Generate the SDK
npx @openapitools/openapi-generator-cli batch \
    --clean \
    openapi-generator.yaml

# Patch setup.py to include keywords, description and README
python3 patch_setup.py
