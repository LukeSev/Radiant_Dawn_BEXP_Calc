from BEXP_calcs import *
from BEXP_GUI import *

def main():
    app = QApplication([])

    window = BEXP_Window()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()