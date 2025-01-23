import toml
from pathlib import Path

# Load configuration
config_path = Path(__file__).parent / "env.toml"
config = toml.load(config_path)
