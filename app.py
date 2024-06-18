from tabpy.tabpy_server.app.app import TabPyApp
import threading
import os

# Define a function to start the TabPy server with dynamic port settings
def start_tabpy_server():
    # Fetch the port from the Azure environment or use a default
    port = os.environ.get('WEBSITE_PORT', '9004')  # Default to 9004 if not set by Azure
    # Modify the configuration file or environment appropriately here if necessary

    # Initialize and start the TabPy server
    app = TabPyApp(config_file='tabpy.ini')
    app.app.config['SERVER_PORT'] = int(port)  # Adjusting the configuration directly
    app.run()

if __name__ == '__main__':
    # Start TabPy server in a separate thread
    tabpy_thread = threading.Thread(target=start_tabpy_server)
    tabpy_thread.start()
    tabpy_thread.join()  # Ensures the main thread waits for the server thread
