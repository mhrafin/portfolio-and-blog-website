# Setup and Installation

Follow these steps to set up the project locally.

## Prerequisites

Ensure you have the following installed on your system:

1.  **Python 3.x**: [Download Python](https://www.python.org/downloads/)
2.  **Node.js & npm**: [Download Node.js](https://nodejs.org/)
3.  **Pipenv**: Install via pip:
    ```bash
    pip install pipenv
    ```
4.  **AWS CLI** (Optional, for deployment): [Install AWS CLI](https://aws.amazon.com/cli/)

## Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd portfolio-and-blog-website
    ```

2.  **Install Python Dependencies**:
    Initialize the virtual environment and install packages from `Pipfile`:
    ```bash
    pipenv install
    ```
    
    This installs the following packages:
    - `pelican[markdown]` - Static site generator with Markdown support
    - `beautifulsoup4` - HTML parsing library
    - `rclone` - Cloud storage sync tool
    - `s3cmd` - S3 command-line tool
    - `pelican-sitemap` - Sitemap plugin
    - `pelican-readtime` - Reading time estimation plugin
    - `pymdown-extensions` - Additional Markdown extensions

3.  **Install Node.js Dependencies**:
    Install TailwindCSS and other frontend tools:
    ```bash
    npm install
    ```
    
    This installs:
    - `@tailwindcss/cli@^4.1.13` - TailwindCSS v4 CLI
    - `tailwindcss@^4.1.13` - TailwindCSS core
    - `flowbite@^3.1.2` - UI component library

4.  **Environment Variables**:
    Create a `.env` file in the root directory if needed (referenced in `Makefile`).
    ```bash
    touch .env
    ```
    *Note: Check `Makefile` for variables that can be overridden via `.env` or command line.*

## Verification

To verify the installation, try building the site:

```bash
make html
```

If successful, the `output/` directory will be populated with the generated site.
