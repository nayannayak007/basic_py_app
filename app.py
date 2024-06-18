from tabpy.tabpy_server.app.app import TabPyApp
import threading
import os

# Define a function to start the TabPy server
def start_tabpy_server():
    # Fetch the port from Azure environment or use a default
    port = os.environ.get('WEBSITE_PORT', '9004')
    # Configure the TabPy server with the port
    app = TabPyApp(config_file='tabpy.ini', port=int(port))
    # Start the server
    app.run()

if __name__ == '__main__':
    # Start TabPy server in a separate thread
    tabpy_thread = threading.Thread(target=start_tabpy_server)
    tabpy_thread.start()
    tabpy_thread.join()  # This ensures the main thread waits for the server thread
    print(f"TabPy server started on port {port}.")
    print("You can now connect to TabPy and use it for predictive analytics.")
