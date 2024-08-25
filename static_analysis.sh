#!/bin/bash

error_count=0
declare -a error_list

# Run black in check mode
echo "Running black..."
black --check algorithms/ 2>&1
black_exit_code=$?
if [ $black_exit_code -ne 0 ]; then
  ((error_count++))
  error_list+=("black")
fi

# Run mypy for type checking
# Note: mypy is disabled for now as it is not yet fully supported by the codebase
# echo "Running mypy..."
# mypy --config-file pyproject.toml algorithms/ 2>&1
# mypy_exit_code=$?
# if [ $mypy_exit_code -ne 0 ]; then
#   ((error_count++))
#   error_list+=("mypy")
# fi

# Run pylint for linting
# Note: pylint is disabled for now as it is not yet fully supported by the codebase
# echo "Running pylint..."
# pylint algorithms/ 2>&1
# pylint_exit_code=$?
# if [ $pylint_exit_code -ne 0 ]; then
#   ((error_count++))
#   error_list+=("pylint")
# fi

# Run isort in check mode
echo "Running isort in check mode..."
isort --check-only algorithms/ 2>&1
isort_exit_code=$?
if [ $isort_exit_code -ne 0 ]; then
  ((error_count++))
  error_list+=("isort")
fi

# Define color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Define a separator line
SEPARATOR="========================================"

# Check if any errors were found
if [ $error_count -ne 0 ]; then
  echo -e "${RED}${SEPARATOR}"
  echo -e "Static analysis found errors."
  echo -e "Errors found by:"
  for tool in "${error_list[@]}"; do
    echo -e "- $tool"
  done
  echo -e "${SEPARATOR}${NC}"
else
  echo -e "${GREEN}${SEPARATOR}"
  echo -e "All static analysis checks passed successfully."
  echo -e "${SEPARATOR}${NC}"
fi
