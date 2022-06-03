from pathlib import Path

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
        print(filepath)
        with filepath.open("r") as chap_file:
            stringy = chap_file.read()
        stringy = stringy.split("##")[0] # Get only introductory paragraph
        stringy = stringy.replace("#", "##")
        summary += "\n"
        summary += stringy
    
    with (Config.appendix_dir/"A.md").open("w") as summary_file:
        summary_file.write(summary)

if __name__ == "__main__":
    main()