import requests
import json

BASE_URL = "https://activate-browser-use.onrender.com"

class BrowserUseActivator:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url
    
    def get_status(self):
        """Get current activation status"""
        try:
            response = requests.get(f"{self.base_url}/status")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting status: {e}")
            return None
    
    def activate(self):
        """Activate the service (set to 1)"""
        try:
            response = requests.post(f"{self.base_url}/activate")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error activating: {e}")
            return None
    
    def deactivate(self):
        """Deactivate the service (set to 0)"""
        try:
            response = requests.post(f"{self.base_url}/deactivate")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error deactivating: {e}")
            return None
    
    def is_active(self):
        """Check if service is currently active"""
        status = self.get_status()
        return status and status.get("value") == 1

# Example usage
activator = BrowserUseActivator()

# Check current status
status = activator.get_status()
print(f"Current status: {status}")

# Activate the service
result = activator.activate()
print(f"Activation result: {result}")

# Check if active
if activator.is_active():
    print("Service is now active!")
    
# Deactivate when done
deactivate_result = activator.deactivate()
print(f"Deactivation result: {deactivate_result}")