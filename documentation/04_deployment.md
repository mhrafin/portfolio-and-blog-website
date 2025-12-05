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
    -   Syncs `output/` to `s3://$(S3BUCKET)/`.
    -   Syncs `content/` to `s3://$(OBSIDIANBUCKET)/content/` (for backup/Obsidian sync).

    *Note: The command uses `--delete`, so files removed locally will be removed from the bucket.*
