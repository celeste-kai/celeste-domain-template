<div align="center">

# 🚀 Celeste Domain Template

### A Standardized Template for Creating New Celeste Domains - Ready-to-Customize Foundation

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![Template](https://img.shields.io/badge/Template-Domain_Foundation-orange?style=for-the-badge&logo=templating&logoColor=white)](#-template-structure)
[![Status](https://img.shields.io/badge/Status-Ready_to_Use-brightgreen?style=for-the-badge)](#-quick-start)

[![Demo](https://img.shields.io/badge/🚀_Try_Example-Streamlit-FF4B4B?style=for-the-badge)](example.py)
[![Documentation](https://img.shields.io/badge/📚_Reference-new_domain.md-blue?style=for-the-badge)](#-reference)

</div>

---

## 🎯 Why Use This Template?

<div align="center">
  <table>
    <tr>
      <td align="center">📐<br><b>Best Practices</b><br>Follows all Celeste architecture patterns</td>
      <td align="center">⚡<br><b>Quick Setup</b><br>Domain ready in minutes</td>
      <td align="center">🔧<br><b>Pre-configured</b><br>Factory, mapping, and examples included</td>
      <td align="center">📋<br><b>Complete Guide</b><br>Step-by-step setup checklist</td>
    </tr>
  </table>
</div>

This template provides a complete, ready-to-customize foundation for creating new Celeste domains. It includes all the necessary files, patterns, and conventions used across the Celeste ecosystem, ensuring consistency and reducing setup time from hours to minutes.

## 🚀 Quick Start

### 1. Copy and Rename Template
```bash
cp -r celeste-domain-template celeste-your-domain-name
cd celeste-your-domain-name
```

### 2. Global Find & Replace
Replace these placeholders throughout all files:
- `celeste-domain-template` → `celeste-your-domain-name`
- `celeste_domain_template` → `celeste_your_domain_name`
- `create_domain_template_client` → `create_your_domain_client`
- `DomainTemplate` → `YourDomain`

### 3. Configure Your Domain

#### A. Add Capability (if new)
```python
# In celeste-core/src/celeste_core/enums/capability.py
YOUR_CAPABILITY = 1 << 14  # Use next available bit
```

#### B. Update mapping.py
```python
CAPABILITY: Capability = Capability.YOUR_CAPABILITY
PROVIDER_MAPPING: dict[Provider, tuple[str, str]] = {
    Provider.GOOGLE: (".providers.google", "GoogleYourDomainClient"),
    # Add your providers...
}
```

#### C. Add Models to Catalog
```python
# In celeste-core/src/celeste_core/models/catalog.py
Model(
    id="your-model-id",
    provider=Provider.GOOGLE,
    capabilities=Capability.YOUR_CAPABILITY,
    display_name="Your Model Name",
),
```

#### D. Update Dependencies
```toml
# In pyproject.toml
dependencies = [
    "celeste-core>=0.1.0",
    "your-provider-sdk>=1.0.0",  # Add provider SDKs
]
```

### 4. Implement Provider
```python
# In src/celeste_your_domain/providers/google.py
from your_provider_sdk import Client
from celeste_core import YourArtifactType
from celeste_core.base.your_base import BaseYourDomain

class GoogleYourDomainClient(BaseYourDomain):
    def __init__(self, model: str = "default-model", **kwargs):
        super().__init__(**kwargs)
        self.client = Client(api_key=settings.google.api_key)
        self.model_name = model

    async def your_main_method(self, input_data: str, **kwargs) -> YourArtifactType:
        # Implement your provider's API call
        response = await self.client.generate(
            model=self.model_name,
            input=input_data,
            **kwargs
        )
        return YourArtifactType(data=response.data)
```

### 5. Update Factory & Base Class
```python
# In src/celeste_your_domain/__init__.py
from celeste_core.base.your_base import BaseYourDomain

def create_your_domain_client(provider: Union[Provider, str], **kwargs) -> BaseYourDomain:
    # Factory implementation
```

### 6. Customize Example
Update `example.py`:
- Replace capability enum
- Add domain-specific UI elements
- Update generation call
- Add appropriate result display (audio player, image display, etc.)

### 7. Test Integration
```bash
# Add to workspace Makefile
make dev-sync  # Should include your domain

# Test the example
streamlit run example.py
```

## 📁 Template Structure

```
celeste-domain-template/
├── README.md                    # This comprehensive guide
├── pyproject.toml              # Package configuration
├── .pre-commit-config.yaml     # Pre-commit hooks for code quality
├── .gitignore                  # Standard ignores
├── example.py                  # Streamlit demo app
└── src/
    └── celeste_domain_template/
        ├── __init__.py         # Factory function
        ├── mapping.py          # Capability & provider mapping
        └── providers/
            ├── __init__.py
            └── google_template.py  # Example provider
```

## 🔧 Key Components

### mapping.py
- **CAPABILITY**: Links to celeste-core capability enum
- **PROVIDER_MAPPING**: Maps providers to implementation classes
- **Single source of truth** for domain configuration

### Factory Function
- **Dynamic provider resolution** from mapping
- **Environment validation** via settings
- **Lazy loading** of provider classes

### Provider Implementation
- **Domain-specific base class** inheritance
- **Async API patterns** for all operations
- **Artifact-based return types** (not generic responses)

### Example App
- **Model catalog integration** for dynamic provider/model discovery
- **Streamlit best practices** with efficient client creation
- **Domain-specific UI** patterns

### Domain-Specific Patterns
- **Catalogs & Registries**: Some domains need specialized registries (e.g., `voice_registry.py` in TTS for voice discovery)
- **Artifact Types**: Define custom artifact types in celeste-core for your domain's output
- **Base Classes**: Create domain-specific base classes when generic BaseClient isn't sufficient

## 📦 Installation

<details open>
<summary><b>Using UV (Recommended)</b></summary>

```bash
git clone https://github.com/yourusername/celeste
cd celeste/celeste-your-domain-name
uv sync
```
</details>

<details>
<summary><b>Using pip</b></summary>

```bash
git clone https://github.com/yourusername/celeste
cd celeste/celeste-your-domain-name
pip install -e .
```
</details>

## 🔧 Configuration

### Environment Configuration

API keys and provider configuration are handled automatically by `celeste-core` settings. No manual environment setup is required for basic usage.

<details>
<summary><b>🔑 Provider API Keys (if needed)</b></summary>

For providers that require API keys, `celeste-core` will automatically detect them from environment variables:

| Provider | Environment Variable | Get API Key |
|----------|---------------------|-------------|
| 🌈 **Google** | `GOOGLE_API_KEY` | [Google AI Studio](https://aistudio.google.com/app/apikey) |
| 🤖 **OpenAI** | `OPENAI_API_KEY` | [OpenAI Platform](https://platform.openai.com/api-keys) |
| 🌊 **Mistral** | `MISTRAL_API_KEY` | [Mistral Console](https://console.mistral.ai/) |
| 🎭 **Anthropic** | `ANTHROPIC_API_KEY` | [Anthropic Console](https://console.anthropic.com/) |
| 🤗 **Hugging Face** | `HUGGINGFACE_TOKEN` | [HF Settings](https://huggingface.co/settings/tokens) |
| 🦙 **Ollama** | *No key needed!* | [Install Ollama](https://ollama.com/download) |

</details>

## 🎮 Interactive Demo

Try the Streamlit example:
```bash
streamlit run example.py
```

## ✅ Customization Checklist

Before using your new domain:

- [ ] **Capability** added to celeste-core (if new)
- [ ] **Models** added to catalog with correct capability
- [ ] **Placeholder strings** replaced throughout all files
- [ ] **Provider implementations** completed with proper async methods
- [ ] **Dependencies** updated in pyproject.toml
- [ ] **Factory function** updated with correct base class import
- [ ] **Example app** customized for your domain's UI needs
- [ ] **Domain** added to workspace Makefile
- [ ] **Tests pass**: `make format lint typecheck`
- [ ] **Integration tested** with `streamlit run example.py`

## 🗺️ Domain Creation Workflow

### Phase 1: Planning
1. **Identify capability** - Does your domain need a new capability or use existing?
2. **Choose providers** - Which AI providers support your use case?
3. **Define artifacts** - What output types will your domain produce?

### Phase 2: Core Setup
1. **Add capability** to celeste-core if needed
2. **Add models** to catalog with proper capability flags
3. **Create base class** in celeste-core if domain-specific patterns needed
4. **Define artifact types** in celeste-core

### Phase 3: Domain Implementation
1. **Copy template** and perform global replacements
2. **Update mapping.py** with capability and provider mappings
3. **Implement providers** with proper async patterns
4. **Create factory function** with dynamic provider resolution

### Phase 4: Integration & Testing
1. **Customize example.py** for your domain's UI needs
2. **Add to workspace** Makefile for development workflow
3. **Test thoroughly** with multiple providers
4. **Validate** with lint, typecheck, and manual testing

## 📚 Reference

- **new_domain.md**: Complete domain creation checklist
- **Existing domains**: celeste-image-generation, celeste-text-to-speech, etc.
- **celeste-core**: Base classes and artifact types

## 🎯 Best Practices

1. **Use existing artifacts** from celeste-core when possible
2. **Follow async patterns** throughout all provider implementations
3. **Implement proper error handling** with meaningful error messages
4. **Keep domains focused** on single capabilities to maintain clarity
5. **Document provider-specific parameters** clearly in docstrings
6. **Test with multiple providers** when applicable for robustness
7. **Use model catalog** for dynamic provider/model discovery in UI
8. **Optimize Streamlit apps** with single list_models() call and efficient client creation

## 🌌 Celeste Ecosystem

| Package | Description | Status |
|---------|-------------|--------|
| 🧩 **celeste-core** | Core types, enums, and base classes | ✅ Available |
| 💬 **celeste-client** | Text generation & chat | ✅ Available |
| 🎨 **celeste-image-generation** | Multi-provider image generation | ✅ Available |
| ✏️ **celeste-image-edit** | Image editing capabilities | ✅ Available |
| 🎧 **celeste-audio-intelligence** | Audio processing & transcription | ✅ Available |
| 📄 **celeste-document-intelligence** | Document analysis & QA | ✅ Available |
| 🔢 **celeste-embeddings** | Text embeddings | ✅ Available |
| 🚀 **celeste-api** | FastAPI backend | ✅ Available |

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Adding a New Provider

1. Create a new file in `src/celeste_your_domain/providers/`
2. Extend the domain-specific base class from `celeste-core`
3. Implement all required async methods
4. Add provider-specific configuration to settings
5. Update `PROVIDER_MAPPING` in `mapping.py`
6. Test thoroughly with the example app

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  Made with ❤️ by the Celeste Team

  <a href="#-celeste-domain-template">⬆ Back to Top</a>
</div>
