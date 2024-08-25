# LeetCode Algorithms Project

This project contains a collection of algorithms to solve various LeetCode problems. The codebase is maintained with high standards of code quality, and static analysis tools are used to ensure the code adheres to these standards.

## Prerequisites

- Python 3.9 or higher
- Docker (if you want to run the analysis in a Docker container)

## Setup

### Virtual Environment

1. **Create a virtual environment**:
   ```sh
   python -m venv .venv
   ```

2. **Activate the virtual environment**:

+ On macOS and Linux:
    ```sh
    source .venv/bin/activate
    ```

+ On Windows:
    ```batch
    .venv\Scripts\activate
    ```

3. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

## Docker

1. **Build the Docker image:**

   ```sh
   docker build -t static-analysis .
   ```

## Usage

## Running Static Analysis

**To run the static analysis script, use the following command:**

+ **With Virtual Environment:**
   ```sh
   ./static_analysis.sh
   ```

+ **With Docker:**
   + Go inside the container
   ```sh
   docker run --rm -it -v $(pwd)/algorithms:/usr/src/app/algorithms static-analysis bash
   ```
   + run:
   ```sh
   ./static_analysis.sh
   ```

## Script Details

The static_analysis.sh script performs the following actions:

+ Checks if any errors were found during the static analysis.
+ Outputs the results of the static analysis.

## Contributing

Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License.
