from tabpy.tabpy_server.app.app import TabPyApp
import threading
import os

def modify_config_file(port):
    # Read the original configuration
    with open('tabpy.ini', 'r') as file:
        config_lines = file.readlines()
    
    # Modify the port in the configuration
    with open('tabpy.ini', 'w') as file:
        for line in config_lines:
            if line.strip().startswith('TABPY_PORT'):
                file.write(f'TABPY_PORT = {port}\n')
            else:
                file.write(line)

# Define a function to start the TabPy server with dynamic port settings
def start_tabpy_server():
    # Fetch the port from the Azure environment or use a default
    port = os.environ.get('WEBSITE_PORT', '9004')  # Default to 9004 if not set by Azure
    # Modify the config file before starting the server
    modify_config_file(port)

    # Initialize and start the TabPy server
    app = TabPyApp(config_file='tabpy.ini')
    app.run()

if __name__ == '__main__':
    # Start TabPy server in a separate thread
    tabpy_thread = threading.Thread(target=start_tabpy_server)
    tabpy_thread.start()
    tabpy_thread.join()  # Ensures the main thread waits for the server thread
