from dataclasses import dataclasses
from pathlib  import pathlib

@dataclasses(frozen=True)
class DataIngestionConfig:
   root_dir: Path
   source_url: str
   local_data_file: Path 
   unzip_dir: Path
