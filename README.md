# Portfolio and Blog Website

This project is a static website generated using **Pelican**, designed to serve as a personal portfolio and blog. It features a custom theme built with **TailwindCSS** and is configured for content synchronization with Obsidian via AWS S3.

## Tech Stack

-   **Static Site Generator**: [Pelican](https://getpelican.com/) (Python)
-   **Styling**: [TailwindCSS](https://tailwindcss.com/) & [Flowbite](https://flowbite.com/)
-   **Build System**: GNU Make
-   **Dependency Management**: Pipenv (Python), npm (Node.js)

## Setup

1.  **Install Python Dependencies**:
    ```bash
    pipenv install
    ```

2.  **Install Node.js Dependencies** (for TailwindCSS):
    ```bash
    npm install
    ```

## Usage

This project uses a `Makefile` to automate common tasks.

-   **Start Development Server** (Auto-regenerates on change):
    ```bash
    make devserver
    ```

-   **Build Website**:
    ```bash
    make html
    ```

-   **Clean Output**:
    ```bash
    make clean
    ```

-   **Sync to AWS** (Requires AWS CLI configuration):
    ```bash
    make sync-to-aws
    ```

## Documentation

For more detailed information, please refer to the [documentation](./documentation/) directory:

-   [Project Overview](./documentation/01_project_overview.md)
-   [Setup and Installation](./documentation/02_setup_and_installation.md)
-   [Usage Guide](./documentation/03_usage_guide.md)
