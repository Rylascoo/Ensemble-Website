#!/usr/bin/env python3
"""Canonical Stage 6M entrypoint; physical/statics hardening is mandatory."""
from stage6m_maquette_hardening import (
    FORMAT,
    FROZEN_INSTRUMENTATION,
    FROZEN_PROJECTION,
    FROZEN_SANITIZATION,
    ValidationError,
    deterministic_bytes,
    main,
    validate_manifest,
)

if __name__ == "__main__":
    raise SystemExit(main())
