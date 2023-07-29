def get_url_input():
    while True:
        try:
            # Using input() to get user input and strip any leading/trailing whitespaces
            url = input("Please enter the data URL from video: ").strip()

            # Checking if the input is not empty
            if url:
                return url
            else:
                print("Error: URL cannot be empty. Please try again.")
        except KeyboardInterrupt:
            # Handling Ctrl+C to exit gracefully
            print("\nOperation aborted by the user.")
            return None