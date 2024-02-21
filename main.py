if __name__ == "__main__":
    from dotenv import load_dotenv
    from flaskp import create_app

    load_dotenv()
    create_app().run(debug=True)
