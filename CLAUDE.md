# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **template repository** for creating new Celeste domain packages. It provides a standardized foundation that follows all Celeste architecture patterns and can be customized to create new AI capabilities (e.g., image generation, text-to-speech, document processing).

## Template Customization Process

### Core Replacements Required
When using this template, perform these global find & replace operations:
- `celeste-domain-template` → `celeste-your-domain-name`
- `celeste_domain_template` → `celeste_your_domain_name`
- `create_domain_template_client` → `create_your_domain_client`
- `DomainTemplate` → `YourDomain`

### Architecture Components

#### mapping.py
- **CAPABILITY**: Links to celeste-core capability enum (may need to add new capability if none exists)
- **PROVIDER_MAPPING**: Maps Provider enums to implementation classes using tuple format `(module_path, class_name)`
- Single source of truth for domain configuration

#### Factory Function (__init__.py)
- Dynamic provider resolution from PROVIDER_MAPPING
- Environment validation via celeste-core settings
- Lazy loading of provider implementation classes
- Must be renamed to match domain (e.g., `create_image_generation_client`)

#### Provider Implementation Pattern
- Inherit from domain-specific base class from celeste-core (not generic BaseClient)
- All methods must be async
- Return domain-specific artifact types (not generic responses)
- Use celeste-core settings for API keys, never custom auth logic
- Follow naming: `{Provider}{Domain}Client` (e.g., `GoogleImageGenerationClient`)

#### Example App (example.py)
- Streamlit demo using the template
- Model catalog integration for dynamic provider/model discovery
- Domain-specific UI elements and configuration
- Efficient client creation pattern
- Must be customized for domain's specific input/output types

## Development Commands

```bash
# Install in editable mode for development
uv sync

# Run code quality checks
ruff check --fix         # Lint and auto-fix
ruff format             # Format code
ruff check              # Lint only

# Run the example Streamlit app
streamlit run example.py

# Install pre-commit hooks
pre-commit install
```

## Integration Requirements

### Before Using Template
1. **Add capability** to celeste-core if new capability needed
2. **Add models** to celeste-core model catalog with correct capability flags
3. **Create domain-specific base class** in celeste-core if needed
4. **Define artifact types** in celeste-core for domain outputs

### Template Setup Checklist
- [ ] Replace all placeholder strings throughout files
- [ ] Update CAPABILITY in mapping.py to correct enum
- [ ] Add provider mappings to PROVIDER_MAPPING
- [ ] Update dependencies in pyproject.toml with provider SDKs
- [ ] Implement provider classes with async methods
- [ ] Customize example.py for domain-specific UI
- [ ] Update factory function name and base class import
- [ ] Test with `streamlit run example.py`

## Key Architectural Patterns

### Provider Resolution
Uses dynamic import pattern: `import_module(f"celeste_domain_template{module_path}")` to lazily load provider implementations based on mapping configuration.

### Settings Integration
Always use `settings.validate_for_provider()` and `settings.{provider}.api_key` from celeste-core. Never implement custom environment variable handling.

### Model Catalog Integration
Example app uses `list_models(capability=your_capability)` to dynamically discover available models, then filters by provider for UI selection.

### Error Handling
Provider validation happens at factory level. Individual provider implementations should focus on API-specific error handling and transformation to domain artifacts.

## File Structure
```
src/celeste_domain_template/
├── __init__.py              # Factory function with dynamic provider resolution
├── mapping.py               # Capability and provider-to-class mapping
└── providers/
    ├── __init__.py
    └── google_template.py   # Example provider implementation template
```

## Dependencies Management
- Use `uv add` for adding new dependencies
- Provider SDKs should be added to `dependencies` array in pyproject.toml
- Development tools go in `[dependency-groups].dev`
- celeste-core is sourced from git repository via `[tool.uv.sources]`

## Important Notes
- This is a **template repository** - it's not meant to be used directly
- All placeholder values and TODO comments must be replaced during customization
- The template includes comprehensive guidance in README.md for domain creation workflow
- Each domain should focus on a single capability for clarity and maintainability
