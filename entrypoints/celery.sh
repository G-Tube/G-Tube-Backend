#!/bin/bash
celery --app config.worker worker --loglevel=${WORKER_LOG_LEVEL:-INFO}
