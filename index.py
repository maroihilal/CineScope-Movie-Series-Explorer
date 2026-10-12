from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QLabel, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QPixmap
import sys
import requests
import json
from PyQt5.QtGui import QIcon

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(BASE_DIR, "logo.jpg")


class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1300, 980)
        self.setStyleSheet("background-color:#7FA9A2")

        self.home = QFrame(self)
        self.home.setGeometry(0, 0, 1300, 980)

        self.logo = QLabel("CineScope", self.home)
        self.logo.setStyleSheet("""
            QLabel {
                color:#F5F0E6;
                font-family:Arial;
                font-size:35px;
                font-weight:900;
            }
            QLabel:hover {
                color:#C47A55;
            }
        """)
        self.logo.setGeometry(40, 10, 300, 80)

        self.home_btn = QPushButton("Home", self.home)
        self.home_btn.setGeometry(1080, 25, 90, 50)
        self.home_btn.setStyleSheet("""
            QPushButton {
                background-color:#123C35;
                color:#F5F0E6;
                font-family:Arial;
                font-size:17px;
                font-weight:700;
                border-radius:12px;
            }
            QPushButton:hover {
                background-color:#3E7770;
            }
        """)
        self.home_btn.clicked.connect(self.home_func)

        self.exit_btn = QPushButton("Exit", self.home)
        self.exit_btn.setGeometry(1180, 25, 90, 50)
        self.exit_btn.setStyleSheet("""
            QPushButton {
                background-color:#542E2E;
                color:#FFFFFF;
                font-family:Arial;
                font-size:17px;
                font-weight:700;
                border-radius:12px;
            }
            QPushButton:hover {
                background-color:#743D3D;
            }
        """)
        self.exit_btn.clicked.connect(self.close)

        self.search_frame = QFrame(self.home)
        self.search_frame.setGeometry(0, 100, 1300, 240)
        self.search_frame.setStyleSheet("background-color:#D8C7AE;")

        self.title1 = QLabel("Discover Your Next Series", self.search_frame)
        self.title1.setGeometry(390, 0, 700, 90)
        self.title1.setStyleSheet("""
            color:#123C35;
            font-family:Arial;
            font-size:40px;
            font-weight:900;
            font-style:italic;
        """)

        self.para = QLabel("Search for a movie to explore its essential information", self.search_frame)
        self.para.setGeometry(300, 75, 700, 40)
        self.para.setStyleSheet("""
            color:#3E7770;
            font-style:italic;
            font-family:Arial;
            font-size:28px;
        """)

        self.input = QLineEdit(self.search_frame)
        self.input.setGeometry(300, 135, 500, 55)
        self.input.setPlaceholderText(" Enter movie name...")
        self.input.setStyleSheet("""
            QLineEdit {
                background-color:#F5F0E6;
                color:#123C35;
                font-size:18px;
                font-family:Arial;
                font-weight:700;
                border-radius:20px;
                border:2px solid #3E7770;
            }
            QLineEdit:focus {
                border:2px solid #C47A55;
            }
        """)

        self.search_btn = QPushButton("Search", self.search_frame)
        self.search_btn.setGeometry(830, 135, 140, 55)
        self.search_btn.setStyleSheet("""
            QPushButton {
                background-color:#C47A55;
                color:#F5F0E6;
                font-family:Arial;
                font-size:17px;
                font-weight:700;
                border-radius:12px;
            }
            QPushButton:hover {
                background-color:#D9926D;
            }
            QPushButton:pressed {
                background-color:#A95F3D;
            }
        """)
        self.search_btn.clicked.connect(self.movie_info)

        self.result = QFrame(self.home)
        self.result.setGeometry(50, 365, 1200, 560)
        self.result.setStyleSheet("background-color:#F5F0E6;border-radius:20px;")

        self.img = QLabel("", self.result)
        self.img.setGeometry(30, 40, 350, 450)
        self.img.setStyleSheet("border:none;border-radius:20px;")

        self.movie = QLabel("", self.result)
        self.movie.setGeometry(420, 30, 740, 70)
        self.movie.setStyleSheet("""
            color:#123C35;
            font-family:Arial;
            font-size:50px;
            font-weight:900;
            font-style:italic;
        """)

        self.language = QLabel("🌐 Language:", self.result)
        self.language.setGeometry(420, 120, 220, 50)
        self.language.setStyleSheet("""
            color:#123C35;
            font-family:Arial;
            font-size:24px;
            font-weight:700;
        """)

        self.language_answer = QLabel("", self.result)
        self.language_answer.setGeometry(640, 120, 220, 50)
        self.language_answer.setStyleSheet("""
            color:#596B3F;
            font-family:Arial;
            font-size:23px;
            font-weight:500;
        """)

        self.Runtime = QLabel("⏱ Runtime:", self.result)
        self.Runtime.setGeometry(870, 120, 180, 50)
        self.Runtime.setStyleSheet("""
            color:#123C35;
            font-family:Arial;
            font-size:24px;
            font-weight:700;
        """)

        self.Runtime_answer = QLabel("", self.result)
        self.Runtime_answer.setGeometry(1050, 120, 100, 50)
        self.Runtime_answer.setStyleSheet("""
            color:#596B3F;
            font-family:Arial;
            font-size:23px;
            font-weight:500;
        """)

        self.Rating = QLabel("★ Rating:", self.result)
        self.Rating.setGeometry(420, 190, 220, 50)
        self.Rating.setStyleSheet("""
            color:#123C35;
            font-family:Arial;
            font-size:24px;
            font-weight:700;
        """)

        self.Rating_answer = QLabel("", self.result)
        self.Rating_answer.setGeometry(640, 190, 220, 50)
        self.Rating_answer.setStyleSheet("""
            color:#C47A55;
            font-family:Arial;
            font-size:23px;
            font-weight:700;
        """)

        self.Genre = QLabel("🎭 Genre:", self.result)
        self.Genre.setGeometry(420, 260, 220, 50)
        self.Genre.setStyleSheet("""
            color:#123C35;
            font-family:Arial;
            font-size:24px;
            font-weight:700;
        """)

        self.Genre_answer = QLabel("", self.result)
        self.Genre_answer.setGeometry(640, 250, 500, 80)
        self.Genre_answer.setStyleSheet("""
            color:#3E7770;
            font-family:Arial;
            font-size:23px;
            font-weight:500;
        """)
        self.Genre_answer.setWordWrap(True)

        self.Description = QLabel("📖 Description:", self.result)
        self.Description.setGeometry(420, 350, 250, 50)
        self.Description.setStyleSheet("""
            color:#123C35;
            font-family:Arial;
            font-size:24px;
            font-weight:700;
        """)

        self.Description_answer = QLabel("", self.result)
        self.Description_answer.setGeometry(420, 400, 730, 120)
        self.Description_answer.setStyleSheet("""
            color:#596B3F;
            font-family:Arial;
            font-size:19px;
            font-weight:500;
        """)
        self.Description_answer.setWordWrap(True)

        self.result.hide()

    def home_func(self):
        self.input.clear()
        self.movie.clear()
        self.language_answer.clear()
        self.Runtime_answer.clear()
        self.Rating_answer.clear()
        self.Genre_answer.clear()
        self.Description_answer.clear()
        self.img.clear()
        self.result.hide()

    def movie_info(self):
        try:
            movie_name = self.input.text().strip()

            if movie_name == "":
                QMessageBox.warning(self, "Error", "Please enter a movie or series name.")
                return

            url = f"https://api.tvmaze.com/singlesearch/shows?q={movie_name}"

            response = requests.get(url, timeout=10)

            print(response.status_code)

            if response.status_code != 200:
                QMessageBox.warning(self, "Not Found", "Movie or series not found.")
                return

            data = response.json()

            with open("project9(movie informations)/books.json", "w") as file:
                json.dump(data, file, indent=4)

            description = data.get("summary", "")
            description = description.replace("<p>", "")
            description = description.replace("</p>", "")
            description = description.replace("<b>", "")
            description = description.replace("</b>", "")

            print("Description:", description)
            print("Name:", data["name"])
            print("Language:", data["language"])
            print("Runtime:", data["averageRuntime"])
            print("Average:", data["rating"]["average"])
            print("Image URL:", data["image"]["original"])
            print("Genre:", " ".join(data["genres"]))

            self.movie.setText(data["name"])
            self.language_answer.setText(data["language"])

            runtime = data.get("averageRuntime")

            if runtime is not None:
                self.Runtime_answer.setText(str(runtime) + " min")
            else:
                self.Runtime_answer.setText("N/A")

            rating = data.get("rating", {}).get("average")

            if rating is not None:
                self.Rating_answer.setText(str(rating))
            else:
                self.Rating_answer.setText("N/A")

            self.Genre_answer.setText(" ".join(data["genres"]))
            self.Description_answer.setText(description)

            image_url = data.get("image", {}).get("original")

            if image_url:
                image_response = requests.get(image_url, timeout=10)

                if image_response.status_code == 200:
                    pixmap = QPixmap()
                    pixmap.loadFromData(image_response.content)
                    self.img.setPixmap(pixmap)
                    self.img.setScaledContents(True)

            self.result.show()

        except requests.exceptions.Timeout:
            QMessageBox.warning(self, "Error", "The request took too long. Please try again.")

        except requests.exceptions.ConnectionError:
            QMessageBox.warning(self, "Error", "No internet connection.")

        except requests.exceptions.RequestException:
            QMessageBox.warning(self, "Error", "An error occurred while connecting to the API.")

        except Exception as e:
            QMessageBox.warning(self, "Error", "Something went wrong.")
            print(e)


def main():
    app = QApplication(sys.argv)
    fenetre = window()
    app.setWindowIcon(QIcon(logo_path))
    fenetre.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()