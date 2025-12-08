#!/usr/bin/env bash
# Exit on error
set -o errexit

# 1. Requirements Install karo
pip install -r requirements.txt

# 2. Static Files Collect karo (CSS, Images)
python manage.py collectstatic --no-input

# 3. Database Migrate karo
python manage.py migrate