#!/bin/bash

celery -A source.config worker -l info
