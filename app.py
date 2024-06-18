from tabpy.tabpy_server.app.app import TabPyApp
import threading
# Define a function to start TabPy server
def start_tabpy_server():
    # Start TabPy server
    app = TabPyApp('tabpy.ini')
    app.run()
if __name__ == '__main__':
    # Start TabPy server in a separate thread
    # tabpy_thread = threading.Thread(target=start_tabpy_server)
    # tabpy_thread.start()
    start_tabpy_server()
    print("TabPy server started on port 9004.")
    print("You can now connect to TabPy and use it for predictive analytics.")
