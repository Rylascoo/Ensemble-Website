#!/usr/bin/env python3
"""Canonical Stage 6M entrypoint; hardening and physical-union rendering are mandatory."""
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
from stage6m_maquette_union_renderer import apply_union_renderer

apply_union_renderer()

if __name__ == "__main__":
    raise SystemExit(main())
