from src.gui.main_window import MainWindow
from src.utils.logger import Logger, Level_en

def main():
    try:
        MainWindow().start()
    except Exception as e:
        Logger.log(e, level=Level_en.ERROR, to_std_out=True)


if __name__ == "__main__":
    main()