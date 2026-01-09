# Deployment

The site is deployed to AWS S3.

## Configuration

Deployment settings are primarily handled in the `Makefile`.

### Makefile Variables
The following variables in `Makefile` control deployment:
-   `S3BUCKET`: The name of the S3 bucket hosting the static site.
-   `OBSIDIANBUCKET`: The S3 bucket used for syncing Obsidian content.
-   `AWSPROFILE`: The AWS CLI profile to use for credentials.

You can override these in your `.env` file or environment:
```bash
export S3BUCKET=my-website-bucket
export AWSPROFILE=my-profile
```

## Deploying

To deploy the site to production:

1.  **Build the Site**:
    ```bash
    make html
    ```
    This generates the site in `output/` using `pelicanconf.py` and builds the CSS.

2.  **Sync to S3**:
    ```bash
    make sync-to-aws
    ```
    This command:
    -   Syncs `output/` to S3 using `s3cmd` with MD5 checksum verification.
    -   Explicitly sets MIME type for CSS files to ensure proper delivery.
    -   Syncs `content/` to `s3://$(OBSIDIANBUCKET)/content/` (for backup/Obsidian sync).

    *Note: The command uses `--delete-removed`, so files removed locally will be removed from the bucket.*

### Individual Sync Commands

**Sync only output to production:**
```bash
make sync-output
```

**Sync only content to backup:**
```bash
make sync-content
```

**Sync content from S3 to local:**
```bash
make sync-content-from-aws
```
