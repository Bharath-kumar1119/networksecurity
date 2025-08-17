from dataclasses import dataclass

### Dataclasses act as a decorator

@dataclass
class DataIngestionArtifact:
    trained_file_path : str
    test_file_path : str