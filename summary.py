from pathlib import Path
import re
from slugify import slugify

class Config():
    start_dir: Path = Path(__file__).parent.resolve()
    chapters_dir: Path = start_dir/"kapitler"
    appendix_dir: Path = start_dir/"appendiks"

def main():
    files: list[Path] = list(Config.chapters_dir.iterdir())
    def sort_method(da_file: Path):
        stringy = da_file.stem
        return int(stringy)
    files.sort(key=sort_method)
    summary = "# A: Sammendrag\n"
    for filepath in files:
        filepath.resolve()
        with filepath.open("r") as chap_file:
            stringy = chap_file.read()
        stringy = stringy.split("##")[0] # Get only introductory paragraph
        stringy = re.sub(r"\(.*\)=\n", "", stringy) # Remove myst labels to avoid duplicates
        title = re.search(r"#\s?\d*:?\s?(.*)\n", stringy).group(1)+" sammendrag" 
        stringy = "("+slugify(title)+")=\n"+stringy # Make new myst label from slug of title
        stringy = stringy.replace("#", "##") # Only one h1 per page
        summary += "\n" + stringy
    
    with (Config.appendix_dir/"A.md").open("w") as summary_file:
        summary_file.write(summary)

if __name__ == "__main__":
    main()