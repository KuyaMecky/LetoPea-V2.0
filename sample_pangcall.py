from CV2_loading import loadingscreen

# create an instance of the loadingscreen class
loading_screen = loadingscreen()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    loading_screen = loadingscreen()
    loading_screen.show()
    sys.exit(app.exec_())
